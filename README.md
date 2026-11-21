# LLM Application Playground

A beginner-friendly LLM playground built using Python, Streamlit, and the Groq API.

## Features

- Accept user prompts
- Connect to an LLM API
- Generate AI responses
- Experiment with different prompts
- Display responses through a Streamlit interface

## Tech Stack

- Python
- Streamlit
- Groq API
- OpenAI Python SDK
- Python-dotenv

## Installation

1. Clone this repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   cd llm-playground
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate it:

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project folder:

   ```env
   GROQ_API_KEY=your_api_key_here
   ```

6. Run the application:

   ```bash
   streamlit run app.py
   ```

## Security

Never upload your API keys or `.env` file to GitHub.

## Project Status

Currently under development. More features will be added, including structured JSON generation, model comparison, token tracking, latency monitoring, and error handling.

# LLM Application Playground

🚀 **Live Demo:** https://llm-application-playground.streamlit.app/

An interactive LLM playground built using Python, Streamlit, and Groq API.