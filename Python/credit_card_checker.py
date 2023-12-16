#write function to check if a card is valid or not using luhn algorithm
card = "8895 6238 9323 4311"

def valid_card(card):
    card = card.replace(" ", "")
    card = card[::-1]
    card = list(card)
    card = [int(i) for i in card]
    
    #double second other digit
    for i in range(1, len(card), 2):
        card[i] = card[i] * 2
        if card[i] > 9:
            card[i] = card[i] - 9
   
    #sum all digits
    sum_card = sum(card)
    
    #check if sum is divisible by 10
    if sum_card % 10 == 0:
        return True
    else:
        return False

