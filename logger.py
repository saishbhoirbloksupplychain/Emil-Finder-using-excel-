import logging
import os
from datetime import datetime
from config import LOG_FILE


def setup_logger():

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename=os.path.join("logs", LOG_FILE),
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )


def log_info(message):
    logging.info(message)
    print("[INFO]", message)


def log_error(message):
    logging.error(message)
    print("[ERROR]", message)


def log_success(company, email):

    logging.info(
        f"SUCCESS | {company} | {email}"
    )

    print(f"✅ {company} -> {email}")


def log_failed(company):

    logging.warning(
        f"NOT FOUND | {company}"
    )

    print(f"❌ {company} -> Email Not Found")