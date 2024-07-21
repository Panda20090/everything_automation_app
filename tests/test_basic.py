import sys
import os
import pytest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.notifications import notify, send_email, generate_report
from app.data_preprocessing import preprocess_data

def test_notify():
    assert notify("Test", "This is a test notification") is None

@patch('app.notifications.smtplib.SMTP')
def test_send_email(mock_smtp):
    mock_smtp.return_value.login.return_value = True
    assert send_email("Test Subject", "Test Body", "recipient@example.com") is None

def test_generate_report():
    data_file = 'data/market_research.json'
    output_file = 'reports/test_report.txt'
    report = generate_report(data_file, output_file)
    assert "Report for" in report

def test_preprocess_data():
    file_path = 'data/sentiment_analysis.csv'
    target_column = 'Sentiment'
    preprocessed_file = preprocess_data(file_path, target_column)
    assert preprocessed_file == 'data/preprocessed_data.csv'
