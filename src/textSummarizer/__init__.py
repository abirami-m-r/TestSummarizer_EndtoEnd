import os 
import logging
import sys
from datetime import datetime

log_dir = "logs"
log_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"

log_file_path = os.path.join(log_dir,f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}_continuous_logs.log")

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format = log_str,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("summarizerlogger")

