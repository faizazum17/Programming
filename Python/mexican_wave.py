#mexican wave, function that takes a string and returns a list of strings that show the string in a mexican wave
def wave (str):
    #your code here
    wave_list = []
    for i in range(len(str)):
        if str[i] != " ":
            wave_list.append(str[:i] + str[i].upper() + str[i+1:])
    return wave_list

#test
print(wave("hello"), ["Hello", "hEllo", "heLlo", "helLo", "hellO"])
print(wave("codewars"), ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"])
print(wave(""), [])