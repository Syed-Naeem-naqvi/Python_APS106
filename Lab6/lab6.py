##############################
# APS106 Winter 2022 - Lab 7 #
##############################

import random
import math as m
from itertools import combinations


#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - NO NEED TO EDIT THESE
#####################################


def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    deck = []
    suits = ['spades', 'clubs', 'diamonds', 'hearts']

    for suit in suits:
        for number in range(1, 14):
            deck.append([suit, number])

    return deck


def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck, len(deck))

    return shuffled_deck


# Generate a simpler deck than the 52-card one

# deck_sample = [['spades', 10], ['hearts', 2], ['clubs', 8]]
# hand_sample = [['diamonds', 3]]
# print(deck_sample)
# print(hand_sample)

#############################
# PART 1 - Deal card
#############################


def deal_card(deck, hand):
    """
    (list,list) -> None

    Deal a card from the first element in the deck list and add it to the list
    representing the player's hand. Both list input parameters
    are nested lists with each element in the list being a two-element
    list representing a card.

    Note that this function returns nothing! It modifies the two lists that
    are passed in as parameters in place.

    """
    # TODO your code here
    card_to_deal = deck.pop(0)
    hand.append(card_to_deal)


# deal_card(deck_sample, hand_sample)
# print(deck_sample)
# print(hand_sample)

#############################
# PART 2 - Score Hand
#############################


def score_hand(hand):
    """
    (list) -> int

    Calculate the cribbage score for a hand of five cards. The input parameter
    is a nested list of length 5 with each element being a two-element list
    representing a card. The first element for each card is a string defining
    the suit of the card and the second element is an int representing the
    number of the card.
    """

    # TODO your code here
    total_points = 0
    points_from_part_one = 0

    # PART 2.1
    # First, Count pairs and calculate points from pairs
    unique_card_values = set()
    unique_card_suits = set()
    hand_values = []
    hand_suits = []

    # Extract hand values, and find the unique ones. Also extract suits for later use
    for i in range(len(hand)):
        unique_card_values.add(hand[i][1])
        hand_values.append(hand[i][1])
        unique_card_suits.add(hand[i][0])
        hand_suits.append(hand[i][0])

    # Use a dictionary to store the number of occurrences of each hand value
    value_dict = {}
    for value in unique_card_values:
        value_dict[value] = hand_values.count(value)

    # Calculate the points from pairs of the same value
    points_from_pairs = 0
    points_from_larger_groups_of_same_cards = 0
    for value in value_dict.values():
        if value == 2:
            points_from_pairs += 2
        elif value > 2:
            points_from_larger_groups_of_same_cards += 2 * m.factorial(value) / (
                    m.factorial(value - 2) * m.factorial(2))

    # Sum up points from part 1
    points_from_part_one = int(points_from_pairs + points_from_larger_groups_of_same_cards)
    # print(points_from_part_one)

    # PART 2.2
    # Now, check if 4 or 5 of the cards have the same suit
    points_from_part_two = 0

    suit_dict = {}
    for suit in unique_card_suits:
        suit_dict[suit] = hand_suits.count(suit)
    for value in suit_dict.values():
        if value == 4:
            points_from_part_two += 4
        elif value == 5:
            points_from_part_two += 5
    # print(points_from_part_two)

    # PART 2.3.0
    # Calculate runs of lengths 3, 4 and 5
    points_from_part_three_point_zero = 0

    # print(hand_values)
    current_run_length = 1
    run_values = []  # EXPERIMENTAL
    run_in_deck = False
    for i in range(len(hand_values)):
        if i < len(hand_values) - 1:
            if hand_values[i] + 1 == hand_values[i + 1]:
                run_in_deck = True
                run_values.append(hand_values[i])  # EXPERIMENTAL
                current_run_length += 1

    points_from_part_three_point_zero = current_run_length
    # print(points_from_part_three_point_zero)

    # Find the missing value in the run values
    if run_in_deck:
        index_before_last_run_value = hand_values.index(run_values[-1])
        run_values.append(hand_values[index_before_last_run_value] + 1)

    # print(run_values)
    if len(run_values) == 2:
        points_from_part_three_point_zero = 0
        run_in_deck = False

    # PART 2.3.A
    # Find all combinations of items in hand_values that result in run_values
    # Can't use loops as the number of loops may be 3, 4, or 5
    # print(run_values)

    run_length_combinations = list(combinations(hand_values, len(run_values)))
    # print(run_length_combinations)

    unique_combos = 0
    if run_in_deck:
        unique_combos = 0
        for combination in run_length_combinations:
            if list(combination) == run_values:
                unique_combos += 1


    # print(unique_combos)
    points_from_part_three = unique_combos * len(run_values)
    # print(points_from_part_three)

    # PART 2.4 DO NOT ADD points_from_part_three_point_zero to the total, if the run has only one combination then it'll be represented in points_from_part_three
    # Now, find all combinations of the hand_values that add up to 15

    points_from_part_three_all_run_combinations = 0
    target = 15
    result = []

    hand_values_upto_ten = hand_values.copy()
    for i in range(len(hand_values_upto_ten)):
        if hand_values_upto_ten[i] > 10:
            hand_values_upto_ten[i] = 10

    # print(hand_values)
    # print(hand_values_upto_ten)

    for i in range(2, len(hand_values_upto_ten) + 1):
        combos = list(combinations(hand_values_upto_ten, i))
        for combo in combos:
            if sum(combo) == target:
                result.append(combo)

    points_from_part_three_all_run_combinations = len(result) * 2
    # print(points_from_part_one, points_from_part_two, points_from_part_three, points_from_part_three_all_run_combinations)
    total_points = points_from_part_one + points_from_part_two + points_from_part_three + points_from_part_three_all_run_combinations
    return total_points


