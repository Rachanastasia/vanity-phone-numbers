# create dictionary to store num => letter conversions


hash = {
    0: None,
    1: None,
    2: {'a', 'b', 'c'},
    3: {'d', 'e', 'f'},
    4: {'g', 'h', 'i'},
    5: {'j', 'k', 'l'},
    6: {'m', 'n', 'o'},
    7: {'p', 'q', 'r', 's'},
    8: {'t', 'u', 'v'},
    9: {'w', 'x', 'y', 'z'}
}


def find_vanity_numbers(num, word):
# loop through numbers
# check against dict
# if first num doesn't match first word, match next



find_vanity_numbers('228', 'cat')
find_vanity_numbers('2283', 'cat')
find_vanity_numbers('52283', 'cat')
find_vanity_numbers('242287', '4cats')