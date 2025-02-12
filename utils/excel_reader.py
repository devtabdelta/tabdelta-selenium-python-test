import openpyxl

class ExcelReader:
    @staticmethod
    def get_test_data(file_path, sheet_name):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        data = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append([cell if cell is not None else "" for cell in row])

        return data
