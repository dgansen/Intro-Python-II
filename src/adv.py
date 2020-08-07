from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
    'blank': Room('Initializer Room', "It's amazing how little there is in this room. A marvel to behold.")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# # Initializer
# room['blank'].n_to = room['blank']
# room['blank'].s_to = room['blank']
# room['blank'].e_to = room['blank']
# room['blank'].w_to = room['blank']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
dir_list = ['n','s','e','w']
def show_loc():
    print(f'Location: {player.current_room.name}\n{player.current_room.description}')
def move(cur_room, direction):
    # Returns new room object
    move_dict = {'n':cur_room.n_to,    
                 's':cur_room.s_to,
                 'e':cur_room.e_to,
                 'w':cur_room.w_to}
    print(cur_room.description)
    print(cur_room.n_to.description)
    print(move_dict[direction])
    return move_dict[direction]

#
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print('Enter "b" to begin the game:')
while True:
    command = input('>').split(',')
    # check if given command is more than 1?

    if command[0] == 'b':
        #Begin the game
        print("The air hangs acrid and heavy, bitterly smoky like ground, bare metal.",
        "Amidst rubble and ruin, you approach with fatigued but determined steps.",
        "Your boots are wet, your mouth is dry.",
        "No normal person would undergo the challenge you have consigned to perform.",
        "But despite it all, here you are, standing before the Cave, dealer of death and destinies, the Docker container of the treasure and glory you seek.",
        "Enter `h` for help, you freak.",
        sep='\n')

    # quit command
    elif command[0]=='q':
        break
    # help command
    elif command[0] == 'h':
        print('''Type your commands separated by a comma:\n
         - "n" to move north\n
         - "s" to move south\n
         - "w" to move west\n
         - "e" to move east\n
         - "h" for help\n
         - "q" to quit the game''')
    elif command[0] in dir_list:
        player.current_room = move(player.current_room, command[0])
    
    # "I don't understand" else block
    else:
        print("I'm afraid that's not a command")
    show_loc()
