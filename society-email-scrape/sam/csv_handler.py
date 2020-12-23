import csv

class CSVHandler:
    fileLocation = ""

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        # self.fileRead = open(fileLocation, "r")
        # self.fileWrite = open(fileLocation, "w")

    def read(self):
        file = open(self.fileLocation, "r")
        reader = csv.reader(file)
        rows = []
        for row in reader:
            rows.append(row)
        return rows

    def write(self, list):
        file = open(self.fileLocation, "w")
        writer = csv.writer(file, dialect='excel')
        writer.writerows(list)