#write roman numerals to integers
#input range 1-3999

def roman_to_int(roman):
    roman = roman.upper()
    roman_dict = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
    int_val = 0
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i-1]]:
            int_val += roman_dict[roman[i]] - 2 * roman_dict[roman[i-1]]
        else:
            int_val += roman_dict[roman[i]]
    return int_val

#write integers to roman numerals
def int_to_roman(n):
    roman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100:'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    roman = ''
    for i in roman_dict:
        roman += roman_dict[i] * (n//i)
        n %= i
    return roman

#refactored to oop
class RomanNumerals:
    def __init__(self):
        self.roman_dict = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        self.int_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100:'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    def from_roman(self, roman):
        roman = roman.upper()
        int_val = 0
        for i in range(len(roman)):
            if i > 0 and self.roman_dict[roman[i]] > self.roman_dict[roman[i-1]]:
                int_val += self.roman_dict[roman[i]] - 2 * self.roman_dict[roman[i-1]]
            else:
                int_val += self.roman_dict[roman[i]]
        return int_val
    
    def to_roman(self, n):
        roman = ''
        for i in self.int_dict:
            roman += self.int_dict[i] * (n//i)
            n %= i
        return roman
        