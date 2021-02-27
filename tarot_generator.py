import numpy as np
import random

# Major Arcana cards

major = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers', 'The Chariot', 'Justice', 'The Hermit', 'Wheel of Furtune', 'Strength', 'The Hanged Man', 'Death', 'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'The World']

# print(len(major))



#Minor Arcana Cards

minor = []
court = ['King', 'Queen', 'Knight', 'Jack']
numbers = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
# print(number)
court_numbers = court + numbers
# print(court_number)
cards = ['Wands', 'Cups', 'Swords', 'Pentacles']
for court_number in court_numbers:
    for card in cards:
        minor_card = court_number  + ' of ' + card
        minor.append(minor_card)

# print(minor)  
# print(len(minor))



#Integrate the whole card deck

card_deck = major + minor

# print(len(card_deck))


#User input

number_of_cards = int(input('How many cards do you want to draw?'))

#Time for playing!

results = random.sample(card_deck, number_of_cards)

# print(results)


result_with_reversion = []


for result in results:
    #Consider Reversal 
    reversed = False
    flip = int(np.round(random.random()))

    if flip == 1:
        reversed = True
    else: 
        reversed = False

    # print(reversed)

    if reversed:
        new_result = result + ', reversed'
    else:
        new_result = result
    result_with_reversion.append(new_result)

print(result_with_reversion)