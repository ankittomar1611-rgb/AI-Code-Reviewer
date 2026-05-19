from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API Key
api_key = os.getenv("API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")

# Flask App
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    review = ""

    if request.method == "POST":

        code = request.form["code"]
        language = request.form["language"]

        prompt = f"""
        You are a senior software engineer.

        Review this {language} code.

        Give:
        1. Bugs
        2. Improvements
        3. Security Issues
        4. Optimized Suggestions

        Code:
        {code}
        """

        response = model.generate_content(prompt)

        review = response.text

    return render_template("index.html", review=review)

if __name__ == "__main__":
    app.run(debug=True)