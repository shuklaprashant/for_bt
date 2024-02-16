import csv

class CSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_csv_file()

    def read_csv_file(self):
        try:
            data = []
            with open(self.file_path, 'r', newline='') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    data.append(row)
            return data
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return []
    
    def csv_header(self):
        return self.data[0]

    def filter_data(self, condition):
        try:
            filtered_data = [row for row in self.data if condition(row)]
            return filtered_data
        except Exception as e:
            print(f"An error occurred while filtering the data: {e}")
            return []
