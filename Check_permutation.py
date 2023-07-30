#Given two strings, write a method to decide if one is a permutation of the other.
# for example 'abc' and 'cab' are permutations of eachother.
# 'abc' and 'bad' are not as they contain different characters.

def Check_Permutations(string1, string2):
    '''Takes in 2 strings and returns true if both are permutations of the other
    This implementation is focused on only using exisisting data at the expense of
    operating time. Space efficient, but less time efficient'''
    for char in string1:
        if char not in string2:
            return False
    for char in string2:
        if char not in string1:
            return False
    return True
        
def Check_Permutations_2(string1, string2):
    '''Takes in 2 strings and returns true if both are permutations of the other
    This implementation is focused on reducing operating time by creating a set
    and only doing one for loop. Time efficient, but less space efficient'''
    list_of_characters = set(string1)
    list_of_characters.union(set(string2))
    for char in list_of_characters:
        if char not in string1:
            return False
        if char not in string2:
            return False
    return True


# test code
strings_to_test = { "abc": "bac",
                    "abc" : "bad",
                    " ": " ",
                    "": "",
                    "pop": "popopop"}

for string, string2 in strings_to_test.items():
    is_unique = Check_Permutations(string, string2)
    print("string \"{str1}\" and string \"{str2}\" permutation is {result}.".format(str1=string, str2=string2, result=is_unique))
    is_unique = Check_Permutations_2(string, string2)
    print("string \"{str1}\" and string \"{str2}\" permutation is {result}.".format(str1=string, str2=string2, result=is_unique))

