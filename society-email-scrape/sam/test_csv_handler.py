import pytest
from csv_handler import CSVHandler

TEST_FILE_LOCATION = "data/test-csv.csv"
TEST_FILE_CONTENTS = [["1", "Peterson", "Bob", "bpeterson@gmail.com"], ["2", "Marley", "Bob", "bob.marley@yahoo.com"]]

class TestCSVHandler:
    testFile = CSVHandler(TEST_FILE_LOCATION)

    def testOpenFile(self):
        assert self.testFile != None
    
    def testRead(self):
        contents = self.testFile.read()
        print(contents)
        
        assert contents == TEST_FILE_CONTENTS

    def testWrite(self):
        self.testFile.write([])
        contents = self.testFile.read()
        assert contents == []

        self.testFile.write(TEST_FILE_CONTENTS)
        contents = self.testFile.read()
        assert contents == TEST_FILE_CONTENTS
