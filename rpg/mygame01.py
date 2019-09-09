#!/usr/bin/enc python3
from pprint import pprint
from random import randrange

# Replace RPG starter project with this code when new instructions are line.

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
=========
Commands:
  go [direction]
  get [item]
  ''')

def showStatus():
    #Print the players current status
    print('-' * 25)
    print('You are in the ' + currentRoom)

    print('Inventory: ' + str(inventory))

    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])

    print('-' * 25)


while True:
    # an inventory which is emty
    inventory = []

    items = [
        "key",
        "potion",
        "monster"
    ]

    rooms = {
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dinning Room',
            'west': 'Living Room',
            'north': 'Bedroom',
        },
        'Bedroom': {
            'south': 'Hall',
        },
        'Kitchen': {
            'north': 'Hall',
            'east': 'Garden',
        },
        'Dinning Room': {
            'west': 'Hall',
            'south': 'Garden',
        },
        'Garden': {
            'north': 'Dinning Room'
        },
        'Living Room': {
            'east': 'Hall',
            'north': 'Bathroom'
        },
        'Bathroom': {
            'south': 'Living Room'
        }
    }
    room_key = []
    for i in rooms.keys():
        if i == "Hall" or i == "Garden":
            continue
        room_key.append(i)

    for i in items:
        x = randrange(0, len(room_key) - 1)
        # if room_key[x] == "Hall":
        #     continue
        rooms[room_key[x]].update({'item': i})
        del room_key[x]

    pprint(rooms)
    currentRoom = 'Hall'

    showInstructions()

    while True:
        showStatus()
        move = ''
        while move == '':
            move = input('>')
        move = move.lower().split()

        if move[0] == 'go':
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print("You can't go that way")

        if move[0] == 'get':
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                inventory += [move[1]]
                print(move[1] + ' got!')
                del rooms[currentRoom]['item']
            else:
                print("Can't get that")
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print(f'You entered {currentRoom} and a monster got you.... GAME OVER!')
            break
        if 'item' in rooms[currentRoom] and 'Garden' and len(items) - 1 == len(inventory):
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!!!')
            break

    play = input("Do you wish to play again? (Y/n): ")
    if play.lower() == "n": break


