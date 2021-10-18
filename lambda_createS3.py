AWS_DEFAULT_REGION = "eu-central-1" #Region lambda
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

backetname = "lambda.created.me.on-" + str(time.time())
def lambda_handler(event, context):
    myS3 = boto3.resorce('s3')
    try:
        results = myS3.create_bucket(
                                Bucket= backetname,
                                CreateBucketConfiguretion={'locationConstraint'; AWS_DEFAULT_REGION}
                                )     
        return("<h1><front color=green>S3 Bucket List:</front></h1><br><br>" + output)
    except:
        return("<h1><front color=red>ERROR!</front></h1><dr><br>")