hand1 = [['hearts', 9], ['spades', 2], ['clubs', 3], ['hearts', 3], ['hearts', 4]]
# print(score_hand(hand1))

hand2 = [['hearts', 10], ['hearts', 2], ['hearts', 3], ['hearts', 6], ['diamonds', 5]]
# print(score_hand(hand2))

hand3 = [['hearts', 10], ['spades', 9], ['diamonds', 11], ['hearts', 12], ['spades', 13]]
# print(score_hand(hand3))


################################
# PART 3 - PLAY
################################


def play(shuffled_deck):
    """
    (list) -> [str, int, int]

    Function deals cards to players, computes player scores, and
    determines game_outcome.

    Function returns a three-element list where the first element is a string
    indicating the game_outcome, the second element is an int specifying player\'s
    score, and the third element is an int specifying dealer\'s score.
    """
    player_hand = []
    dealer_hand = []

    # TODO complete the function
    # Look at the deck before dealing
    # print(shuffled_deck)

    for i in range(1, 11):
        if i % 2 == 0:
            deal_card(shuffled_deck, player_hand)
        elif i % 2 != 0:
            deal_card(shuffled_deck, dealer_hand)

    # print(shuffled_deck)
    # print(player_hand)
    # print(dealer_hand)

    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)

    # print(player_score, dealer_score)

    # Determine game_outcome
    game_outcome = ''
    if player_score > dealer_score:
        game_outcome = 'player wins'
    elif player_score <= dealer_score:
        game_outcome = 'dealer wins'

    match_summary = [game_outcome, player_score, dealer_score]
    return match_summary


my_deck = generate_deck()
my_deck = shuffle(my_deck)
print(play(my_deck))


# Run many matches

player_wins = 0
dealer_wins = 0
ties = 0
trials = 0
while trials < 1000:
    my_deck = generate_deck()
    my_deck = shuffle(my_deck)
    if play(my_deck)[0] == 'dealer wins':
        dealer_wins += 1
    else:
        player_wins += 1
    if play(my_deck)[1] == play(my_deck)[2]:
        ties += 1
    trials += 1

print('Player wins: ', player_wins, 'Dealer wins: ', dealer_wins)
print('_______________')
print('Tie Percentage: ', (ties/1000)*100)

