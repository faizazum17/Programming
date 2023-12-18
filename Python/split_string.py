#split the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
def split_string(str):
    result =[]
    if len(str) % 2 != 0:
        str = str + "_"
    for i in range(0, len(str), 2):
        result.append(str[i:i+2])
    return result

#refacrored
def split_string2(str):
    return [str[i:i+2] for i in range(0, len(str), 2)]