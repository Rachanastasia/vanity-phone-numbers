hash = {
    '0': None,
    '1': None,
    '2': (['a', 'b', 'c', '2']),
    '3': (['d', 'e', 'f', '3']),
    '4': (['g', 'h', 'i', '4']),
    '5': (['j', 'k', 'l', '5']),
    '6': (['m', 'n', 'o', '6']),
    '7': (['p', 'q', 'r', 's', '7']),
    '8': (['t', 'u', 'v', '8']),
    '9': (['w', 'x', 'y', 'z', '9'])
}

def make_items_new_list_items(list, num):
    #return set
    #loop through set and add to set
    #remove item from set
    #duplicate base item
    

    #return all values in set

def change_list_items(list, add_char):
    for i in range(0, len(list)): 
        list[i] = list[i] + add_char
    return list



def find_vanity_numbers(num, word):
    combos = [] #different letter combinations

#make set to return all valid letters 

    i=0 #idx for letters in words
    for n in num: 
        if i >= len(word):
            # new_list =  
            print('HANDLE THIS')
        elif word[i] in hash[n]:
            combos = change_list_items(combos, word[i])
            i+=1 #handle case when i > len
        else: 
            #return a list of matching strings







# loop through numbers
# check against dict
# if first num doesn't match first word, match next

# if valid match of whole word is found, find all other letter combinations by 
# reaching into table and looping through the set, returning all



find_vanity_numbers('228', 'cat')
find_vanity_numbers('2283', 'cat')
find_vanity_numbers('52283', 'cat')
find_vanity_numbers('242287', '4cats')