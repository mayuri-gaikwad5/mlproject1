import logging
import os
from datetime import datetime

import logging
import os
from datetime import datetime

# Step 1: Create log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Create logs folder path
logs_dir = os.path.join(os.getcwd(), "logs")

# Step 3: Create only the directory
os.makedirs(logs_dir, exist_ok=True)

# Step 4: Create full file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Step 5: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")