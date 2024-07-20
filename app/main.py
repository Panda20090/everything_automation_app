import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import json
from jinja2 import Environment, FileSystemLoader
import datetime
from data_retrieval import retrieve_google_trends_data, retrieve_twitter_data
from data_processing import process_google_trends_data, process_twitter_data
from data_visualization import visualize_data
from content_generation import generate_google_trends_report, generate_twitter_report
from content_publishing import publish_to_medium, publish_to_wordpress, publish_to_twitter
from monitoring import track_metrics, analyze_feedback
from data_cleanup import clean_google_trends_data, clean_twitter_data
from data_storage import setup_database, insert_data, query_data
from notifications import send_email, generate_report
from scheduler import schedule_tasks
import threading
from backup_restore import backup_database, restore_database
from dashboard import create_dashboard
from data_analysis import analyze_google_trends_data, analyze_twitter_data





class DataAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Automation Application")
        self.create_widgets()

    def create_widgets(self):
        # Create buttons for each automation task
        self.create_button = tk.Button(self.root, text="Define Goals and Objectives", command=self.define_goals)
        self.create_button.grid(row=0, column=0, padx=10, pady=10)

        self.market_button = tk.Button(self.root, text="Conduct Market Research", command=self.market_research)
        self.market_button.grid(row=1, column=0, padx=10, pady=10)

        self.resource_button = tk.Button(self.root, text="Evaluate Available Resources", command=self.evaluate_resources)
        self.resource_button.grid(row=2, column=0, padx=10, pady=10)

        self.content_button = tk.Button(self.root, text="Plan Content Strategy", command=self.create_content_calendar)
        self.content_button.grid(row=3, column=0, padx=10, pady=10)

        self.google_trends_button = tk.Button(self.root, text="Generate Google Trends Report", command=self.create_google_trends_report)
        self.google_trends_button.grid(row=4, column=0, padx=10, pady=10)

        self.twitter_button = tk.Button(self.root, text="Generate Twitter Report", command=self.create_twitter_report)
        self.twitter_button.grid(row=5, column=0, padx=10, pady=10)

        self.retrieve_google_trends_button = tk.Button(self.root, text="Retrieve Google Trends Data", command=self.retrieve_google_trends)
        self.retrieve_google_trends_button.grid(row=6, column=0, padx=10, pady=10)

        self.retrieve_twitter_button = tk.Button(self.root, text="Retrieve Twitter Data", command=self.retrieve_twitter)
        self.retrieve_twitter_button.grid(row=7, column=0, padx=10, pady=10)

        self.process_google_trends_button = tk.Button(self.root, text="Process Google Trends Data", command=self.process_google_trends)
        self.process_google_trends_button.grid(row=8, column=0, padx=10, pady=10)

        self.process_twitter_button = tk.Button(self.root, text="Process Twitter Data", command=self.process_twitter)
        self.process_twitter_button.grid(row=9, column=0, padx=10, pady=10)

        self.visualize_google_trends_button = tk.Button(self.root, text="Visualize Google Trends Data", command=self.visualize_google_trends)
        self.visualize_google_trends_button.grid(row=10, column=0, padx=10, pady=10)

        self.visualize_twitter_button = tk.Button(self.root, text="Visualize Twitter Data", command=self.visualize_twitter)
        self.visualize_twitter_button.grid(row=11, column=0, padx=10, pady=10)

        self.generate_google_trends_report_button = tk.Button(self.root, text="Generate Google Trends Report", command=self.generate_google_trends_report)
        self.generate_google_trends_report_button.grid(row=12, column=0, padx=10, pady=10)

        self.generate_twitter_report_button = tk.Button(self.root, text="Generate Twitter Report", command=self.generate_twitter_report)
        self.generate_twitter_report_button.grid(row=13, column=0, padx=10, pady=10)

        self.publish_medium_button = tk.Button(self.root, text="Publish to Medium", command=self.publish_medium)
        self.publish_medium_button.grid(row=14, column=0, padx=10, pady=10)

        self.publish_wordpress_button = tk.Button(self.root, text="Publish to WordPress", command=self.publish_wordpress)
        self.publish_wordpress_button.grid(row=15, column=0, padx=10, pady=10)

        self.publish_twitter_button = tk.Button(self.root, text="Publish to Twitter", command=self.publish_twitter)
        self.publish_twitter_button.grid(row=16, column=0, padx=10, pady=10)

        self.track_metrics_button = tk.Button(self.root, text="Track Performance Metrics", command=self.track_metrics)
        self.track_metrics_button.grid(row=17, column=0, padx=10, pady=10)
    
        self.analyze_feedback_button = tk.Button(self.root, text="Analyze Feedback", command=self.analyze_feedback)
        self.analyze_feedback_button.grid(row=18, column=0, padx=10, pady=10)

        self.clean_google_trends_button = tk.Button(self.root, text="Clean Google Trends Data", command=self.clean_google_trends)
        self.clean_google_trends_button.grid(row=19, column=0, padx=10, pady=10)

        self.clean_twitter_button = tk.Button(self.root, text="Clean Twitter Data", command=self.clean_twitter)
        self.clean_twitter_button.grid(row=20, column=0, padx=10, pady=10)

        self.store_google_trends_button = tk.Button(self.root, text="Store Google Trends Data", command=self.store_google_trends_data)
        self.store_google_trends_button.grid(row=21, column=0, padx=10, pady=10)

        self.store_twitter_button = tk.Button(self.root, text="Store Twitter Data", command=self.store_twitter_data)
        self.store_twitter_button.grid(row=22, column=0, padx=10, pady=10)

        self.query_google_trends_button = tk.Button(self.root, text="Query Google Trends Data", command=self.query_google_trends_data)
        self.query_google_trends_button.grid(row=23, column=0, padx=10, pady=10)

        self.query_twitter_button = tk.Button(self.root, text="Query Twitter Data", command=self.query_twitter_data)
        self.query_twitter_button.grid(row=24, column=0, padx=10, pady=10)

        self.send_email_button = tk.Button(self.root, text="Send Email Notification", command=self.send_email)
        self.send_email_button.grid(row=25, column=0, padx=10, pady=10)

        self.generate_report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.generate_report_button.grid(row=26, column=0, padx=10, pady=10)

        self.start_scheduler_button = tk.Button(self.root, text="Start Scheduler", command=self.start_scheduler)
        self.start_scheduler_button.grid(row=27, column=0, padx=10, pady=10)

        self.backup_database_button = tk.Button(self.root, text="Backup Database", command=self.backup_database)
        self.backup_database_button.grid(row=28, column=0, padx=10, pady=10)

        self.restore_database_button = tk.Button(self.root, text="Restore Database", command=self.restore_database)
        self.restore_database_button.grid(row=29, column=0, padx=10, pady=10)

        self.launch_dashboard_button = tk.Button(self.root, text="Launch Dashboard", command=self.launch_dashboard)
        self.launch_dashboard_button.grid(row=30, column=0, padx=10, pady=10)

        self.analyze_google_trends_button = tk.Button(self.root, text="Analyze Google Trends Data", command=self.analyze_google_trends)
        self.analyze_google_trends_button.grid(row=31, column=0, padx=10, pady=10)

        self.analyze_twitter_button = tk.Button(self.root, text="Analyze Twitter Data", command=self.analyze_twitter)
        self.analyze_twitter_button.grid(row=32, column=0, padx=10, pady=10)







        # Create frame for graphs/charts
        self.chart_frame = ttk.LabelFrame(self.root, text="Graphs/Charts")
        self.chart_frame.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

        # Create output text window
        self.output_text = scrolledtext.ScrolledText(self.root, width=50, height=20)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def define_goals(self):
        goals = {
            "goal1": "Generate $500 monthly passive income through AI-driven content.",
            "goal2": "Automate 80% of the content creation process."
        }
        with open('data/goals.json', 'w') as f:
            json.dump(goals, f)
        self.output_text.insert(tk.END, "Goals and objectives defined and stored in goals.json.\n")

    def market_research(self):
        # Simulated market research data
        data = {
            "keyword": "AI content creation",
            "volume": 10000,
            "competition": "low"
        }
        with open('data/market_research.json', 'w') as f:
            json.dump(data, f)
        self.output_text.insert(tk.END, "Market research conducted and stored in market_research.json.\n")

    def evaluate_resources(self):
        resources = {
            "skills": ["Python", "AI", "Data Analysis"],
            "tools": ["Jupyter", "VS Code", "Google Analytics"]
        }
        with open('data/resources.json', 'w') as f:
            json.dump(resources, f)
        self.output_text.insert(tk.END, "Available resources evaluated and stored in resources.json.\n")

    def create_content_calendar(self):
        calendar = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2024', periods=30, freq='D'),
            'Content Type': ['Blog Post']*30
        })
        calendar.to_csv('data/content_calendar.csv', index=False)
        self.output_text.insert(tk.END, "Content calendar created and stored in content_calendar.csv.\n")
        self.show_chart(calendar)

    def show_chart(self, data):
        fig, ax = plt.subplots()
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        data['Count'] = 1
        data['Count'].plot(ax=ax)
        ax.set_title('Content Calendar')
        ax.set_ylabel('Number of Posts')
        ax.set_xlabel('Date')

        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    def generate_content(self, template_file, output_file, context):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(template_file)
        content = template.render(context)
        with open(output_file, 'w') as f:
            f.write(content)

    def create_google_trends_report(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        context = {'date': date}
        self.generate_content('google_trends_template.html', 'data/google_trends_report.html', context)
        self.output_text.insert(tk.END, "Google Trends report generated and stored in data/google_trends_report.html.\n")

    def create_twitter_report(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        context = {'date': date}
        self.generate_content('twitter_template.html', 'data/twitter_report.html', context)
        self.output_text.insert(tk.END, "Twitter report generated and stored in data/twitter_report.html.\n")

    def retrieve_google_trends(self):
        api_key = 'your_google_trends_api_key'
        keyword = 'AI content creation'
        data = retrieve_google_trends_data(api_key, keyword)
        self.output_text.insert(tk.END, "Google Trends data retrieved and stored in data/google_trends_data.json.\n")

    def retrieve_twitter(self):
        api_key = 'your_twitter_api_key'
        query = 'AI content creation'
        data = retrieve_twitter_data(api_key, query)
        self.output_text.insert(tk.END, "Twitter data retrieved and stored in data/twitter_data.json.\n")
    
    def process_google_trends(self):
        df = process_google_trends_data('data/google_trends_data.json')
        self.output_text.insert(tk.END, "Google Trends data processed and stored in data/processed_google_trends_data.csv.\n")
        self.show_chart(df)

    def process_twitter(self):
        df = process_twitter_data('data/twitter_data.json')
        self.output_text.insert(tk.END, "Twitter data processed and stored in data/processed_twitter_data.csv.\n")
        self.show_chart(df)

    def visualize_google_trends(self):
        output_file = visualize_data('data/processed_google_trends_data.csv', 'Google Trends Data', 'assets/charts/google_trends_visualization.png')
        self.output_text.insert(tk.END, f"Google Trends data visualized and saved to {output_file}.\n")
        self.show_image(output_file)

    def visualize_twitter(self):
        output_file = visualize_data('data/processed_twitter_data.csv', 'Twitter Data', 'assets/charts/twitter_visualization.png')
        self.output_text.insert(tk.END, f"Twitter data visualized and saved to {output_file}.\n")
        self.show_image(output_file)

    def show_image(self, image_path):
        img = tk.PhotoImage(file=image_path)
        img_label = tk.Label(self.chart_frame, image=img)
        img_label.image = img
        img_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def generate_google_trends_report(self):
        output_file = generate_google_trends_report()
        self.output_text.insert(tk.END, f"Google Trends report generated and stored in {output_file}.\n")

    def generate_twitter_report(self):
        output_file = generate_twitter_report()
        self.output_text.insert(tk.END, f"Twitter report generated and stored in {output_file}.\n")

    def publish_medium(self):
        title = "Your Report Title"
        with open('data/google_trends_report.html', 'r') as file:
            content = file.read()
        access_token = 'your_medium_access_token'
        response = publish_to_medium(title, content, access_token)
        self.output_text.insert(tk.END, f"Published to Medium: {response}\n")

    def publish_wordpress(self):
        title = "Your Report Title"
        with open('data/google_trends_report.html', 'r') as file:
            content = file.read()
        url = 'https://yourblog.wordpress.com/xmlrpc.php'
        username = 'your_username'
        password = 'your_password'
        post_id = publish_to_wordpress(title, content, url, username, password)
        self.output_text.insert(tk.END, f"Published to WordPress with post ID: {post_id}\n")

    def publish_twitter(self):
        with open('data/twitter_report.html', 'r') as file:
            content = file.read()
        api_key = 'your_api_key'
        api_secret_key = 'your_api_secret_key'
        access_token = 'your_access_token'
        access_token_secret = 'your_access_token_secret'
        status_id = publish_to_twitter(content, api_key, api_secret_key, access_token, access_token_secret)
        self.output_text.insert(tk.END, f"Published to Twitter with status ID: {status_id}\n")



    def track_metrics(self):
        metrics = track_metrics()
        self.output_text.insert(tk.END, f"Performance metrics tracked and stored in data/performance_metrics.json.\n")

    def analyze_feedback(self):
        feedback_file = 'data/feedback.json'
        analysis = analyze_feedback(feedback_file)
        self.output_text.insert(tk.END, f"Feedback analyzed and stored in data/feedback_analysis.json.\n")

    def clean_google_trends(self):
        df = clean_google_trends_data('data/processed_google_trends_data.csv')
        self.output_text.insert(tk.END, "Google Trends data cleaned and stored in data/cleaned_google_trends_data.csv.\n")
        self.show_chart(df)

    def clean_twitter(self):
        df = clean_twitter_data('data/processed_twitter_data.csv')
        self.output_text.insert(tk.END, "Twitter data cleaned and stored in data/cleaned_twitter_data.csv.\n")
        self.show_chart(df)


    def store_google_trends_data(self):
        conn = setup_database()
        df = pd.read_csv('data/cleaned_google_trends_data.csv')
        for index, row in df.iterrows():
            data = {
                'date': row['date'],
                'value': row['normalized_value']
            }
            insert_data(conn, 'google_trends', data)
        self.output_text.insert(tk.END, "Google Trends data stored in the database.\n")

    def store_twitter_data(self):
        conn = setup_database()
        df = pd.read_csv('data/cleaned_twitter_data.csv')
        for index, row in df.iterrows():
            data = {
                'created_at': row['created_at'],
                'text': row['text']
            }
            insert_data(conn, 'twitter', data)
        self.output_text.insert(tk.END, "Twitter data stored in the database.\n")

    def query_google_trends_data(self):
        conn = setup_database()
        query = "SELECT * FROM google_trends"
        rows = query_data(conn, query)
        for row in rows:
            self.output_text.insert(tk.END, f"{row}\n")

    def query_twitter_data(self):
        conn = setup_database()
        query = "SELECT * FROM twitter"
        rows = query_data(conn, query)
        for row in rows:
            self.output_text.insert(tk.END, f"{row}\n")

    def send_email(self):
        subject = "Automated Data Report"
        body = "Your data report is ready."
        to_email = "recipient@example.com"
        send_email(subject, body, to_email)
        self.output_text.insert(tk.END, "Email notification sent.\n")

    def generate_report(self):
        data_file = 'data/performance_metrics.json'
        output_file = 'data/performance_report.txt'
        report = generate_report(data_file, output_file)
        self.output_text.insert(tk.END, f"Report generated and stored in {output_file}.\n{report}\n")

    def start_scheduler(self):
        scheduler_thread = threading.Thread(target=schedule_tasks)
        scheduler_thread.start()
        self.output_text.insert(tk.END, "Scheduler started.\n")

    def backup_database(self):
        backup_path = backup_database()
        self.output_text.insert(tk.END, f"Database backed up to {backup_path}.\n")

    def restore_database(self):
        restore_path = restore_database()
        if restore_path:
            self.output_text.insert(tk.END, f"Database restored from {restore_path}.\n")
        else:
            self.output_text.insert(tk.END, "No backup found to restore.\n")

    def launch_dashboard(self):
        dashboard_thread = threading.Thread(target=create_dashboard)
        dashboard_thread.start()
        self.output_text.insert(tk.END, "Dashboard launched.\n")

    def analyze_google_trends(self):
        insights = analyze_google_trends_data('data/cleaned_google_trends_data.csv')
        self.output_text.insert(tk.END, f"Google Trends data analyzed. Insights stored in data/google_trends_insights.json.\n{insights}\n")

    def analyze_twitter(self):
        insights = analyze_twitter_data('data/cleaned_twitter_data.csv')
        self.output_text.insert(tk.END, f"Twitter data analyzed. Insights stored in data/twitter_insights.json.\n{insights}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = DataAutomationApp(root)
    root.mainloop()
