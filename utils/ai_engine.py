from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(
    api_key=os.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "models/gemini-2.5-flash"
)

def generate_insights(df):

    summary = df.describe().to_string()

    prompt = f"""
    Analyze this business dataset.

    {summary}

    Provide:

    1. Key Insights
    2. Trends
    3. Risks
    4. Recommendations
    """

    response = model.generate_content(prompt)

    return response.text


def ask_question(df, question):

    sample = df.head(100).to_string()

    prompt = f"""
    Dataset:

    {sample}

    Question:

    {question}

    Answer using only dataset information.
    """

    response = model.generate_content(prompt)

    return response.text