import boto3, os

def lambda_function(event, context):
    # TODO implement
    myS3 = doto3.client('s3')
    try:
        results = myS3.list_buckets()
        print(results)
        output = ""
        for bucket in results['Buckets']:
            output = output + bucket['Name'] + "<br>"
            return("<h1><front color=green>S3 Bucket List:</front></h1><br><br>" + output)
        except:
            return("<h1><front color=red>ERROR!</front></h1><dr><br>")
            
