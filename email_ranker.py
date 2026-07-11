import email
import re
from urllib.parse import urlparse

GOOD_PREFIX = {
    "info": 100,
    "contact": 98,
    "customerservice": 96,
    "customer": 94,
    "support": 92,
    "sales": 90,
    "service": 88,
    "office": 85,
    "admin": 80,
    "marketing": 75,
    "hr": 70,
    "careers": 65,
    "helpdesk": 60
}

BAD_WORDS = [
    "noreply",
    "no-reply",
    "donotreply",
    "example",
    "sample",
    "test",
    "abc",
    "xyz",
    "lorem",
    "ipsum",
    "dummy",
    "placeholder",
    "privacy",
    "security",
    "alert",
    "abuse",
    "spam"
]
BAD_PREFIX = [
    "forms",
    "dealer",
    "retailer",
    "showroom",
    "telemarketing",
    "crm",
    "digital",
    "ceo",
    "chairman",
    "director",
    "president",
    "manager",
    "salesmanager",
    "trainer",
    "marketinghead",
    "webmaster",
    "postmaster",
    "admin1",
    "test",
    "demo"
]
FREE_EMAILS = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "live.com",
    "icloud.com"
]
BAD_CONTAINS = [
    ".",
    "ceo",
    "chairman",
    "director",
    "manager",
    "president",
    "engineer",
    "marketing",
    "telemarketing",
    "crm",
    "digital",
    "trainer",
    "forms"
]
def score_email(email):

    email = email.lower()

    if any(word in email for word in BAD_WORDS):
        return -1000

    username = email.split("@")[0]

    score = 0

    # Reject obvious personal names
    parts = username.replace("_", ".").replace("-", ".").split(".")

    if len(parts) >= 2:
        if len(parts[0]) > 2 and len(parts[1]) > 2:
            score -= 80

    # Reject unwanted prefixes
    BAD_PREFIX = [
        "ceo",
        "chairman",
        "president",
        "director",
        "manager",
        "founder",
        "owner",
        "employee",
        "admin1",
        "webmaster"
    ]

    for prefix in BAD_PREFIX:
        if username.startswith(prefix):
            score -= 100

    # Reject usernames containing these words
    BAD_CONTAINS = [
        "telemarketing",
        "crm",
        "ccm",
        "trainer",
        "digitalhead",
        "branch",
        "dealer",
        "showroom",
        "salesmanager",
        "executive",
        "marketinghead",
        "hrteam",
        "careerteam",
        "forms"
    ]

    for word in BAD_CONTAINS:
        if word in username:
            score -= 80

    # Good prefixes
    for prefix, value in GOOD_PREFIX.items():
        if username.startswith(prefix):
            score += value

    # Slight penalty for firstname.lastname
    if "." in username:
        score -= 10

    if len(username) > 20:
        score -= 5

    return score
import re

FREE_EMAILS = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "live.com",
    "icloud.com",
    "aol.com",
    "rediffmail.com"
]


def best_email(emails, company_name=""):

    if not emails:
        return ""

    emails = list(set(emails))

    company = company_name.lower()

    ignore = {
        "india",
        "limited",
        "ltd",
        "private",
        "pvt",
        "company",
        "co",
        "corporation",
        "motor",
        "motors",
        "industries",
        "industrial",
        "group"
    }

    keywords = [
        w for w in re.findall(r"[a-z]+", company)
        if len(w) > 2 and w not in ignore
    ]

    best = ""
    best_score = -9999

    for email in emails:

        score = score_email(email)

        username, domain = email.split("@")

        # Reject Gmail etc.
        if domain in FREE_EMAILS:
            score -= 1000

        # Company keyword in domain
        for word in keywords:
            if word in domain:
                score += 70

        # Company keyword in username
        for word in keywords:
            if word in username:
                score += 30

        print(f"{email} -> Score: {score}")

        if score > best_score:
            best_score = score
            best = email

    print(f"Selected: {best}\n")

    if best_score < 50:
        return ""

    return best