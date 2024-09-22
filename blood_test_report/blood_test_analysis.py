import os
from PyPDF2 import PdfReader
from crewai import Agent, Task
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()


llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash',
                            verbose=True,
                            temperature=0.5,
                            goggle_api_key=os.getenv('GOOGLE_API_KEY'))

# Extracting text from PDF blood report
def extract_blood_test_report(pdf_path, pages_to_extract):
    raw_text = ''
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in pages_to_extract:
            page = reader.pages[page_num - 1]
            content = page.extract_text()
            if content:
                raw_text += content
    return raw_text


# Create Blood Test Analyst Agent
blood_test_analyst = Agent(
    role='Blood Test Analyst',
    goal='Analyze the blood test report and summarize the findings.',
    backstory='A medical expert specializing in blood test analysis.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define Task for blood test analysis
def create_blood_test_task(raw_text):
    return Task(
        description=f'You have to analyze the blood test report from "{raw_text}" blood report.',
        expected_output='A summary of the blood test results.',
        agent=blood_test_analyst
    )


if __name__ == '__main__':
  text = extract_blood_test_report("drive/MyDrive/CrewAIAssignment/WM17S_blood_sample_test.pdf", [1])
  print(text)
