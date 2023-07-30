# This application thakes a string as an input and returns true or false
# for wether or not the string is composed of unique characters. For the
# purposes of this exercise all characters are considered including spaces,
# numbers and symbols.

def Is_Unique(test_string):
    '''Takes in a string and returns a boolean if each character is unique'''
    if len(test_string) == 0:
         return True # No duplicates
    
    for char in test_string:
         print("evaluating Character %s" %char)
         if test_string.count(char) > 1: 
             print("Duplicate character found! \'{char}\' was found more than once in string {string}".format(char=char, string=test_string))
             return False # Duplicate found! string is not unique
         else:
            print("Character {} is unique and not duplicated in the string".format(char))
    
    return True 

def Is_Unique_hash_table(test_string):
    '''takes in a string and generates a hash table with the character as a key and the value as the
    amount of times a character was duplicated. This results in a better understanding of all duplicated letters'''
    dict = {}
    for char in test_string:
        if char in dict.keys():
            continue
        dict[char] = string.count(char)
    return dict


# test code
strings_to_test = { "eve":False, 
                    "Beat":True,
                    "Bob":True,
                    "":True,
                    "  ":False,
                    "123456":True,
                    "!@#$%":True, 
                    "astonishing":False,
                    "I like to go boating on Sundays!": False}

for string, result in strings_to_test.items():
    is_unique = Is_Unique(string)
    print(Is_Unique_hash_table(string))
    if is_unique != result:
        print ("FAILED")
