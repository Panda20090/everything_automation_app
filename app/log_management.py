import logging

def setup_logging(log_file='data_automation.log'):
    logging.basicConfig(
        filename=log_file,
        filemode='a',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
