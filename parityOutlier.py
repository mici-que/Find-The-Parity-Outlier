def findOutlier(integers=None):
    if validInput(integers):
        remaindersList = [x % 2 for x in integers]
        remaindersSum = sum(remaindersList)
        # remaindersSum = 1, return odd position integers(index of 1 in remaindersList)
        # remaindersSum > 1, return even position integers(index of 0 in remaindersList)
        #
        return integers[remaindersList.index(not bool(remaindersSum - 1))]
    return False


def validInput(a=None):
    return (
        "a" in vars()  # param defined
        and isinstance(a, list)  # param is list
        and len(a) >= 3  # list has at least 3 entries
        and (all(isinstance(n, int) for n in a))  # list entries are ints
    )


def function_not_covered(a):
    if a == None:
        return "none"
