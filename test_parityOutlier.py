import parityOutlier


# 1
def testparityOutlier_NoInput() -> None:
    """If no parameters passed, return False"""
    assert parityOutlier.findOutlier() is False, "no input, should return false"


def testparityOutlier_WrongInputType() -> None:
    """paramter isn't a list, return False"""
    parameter = "string"
    assert (
        parityOutlier.findOutlier(parameter) is False
    ), "input isn't list, should return false"


def testparityOutlier_WrongListEntryType() -> None:
    """list entries are not ints, return False"""
    parameter = ["1", "2", "3", "4"]
    assert (
        parityOutlier.findOutlier(parameter) is False
    ), "list entries are not ints, should return false"


def testparityOutlier_ShortList() -> None:
    """list should have minimum 3 entries, return False"""
    parameter = [1, 2]
    assert (
        parityOutlier.findOutlier(parameter) is False
    ), "list is too short, should return false"


# 2
def testparityOutlier_List0() -> None:
    """[1,1,2] -> 2"""
    parameter = [1, 1, 2]
    assert parityOutlier.findOutlier(parameter) == 2, "[1,1,2] -> 2"


def testparityOutlier_List1() -> None:
    """[2, 4, 6, 8, 10, 3] -> 3"""
    parameter = [2, 4, 6, 8, 10, 3]
    assert parityOutlier.findOutlier(parameter) == 3, "[2, 4, 6, 8, 10, 3] -> 3"
