import datetime
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def valid_date(data):
    try:
        date_obj = datetime.datetime.strptime(data, "%Y-%m-%d").date()
        current_date = datetime.date.today()
        return date_obj.year == current_date.year and date_obj >= current_date
    except ValueError:
        return False