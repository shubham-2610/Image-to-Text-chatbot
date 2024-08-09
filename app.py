import google.generativeai as genai
import os
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",google_api_key=GOOGLE_API_KEY)
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "who is customer?",
        },
        {"type": "image_url", "image_url": "/content/sample_img.png"},
    ]
)
llm.invoke([message])