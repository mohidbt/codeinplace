import json

LP_STARTER = 8000

def main():
    lp_1 = LP_STARTER
    lp_2 = LP_STARTER
    intro()
    open_doc('cardinfo.php')
    while lp_1 > 0 and lp_2 > 0 :
        unknown = round(1, lp_1, lp_2)
        if type(unknown) == type(5):
            lp_1 = unknown
        else:
            lp_2 = int(unknown)
        print("MY REAL LP ARE " + str(lp_1))
        print("HIS REAL LP ARE " + str(lp_2))

        if lp_1 < 0:
            print("Player 2 won.")


def intro():
    print(
        "Hi, this is a all-in-one Yugioh card game companion, for 2 players. At first enter the LP you'd like to play with."
        + " " +
        "For every round then input the monsters you are attacking with and the victims.")

def open_doc(file):
    with open(file) as dict_file:
        dict = json.load(dict_file)
    return dict

def round(player, lp_self, lp_other):
    print("It's Player " + str(player) + "'s turn")
    card_1_name = get_card(1)
    card_2_name = get_card(2)
    result = genius_calc(card_1_name, card_2_name)

    if result < 0:
        minus_self = result
        lp_self += minus_self
        print("My new LP are " + str(lp_self))
        return lp_self
    elif result > 0:
        minus_other = result
        lp_other -= minus_other
        print("Opponents new LP are " + str(lp_other))
        return str(lp_other)
    elif result == 0:
        minus_self = result
        lp_self += minus_self
        print("My new LP are " + str(lp_self))
        return lp_self

def genius_calc(name_1, name_2):
    first = int(input("Enter additional ATK points, if you have equipped your monster. Else enter 0. ")) + get_atk(name_1)
    if input("Is your victim in def-mode? Then submit 'def'. If not, only press enter. ") == 'def':
        second = get_def(name_2)
        print("Your ATK is " + str(first) + ", your opponent's DEF is " + str(second) + ".")
        dif = first - second
        if dif >= 0 :
            minus_other = 0
            print(str(name_2) + " destroyed, but your opponent gets " + str(minus_other) + " damage, as card was in defense.")
            return minus_other
        else:
            minus_self = dif
            print("You get " + str(minus_self) + " damage, as opponents DEF > your ATK.")
            return minus_self
    else:
        second = get_atk(name_2)
        print("Your ATK is " + str(first) + ", your opponent's ATK is " + str(second) + ".")
        dif = first - second
        if dif >= 0:
            minus_other = dif
            print(str(name_2) + " gets destroyed, opponent gets " + str(minus_other) + " damage, as your ATK > opponent's ATK.")
            return minus_other
        else:
            minus_self = dif
            print(str(name_1) + " gets destroyed, you get " + str(minus_self) + " damage, as opponents ATK > your ATK.")
            return minus_self



def get_atk(card_name):
    atk_value = get_number(card_name, 'atk')
    return atk_value

def get_def(card_name):
    def_value = get_number(card_name, 'def')
    return def_value

def get_number(card_name, mode):
    full_dict = open_doc('cardinfo.php')
    data_value_list = full_dict['data']  # list with all card dictionaries as elements
    for i in range(len(data_value_list)):
        card_dict = data_value_list[i]  # card dictionaries
        if card_dict['name'] == str(card_name):
            if card_dict['type'] == 'Effect Monster' or 'XYZ Monster' or 'Normal Monster' or 'Synchro Monster':  # FUNKTION: if ...type CONTAINS 'Monster'
                card_value = card_dict[mode]  # define ATK of Monster 1
                '''print(card_value)  # MUSS RAUS'''
            else:
                card_name = input("This is not a monster, enter again: ")
                # FUNKTION: falls input nicht im dict enthalten
                ''' while card_dict['name'] != str(card_1_name):                                                                   
        card_1_name =  
'''
                '''        while card_dict['name'] == str(card_1_name):
            if card_dict['name'] == str(card_1_name):
                if card_dict['type'] == 'Effect Monster' or 'XYZ Monster' or 'Normal Monster' or 'Synchro Monster':  # FUKTION: if ...type CONTAINS 'Monster'                  # filter non-monsters out
                    card_1_atk = card_dict['atk']                             # define ATK of Monster 1
                    print(card_1_atk)                                         # MUSS RAUS
                    break
                elif card_dict['type'] == 'Trap Card' or 'Spell Card':
                    card_1_name = input("This is not a monster, enter again: ")
                elif i == range(len(data_value_list)):
                    input("This is not a card, enter again: ")
'''
    return card_value
def get_card(turn):
    if turn == 1:
        card_name = input("Your cards name: ")
    if turn == 2:
        card_name = input("Opponent cards name: ")
    return card_name

"""
def get_p_names():
    return get_p_name(1) and get_p_name(2)


def get_p_name(player):
    if player == 1:
        P1_NAME = input("Player 1, what's your name?")
        return P1_NAME
    elif player == 2:
        P2_NAME = input("Player 2, what's your name?")
        return P2_NAME
"""

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
