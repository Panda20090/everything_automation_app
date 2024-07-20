from jinja2 import Environment, FileSystemLoader
import datetime

def generate_content(template_file, output_file, context):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)
    content = template.render(context)
    with open(output_file, 'w') as f:
        f.write(content)
    return output_file

def generate_google_trends_report():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    context = {'date': date}
    return generate_content('google_trends_template.html', 'data/google_trends_report.html', context)

def generate_twitter_report():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    context = {'date': date}
    return generate_content('twitter_template.html', 'data/twitter_report.html', context)
