import logging
import os

# Create a custom logger
logger = logging.getLogger("textSummarizerLogger")

# Set the default logging level
logger.setLevel(logging.INFO)

# Create a formatter for log messages
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Create a file handler
log_file = "logs/application.log"
os.makedirs(os.path.dirname(log_file), exist_ok=True)
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example usage
logger.info("This is an info message.")
logger.error("This is an error message.")