import random


def build_deck():
    '''creates the deck'''
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = [
        'A',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'J',
        'Q',
        'K',
    ]
    deck = []
    for suit in suits:
        for j in range(len(suits)):
            card = {
                'suit': suit,
                'rank': ranks[j],
                'value': j
            }
            deck.append(card)
    return deck


def compare(card1, card2):
    '''takes the difference of the two cards'''
    return card1['value'] - card2['value']


def guess(card1, card2):
    '''tells the user their card, received and evaluates their guess'''
    print(f"The current card is the {card1['rank']} of {card1['suit']}")
    selection = input('Will the next card be higher(h) or lower(l)?')
    if selection == 'h':
        return compare(card1, card2) < 0
    elif selection == 'l':
        return compare(card1, card2) > 0
    else:
        print("it's either h or l bozo, you just lost a turn")
        return False


def play_game():
    '''The main game loop'''
    deck = build_deck()
    random.shuffle(deck)
    name = str(input("What's your name? "))
    print(name)
    score = 0
    current_card = deck.pop()
    while score < 5 and 0 < len(deck):
        next_card = deck.pop()
        print('-------------------')
        if (guess(current_card, next_card)):
            score += 1
            print(f'Congrats {name}.  Your score is now {score}.')
        else:
            print(f"You didn't get it. Your score is still {score}")
        current_card = next_card
    if len(deck) > 0:
        print('You won!')
    else:
        print('You lose.')


play_game()
