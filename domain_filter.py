BAD_DOMAINS = {
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
    "glassdoor.com",
    "tradeindia.com",
    "exportersindia.com"
}


def is_good_domain(url):

    url = url.lower()

    for domain in BAD_DOMAINS:
        if domain in url:
            return False

    return True