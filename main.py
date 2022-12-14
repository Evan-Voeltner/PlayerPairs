import random

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

def GetPlayers(given_number_of_players):
    list_of_players = []

    for player in range(1,int(given_number_of_players)+1):
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
    given_player.update({'number_of_pairs' : total_pairs})
    return given_player

def PrintPlayerInfo(given_player):
    player_num = given_player.get('player_number')
    player_hand = given_player.get('player_hand')
    player_pairs = given_player.get('number_of_pairs')

    return f'Player {player_num} | Hand {player_hand} | Number of pairs: {player_pairs}'

def FindWinner(given_list_of_players):
    order_of_pairs = []
    winner_numbers = []

    for player in given_list_of_players:
        string_to_add = f'{str(player.get("number_of_pairs"))}{str(player.get("player_number"))}'
        order_of_pairs.append(string_to_add)

    order_of_pairs.sort(reverse = True)

    highest_pair = int(list(order_of_pairs[0])[0])

    if highest_pair == 0:
        return 'There is no winner.'

    for player_index in range(len(order_of_pairs)-1):

        number_of_pairs = int(list(order_of_pairs[player_index])[0])
        if number_of_pairs == highest_pair:
            winner_numbers.append(int(order_of_pairs[player_index][1:]))
        else:
            break
    
    winner_numbers.sort()

    if len(winner_numbers) == 1:
        return(f'The winner is Player {winner_numbers[0]}!')
    else:
        final_string = 'The players who tied are: '
        for winner_number in winner_numbers:
            final_string += f'''
Player {winner_number} '''
        return final_string


def RunGame():
    number_of_players = int(input('How many players are there?: '))
    number_of_rounds = int(input('How many rounds do you want to play?: '))
    
    for round in range(number_of_rounds):
        deck = GetSuffledDeck()
        players_list = GetPlayers(number_of_players)
        for delt in range(5):
            for player_num in range(1, len(players_list)+1):
                new_card = GetCard(deck)
                current_player = players_list[player_num-1]
                updated_player = DealCard(current_player, new_card)
                players_list[player_num-1] = updated_player

        for player_index in range(len(players_list)):
            players_list[player_index] = FindPairs(players_list[player_index])

        for player in players_list:
            print(PrintPlayerInfo(player))
        
        print(FindWinner(players_list))

RunGame()