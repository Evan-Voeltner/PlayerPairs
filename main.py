import random
from turtle import update

def GetSuffledDeck():
    unshuffled_deck = ['Ace', 'Ace', 'Ace', 'Ace', 'One', 'One', 'One', 'One',
    'Two', 'Two', 'Two', 'Two', 'Three', 'Three', 'Three', 'Three',
    'Four', 'Four', 'Four', 'Four', 'Five', 'Five', 'Five', 'Five', 'Five',
    'Six', 'Six', 'Six', 'Six', 'Seven', 'Seven', 'Seven', 'Seven',
    'Eight', 'Eight', 'Eight', 'Eight', 'Nine', 'Nine', 'Nine', 'Nine',
    'Ten', 'Ten', 'Ten', 'Ten', 'Jack', 'Jack', 'Jack', 'Jack', 'Jack',
    'Queen', 'Queen', 'Queen', 'Queen', 'King', 'King', 'King', 'King']
    
    shuffled_deck = []
    while len(shuffled_deck) != 52:
        card_to_add = unshuffled_deck.pop(random.randint(0,len(unshuffled_deck)-1))
        shuffled_deck.append(card_to_add)

    return shuffled_deck

def GetCard(given_deck):
    return given_deck.pop()

def GetPlayers():
    number_of_players = input('How many players are there?: ')
    list_of_players = []

    for player in range(1,int(number_of_players)+1):
        new_player = {
            'player_number' : player,
            'player_hand' : [],
            'number_of_pairs' : 0
        }
        list_of_players.append(new_player)

    return list_of_players

def DealCard(given_player, given_card):
    current_hand = given_player.get('player_hand')
    current_hand.append(given_card)
    given_player.update({'player_hand' : current_hand})
    return given_player

def FindPairs(given_player):
    current_hand = given_player.get('player_hand')
    total_pairs = 0

    for first_card_index in range(len(current_hand)):
        for second_card_index in range(first_card_index, len(current_hand)):
            if first_card_index == second_card_index:
                continue
            if first_card_index == len(current_hand) - 1:
                break
            if current_hand[first_card_index] == current_hand[second_card_index]:
                total_pairs += 1
    
    return given_player.update({'number_of_pairs' : total_pairs})

def RunGame():
    deck = GetSuffledDeck()
    players_list = GetPlayers() 
    print(players_list)
    for delt in range(4):
        for player_num in range(1, len(players_list)+1):
            new_card = GetCard(deck)
            current_player = players_list[player_num-1]
            updated_player = DealCard(current_player, new_card)
            players_list[player_num-1] = updated_player


    


RunGame()