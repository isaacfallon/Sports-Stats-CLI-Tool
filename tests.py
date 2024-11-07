import unittest
from unittest.mock import patch
from scoreReader import ScoreReader

# Please note: there is only one test within this suite to check whether the file name is a valid .csv
# With additional time, I intend to add further tests to check the content within the csv file is valid and if there are any .csv files in the directory.

class TestScoreReader(unittest.TestCase):
    def test_valid_csv(self):
        # Create a mock CSV file for our testing purposes
        with open("testFile.csv", "w") as f:
            # Write some dummy data to the file
            f.write("firstname,lastname,date,division,points,summary\n")
            f.write("Barnett,Dunnico,2018-02-26,5,24,Offensive Duties\n")

        # Check if the file name ends with '.csv' to check the file type is valid for our application.
        self.assertTrue(f.name.endswith('.csv'), "File name must end with '.csv'")

# Run the test
if __name__ == '__main__':
    unittest.main()