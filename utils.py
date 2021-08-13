import itertools

from os import name, system
from copy import deepcopy


def positioning(first_player, players):
    rearr_players = players[:]
    rearr_players[0] = players[0] if first_player == 1 \
        else( players[1] if first_player == 2 \
            else (players[2] if first_player == 3 else players[3]))
    rearr_players[1] = players[1] if first_player == 1 \
        else( players[2] if first_player == 2 \
            else (players[3] if first_player == 3 else players[0]))
    rearr_players[2] = players[2] if first_player == 1 \
        else( players[3] if first_player == 2 \
            else (players[0] if first_player == 3 else players[1]))
    rearr_players[3] = players[3] if first_player == 1 \
        else( players[0] if first_player == 2 \
            else (players[1] if first_player == 3 else players[2]))
    return rearr_players


def layout_ends(layout):
    ch = list(itertools.chain(layout))
    ends = []
    ends.append(ch[0].nose)
    ends.append(ch[-1].mouth)
    return ends 


def check_hand(hand, lst):
    for x in hand:
        if x.nose in lst or x.mouth in lst:
            return True


def play_tile(player, ends):
    #if player.type == "human":
    while True:
        try:
            tile_index = int(input("Play a tile:  "))
            if 1 <= tile_index <= len(player.hand):
                if player.hand[tile_index-1].nose in ends or player.hand[tile_index-1].mouth in ends: 
                    break
                else:
                    print(f'{player.hand[tile_index-1]} cannot be played.')
            else:
                print(f'Choose a number between 1 and {len(player.hand)}.')
        except:
            print(f'Choose a number between 1 and {len(player.hand)}.')
    return player.hand[tile_index-1]


def choose_tile(player, ends):
    candidates = []
    eyes_lst = []
    for x in player.hand:
        if x.nose in ends or x.mouth in ends:
            candidates.append(x)
    if len(candidates) == 1:
        return candidates[0]
    else:
        for candidate in candidates:
            eyes = candidate.nose + candidate.mouth
            eyes_lst.append(eyes)
        cand_index = eyes_lst.index(max(eyes_lst))
        return candidates[cand_index]
    

def add_tile(tile, ends, layout):
    strng = '|'
    tile_copy = deepcopy(tile)
    if tile_copy.nose == ends[0]:
        tile_copy.switch()
        layout.insert(0, tile_copy)
    elif tile_copy.nose == ends[1]:
        layout.insert(len(layout), tile_copy)
    elif tile_copy.mouth == ends[0]:
        layout.insert(0, tile_copy)
    else:
        tile_copy.switch()
        layout.insert(len(layout), tile_copy)
    for el in layout:
        strng += str(el.nose)+'/'+str(el.mouth)+'|'
        if len(strng) >= 40 and len(strng) < 44 or len(strng) >= 87 and len(strng) < 91:
            strng += '\n|     |'
    return strng


def remove_tile(tile, hand):
    ind = hand.index(tile)
    return hand.pop(ind)


def hand_empty(*hands):
    if all(*hands):
        return True


def active_player(positions, active_position):
    for player in positions:
        if positions.index(player) == active_position:
            player.active = '+'
        else:
            player.active = ' '

def calc_spots(players):
    all_spots = []
    for player in players:        
        spots = 0
        for tiles in player.hand:
            x = tiles.nose + tiles.mouth
            spots += x
        all_spots.append(spots)  
    min_spots = min(all_spots)  
    for player in players:
        if players.index(player) == all_spots.index(min_spots):
            return player, min_spots
        else:
            pass


def add_won_game(winner):
    winner.games_won += 1
    
    
def clear():  
    if name == 'nt':
        system('cls') 
    else:
        system('clear')







