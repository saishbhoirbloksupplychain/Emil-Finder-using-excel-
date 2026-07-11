from crawler import collect_pages
from email_extractor import extract_email
from email_ranker import best_email
import time


def hunt_email(driver, company_name):

    # ---------- Check Homepage ----------
    emails = extract_email(driver)

    if emails:
        print("Found:", emails)

        selected = best_email(
    emails,
    company_name,
    driver.current_url
)

        if selected:
            return selected

        print("Rejected. Continuing search...")

    # ---------- Crawl Important Pages ----------
    pages = collect_pages(driver)

    print(f"Checking {len(pages)} pages...")

    visited = set()

    for page in pages:

        if page in visited:
            continue

        visited.add(page)

        try:

            print("Visiting:", page)

            driver.get(page)

            time.sleep(2)

            emails = extract_email(driver)

            if not emails:
                continue

            print("Found:", emails)
            selected = best_email(
                emails,
                company_name,
                driver.current_url
            )

            if selected:
                return selected

            print("Rejected. Continuing search...")

        except Exception as e:
            print("Error:", e)
            continue

    return ""