import json
import re


class JsonParser:

    @staticmethod
    def parse(text):

        # Remove markdown code fences
        text = re.sub(r"^```json", "", text.strip(), flags=re.MULTILINE)
        text = re.sub(r"^```", "", text.strip(), flags=re.MULTILINE)
        text = text.replace("```", "")

        # Remove extra whitespace
        text = text.strip()

        return json.loads(text)
