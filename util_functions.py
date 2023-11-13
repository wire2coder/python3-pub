# array_combiner.py

class UtilFunctions:

    @staticmethod # a 'class method' that 'everybody' can use
    def combine(array1, array2):
        return array1 + array2

    @staticmethod
    def reverse_string(string):
        return string[: : -1]
    
    @staticmethod
    def anagram_checker(string1, string2):

        # remove whitespace and lowered case letters
        string1, string2 = string1.replace(" ", "").lower(), string2.replace(" ", "").lower()    

        # make sure both strings are the same length
        if len(string1) != len(string2):
            return False

        # check if both strings have the same 'set' of letters
        if set(string1) != set(string2):
            return False



















