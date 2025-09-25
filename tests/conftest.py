import os
import sys
import logging
import pathlib
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

# Ensure report directories exist
REPORT_DIR = pathlib.Path("reports")
REPORT_DIR.mkdir(exist_ok=True)

# Load .env from project root
load_dotenv(dotenv_path=pathlib.Path(__file__).resolve().parents[1] / ".env")

# Basic logging config
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(REPORT_DIR / "test_run.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger("tests")

BASE_URL = os.getenv("BASE_URL", "https://ecarla.pl")

@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    if os.getenv("HEADLESS", "1") == "1":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    logger.info("Starting Chrome WebDriver (headless=%s)", os.getenv("HEADLESS", "1"))
    driver = webdriver.Chrome(service=ChromeService(), options=options)
    yield driver
    logger.info("Quitting Chrome WebDriver")
    driver.quit()

@pytest.fixture()
def base_url():
    return BASE_URL