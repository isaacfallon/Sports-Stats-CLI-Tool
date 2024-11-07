# Import pathname module to allow pathname checking/manipulation
import os.path  
import csv

class ScoreReader:
    
    # Function to import csv manipulation module and display the contents of the csv file decided by the user.
    def process_CSV_file(file_input):
        print('records:\n')
        # Import the csv module, open the csv in 'read-only' and set a csv.DictReader object containing the file's rows to a variable.
        with open(file_input, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            # The csv.DictReader object is sorted based on row in ascending order and points in descending order. 
            # The sorted list is then limited to the top three results and saved to a variable.
            sortedData = sorted(reader, key=lambda row: (row['division'], -int(row['points'])))[:3]
                #  The variable containing the sorted data is displayed based on the data in its rows.
            for row in sortedData:
                print("name: " + row['firstname'], row['lastname'])
                print("details: in division " + row['division'] + " from " + row['date'] + " performing " + row['summary'] + row['points']+ "\n")

    # Start by prompting the user for a csv file name and check if the file exists. If it does, fun our CSV 
    file_input = input('Please enter the csv file name (without the file type extension) in this directory: ') + '.csv'
    check_file = os.path.isfile(file_input)
    if check_file:
        process_CSV_file(file_input)

        # Run a while loop if there is no file name detected. Once a file is found, run our importFoundCSV() function above to read the contents of the file. 
    while check_file is False:
        file_input = input('No CSV file found, please try again: ') + '.csv'
        check_file = os.path.isfile(file_input)
        if check_file:
            process_CSV_file(file_input)