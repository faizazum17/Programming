#function that given string, return the score of the string
def high_score(arr):
    #your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    score = 0
    high_score = 0
    high_score_word = ""
    for word in arr.split():
        for letter in word:
            score += alphabet.index(letter) + 1
            if score > high_score:
                high_score = score
                high_score_word = word
        score = 0
    return high_score_word

#test
print(high_score('man i need a taxi up to ubud'), 'taxi')
print(high_score('what time are we climbing up the volcano'), 'volcano')

