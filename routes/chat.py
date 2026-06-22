from flask import Blueprint

from services.bedrock_service import BedrockService
from services.prompt_builder import PromptBuilder

chat = Blueprint("chat", __name__)

bedrock = BedrockService()


@chat.route("/chat")
def test_chat():

    prompt = PromptBuilder.test_prompt()

    response = bedrock.chat(prompt)

    return response
