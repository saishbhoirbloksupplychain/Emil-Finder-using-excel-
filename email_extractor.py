import re

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

BAD_WORDS = [
    "noreply",
    "no-reply",
    "donotreply",
    "alert",
    "security",
    "privacy",
    "abuse",
    "spam",
    "copyright",
    "webmaster",
    "example",
    "test",
    "abc",
    "xyz"
]
BAD_DOMAINS = [
    "kamalhyundai",
    "deephyundai",
    "triumphauto",
    "vsmotors",
    "pahwa",
    "capitalhyundai",
    "ramaahyundai",
    "unityhyundai",
    "dreamhyundai",
    "sunrisehyundai",
    "baggalink",
    "mrdeeksha",
    "himgiri",
    "shreemhyundai",
    "malwaautotech"
]

def extract_email(driver):

    html = driver.page_source.lower()

    emails = list(set(re.findall(EMAIL_REGEX, html)))

    good = []

    for email in emails:

        # Ignore image filenames
        if email.endswith((".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp")):
            continue

        if any(word in email for word in BAD_WORDS):
            continue

        good.append(email)

    return good