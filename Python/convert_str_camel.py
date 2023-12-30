#function that converts dash/underscore delimited words into camel casing
#the first word within the output should be capitalized only if the original word was capitalized. the next word always starts with a capital letter

#refactored
def to_camel(text):
    words = text.replace('-', '_').split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

#test
print(to_camel("the-stealth-warrior")) # "theStealthWarrior"
print(to_camel("The_Stealth_Warrior")) # "TheStealthWarrior"
print(to_camel("the_stealth_warrior")) # "theStealthWarrior"
print(to_camel("The-Stealth-Warrior")) # "TheStealthWarrior"˜