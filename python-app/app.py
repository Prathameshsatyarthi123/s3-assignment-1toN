from flask import Flask, jsonify, make_response
from flask_cors import CORS
import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os

app = Flask(__name__)
CORS(app)

@app.route('/list-bucket-content/<path:bucket_prefix>', methods=['GET'])
@app.route('/list-bucket-content', defaults={'bucket_prefix': ''}, methods=['GET'])
def list_bucket_content(bucket_prefix):
    try:
        if bucket_prefix and not bucket_prefix.endswith('/'):
            bucket_prefix += '/'

        s3_client = boto3.client('s3')
        bucket_name = os.getenv('BUCKET_NAME')

        s3_response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=bucket_prefix, Delimiter='/')
        print(s3_response)
        bucket_content = []

        if 'CommonPrefixes' in s3_response:
            bucket_content.extend([prefix['Prefix'].rstrip('/') for prefix in s3_response['CommonPrefixes']])
        if 'Contents' in s3_response:
            bucket_content.extend(
                obj["Key"].split("/")[-1]
                for obj in s3_response["Contents"]
                if obj["Key"] != bucket_prefix
            )
        if 'Contents' not in s3_response and 'CommonPrefixes' not in s3_response:
            return make_response(jsonify({"error": "Path not found"}), 404)

        return jsonify({"content": bucket_content})

    except ClientError as e:
        error_message = e.response.get('Error', {}).get('Message', 'An error occurred')
        return make_response(jsonify({"error": error_message}), 500)

    except BotoCoreError as e:
        return make_response(jsonify({"error": str(e)}), 500)

    except Exception as e:
        return make_response(jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500)

@app.route("/health", methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Resource not found"}), 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
