from jinja2 import Environment, FileSystemLoader
import datetime

def generate_google_trends_report():
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('google_trends_template.html')
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    context = {'date': date}
    content = template.render(context)
    output_file = 'data/google_trends_report.html'
    with open(output_file, 'w') as f:
        f.write(content)
    return output_file

def generate_twitter_report():
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('twitter_template.html')
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    context = {'date': date}
    content = template.render(context)
    output_file = 'data/twitter_report.html'
    with open(output_file, 'w') as f:
        f.write(content)
    return output_file
