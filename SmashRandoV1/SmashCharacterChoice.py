import tkinter as tk
import random
import Character_list



def choose_character(curr_player):
    #Take the player list from Character_List
    curr_player_list = Character_list.Players[curr_player]
    if len(curr_player_list) >=81:
        list_to_delete = Character_list.Players[curr_player]
        list_to_delete.clear()
        Character_list.Players[curr_player] = list_to_delete
    potential_character = random.randint(1,81)
    repeated_character = True
    #The first selection would always be a new character
    if len(curr_player_list) < 1:
            curr_player_list.append(potential_character)
            Character_list.Players[curr_player] = curr_player_list
            return potential_character
    else:
        #Continuously loop and select a new character until one that
        #has not been played before has been selected
        while potential_character in curr_player_list:
            potential_character = random.randint(1,81)
        curr_player_list.append(potential_character)
        Character_list.Players[curr_player] = curr_player_list
        return potential_character
    
#Clears all players        
def clear_players():
    for i in range(8):
        list_to_delete = Character_list.Players[i+1]
        list_to_delete.clear()
        Character_list.Players[i+1] = list_to_delete
        lbl_char_num = tk.Label(master = frm_character, text="                                   ", width = 15)
        if i < 4:
            lbl_char_num.grid(row=i, column=1, sticky="w")
        else:
            lbl_char_num.grid(row=i - 4, column=4, sticky="w")
    print("Characters have been cleared")
            
        
def character_select():
    global lbl_char_num
    global lbl_player_num
    global frm_character
    amount_lines = int(ent_first_name.get())
    character_num = 0
    for j in range(8):
            lbl_char_num = tk.Label(master = frm_character, text="                                   ", width = 15)
            if j < 4:
                lbl_char_num.grid(row=j, column=1, sticky="w")
            else:
                lbl_char_num.grid(row=j - 4, column=4, sticky="w")
    #This will put the characters as labels for each Player
    for i in range(amount_lines):
        player_num = str(i + 1)
        lbl_player_num = tk.Label(master=frm_character, text=("Player", player_num))
        if i < 4:
            lbl_player_num.grid(row=i, column=0, sticky="e")
        else:
            lbl_player_num.grid(row=i - 4, column=3, sticky="e")
        #lbl_player_num.grid(row=i, column=0, sticky="w")   
        #Get rid of the previous character
        
        #lbl_char_num.grid(row=i, column=1, sticky="e")
        
        character_num = choose_character(i+1)
        #Use the Dictionary present in the Character List file to select the corresponding character
        lbl_char_num = tk.Label(master = frm_character, text=Character_list.Characters[character_num])
        if i < 4:
            lbl_char_num.grid(row=i, column=1, sticky="w")
        else:
            lbl_char_num.grid(row=i - 4, column=4, sticky="w")
        

window = tk.Tk()
window.title("Smash Ultimate Randomizer")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

lbl_first_name = tk.Label(master=frm_form, text="Amount of Players")
ent_first_name = tk.Entry(master=frm_form, width=50)
ent_first_name.insert(0, "1")

lbl_first_name.grid(row=0, column=0, sticky="e")
ent_first_name.grid(row=0, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_clear = tk.Button(master=frm_buttons, text="Clear", command = clear_players)
btn_clear.pack(side=tk.RIGHT, ipadx=10)

btn_submit = tk.Button(master=frm_buttons, text="Randomize", command = character_select)
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

frm_character = tk.Frame(relief=tk.RAISED, borderwidth=5)
frm_character.pack(fill=tk.X)

lbl_player_num = tk.Label()
lbl_char_num = tk.Label()

for i in range(4):
        player_num = str(i + 1)
        lbl_player_num = tk.Label(master=frm_character, text=("Player", player_num))
        lbl_player_num.grid(row=i, column=0, sticky="w")

for i in range(4):
        player_num = str(i + 5)
        lbl_player_num = tk.Label(master=frm_character, text=("Player", player_num))
        lbl_player_num.grid(row=i, column=3, sticky="w")



# Start the application
window.mainloop()

