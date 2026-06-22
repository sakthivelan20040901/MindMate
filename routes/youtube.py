from flask import Blueprint, jsonify, request

from services.youtube_service import YouTubeService
from services.prompt_builder import PromptBuilder
from services.bedrock_service import BedrockService
from utils.json_parser import JsonParser

youtube_bp = Blueprint("youtube", __name__)

bedrock = BedrockService()
youtube_service = YouTubeService()


@youtube_bp.route("/youtube", methods=["POST"])
def generate_youtube():

    data = request.get_json()

    prompt = PromptBuilder.youtube_query(
        data["name"],
        data["mood"],
        data["goal"],
        data["interest"]
    )

    ai_response = bedrock.chat(prompt)

    query_json = JsonParser.parse(ai_response)

    videos = []

    for query in query_json["queries"]:
        videos.extend(youtube_service.search(query, 1))

    return jsonify(videos)
