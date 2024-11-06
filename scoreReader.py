# Import pathname module to allow pathname checking/manipulation
import os.path  

# Function to import csv module and reveal the contents of the csv file name the user has input
def importFoundCSV():
    print('records:\n')
    import csv
    with open(fileInput, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # For each row in the csv file, we output the desired csv data
        for row in reader:
            print("name: " + row['firstname'], row['lastname'])
            print("details: in division " + row['division'] + " from " + row['date'] + " performing " + row['summary'] + "\n")

# The program starts by prompting the user for a file name. If the file name exists, run our importFoundCSV() function above to read the contents of the file. 
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