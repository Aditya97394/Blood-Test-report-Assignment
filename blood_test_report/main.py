from crew_config import create_crew
from blood_test_analysis import extract_blood_test_report
import os
from dotenv import load_dotenv
load_dotenv()


def execute_crew(pdf_path, pages_to_extract):
    # Extract blood test report
    raw_text = extract_blood_test_report(pdf_path, pages_to_extract)

    # Placeholder for results, this should be run in sequence
    analysis_result = 'Blood test analysis result'
    article_list = ['List of articles based on analysis']

    # Create and run the crew
    crew = create_crew(raw_text, analysis_result, article_list)
    crew.kickoff()

    # Get results
    blood_test_summary = crew.tasks[0].output.raw_output
    found_articles = crew.tasks[1].output.raw_output
    recommendations = crew.tasks[2].output.raw_output

    return blood_test_summary, found_articles, recommendations


if __name__ == "__main__":
    pdf_path = "drive/MyDrive/CrewAIAssignment/WM17S_blood_sample_test.pdf"
    pages_to_extract = [1]
    execute_crew(pdf_path, pages_to_extract)
