from flask import Blueprint
from flask import request
from flask import jsonify

import json

from services.bedrock_service import BedrockService
from services.prompt_builder import PromptBuilder
from utils.json_parser import JsonParser

newsletter = Blueprint("newsletter", __name__)

bedrock = BedrockService()


@newsletter.route("/newsletter", methods=["POST"])
def generate_newsletter():

    data = request.get_json()

    prompt = PromptBuilder.newsletter(

        data["name"],

        data["mood"],

        data["goal"],

        data["interest"]

    )

    ai_response = bedrock.chat(prompt)

    try:

        newsletter_json = JsonParser.parse(ai_response)

    except Exception:

        newsletter_json = {

            "greeting": "Parsing Error",

            "motivation": ai_response,

            "productivity_tip": "",

            "wellness_tip": "",

            "quote": "",

            "closing": ""

        }

    return jsonify(newsletter_json)
