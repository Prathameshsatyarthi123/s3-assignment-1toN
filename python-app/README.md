# s3-assignment-1toN

``` Project- crasp ```

``` Getting Started ```

``` Follow this setp to run s3-listing python application ```

```Prerequisites:```

Python (ensure it's installed by running python --version)

Git (to clone the repository) 

``` use:
 git clone https://github.com/Prathameshsatyarthi123/S3-assignment.git
 ```



```Installation ```

```- Clone the repository```

```
git clone https://github.com/Prathameshsatyarthi123/S3-assignment.git
```
```
 cd S3-assignment
```

``` Install dependencies & packages```

```
 pip install -r requirements.txt
```


```- Configure aws and export bucket-name```

```
 aws configure (AWS_ACCESS_KEY_ID = xxx , AWS_SECRET_ACCESS_KEY = xxx , AWS_REGION = xxx)
 export = 'BUCKET_NAME'
```


``` -Running the Application```

```
 python app.py
```

 ``` Dockerizing python app ```

``` - Build the Docker image```

```
 docker build -t your-image-name .
```

 ```-Run Docker container```

```
 docker run --env-file .env -p 8000:8000 your-image-name

```
