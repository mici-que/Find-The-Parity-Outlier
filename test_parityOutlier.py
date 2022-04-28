import parityOutlier

# 1
def test_parityOutlier_NoInput() -> None:
    """If no parameters passed, return False"""
    assert parityOutlier.find_outlier() == False , "no input, should return false"

def test_parityOutlier_WrongInputType() -> None:
    """paramter isn't a list, return False"""
    parameter="string"
    assert parityOutlier.find_outlier(parameter) == False , "input isn't list, should return false"

def test_parityOutlier_WrongListEntryType() -> None:
    """list entries are not ints, return False"""
    parameter=["1","2","3","4"]
    assert parityOutlier.find_outlier(parameter) == False , "list entries are not ints, should return false"    

def test_parityOutlier_ShortList() -> None:
    """list should have minimum 3 entries, return False"""
    parameter=[1,2]
    assert parityOutlier.find_outlier(parameter) == False , "list is too short, should return false"        