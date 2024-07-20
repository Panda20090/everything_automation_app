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
from notifications import notify, send_email, generate_report
from scheduler import schedule_tasks
import threading
from backup_restore import backup_database, restore_database
from dashboard import create_dashboard
from data_analysis import analyze_google_trends_data, analyze_twitter_data
from data_export import export_to_csv, export_to_excel, export_to_json
from data_security import generate_key, encrypt_file, decrypt_file
from log_management import setup_logging, log_info, log_error
from api_key_management import generate_key, encrypt_api_key, decrypt_api_key
from visualization_enhancements import enhanced_visualization
from data_sync import upload_to_dropbox, download_from_dropbox
from auth import create_user_table, register_user, verify_user
import sqlite3
from email_reporting import send_report
from cloud_backup import backup_to_gdrive, download_from_gdrive
from web_scraping import scrape_website
from advanced_charts import create_heatmap, create_histogram, create_pie_chart
from sentiment_analysis import analyze_file_sentiment
from model_training import train_model
from data_preprocessing import preprocess_data

class DataAutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Automation Application")
        create_user_table()
        setup_logging()
        self.create_login_register_frames()
        log_info("Application started")

    def create_login_register_frames(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.grid(row=0, column=0, padx=10, pady=10)

        self.register_frame = tk.Frame(self.root)
        self.register_frame.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0)
        tk.Label(self.login_frame, text="Password").grid(row=1, column=0)
        self.login_username = tk.Entry(self.login_frame)
        self.login_username.grid(row=0, column=1)
        self.login_password = tk.Entry(self.login_frame, show='*')
        self.login_password.grid(row=1, column=1)
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2)

        tk.Label(self.register_frame, text="Username").grid(row=0, column=0)
        tk.Label(self.register_frame, text="Password").grid(row=1, column=0)
        self.register_username = tk.Entry(self.register_frame)
        self.register_username.grid(row=0, column=1)
        self.register_password = tk.Entry(self.register_frame, show='*')
        self.register_password.grid(row=1, column=1)
        self.register_button = tk.Button(self.register_frame, text="Register", command=self.register)
        self.register_button.grid(row=2, column=0, columnspan=2)

        self.main_frame = None

    def show_main_interface(self):
        if self.main_frame is not None:
            self.main_frame.destroy()
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)
        self.create_main_interface()

    def create_main_interface(self):
        # Create buttons for each automation task in the main frame
        self.main_buttons = [
            ("Define Goals and Objectives", self.define_goals),
            ("Conduct Market Research", self.market_research),
            ("Evaluate Available Resources", self.evaluate_resources),
            ("Plan Content Strategy", self.create_content_calendar),
            ("Generate Google Trends Report", self.create_google_trends_report),
            ("Generate Twitter Report", self.create_twitter_report),
            ("Retrieve Google Trends Data", self.retrieve_google_trends),
            ("Retrieve Twitter Data", self.retrieve_twitter),
            ("Process Google Trends Data", self.process_google_trends),
            ("Process Twitter Data", self.process_twitter),
            ("Visualize Google Trends Data", self.visualize_google_trends),
            ("Visualize Twitter Data", self.visualize_twitter),
            ("Publish to Medium", self.publish_medium),
            ("Publish to WordPress", self.publish_wordpress),
            ("Publish to Twitter", self.publish_twitter),
            ("Track Performance Metrics", self.track_metrics),
            ("Analyze Feedback", self.analyze_feedback),
            ("Clean Google Trends Data", self.clean_google_trends),
            ("Clean Twitter Data", self.clean_twitter),
            ("Store Google Trends Data", self.store_google_trends_data),
            ("Store Twitter Data", self.store_twitter_data),
            ("Query Google Trends Data", self.query_google_trends_data),
            ("Query Twitter Data", self.query_twitter_data),
            ("Send Email Notification", self.send_email),
            ("Generate Report", self.generate_report),
            ("Start Scheduler", self.start_scheduler),
            ("Backup Database", self.backup_database),
            ("Restore Database", self.restore_database),
            ("Launch Dashboard", self.launch_dashboard),
            ("Analyze Google Trends Data", self.analyze_google_trends),
            ("Analyze Twitter Data", self.analyze_twitter),
            ("Export Google Trends to CSV", self.export_google_trends_csv),
            ("Export Google Trends to Excel", self.export_google_trends_excel),
            ("Export Google Trends to JSON", self.export_google_trends_json),
            ("Generate Encryption Key", self.generate_key),
            ("Encrypt Data File", self.encrypt_file),
            ("Decrypt Data File", self.decrypt_file),
            ("Generate API Key Encryption Key", self.generate_api_key_key),
            ("Encrypt API Key", self.encrypt_api_key),
            ("Decrypt API Key", self.decrypt_api_key),
            ("Enhanced Google Trends Visualization", self.enhanced_google_trends),
            ("Enhanced Twitter Visualization", self.enhanced_twitter),
            ("Upload to Dropbox", self.upload_to_dropbox),
            ("Download from Dropbox", self.download_from_dropbox),
            ("Send Email Report", self.send_email_report),
            ("Backup to Google Drive", self.backup_to_gdrive),
            ("Download from Google Drive", self.download_from_gdrive),
            ("Scrape Website", self.scrape_website),
            ("Generate Heatmap", self.generate_heatmap),
            ("Generate Histogram", self.generate_histogram),
            ("Generate Pie Chart", self.generate_pie_chart),
            ("Analyze Sentiment", self.analyze_sentiment),
            ("Train Model", self.train_model),
            ("Preprocess Data", self.preprocess_data),
        ]

        for i, (text, command) in enumerate(self.main_buttons):
            tk.Button(self.main_frame, text=text, command=command).grid(row=i, column=0, padx=10, pady=5, sticky='ew')

        # Create frame for graphs/charts
        self.chart_frame = ttk.LabelFrame(self.main_frame, text="Graphs/Charts")
        self.chart_frame.grid(row=0, column=1, rowspan=15, padx=10, pady=10)

        # Create output text window
        self.output_text = scrolledtext.ScrolledText(self.main_frame, width=50, height=20)
        self.output_text.grid(row=15, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.login_username.get()
        password = self.login_password.get()
        if verify_user(username, password):
            self.login_frame.grid_forget()
            self.register_frame.grid_forget()
            self.show_main_interface()
            self.output_text.insert(tk.END, "Login successful.\n")
        else:
            self.output_text.insert(tk.END, "Login failed.\n")

    def register(self):
        username = self.register_username.get()
        password = self.register_password.get()
        try:
            register_user(username, password)
            self.output_text.insert(tk.END, "Registration successful.\n")
        except sqlite3.IntegrityError:
            self.output_text.insert(tk.END, "Registration failed: Username already exists.\n")

    # Define the functions for each button below...

    def define_goals(self):
        try:
            goals = {
                "goal1": "Generate $500 monthly passive income through AI-driven content.",
                "goal2": "Automate 80% of the content creation process."
            }
            with open('data/goals.json', 'w') as f:
                json.dump(goals, f)
            self.output_text.insert(tk.END, "Goals and objectives defined and stored in goals.json.\n")
            log_info("Goals and objectives defined.")
            notify("Task Completed", "Goals and objectives have been defined.")
            send_email("Task Completed", "Goals and objectives have been defined.", "recipient@example.com")
        except Exception as e:
            self.output_text.insert(tk.END, f"Error defining goals: {e}\n")
            log_error(f"Error defining goals: {e}")

    def market_research(self):
        try:
            data = {
                "keyword": "AI content creation",
                "volume": 10000,
                "competition": "low"
            }
            with open('data/market_research.json', 'w') as f:
                json.dump(data, f)
            self.output_text.insert(tk.END, "Market research conducted and stored in market_research.json.\n")
            log_info("Market research conducted.")
            notify("Task Completed", "Market research has been conducted.")
            report = generate_report('data/market_research.json', 'reports/market_research_report.txt')
            send_email("Task Completed", report, "recipient@example.com")
        except Exception as e:
            self.output_text.insert(tk.END, f"Error conducting market research: {e}\n")
            log_error(f"Error conducting market research: {e}")

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
        rows = query_data(conn, query)  # Ensure rows is defined here
        for row in rows:
            self.output_text.insert(tk.END, f"{row}\n")

    def query_twitter_data(self):
        conn = setup_database()
        query = "SELECT * FROM twitter"
        rows = query_data(conn, query)  # Ensure rows is defined here
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

    def export_google_trends_csv(self):
        df = pd.read_csv('data/cleaned_google_trends_data.csv')
        file_path = export_to_csv(df, 'data/exported_google_trends_data.csv')
        self.output_text.insert(tk.END, f"Google Trends data exported to {file_path}.\n")

    def export_google_trends_excel(self):
        df = pd.read_csv('data/cleaned_google_trends_data.csv')
        file_path = export_to_excel(df, 'data/exported_google_trends_data.xlsx')
        self.output_text.insert(tk.END, f"Google Trends data exported to {file_path}.\n")

    def export_google_trends_json(self):
        df = pd.read_csv('data/cleaned_google_trends_data.csv')
        file_path = export_to_json(df, 'data/exported_google_trends_data.json')
        self.output_text.insert(tk.END, f"Google Trends data exported to {file_path}.\n")

    def generate_key(self):
        key = generate_key()
        self.output_text.insert(tk.END, "Encryption key generated and stored in data/secret.key.\n")

    def encrypt_file(self):
        file_path = 'data/cleaned_google_trends_data.csv'  # Example file to encrypt
        encrypted_file_path = encrypt_file(file_path)
        self.output_text.insert(tk.END, f"File {file_path} encrypted and stored as {encrypted_file_path}.\n")

    def decrypt_file(self):
        encrypted_file_path = 'data/cleaned_google_trends_data.csv.enc'  # Example encrypted file
        decrypted_file_path = decrypt_file(encrypted_file_path)
        self.output_text.insert(tk.END, f"File {encrypted_file_path} decrypted and stored as {decrypted_file_path}.\n")

    def generate_api_key_key(self):
        generate_key()
        self.output_text.insert(tk.END, "API key encryption key generated and stored in data/secret.key.\n")

    def encrypt_api_key(self):
        api_key = 'your_api_key'  # Replace this with the actual API key to encrypt
        encrypt_api_key(api_key)
        self.output_text.insert(tk.END, "API key encrypted and stored in data/encrypted_api_key.enc.\n")

    def decrypt_api_key(self):
        decrypted_api_key = decrypt_api_key()
        self.output_text.insert(tk.END, f"Decrypted API key: {decrypted_api_key}\n")

    def enhanced_google_trends(self):
        fig = enhanced_visualization('data/cleaned_google_trends_data.csv', chart_type='line', title='Enhanced Google Trends Data')
        fig.show()
        self.output_text.insert(tk.END, "Enhanced Google Trends visualization generated.\n")

    def enhanced_twitter(self):
        fig = enhanced_visualization('data/cleaned_twitter_data.csv', chart_type='scatter', title='Enhanced Twitter Data')
        fig.show()
        self.output_text.insert(tk.END, "Enhanced Twitter visualization generated.\n")

    def upload_to_dropbox(self):
        local_file = 'data/cleaned_google_trends_data.csv'  # Example file to upload
        dropbox_path = '/data/cleaned_google_trends_data.csv'
        access_token = 'your_dropbox_access_token'  # Replace with your actual access token
        message = upload_to_dropbox(local_file, dropbox_path, access_token)
        self.output_text.insert(tk.END, f"{message}\n")

    def download_from_dropbox(self):
        dropbox_path = '/data/cleaned_google_trends_data.csv'
        local_file = 'data/downloaded_google_trends_data.csv'
        access_token = 'your_dropbox_access_token'  # Replace with your actual access token
        message = download_from_dropbox(dropbox_path, local_file, access_token)
        self.output_text.insert(tk.END, f"{message}\n")

    def send_email_report(self):
        send_report()
        self.output_text.insert(tk.END, "Email report sent.\n")

    def backup_to_gdrive(self):
        local_file = 'data/data_automation.db'  # Example file to upload
        drive_folder_id = 'your_drive_folder_id'  # Replace with your actual Google Drive folder ID
        message = backup_to_gdrive(local_file, drive_folder_id)
        self.output_text.insert(tk.END, f"{message}\n")

    def download_from_gdrive(self):
        file_id = 'your_file_id'  # Replace with your actual Google Drive file ID
        local_path = 'data/downloaded_data_automation.db'
        message = download_from_gdrive(file_id, local_path)
        self.output_text.insert(tk.END, f"{message}\n")

    def scrape_website(self):
        url = 'https://example.com'  # Replace with the actual URL
        target_element = 'div'  # Replace with the actual target element
        target_class = 'target-class'  # Replace with the actual target class
        file_path = scrape_website(url, target_element, target_class)
        if file_path:
            self.output_text.insert(tk.END, f"Data scraped and stored in {file_path}.\n")
        else:
            self.output_text.insert(tk.END, "Failed to scrape data from the website.\n")

    def generate_heatmap(self):
        file_path = 'data/cleaned_google_trends_data.csv'
        fig = create_heatmap(file_path, title='Google Trends Heatmap')
        fig.show()
        self.output_text.insert(tk.END, "Heatmap generated.\n")

    def generate_histogram(self):
        file_path = 'data/cleaned_google_trends_data.csv'
        fig = create_histogram(file_path, column='normalized_value', title='Google Trends Histogram')
        fig.show()
        self.output_text.insert(tk.END, "Histogram generated.\n")

    def generate_pie_chart(self):
        file_path = 'data/cleaned_twitter_data.csv'
        fig = create_pie_chart(file_path, column='text', title='Twitter Pie Chart')
        fig.show()
        self.output_text.insert(tk.END, "Pie chart generated.\n")

    def analyze_sentiment(self):
        file_path = 'data/cleaned_twitter_data.csv'
        output_file = analyze_file_sentiment(file_path)
        self.output_text.insert(tk.END, f"Sentiment analysis complete. Results stored in {output_file}.\n")

    def train_model(self):
        file_path = 'data/sentiment_analysis.csv'
        target_column = 'Sentiment'
        accuracy, model_path = train_model(file_path, target_column)
        self.output_text.insert(tk.END, f"Model trained with accuracy: {accuracy:.2f}\nModel saved to {model_path}\n")

    def preprocess_data(self):
        file_path = 'data/sentiment_analysis.csv'
        target_column = 'Sentiment'
        preprocessed_file = preprocess_data(file_path, target_column)
        self.output_text.insert(tk.END, f"Data preprocessed and stored in {preprocessed_file}\n")
        notify("Task Completed", "Data preprocessing is complete.")
        report = generate_report(preprocessed_file, 'reports/preprocessed_data_report.txt')
        send_email("Task Completed", report, "recipient@example.com")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataAutomationApp(root)
    root.mainloop()
