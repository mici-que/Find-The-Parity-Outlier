def     find_outlier( integers=None ):

    if findoutlier (integers) :
        if not ValidInput(integers):
            return False
        remaindersList = [x % 2 for x in integers]
        if sum(remaindersList) == 1:
            return integers[remaindersList.index(1)]
        else:
            return  integers[remaindersList.index(0)]

def ValidInput ( a=None ):
    if (
        "a" in vars()  # param defined
        and isinstance(a, list)  # param is list
        and len(a) >= 3  # list has at least 3 entries
        and (all(isinstance(n, int) for n in a))
    ):  # list entries are ints
        return True
def findoutlier(integers=None):
    return True