# AWS SAM Examples

# Overview
This repository contain following SAM based functions:
* app.py: simple Hello World example
* SendEmail: sending Email with Lambda and API Gateway

## Usage
* Create a S3 bucket: `aws s3 mb s3://$YOUR_SAM_PROJ_NAME`
* Build project: see `build` in `buildspec.yml`
* Deploy:

```
aws cloudformation deploy --template-file ./serverless-output.yaml --stack-name $YOUR_SAM_PROJ_NAME --capabilities=CAPABILITY_IAM
```

## Test Lambda locally 
* `sam local start-lambda` + `sam local invoke HelloWorldFunction --event ./test/HelloWorldPayload.json`

## Test Api locally 
* `sam local start-api` + `curl http://localhost:3000/hello?name=SAM_TEST`