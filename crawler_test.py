from selenium_engine import start_browser, open_company_website
from crawler import collect_pages

driver = start_browser()

open_company_website(driver, "Infosys", "Bengaluru")

pages = collect_pages(driver)

print("\nPages Found:\n")

for page in pages:
    print(page)

input("Press Enter...")
driver.quit()