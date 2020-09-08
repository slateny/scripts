## Overview
1. Create AWS account
2. Create EC2 instance
3. Setup bot in EC2

## Create AWS account
1. Go to [signup](https://portal.aws.amazon.com/billing/signup) and fill in details

## Create EC2 instance
1. Go to [the EC2 page](https://console.aws.amazon.com/ec2)
2. Go to **Launch Instance**
3. Select an AMI (*Ubuntu Server* will work for this guide)
4. Select an instance type — if not using free tier, refer to the [AWS Pricing Calculator](https://calculator.aws/#/addService) for more information on cost
5. Skip (or review) the steps until the **Add Storage** — if not using free tier, refer to the [EBS pricing](https://aws.amazon.com/ebs/pricing/) for more information on storage costs
6. Skip (or review) the steps until the **Configure Security Group** step, then restrict the source IP to **My IP**
7. Continue to **Review and Launch**
8. Continue to **Launch**
9. Create (or use an existing) key pair, and download it before continuing to **Launch Instance**

## Setup bot in EC2
1. Verify that the instance is created in [the EC2 page](https://console.aws.amazon.com/ec2)
2. Connect to the newly created EC2 instance with [ssh instructions here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) — if using ubuntu, the instance user name will be `ubuntu`
3. Once connected, follow instructions in [bot-sample](../bot-sample)
