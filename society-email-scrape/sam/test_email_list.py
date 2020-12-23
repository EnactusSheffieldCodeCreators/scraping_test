import pytest
from csv_handler import CSVHandler

EMAIL_FILE_LOCATION = "data/email-list.csv"

@pytest.mark.skip
def testCommitteeExists(committee):
    emailFile = CSVHandler(EMAIL_FILE_LOCATION)
    contents = emailFile.read()
    isInList = False
    print(committee)
    for x in contents:
        print(x)
        if(x[0] == committee[0]):
            isInList = True
    return isInList


class TestEmailList:
    def testWelfareCommitteeExists(self):
        welfareCommittee = ["Welfare Committee",
                            "welfare.committee@sheffield.ac.uk"]
        assert testCommitteeExists(welfareCommittee)

    def testBoardGamesSocietyExists(self):
        boardGamesSociety = ["Board Games Society", "boardsoc@sheffield.ac.uk"]
        assert testCommitteeExists(boardGamesSociety)

    def testNumbersAreRoughlyCorrect(self):
        emailFile = CSVHandler(EMAIL_FILE_LOCATION)
        contents = emailFile.read()
        socCount = len(contents)
        assert socCount > 390
        assert socCount < 400
