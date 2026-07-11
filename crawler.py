from selenium.webdriver.common.by import By
from urllib.parse import urljoin, urlparse

KEYWORDS = [
    "contact",
    "contact us",
    "about",
    "about us",
    "support",
    "career",
    "careers",
    "location",
    "locations",
    "office",
    "reach us"
]

SKIP = [
    ".pdf",
    "javascript:",
    "mailto:",
    "#"
]
GOOD_PAGES = [
    "contact",
    "about",
    "company",
    "corporate",
    "office",
    "location",
    "support",
    "help",
    "customer",
    "investor",
    "career"
]

BAD_PAGES = [
    "dealer",
    "dealers",
    "find-a-dealer",
    "find-dealer",
    "distributor",
    "retailer",
    "showroom",
    "store-locator",
    "buying-tools",
    "buy-now",
    "locate-us",
    "network",
    "channel-partner"
]
BAD_URLS = [
    "dealer",
    "dealership",
    "find-a-dealer",
    "request-quote",
    "request-demo",
    "click-to-buy",
    "book-test-drive",
    "buying-tools",
    "network",
    "showroom"
]

def collect_pages(driver):

    pages = []
    base = driver.current_url
    domain = urlparse(base).netloc

    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        try:
            href = link.get_attribute("href") or ""
            page = href.lower()

            if any(word in page for word in BAD_PAGES):
                print("Skipping dealer page:", href)
                continue
            text = (link.text or "").lower().strip()

            if not href:
                continue

            href = urljoin(base, href)

            # Stay on the same website
            if urlparse(href).netloc != domain:
                continue

            href_lower = href.lower()

            # Skip unwanted links
            if any(word in href_lower for word in SKIP):
                continue

            # Match either URL or visible text
            if any(word in href_lower or word in text for word in KEYWORDS):
                if href not in pages:
                    pages.append(href)

        except Exception:
            pass

    return pages[:10]