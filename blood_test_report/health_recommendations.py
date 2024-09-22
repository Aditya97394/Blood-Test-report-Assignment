from crewai import Agent, Task
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
                            verbose=True,
                            temperature=0.5,
                            goggle_api_key=os.getenv('GOOGLE_API_KEY'))


# Create Health Advisor Agent
health_advisor = Agent(
    role='Health Advisor',
    goal='Provide health recommendations based on the articles found.',
    verbose=True,
    allow_delegation=False,
    llm=llm,
    backstory=(
        "The Health Advisor was developed to assist individuals in making sense of the vast amount of health information available online. "
        "After the Article Researcher locates relevant articles based on blood test results or other health data, the Health Advisor steps in "
        "to analyze that information and provide personalized recommendations. With an advanced understanding of medical literature, this agent "
        "was designed to empower users by delivering practical, actionable health advice tailored to their unique needs. It serves as a digital health guide, "
        "bridging the gap between research and personal wellness."
    )
)

# Define Task for health recommendations
def create_health_recommendations_task(article_list):
    return Task(
        description=f'Provide health recommendations based on the articles: "{article_list}".',
        expected_output='Health recommendations with links to the articles.',
        agent=health_advisor
    )
