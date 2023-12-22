#validate user input password a string is alphanumeric with at least one digit, latin letters and digit and no spaces
#refactoreds
def alphanumeric(pw):
    return pw.isalnum() and any(x.isdigit() for x in pw) and any(x.isalpha() for x in pw) and not ' ' in pw

#test
print(alphanumeric("a")) # False
