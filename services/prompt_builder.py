class PromptBuilder:

    @staticmethod
    def test_prompt():
        return """
You are MindMate.

Say hello to the user.

Introduce yourself in two lines.
"""

    @staticmethod
    def newsletter(name, mood, goal, interest):
        return f"""
You are MindMate.

You MUST respond ONLY with valid JSON.

Do not use markdown.
Do not explain.

Return exactly this JSON.

{{
    "greeting":"",
    "motivation":"",
    "productivity_tip":"",
    "wellness_tip":"",
    "quote":"",
    "closing":""
}}

Generate a personalized motivational newsletter.

User

Name: {name}
Mood: {mood}
Goal: {goal}
Interest: {interest}
"""

    @staticmethod
    def youtube_query(name, mood, goal, interest):
        return f"""
You are MindMate.

Return ONLY valid JSON.

Do not use markdown.
Do not explain.

Return exactly this schema.

{{
    "queries":[
        "",
        "",
        "",
        "",
        ""
    ]
}}

Generate five YouTube search queries.

User

Name: {name}
Mood: {mood}
Goal: {goal}
Interest: {interest}

The searches should help improve the user's mood and help achieve the goal.
"""

    @staticmethod
    def dashboard_prompt(name, mood, goal, interest):
        return f"""
You are MindMate.

Return ONLY valid JSON.

Do not use markdown.
Do not explain.

Return exactly this JSON.

{{
    "newsletter": {{
        "greeting": "",
        "motivation": "",
        "productivity_tip": "",
        "wellness_tip": "",
        "quote": "",
        "closing": ""
    }},
    "youtube_queries": [
        "",
        "",
        "",
        "",
        ""
    ]
}}

Generate everything based on:

Name: {name}
Mood: {mood}
Goal: {goal}
Interest: {interest}
"""
