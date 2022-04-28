def find_outlier (integers=None):
    if not ValidInput(integers): return False
    pass


def ValidInput(a=None):
    if ('a' in vars() # param defined
    and isinstance(a,list) # param is list
    and len(a)>=3 # list has at least 3 entries
    and (all(isinstance(n,int) for n in a))): # list entries are ints
       return True