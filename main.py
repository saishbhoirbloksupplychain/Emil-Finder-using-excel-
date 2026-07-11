from excel_handler import ExcelHandler
from output_writer import OutputWriter
from selenium_engine import start_browser, open_company_website
from contact_finder import open_contact_page
from email_hunter import hunt_email
from logger import *

EXCEL_FILE = "companies.xlsx"

setup_logger()

excel = ExcelHandler(EXCEL_FILE)
writer = OutputWriter(EXCEL_FILE)

driver = start_browser()

total = excel.total_rows()

try:

    for row in range(2, total + 1):

        if excel.has_email(row):
            print(f"[{row}/{total}] Skipped (Already has email)")
            continue

        company, location = excel.get_company(row)

        log_info(f"[{row}/{total}] Searching: {company} - {location}")

        try:

            open_company_website(driver, company, location)
            print("Current URL:", driver.current_url)
            print("Page title:", driver.title)
            email = hunt_email(driver, company)

            if email:

                writer.update_email(row, email)
                log_success(company, email)

            else:

                log_failed(company)

            # Auto save every 10 companies
        # Save after every company
            writer.save()
            log_info(f"Progress saved at row {row}")

        except Exception as e:

            log_error(f"{company}: {str(e)}")
            writer.save()
            continue

    writer.save()

finally:

    driver.quit()

print("Finished processing all companies.")