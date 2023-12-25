#function that return true if the string ends with the specified suffix, otherwise return false
def solution(str, end):
    return str.endswith(end)

#test
print(solution('abcde', 'cde')) # True
print(solution('abcde', 'abc')) # False
print(solution('abc', '')) # True
print(solution('abc', 'd')) # False
