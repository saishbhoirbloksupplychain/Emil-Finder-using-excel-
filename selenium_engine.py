from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from domain_filter import is_good_domain

import time

BAD_DOMAINS = [
    "tofler.in",
    "justdial.com",
    "indiamart.com",
    "linkedin.com",
    "facebook.com",
    "instagram.com",
    "youtube.com",
    "twitter.com",
    "x.com",
    "wikipedia.org",
    "crunchbase.com",
    "zoominfo.com",
    "rocketreach.co",
    "signalhire.com",
    "glassdoor.com"
]


def start_browser():

    options = Options()

    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


def open_company_website(driver, company, location):

    query = f"{company} {location} India"

    driver.get(f"https://www.google.com/search?q={query}")

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
    )

    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:

        href = link.get_attribute("href")

        if not href:
            continue

        href = href.lower()

        if "http" not in href:
            continue

        if "google." in href:
            continue

        if not is_good_domain(href):
            print("skipping:", href)
            continue
        print("Opening:", href)

        # Try the original URL
        try:
            driver.get(href)
        except Exception:
            # if navigation fails, skip to next link
            continue

        time.sleep(3)

        # If Chrome shows an SSL warning, try removing 'www.'
        if "privacyerror" in driver.current_url or "Your connection is not private" in driver.page_source:
            if "://www." in href:
                new_url = href.replace("://www.", "://")
                print("SSL warning detected. Trying:", new_url)
                try:
                    driver.get(new_url)
                except Exception:
                    continue
                time.sleep(3)

        # At this point we've opened a candidate site
        return True

    # No suitable link found
    return False