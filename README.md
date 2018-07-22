# AWS SAM Examples

# Overview
This repository contain following SAM based functions:
* app.py: simple Hello World example
* SendEmail: sending Email with Lambda and API Gateway

## Usage
* `export YOUR_SAM_PROJ_NAME=andrejmaya-sam-example`
* `aws s3 mb s3://$YOUR_SAM_PROJ_NAME`
* 
```
aws cloudformation package \
    --template-file ./template.yaml \
    --s3-bucket $YOUR_SAM_PROJ_NAME \
    --output-template-file serverless-output.yaml
```
* 
```
aws cloudformation deploy --template-file ./serverless-output.yaml --stack-name $YOUR_SAM_PROJ_NAME --capabilities=CAPABILITY_IAM
```

