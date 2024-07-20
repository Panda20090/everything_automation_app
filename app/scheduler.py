import schedule
import time
from datetime import datetime
from content_generation import generate_google_trends_report, generate_twitter_report
from data_retrieval import retrieve_google_trends_data, retrieve_twitter_data
from data_processing import process_google_trends_data, process_twitter_data
from data_cleanup import clean_google_trends_data, clean_twitter_data
from data_visualization import visualize_data
from notifications import send_email

def job():
    print(f"Job started at {datetime.now()}")
    # Retrieve data
    retrieve_google_trends_data('your_google_trends_api_key', 'AI content creation')
    retrieve_twitter_data('your_twitter_api_key', 'AI content creation')
    # Process data
    process_google_trends_data('data/google_trends_data.json')
    process_twitter_data('data/twitter_data.json')
    # Clean data
    clean_google_trends_data('data/processed_google_trends_data.csv')
    clean_twitter_data('data/processed_twitter_data.csv')
    # Generate reports
    generate_google_trends_report()
    generate_twitter_report()
    # Visualize data
    visualize_data('data/cleaned_google_trends_data.csv', 'Google Trends Data', 'assets/charts/google_trends_visualization.png')
    visualize_data('data/cleaned_twitter_data.csv', 'Twitter Data', 'assets/charts/twitter_visualization.png')
    # Send notification
    send_email("Automated Data Report", "Your data report is ready.", "recipient@example.com")
    print(f"Job completed at {datetime.now()}")

def schedule_tasks():
    schedule.every().day.at("09:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
