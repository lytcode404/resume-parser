from flask import Flask, request, jsonify
import os
from flask_cors import CORS
import google.generativeai as genai


app = Flask(__name__, template_folder="templates")
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
api_key = "AIzaSyDVCdu-XGZRa6_ty_Fc32RCdz1Nb4zy0gk"

# Configure Gemini API
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)


@app.route("/generate-test", methods=["POST"])
def generate_test():
    data = request.json
    topic = data.get("topic")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    prompt = f"Give me a JSON formatted test of 20 questions with 4 options each. The JSON test should be of topic '{topic}'."

    chat_session = model.start_chat()
    response = chat_session.send_message(prompt)

    return jsonify(response.text)


if __name__ == "__main__":
    app.run(debug=True)
