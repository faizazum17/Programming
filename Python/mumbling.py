def accum(string):
    result = []
    for i in range(len(string)):
        result.append(string[i].upper() + string[i].lower() * i)
    return "-".join(result)

print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))