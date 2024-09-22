# Blood Test Analysis and Health Recommendations System
Overview 📝
This project automates the analysis of blood test reports, searches for relevant health articles, and provides health recommendations. It uses multiple agents to extract text from PDFs, find relevant articles, and deliver health advice based on findings. The project is powered by Python, Conda, Streamlit, Langchain, and Google Generative AI.

# Methodology ⚙️
Blood Test Analysis:

1. Extracts text from PDF blood test reports using PyPDF2.
Summarizes findings with the Google Generative AI model (gemini-1.5-flash).
Health Article Search:

2. Uses the SerperDevTool to search the internet for health-related articles based on blood test results.

3. Retrieves reliable information from trusted sources.Health Recommendations:

4. AI analyzes collected health articles to provide personalized health recommendations.
Email Delivery:

5. Sends an email containing the blood test summary, article links, and health recommendations using the Flask API and yagmail.

# Prerequisites 🔧
Make sure you have the following installed before setting up the project:

Python 3.8+
Conda for environment management
Insta

# Installation and Setup 🚀
1. Clone the Repository
# git clone https://github.com/your-repo/crewai_assignment.git
cd crewai_assignment

2. Set Up Conda Environment
# conda create --name crewai_assignment python=3.8
# conda activate crewai_assignment

3. Install Dependencies
# pip install -r requirements.txt

4. API Keys Configuration
Set the following environment variables either in a .env file or export them in your terminal:
GOOGLE_API_KEY: Your Google API key for the Generative AI model.
SERPER_API_KEY: Your Serper API key for web searches.
JWT_SECRET_KEY: Secret key for JWT authentication.

5. Run the Flask Application
# python email_api.py

6. Configure Ngrok
ngrok authtoken your_ngrok_token

# Project Structure 
1. requirements.txt: Lists all dependencies.
2. blood_test_analysis.py: Extracts and analyzes blood test reports.
3. article_search.py: Searches for relevant health-related articles.
4. health_recommendations.py: Provides personalized health recommendations.
5. crew_config.py: Configures the tasks and agents.
6. email_api.py: Flask API for user authentication and email reports.
7. main.py: Orchestrates the overall task execution.

# How to Run
1. Extract and Analyze Blood Test Report
# python blood_test_analysis.py

2. Search for Relevant Health Articles
# python article_search.py

3. Provide Health Recommendations
# python health_recommendations.py

4. Start the Flask API
# python email_api.py

API Usage 
Login:

Endpoint: /login
Method: POST
Content-Type: application/json


{
    "username": "user1",
    "password": "password1"
}

Send Blood Test Analysis via Email:

Endpoint: /send-analysis
Method: POST
Authorization: Bearer <token>
Content-Type: application/json

{
    "email": "recipient@example.com",
    "blood_test_report": "<base64_encoded_pdf>"
}



