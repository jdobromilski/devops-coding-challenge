DevOps Coding Test
==================

# Goal

Script the creation of a service, and a healthcheck script to verify it is up and responding correctly.

# Prerequisites

You will need an AWS account. Create one if you don't own one already. You can use free-tier resources for this test.

# The Task

You are required to provision and deploy a new service in AWS. It must:

* Be publicly accessible, but *only* on port 80.
* Return the current time on `/now`.

# Mandatory Work

Fork this repository.

* Script your service using CloudFormation, and your server configuration management tool of choice should you need one.
* Provision the service in your AWS account.
* Write a healthcheck script in Python that can be run externally to periodically check if the service is up and its clock is not desynchronised by more than 1 second.
* Alter the README to contain instructions required to:
  * Provision the service.
  * Run the healthcheck script.
* Provide us IAM credentials to login to the AWS account. If you have other resources in it make sure we can only access what is related to this test.

Once done, give us access to your fork. Feel free to ask questions as you go if anything is unclear, confusing, or just plain missing.

# Extra Credit

We know time is precious, we won't mark you down for not doing the extra credits, but if you want to give them a go...

* Run the service inside a Docker container.
* Make it highly available.

# Questions

#### What scripting languages can I use?

Please use Python and CloudFormation, as we would like to see your skills with these tools. For configuration management we use Puppet internally, but feel free to use anything you're familiar with. You'll need to be able to justify and discuss your choices.

#### Will I have to pay for the AWS charges?

No. You are expected to use free-tier resources only and not generate any charges. Please remember to delete your resources once the review process is over so you are not charged by AWS.

#### What will you be grading me on?

Scripting skills, security, elegance, understanding of the technologies you use, documentation.

#### What will you not take into account?

Brevity. We know there are very simple ways of solving this exercise, but we need to see your skills. We will not be able to evaluate you if you provide five lines of code.

#### Will I have a chance to explain my choices?

If we proceed to a phone interview, we’ll be asking questions about why you made the choices you made. Comments in the code are also very helpful.

#### Why doesn't the test include X?

Good question. Feel free to tell us how to make the test better. Or, you know, fork it and improve it!

# Provisioning service

#### Requirements

The service can be provisioned using awscli although I found it useful to use NodeJs application called cfn-create-or-update. Thanks to that the service can be provisioned and updated using for example Jenkins task.
https://github.com/widdix/cfn-create-or-update

To install cfn-create-or-update nodejs needs to be installed on the system and we need to run the following command:

npm install -g cfn-create-or-update

#### Service provisioning
To provision the service please run the following command:

* Infrastructure:
cfn-create-or-update --stack-name jarek-myapp-networking --template-body file://infrastructure/01_networking.yaml --capabilities CAPABILITY_IAM --region eu-west-1 --profile {your_aws_profile_name}

* Service:
cfn-create-or-update --stack-name jarek-myapp-containers --template-body file://02_service.yaml --region eu-west-1 --profile {your_aws_profile_name}

#### Health check
Correct operation of the service can be verified using simple AWS Lambda function:
lambda://jarek-myapp-healthcheck

* Code of the function resides in healthcheck directory - healthcheck.py. It requires python `requests` module and can be executed from command line.
If required can be installed using:
pip install requests

* Lambda package - healthcheck script is also packaged with the right modules and zipped as healthcheck.zip in the root folder of the repo.

* Lambda - packaging software and updating lambda function
In the healthcheck folder the following command needs to be run:
zip -r9 ../healthcheck.zip .

To upload new version of the function following command needs to be run in repository root folder:
aws lambda update-function-code --function-name jarek-myapp-healthcheck --zip-file fileb://healthcheck.zip --profile {your_aws_profile_name}


* Lambda execution:
The instance of the healthcheck is also deployed as an AWS Lambda function and can be executed directly from the console.
Function name: jarek-myapp-healthcheck
https://eu-west-1.console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/jarek-myapp-healthcheck?tab=configuration

* Result:
  - it would return 'OK' if the service is running and the time difference is less than 1 second.
  - it would return 'Failed' if the service is not available or the time difference is more than 1 second.
