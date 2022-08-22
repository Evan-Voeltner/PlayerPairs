import random

def GetSuffledDeck():
    unshuffled_deck = ['Ace', 'Ace', 'Ace', 'Ace', 'One', 'One', 'One', 'One',
    'Two', 'Two', 'Two', 'Two', 'Three', 'Three', 'Three', 'Three',
    'Four', 'Four', 'Four', 'Four', 'Five', 'Five', 'Five', 'Five', 'Five',
    'Six', 'Six', 'Six', 'Six', 'Seven', 'Seven', 'Seven', 'Seven',
    'Eight', 'Eight', 'Eight', 'Eight', 'Nine', 'Nine', 'Nine', 'Nine',
    'Ten', 'Ten', 'Ten', 'Ten', 'Jack', 'Jack', 'Jack', 'Jack', 'Jack',
    'Queen', 'Queen', 'Queen', 'Queen', 'King' 'King' 'King' 'King']
    
    shuffled_deck = []
    while len(shuffled_deck) != 52:
        card_to_add = unshuffled_deck.pop(random.randint(0,len(unshuffled_deck)-1))
        shuffled_deck.append(card_to_add)

    return shuffled_deck

print(GetSuffledDeck())