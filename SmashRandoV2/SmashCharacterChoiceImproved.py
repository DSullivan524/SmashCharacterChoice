import tkinter as tk
import random
import Character_list2
import keyboard

background_image = PhotoImage()

#The only changes that could be made, as of now, is to change it somehow
#where if the same name is entered in 2 different fields, only randomize
#for them once.


def choose_character(curr_player):
    
    #Take the player set from Character_List2
    curr_player_set = Character_list2.Players[curr_player]
    
    #If the player has played all characters, it will reset their set
    if len(curr_player_set) >= 81:
        set_to_delete = Character_list2.Players[curr_player]
        set_to_delete.clear()
        Character_list2.Players[curr_player] = set_to_delete
        print("Reset the list")
        curr_player_set.clear()
        
    potential_character = random.randint(1,81)
    repeated_character = True
    #The first selection would always be a new character
    if len(curr_player_set) < 1:
            curr_player_set.add(potential_character)
            Character_list2.Players[curr_player] = curr_player_set
            return potential_character
    else:
        #Continuously loop and select a new character until one that
        #has not been played before has been selected
        while potential_character in curr_player_set:
            potential_character = random.randint(1,81)
        curr_player_set.add(potential_character)
        #curr_player_set = set(curr_player_list)
        Character_list2.Players[curr_player] = curr_player_set
        return potential_character
    

#This will set only new players
def set_players():
    global entries
    for entry in entries:
        if entry.get() != "":
            if entry.get() not in Character_list2.Players:        
                player_name = entry.get()
                player_list = set()
                Character_list2.Players[player_name] = player_list


#Just a check to see if Players and their sets have been properly
#added or reset based on the situtation
def print_players(event):
    print(Character_list2.Players)


#This is used to remove players and their characters
#for whoever is not playing that round
def clear_names():
    global frm_character
    global labels_players
    global labels_char
    
    for label in labels_players:
        label.destroy()

    for label in labels_char:
        label.destroy()

    
#Clears the sets for all registered Players
#Can be set to only delete sets for Players currently playing
def clear_players():
    for i in Character_list2.Players:
        set_to_delete = set()
        Character_list2.Players[i] = set()
    clear_names()
    print("Characters have been cleared")


#This code is executed when the randomize button is clicked      
def character_select():
    global lbl_char_num
    global lbl_player_num
    global frm_character
    global entries
    global labels_players
    global labels_char
    
    character_num = 0
    clear_names()
    set_players()
    lbl_player_num.destroy()

    i=0
    for entry in entries: 
        #This for loop will iterate through the entry fields present in the window
        if entry.get() in Character_list2.Players:
            
            lbl_player_num = tk.Label(master=frm_character, text=(entry.get()), width = 15)
            if i < 4:
                lbl_player_num.grid(row=i, column=0, sticky="w")
            else:
                lbl_player_num.grid(row=i - 4, column=3, sticky="w")
            character_num = choose_character(entry.get())
            labels_players.append(lbl_player_num)
            
            #Use the dictionary in Character_list2 to show which character it is
            lbl_char_num = tk.Label(master = frm_character, text=Character_list2.Characters[character_num], width = 15)
            if i < 4:
                lbl_char_num.grid(row=i, column=1, sticky="w")
            else:
                lbl_char_num.grid(row=i - 4, column=4, sticky="w")
            labels_char.append(lbl_char_num)
            i += 1
        
        

window = tk.Tk()
window.title("Smash Ultimate Randomizer")

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack(expand = True)

players = [ "Player 1",
            "Player 2",
            "Player 3",
            "Player 4",
            "Player 5",
            "Player 6",
            "Player 7",
            "Player 8",
            ]

#Sepereates each entry field to read from them indiviually later
entries = []

for idx, text in enumerate(players):
    lbl_player_num = tk.Label(master=frm_form, text=(text))
    ent_player_name = tk.Entry(master=frm_form, width=50)
    
    lbl_player_num.grid(row=idx, column=0, sticky="e")
    ent_player_name.grid(row=idx, column=1)
    
    entries.append(ent_player_name)


frm_buttons = tk.Frame()
frm_buttons.pack(ipadx=5, ipady=5, expand=True)

btn_rand = tk.Button(master=frm_buttons, text="Randomize", command = character_select)
btn_rand.pack(padx=10, ipadx=10)

btn_clear = tk.Button(master=frm_buttons, text="Clear", command = clear_players)
btn_clear.pack(ipadx=10)


frm_character = tk.Frame(relief=tk.RAISED, borderwidth=5)
frm_character.pack(ipadx=5, ipady=5, expand = True)


lbl_player_num = tk.Label()
lbl_char_num = tk.Label()


labels_players = []
labels_char = []


#This is used to display the currently registered players
#and their respective sets
window.bind("<Return>", print_players)

# Start the application
window.mainloop()

