import logging
import os 
from datetime import datetime

# Use valid characters for filenames (- instead of / and _ instead of :)
LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"

# Find the project root directory (assuming this code is in src/logger.py)
# This gets the parent directory of the current file's directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create logs directory path at the project root level
logs_dir = os.path.join(project_root, "logs")

# Create logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Create full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)