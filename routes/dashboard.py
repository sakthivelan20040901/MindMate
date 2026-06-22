from flask import Blueprint
from flask import request
from flask import jsonify

from services.bedrock_service import BedrockService
from services.youtube_service import YouTubeService
from services.prompt_builder import PromptBuilder

from utils.json_parser import JsonParser


dashboard_bp = Blueprint("dashboard", __name__)

bedrock = BedrockService()

youtube = YouTubeService()


@dashboard_bp.route("/generate-dashboard", methods=["POST"])
def generate_dashboard():

    data = request.get_json()

    prompt = PromptBuilder.dashboard_prompt(

        data["name"],

        data["mood"],

        data["goal"],

        data["interest"]

    )

    ai_response = bedrock.chat(prompt)

    result = JsonParser.parse(ai_response)

    newsletter = result["newsletter"]

    queries = result["youtube_queries"]

    videos = []

    for query in queries:

        video = youtube.search(query, 1)

        videos.extend(video)

    return jsonify({

        "newsletter": newsletter,

        "videos": videos

    })
