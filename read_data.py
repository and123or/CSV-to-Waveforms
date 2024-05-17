import pandas as pd
#import matplotlib.pyplot as plt
from tkinter import filedialog, Tk

def read_and_modify_csv_file():
    """  
    Open a file dialog to select a CSV file, modify it if necessary, and return the data.
    """
    try:
        Tk().withdraw()  # Hide the root window
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            print("No file selected")
            return None

        # Read the CSV file without skipping rows
        data = pd.read_csv(file_path)

        # Check if the header is already correct
        correct_headers = ['second', 'Volt1', 'Volt2', 'Volt3', 'Volt4']
        if list(data.columns)[:len(correct_headers)] == correct_headers[:len(data.columns)]:
            print("Headers are already correct.")
            return data        

        # Read the CSV file and drop the first 10 rows
        data = pd.read_csv(file_path, skiprows=10, header=None)

        # Determine the number of columns
        num_columns = data.shape[1]

        # Set new header based on the number of columns
        new_headers = ['second'] + [f'Volt{i}' for i in range(1, num_columns)]
        if num_columns < 2 or num_columns > 5:
            print(f"Unexpected number of columns: {num_columns}")
            return None
        data.columns = new_headers

        # Save the modified data back to the original file
        data.to_csv(file_path, index=False)
        print("File has been modified and saved successfully.")
        return data
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None
# Example usage:
if __name__ == "__main__":
    data = read_and_modify_csv_file()