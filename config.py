import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")

    AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

    AWS_REGION = os.getenv("AWS_REGION")

    BEDROCK_MODEL = os.getenv("BEDROCK_MODEL_ID")

    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
