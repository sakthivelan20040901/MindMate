import boto3
from botocore.exceptions import ClientError
from config import Config


class BedrockService:

    def __init__(self):

        self.client = boto3.client(
            service_name="bedrock-runtime",
            region_name=Config.AWS_REGION,
            aws_access_key_id=Config.AWS_ACCESS_KEY,
            aws_secret_access_key=Config.AWS_SECRET_KEY,
        )

        self.model_id = Config.BEDROCK_MODEL

    def chat(self, prompt: str):

        try:

            response = self.client.converse(

                modelId=self.model_id,

                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "text": prompt
                            }
                        ]
                    }
                ],

                inferenceConfig={
                    "temperature": 0.7,
                    "maxTokens": 500,
                    "topP": 0.9
                }

            )

            return response["output"]["message"]["content"][0]["text"]

        except ClientError as e:

            print(e)

            return str(e)
