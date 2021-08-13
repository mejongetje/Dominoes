import itertools
import random
import os

import classes
import header
import utils


hand_able = True
np = 0

os.system('cls')

play = classes.Game()

hand = itertools.chain(*play.hand)
# Assign the hands
classes.p1.hand, classes.p2.hand, classes.p3.hand, classes.p4.hand = play.hand[0], play.hand[1], play.hand[2], play.hand[3]

opening_player = play.sixsix
positions = utils.positioning(opening_player, classes.Player.players)

layout = []
layout.append(positions[0].hand.pop(0))
ends = utils.layout_ends(layout)

strng = '|' + str('6/6|')


while True:

    header.header()
    inp2 = input('Click enter to play.')
    os.system('cls')


    # BEGIN OF GAME LOOP
    while hand_able:

        str_hand = ''
        i = 1
        for el in classes.p4.hand:
            str_hand +=  '['+str(i)+']'+ str(el.nose)+'/'+str(el.mouth) +' '
            i += 1

        play.active_position += 1
        
        if play.active_position >= 4:
            play.active_position = 0

        utils.active_player(positions, play.active_position)

        header.header()
        print(f'|_{classes.p2.active}| BIGGA  \t\t\t\t    POPS |{classes.p3.active}_|')
        print(f'|     {len(classes.p2.hand)}\t\t\t\t\t       {len(classes.p3.hand)}    |')
        print('|                                                   |')
        print('|                                                   |')
        print(f'|    {strng.center(42)}')
        print('|                                                   |')
        print('|                                                   |')
        print(f'|__   {len(classes.p1.hand)}\t\t\t\t\t       {len(classes.p4.hand)}  __|')
        print(f'| {classes.p1.active}| FROGGY  \t\t\t\t     YOU |{classes.p4.active} |')
        print('|===================================================|')
        print('| --------------  y o u r   h a n d  -------------- |')
        print(f'|{str_hand.center(51)}|')                      
        print(' =================================================== ')
        
        

        

        # for player in positions:
        #     if  play.active_position == positions.index(player):
        #         player.active = '+'
        #     else:
        #         player.active = ' '

        # check if end is in hand
        chand = utils.check_hand(positions[play.active_position].hand, ends)

        if chand:
            np = 0
            # check if player is human or computer
            # Choose Tile / Human
            if positions[play.active_position].type == "human":
                tile = utils.play_tile(positions[play.active_position], ends)
                
                # where do you want to drop it? left or right? - in case this is possible
                os.system('cls')
                #print('------------------------------------------------------------------------')    
                    
            else:
                tile = utils.choose_tile(positions[play.active_position], ends)
                print(f'{positions[play.active_position]} plays {tile}')
                inp3 = input('Press enter to continue.')

                os.system('cls')
        
            # Remove Tile from Hand
            positions[play.active_position].hand.remove(tile)

            # Play Tile - add to Layout 
            # Switch Tile if necessary
            
            strng = utils.add_tile(tile, ends, layout)

            # Update Ends / Print Ends
            ends = utils.layout_ends(layout)

            # Check if There is an Empty Hand
            hand_able = utils.hand_empty(play.hand)
            if not hand_able:
                utils.add_won_game(positions[play.active_position])
                print(f'The Winner of the Round is {positions[play.active_position]}!\n')   
                inp3 = input('Press enter if you want to continue')
                os.system('cls')
    
        else:
            print(f'{positions[play.active_position].name} has no tile to play...')
            np += 1
            if np >= 4:
                winner, spots = utils.calc_spots(positions)
                print(f'{winner} is the winner, with {spots} spots.')
                utils.add_won_game(winner)
                #print(classes.p1.hand, classes.p2.hand, classes.p3.hand, classes.p4.hand)
                inp3 = input('Press enter to continue')
                os.system('cls')
                break
            inp3 = input('Press enter to continue')
            os.system('cls')

    header.header()
    print('|                S C O R E B O A R D                |')
    print('|---------------------------------------------------|')
    print('|      Name                 |       Games Won       |')
    print('|---------------------------------------------------|')
    print('|                           |                       |')
    print(f'|     FROGGY                |\t\t{classes.p1.games_won}\t    |')
    print(f'|     BIGGA                 |\t\t{classes.p2.games_won}\t    |')
    print(f'|      POPS                 |\t\t{classes.p3.games_won}\t    |')
    print(f'|      YOU                  |\t\t{classes.p4.games_won}\t    |')
    print('|                           |                       |')
    print(' =================================================== ')
    inp_cont = input('Do you want to continue? y or n: ')
    if inp_cont == 'n':
        break
    os.system('cls')    



