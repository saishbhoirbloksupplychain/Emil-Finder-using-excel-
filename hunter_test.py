from selenium_engine import start_browser, open_company_website
from email_hunter import hunt_email

driver = start_browser()

open_company_website(driver, "Infosys", "Bengaluru")

email = hunt_email(driver)

print("\nResult:", email)

input("Press Enter...")

driver.quit()