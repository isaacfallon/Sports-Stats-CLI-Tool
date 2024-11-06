# Import pathname module to allow pathname checking/manipulation
import os.path  

# Function to import csv manipulation module and display the contents of the csv file decided by the user.
def importFoundCSV():
    print('records:\n')
    # Import the csv module, open the csv in 'read-only' and set a csv.DictReader object containing the file's rows to a variable.
    import csv
    with open(fileInput, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # The csv.DictReader object is sorted based on row in ascending order and points in descending order. The sorted list is limited to the top three results and saved to a variable.
        sortedData = sorted(reader, key=lambda row: (row['division'], -int(row['points'])))[:3]
            #  The variable containing the sorted data is displayed based on the data in its rows.
        for row in sortedData:
            print("name: " + row['firstname'], row['lastname'])
            print("details: in division " + row['division'] + " from " + row['date'] + " performing " + row['summary'] + row['points']+ "\n")

# The program is initialised by prompting the user for a file name. If the file name exists, run our importFoundCSV() function above to read the contents of the file. 
fileInput = input('Please enter the csv file name in this directory: ')
check_file = os.path.isfile(fileInput)
if check_file is True:
        importFoundCSV()

# Run a while loop if there is no file name detected. Once a file is found, run our importFoundCSV() function above to read the contents of the file. 
while check_file is False:
    fileInput = input('No file found, please try again: ')
    check_file = os.path.isfile(fileInput)
    if check_file is True:
        importFoundCSV()