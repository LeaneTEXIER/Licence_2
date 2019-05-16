import card
import random

def create_game():
    """
    Creates a game of 32 cards

    :return: a game of 32 cards with values and colors
    :rtype: list
    """
    game=[]
    for value in card.values:
        for color in card.colors:
            game.append(card.create(value,color))
    return game

def melange():
    """
    Mix a game of 32 cards

    :return: a mix game of 32 cards with values and colors
    :rtype: list
    """
    game_base=create_game()
    game_mix=[]
    while len(game_base)!=0:
        add=random.randrange(len(game_base))
        game_mix.append(game_base[add])
        del game_base[add]
    return game_mix

def init(n):
    """
    Distributes n cards to each of the 2 players

    :param n: number of cards per player
    :type n: int (0<n<=16)
    :return: The cards of the 2 players
    :rtype: list, list
    :UC: The number of cards must be an int included between 1 and 16
    :Example:
    
    >>>init(2)
    ([{'color': 'heart', 'value': '9'}, {'color': 'spade', 'value': '10'}], [{'color': 'heart', 'value': '10'}, {'color': 'spade', 'value': '7'}])
    """
    assert type(n)==int,"The number of cards must be an int"
    assert 0<n<=16, "The number of cards must be inclued between 1 and 16."
    game_mix=melange()
    player1=[]
    player2=[]
    for i in range (0,2*n,2):
        player1.append(game_mix[i])
        player2.append(game_mix[i+1])
    return player1, player2

def play(n):
    """
    The computer plays the game
    If the 2 cards have the same values, they are "forgotten"

    :param n: number of cards per player
    :type n: int (0<n<=16)
    :return (print): The cards of the 2 players when they play them and, at the end, the "name" of the winner 
    :UC: The number of cards must be an int included between 1 and 16
    """
    assert type(n)==int,"The number of cards must be an int"
    assert 0<n<=16, "The number of cards must be inclued between 1 and 16."
    player1,player2 = init(n)
    while len(player1)!=0 and len(player2)!=0 :
        card1=player1[0]
        card2=player2[0]
        print ("Card player 1 :", end=" ")
        card.print(card1)
        print ("Card player 2 :", end=" ")
        card.print(card2)
        comp=card.compare_value(card1,card2)
        if comp==1:
            player1+=card1,card2
        elif comp==-1 :
            player2+=card1,card2
        player1=player1[1:]
        player2=player2[1:]
    if len(player1)!=0:
        print ("The winner is the player 1 !!!")
    else :
        print ("The winner is the player 2 !!!")
        
    
