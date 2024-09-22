from crewai import Agent, Task
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
import os

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
                            verbose=True,
                            temperature=0.5,
                            goggle_api_key=os.getenv('GOOGLE_API_KEY'))

# Define tools for article search
search_tool = SerperDevTool()
web_search_tool = tool = WebsiteSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-flash",
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
            ),
        ),
    )
)

# Create Article Researcher Agent
article_researcher = Agent(
    role='Article Researcher',
    goal='Search for health articles based on blood test results.',
    tools=[search_tool, web_search_tool],
    verbose=True,
    allow_delegation=False,
    llm=llm,
    backstory=(
        "The Article Researcher was created to help individuals make sense of their blood test results. "
        "Many people receive complex medical reports that they struggle to interpret. By leveraging advanced "
        "AI technologies, the agent aims to search for reliable health articles that explain what specific blood test values mean. "
        "This agent acts as a personal health researcher, bridging the gap between raw medical data and easily digestible insights, "
        "allowing users to make informed decisions about their health."
    )
)

# Define the Task to find articles
def create_article_search_task(analysis_result):
    return Task(
        description=f'Search for health articles based on the analysis: "{analysis_result}".',
        expected_output='A list of relevant health articles with links.',
        agent=article_researcher
    )
