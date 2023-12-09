import boto3

AWS_ACCESS_KEY_ID = "your_access_key"
AWS_SECRET_ACCESS_KEY = "your_secret_key"
AWS_REGION = 'us-east-1'

def send_email(subject, message, recipient):
    sns = boto3.client('sns', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)
    ses = boto3.client('ses', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

    topic_arn = sns.create_topic(Name='email-topic')['TopicArn']

    email_from = "your_verified_email@example.com"

    ses.send_email(
        Source=email_from,
        Destination={'ToAddresses': [recipient]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': message}}
        }
    )

    sns.publish(TopicArn=topic_arn, Message=message, Subject=subject)

    print("Email sent successfully!")

if __name__ == "__main__":
    send_email('Test Email', 'Hello, this is a test email sent using Amazon SNS and SES.', 'your_verified_email@example.com')
