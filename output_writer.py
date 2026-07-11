from openpyxl import load_workbook

class OutputWriter:

    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = load_workbook(file_path)
        self.sheet = self.workbook.active

        headers = [cell.value for cell in self.sheet[1]]

        self.company_col = headers.index("Company Name") + 1
        self.location_col = headers.index("Location") + 1
        self.email_col = headers.index("EMAIL") + 1

    def update_email(self, row_number, email):

        self.sheet.cell(row=row_number, column=self.email_col).value = email

    def save(self):

        self.workbook.save(self.file_path)