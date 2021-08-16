# SmashCharacterChoice

These files are used in Smash Ultimate to randomly select each available character only once.

SmashCharacterChoice is used in conjuction with Character_list and SmashCharacterChoiceImproved
is used in conjuction with Character_list2. The only difference in the 2 character list files is
one has the Players being set up ahead of time and only keeps record of players 1 through 8, whereas
Character_list2 is able to accept multiple players, each with their own unique set. Each Character list
has a dictionary containing every character available with the exception of Piranha Plant and the Mii fighters.
If you want to include those characters the only change would be to include those characters to the 
dictionaries in each Character list file and change the random functions in each SmashCharacterChoice
file to include 1 through 85



The original SmashCharacterChoice program has each of the 8 available players set up as their 
own unique sets. There is an entry field that will ask how many players are currently playing to
determine how many characters to  be chosen When the program is executed each player currently 
playing will get a new randomly chosen character to play as for the next round. Each player will 
get a new character to play as up until each player reaches all 81 characters. Once a player has 
played all 81 characters only their list will be cleared, no other player will have their list reset. 
One drawback to this program is if a new player wanted to take an existing player's position, they 
would not be able to playany characters played by the existing player. The clear button will clear 
the played character listfor each player regardless of how many they have already played.



The improved SmashCharacterChoice has a few improvements over the original program.
The first major improvement is instead of only having 8 unique lists for the 8 possible players,
there are now 8 entry fields. Each of these 8 fields corresponds to each of the possible players
currently playing. You will enter the name each person will go by and that name will then get
a unique set associated to it. That set will be used when determining if that player has played
a certain character before. The player's name and their respective set will remain unitl the 
program is closed. The benefit over this method over the original is that instead of
connecting the list to the player number, it is instead connected to the player's name.
This means that if someone who is currently playing steps away or if someone takes their place 
their set is preserved and the new player will get their own unique set. If the player that stepped
away decides to come back, all they have to do is put their name back into an entry field and
the program will recognize that player already has a set to their name. Their set will be pulled
regardless of which player position they are playing in. 

The next major improvement is that instead of the output being in the format "Player #  Character" 
it is now in the format "'Player name'   'Character'". This makes it slightly easier to tell who is 
playing which characterinstead of remembering which player each person is. The output will scale with 
the amount of people currently playing, meaning if 4 players are currently playing, and one of them 
steps away, the window will resize appropriately and only randomize and show the results of the randomization 
for the 3 remaining players. 

A small improvement over the original is the method that is used to clear the
output each time the randomizer is run. The first iteration just covered the previous results with
another label with a group of spaces being the text. This iteration changes that by instead of
covering the previous results it destroys the previous labels and replaces them by the new results.
This iteration also has an extra function that is binded to the enter key to show all currently
registered players and their sets. This function is primarily used to determine if the program is 
running correctly and can be commented out if not needed without any issue. The program will 
automatically register any new names when randomized, but will not register a name more than once.
The clear button works the same as in the previous iteration where all registered players will have
their played character sets reset. 

The improved SmashCharacterChoice will now read and write to a text file found in the same directory as
the program itself. When the code is first started it will check to see if the particular text file 
already exists. If it does the program will continue, and if not the program will create the text file
before continuing. The text file the program creates is called Player_list.txt and its purpose is to 
carry over the players and their used characters between sessions. The program will first read the file 
and if the file already has preivous data it will update the Player list accordingly. The program will 
continue normally up until the program is ended. Before the file is closed, the contents of the Player 
list will be put into this text file to be used the next time this program is run.


