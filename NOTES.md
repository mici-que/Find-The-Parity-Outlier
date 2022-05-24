# 1 input validation

- input is present, 
- input is list, 
- input entries are ints, 
- input lenght min 3

# 2 calculate

- create set from list
- create list with remainders of 2
- create counter for 0 and 1

assuming there might be none #GREEN
- loop remainder list and increment counters for 1 and 0 accordingly
- if not one of counters
- return the counter which is equal to 1

assuming there is always a parity outlier #REFACTOR
- loop remainder list:
    - if counter for this entry is 0 and other counter is > 1, return integer from original set
    - increment counter for this entry

