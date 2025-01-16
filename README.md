# Chatbot Application

A Flask-based web application that provides interactive chatbot services to guide users through **Segment**, **mParticle**, **Lytics**, and **Zeotap** CDPs. The chatbot delivers step-by-step instructions by extracting data from official documentation of each platform.

## Overview
This chatbot application allows users to get answers to their queries about Customer Data Platforms (CDPs). The backend is powered by **Flask** and uses the **Generative AI** API for dynamic responses based on official platform documentation. The frontend provides a clean, interactive chat interface for users to easily interact with the bot.

## Features
- **Interactive Chat Interface**: A user-friendly chat window where users can ask questions related to CDPs.
- **Step-by-Step Guidance**: The chatbot provides clear, concise answers with actionable steps, directly sourced from platform documentation.
- **Typing Animation**: A realistic "typing" animation to simulate an engaging chat experience.
- **Responsive Design**: Optimized to work seamlessly across different devices including desktops, tablets, and smartphones.
- **Integration with Official Documentation**: Uses official platform documentation (Segment, mParticle, Lytics, Zeotap) to provide accurate and up-to-date information.
- **Environment Configurable**: Requires API key setup for accessing the Generative AI API, ensuring secure and efficient communication.

## How to Use
1. Clone the repository and install the required dependencies.
2. Set your **Generative AI API Key** as an environment variable.
3. Run the Flask application to start the chatbot server.
4. Open the application in a web browser to interact with the chatbot.
5. Ask questions related to **Segment**, **mParticle**, **Lytics**, or **Zeotap** for step-by-step guidance.

## Notes
- Ensure to configure the API key correctly to enable chatbot functionality.
- The chatbot extracts information directly from official platform documentation for accurate responses.
