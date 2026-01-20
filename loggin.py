import logging
from datetime import datetime

# налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d"
)

# запис повідомлення
logging.info("Програма запущена")
