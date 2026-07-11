from selenium.webdriver.common.by import By
import time

PRIORITY = [
    "contact us",
    "contact",
    "support",
    "customer support",
    "customer service",
    "reach us",
    "locations",
    "corporate",
    "office",
    "about us",
    "about"
]

IGNORE = [
    "cookie",
    "privacy",
    "warning",
    "accept",
    "terms",
    "policy",
    "learn more",
    "login",
    "signin",
    "sign in"
]


def open_contact_page(driver):

    links = driver.find_elements(By.TAG_NAME, "a")

    candidates = []

    for link in links:

        try:
            text = link.text.strip().lower()

            if not text:
                continue

            if any(word in text for word in IGNORE):
                continue

            for keyword in PRIORITY:
                if keyword in text:
                    candidates.append((keyword, link))
                    break

        except:
            pass

    for keyword in PRIORITY:

        for k, link in candidates:

            if k != keyword:
                continue

            try:
                print("Opening:", link.text)

                driver.execute_script(
                    "arguments[0].scrollIntoView();",
                    link
                )

                time.sleep(1)

                driver.execute_script(
                    "arguments[0].click();",
                    link
                )

                time.sleep(4)

                return True

            except:
                continue

    return False