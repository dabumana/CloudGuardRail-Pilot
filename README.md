# CloudGuardRail-Pilot
As part of the template for AWS context, some of the components included are:

## Service mesh components

* SQS
* SNS
* IAM
* VPC
* Lambda

## CI/CD (Optional)

* Github Actions

## Requirements
Based on composed template for CloudFormation, some tools are required to be installed before you can start testing, as a main requirement an AWS account, with the main purpose of cloud and local testing, we will be using make to execute some of the actions, validate that you have installed the following tools:

* AWS Cli
* Python
* Make
* Github Cli (Optional for CI/CD)

## How to use?
You can use make to execute actions like:

### Create
* Create and deploy stack using CloudFormation on AWS
```
make create
```

### Validate
* Validate stack composed
```
make validate
```

## What's next?
Aspects to be considered for future implementation:

* Secure secrets and environment variables
* Define region and zones to be used in case of failure
* Add a B/G strategy to handle releases and keep artifacts inventory
* Include a GTM per region with a LTM per zone
* Include additional RBAC policies

## Conclusion
This is a general approach to use a template that can be triggered according to specific actions or contextual cloud providers.
