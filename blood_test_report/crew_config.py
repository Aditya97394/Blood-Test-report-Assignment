from crewai import Crew
from blood_test_analysis import create_blood_test_task
from article_search import create_article_search_task
from health_recommendations import create_health_recommendations_task

# Define the crew and tasks
def create_crew(raw_text, analysis_result, article_list):
    blood_test_task = create_blood_test_task(raw_text)
    article_search_task = create_article_search_task(analysis_result)
    health_recommendations_task = create_health_recommendations_task(article_list)

    # Crew configuration
    crew = Crew(
        agents=[blood_test_task.agent, article_search_task.agent, health_recommendations_task.agent],
        tasks=[blood_test_task, article_search_task, health_recommendations_task],
        verbose=True
    )
    return crew
