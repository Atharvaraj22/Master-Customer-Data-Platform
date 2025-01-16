from flask import Flask, render_template, request, jsonify
import pandas as pd
import requests
from math import radians, sin, cos, sqrt, atan2
import os
import google.generativeai as genai
app = Flask(__name__)


# Route to render the HTML page (Frontend)
@app.route('/')
def home():
    return render_template('index.html')  # This will render your index.html file

# Route to handle chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    history2 = []
    if not user_input:
        return jsonify({"error": "No message received"}), 400

 

    genai.configure(api_key="") #replace with your api key

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
    ]
    )
#     query = f"""You are a chatbot designed to help users find suitable agencies for their needs.

# Task:
# Analyze the user's query by asking up to 4-5 key questions, one at a time. Gather essential details to create a summarized paragraph of the user’s requirements, which will be shared with an AI for matchmaking.

# Required Information:
# Industry Category: Ask which category the user’s need falls under: Marketing, Tech, Media, or IT.
# Specific Requirements: Inquire about the specific services or solutions they are looking for.
# Current Status: Ask if they have any prior work, materials, or progress related to their requirement.
# Budget: Understand their budget range for the project.
# Work Preference: Determine if they are open to remote work or prefer a local/on-site agency.
# Guidelines:
# Sequential Questions: Ask one question at a time and wait for the user’s response before proceeding to the next question.
# Avoid Repetition: Use previous responses or chat history to avoid repeating questions unnecessarily.
# Friendly Prompts: If the user’s input lacks critical information, prompt them gently for clarification.
# Context Awareness: Take into account chat history for better context and personalization.
# Output Format:
# Once sufficient information is gathered, return a comma-separated summary in the format:
# Summary, [summarized description]

# Use this chat history and current user input for better context and personalization
# Chat History: {history2}
# User Query: {user_input}
# """
    
    query = f"""
"You are an intelligent assistant specialized in Customer Data Platforms (CDPs), providing precise and actionable guidance on how to use Segment, mParticle, Lytics, and Zeotap. Your role is to help users answer 'how-to' questions by extracting accurate and relevant information from the official documentation of these platforms.
You will need to answer in short without any bold headings.
Instructions:
Understand and respond to questions about Segment, mParticle, Lytics, and Zeotap, focusing on specific tasks or features within each platform.

Example questions include:
'How do I set up a new source in Segment?'
'How can I create a user profile in mParticle?'
'How do I build an audience segment in Lytics?'
'How can I integrate my data with Zeotap?'
Use the provided official documentation as your source of truth:

Segment Documentation: https://segment.com/docs/?ref=nav  
mParticle Documentation: https://docs.mparticle.com/  
Lytics Documentation: https://docs.lytics.com/  
Zeotap Documentation: https://docs.zeotap.com/home/en-us/  
Extract relevant information by:

Navigating the documentation structure.
Identifying the correct sections, steps, or details related to user queries.
Handle variations in questions, ensuring flexibility to understand:

Different phrasings of the same question.
Longer or detailed queries without breaking them down unnecessarily.
Address unrelated or out-of-scope questions politely:

Example: If asked, 'Which movie is releasing this week?' respond with: 'I specialize in answering questions about Segment, mParticle, Lytics, and Zeotap. Please ask about these platforms!'
Response Format:
Provide concise, clear, and structured answers with step-by-step guidance where applicable.
For complex tasks, include links to specific sections in the documentation to direct users to more detailed explanations.
Additional Context:
Always prioritize accuracy and ensure that your responses align with the official documentation.
Avoid providing speculative or unverified information."

user input: {user_input}
"""
    
    response = chat_session.send_message(query)
    x = "user input: " + user_input
    y = "bot response: " + response.text
    history2.append(x)
    history2.append(y)
    responses = str(response.text).split(',')
    print(responses)
    print(history2)
    final_respone = response.text.strip()
    return jsonify("Bot:" + final_respone)

if __name__ == '__main__':
    app.run(debug=True)
