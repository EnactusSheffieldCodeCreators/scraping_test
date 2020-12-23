"""

"""
import pytest
from csv_handler import CSVHandler

EMAIL_FILE_LOCATION = "data/email-list.csv"

# Marked to skip as this function is a utility for the 
# other tests to use.
@pytest.mark.skip
def testCommitteeExists(committee):
    """
    Args:
        committee: list of information about a committee.

    Returns:
        boolean which is true if and only if the committe 
        is in the CSV file.
    """
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
    # Test if spesific known data is in the CSV.
    def testWelfareCommitteeExists(self):
        welfareCommittee = ["Welfare Committee",
                            "welfare.committee@sheffield.ac.uk"]
        assert testCommitteeExists(welfareCommittee)

    def testBoardGamesSocietyExists(self):
        boardGamesSociety = ["Board Games Society", "boardsoc@sheffield.ac.uk"]
        assert testCommitteeExists(boardGamesSociety)

    # Test if the number of societies in the CSV is about expected.
    def testNumbersAreRoughlyCorrect(self):
        emailFile = CSVHandler(EMAIL_FILE_LOCATION)
        contents = emailFile.read()
        socCount = len(contents)
        assert socCount > 380
        assert socCount < 400
