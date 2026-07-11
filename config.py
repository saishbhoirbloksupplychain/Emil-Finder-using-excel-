# config.py

SEARCH_DELAY = 3
PAGE_DELAY = 4

AUTO_SAVE_AFTER = 10

HEADLESS = False

OUTPUT_FILE = "companies_with_emails.xlsx"

LOG_FILE = "email_finder.log"

BAD_DOMAINS = [
    "indiamart.com",
    "justdial.com",
    "tradeindia.com",
    "facebook.com",
    "linkedin.com",
    "youtube.com",
    "exportersindia.com",
    "alibaba.com"
]

CONTACT_PATHS = [
    "/contact",
    "/contact-us",
    "/about",
    "/about-us",
    "/support",
    "/help",
    "/reach-us",
    "/corporate",
    "/office",
    "/careers"
]

GOOD_EMAIL_PREFIX = [
    "info@",
    "contact@",
    "sales@",
    "support@",
    "office@",
    "admin@",
    "marketing@",
    "hr@"
]

BAD_EMAIL_WORDS = [
    "noreply",
    "alert",
    "security",
    "privacy",
    "abuse",
    "spam"
]