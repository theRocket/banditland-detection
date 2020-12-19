
import boto3

# requires aws cli config working, to be documented
class AwsNotifier:
    def __init__(self, region='us-west-2',topicArn='arn:aws:sns:us-west-2:876612415673:xavier_securitycam'):
        self.region = region
        self.topic = topicArn
        # Create an SNS client
        self.sns = boto3.client('sns', region_name=self.region)

    def publish(self, message):
        # Publish a simple message to the specified SNS topic
        response = self.sns.publish(TopicArn=self.topic, Message=message)