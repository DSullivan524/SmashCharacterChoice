import tkinter as tk
import random
import Character_list


def choose_character(curr_player):
    curr_player_list = Character_list.Players[curr_player]
    potential_character = random.randint(1,81)
    print(curr_player_list)
    new_character = True
    print(type(Character_list.Players[curr_player]))
    if len(curr_player_list) < 1:
        curr_player_list.append(potential_character)
        Character_list.Players[curr_player] = curr_player_list
        return potential_character
    for i in range(len(Character_list.Players[curr_player])):
        print("For loop")
        if curr_player_list[i] == potential_character:
            new_character = False
    if new_character:
        curr_player_list.append(potential_character)
        Character_list.Players[curr_player] = curr_player_list
        print("if branch")
        print("Potential Character", potential_character)
        return potential_character
    else:
        print("else branch")
        choose_character(curr_player)
        

            

        
def character_select():
    
    global frm_character
    amount_lines = int(ent_first_name.get())
    
    # Create the Label and Entry widgets for "First Name"
    for i in range(amount_lines):
        player_num = str(i + 1)
        lbl_player_num = tk.Label(master=frm_character, text=("Player", player_num))
        # Use the grid geometry manager to place the Label and
        # Entry widgets in the first and second columns of the
        # first row of the grid
        lbl_char_num = tk.Label(master = frm_character, text="                                   ")
        lbl_char_num.grid(row=i, column=1, sticky="w")
        lbl_player_num.grid(row=i, column=0, sticky="e")
        character_num = choose_character(i+1)
        print("Character num", character_num)
        lbl_char_num = tk.Label(master = frm_character, text=Character_list.Characters[character_num])
        lbl_char_num.grid(row=i, column=1, sticky="w")
        

# Create a new window with the title "Address Entry Form"
window = tk.Tk()
window.title("Address Entry Form")




# Create a new frame `frm_form` to contain the Label
# and Entry widgets for entering address information.
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
# Pack the frame into the window
frm_form.pack()

# Create the Label and Entry widgets for "First Name"
lbl_first_name = tk.Label(master=frm_form, text="Amount of Players")
ent_first_name = tk.Entry(master=frm_form, width=50)
ent_first_name.insert(0, "2")
# Use the grid geometry manager to place the Label and
# Entry widgets in the first and second columns of the
# first row of the grid
lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)





# Create a new frame `frm_buttons` to contain the
# Submit and Clear buttons. This frame fills the
# whole window in the horizontal direction and has
# 5 pixels of horizontal and vertical padding.
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

# Create the "Submit" button and pack it to the
# right side of `frm_buttons`
btn_submit = tk.Button(master=frm_buttons, text="Submit", command = character_select)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Create the "Clear" button and pack it to the
# right side of `frm_buttons`
btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

frm_character = tk.Frame(relief=tk.RAISED, borderwidth=5)
    # Pack the frame into the window
frm_character.pack(fill = tk.X)


# Start the application
window.mainloop()
