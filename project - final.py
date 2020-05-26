import json
import tkinter
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO


def main():
    LP_STARTER = 8000
    lp_1 = LP_STARTER
    lp_2 = LP_STARTER
    intro()
    open_doc('cardinfo.php')
    while lp_1 > 0 and lp_2 > 0 :
        unknown = round(1, lp_1, lp_2)
        if type(unknown[0]) == type(5):
            lp_1 = unknown
        else:
            lp_2 = int(unknown[0])
        graphics(unknown[1], unknown[2], lp_1, lp_2)
        win(lp_1, lp_2)
        unknown2 = round(2, lp_2, lp_1)
        if type(unknown2[0]) == type(5):
            lp_2 = unknown2
        else:
            lp_1 = int(unknown2[0])
        graphics(unknown[1], unknown[2], lp_1, lp_2)
        win(lp_1, lp_2)





def intro():
    print(
        "Hi, this is a all-in-one Yugioh card game companion, for 2 players. \nAt first enter the LP you'd like to play with. \n"
        "For every round then input the monsters you are attacking with and the victims.")

    canvas = make_canvas(1000, 1000, 'Yu-Gi-Oh! Master')
    u = urllib.request.urlopen('https://www.gtnm.at/wp-content/uploads/2017/05/a32dad516b6d10c5ab6ac415a297eaf0_yugioh-yugioh-clipart-logo_500-175.png')
    raw_data = u.read()
    u.close()
    im = Image.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im)
    canvas.create_image(500, 500, image=photo)

    canvas.create_text(500, 750, anchor='center', font='Courier', text=
        "Hi, this is a all-in-one Yugioh card game companion, for 2 players. \nAt first enter the LP you'd like to play with.\n"
        "For every round then input the monsters you are attacking with and the victims.")

    canvas.mainloop()

def open_doc(file):
    with open(file) as dict_file:
        dict = json.load(dict_file)
    return dict

def win(first_lp, second_lp):
    if first_lp < 0:
        print("Player 2 won.")
    if second_lp < 0:
        print("Player 1 won.")

def round(player, lp_self, lp_other):
    print("It's Player " + str(player) + "'s turn")
    card_1_name = get_card(1)
    card_2_name = get_card(2)
    result = genius_calc(card_1_name, card_2_name)

    if result < 0:
        minus_self = result
        lp_self += minus_self
        print("My new LP are " + str(lp_self))
        return lp_self, card_1_name, card_2_name
    elif result > 0:
        minus_other = result
        lp_other -= minus_other
        print("Opponents new LP are " + str(lp_other))
        return str(lp_other), card_1_name, card_2_name
    elif result == 0:
        minus_self = result
        lp_self += minus_self
        print("My new LP are " + str(lp_self))
        return lp_self, card_1_name, card_2_name

def genius_calc(name_1, name_2):
    first = get_atk(name_1) + int(input("Enter additional ATK points, if you have equipped your monster. Else enter 0. "))
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

def get_pic(card_name):
    pic_list = get_number(card_name, 'card_images')
    pic_dict = pic_list[0]
    card_url = pic_dict['image_url']
    return card_url

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
            if 'Monster' in card_dict['type'] :
                card_value = card_dict[mode]  # define ATK of Monster
                '''print(card_value)  # MUSS RAUS'''
            else:
                card_name = input("This is not a monster, enter again: ")

    return card_value
def get_card(turn):
    if turn == 1:
        card_name = input("Your cards name: ")
    if turn == 2:
        card_name = input("Opponent cards name: ")
    return card_name


"GRAPHICS"

def graphics(card_1_name, card_2_name, lp_1, lp_2):
    card_url_1 = get_pic(card_1_name)
    card_url_2 = get_pic(card_2_name)
    canvas = make_canvas(1000, 1000, 'Yu-Gi-Oh! Master')
    u1 = urllib.request.urlopen(card_url_1)
    raw_data1 = u1.read()
    u1.close()
    im1 = Image.open(BytesIO(raw_data1))
    photo1 = ImageTk.PhotoImage(im1)
    canvas.create_image(250, 500, image=photo1)
    u2 = urllib.request.urlopen(card_url_2)
    raw_data2 = u2.read()
    u2.close()
    im2 = Image.open(BytesIO(raw_data2))
    photo2 = ImageTk.PhotoImage(im2)
    canvas.create_image(750, 500, image=photo2)
    canvas.create_text(250, 100, anchor='center', font='Courier', text= 'Life Points of Player 1 are ' + str(lp_1))
    canvas.create_text(750, 100, anchor='center', font='Courier', text= 'Life Points of Player 2 are ' + str(lp_2))
    canvas.mainloop()


def make_canvas(width, height, title):
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
