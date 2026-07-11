from openpyxl import load_workbook

class ExcelHandler:

    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = load_workbook(file_path)
        self.sheet = self.workbook.active

        headers = [str(cell.value).strip() for cell in self.sheet[1]]

        self.company_col = headers.index("Company Name") + 1
        self.location_col = headers.index("Location") + 1
        self.email_col = headers.index("EMAIL") + 1

    def get_company(self, row):
        company = self.sheet.cell(row=row, column=self.company_col).value
        location = self.sheet.cell(row=row, column=self.location_col).value
        return company, location

    def total_rows(self):
        return self.sheet.max_row

    def has_email(self, row):
        value = self.sheet.cell(row=row, column=self.email_col).value

        if value is None:
            return False

        return str(value).strip() != ""