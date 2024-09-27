# The Mysterious Myth
# INF 120 Fall 2022
# Cheyenne Korda

#help function
#this will allow the user to ask for help throughout the entire came in order to know what to do
def help():
    print('The game is simple, really. Use directions to move around the house you have found yourself stuc in')
    print('You can use N,E,S,W,NE,NW,SE,SW or north, east, south, west, northeast,northwest,southeast,southwest')
    print('You are trapped in the room, so the object of the game will be to get out of it somehow!')
    print('On your way through the house you may see some extra available commands in the room descriptions')
    print('You can use these commands to sometimes grab objects, and other times move a new direction')
    print('Im going to be honest with you there is a chance you may make it out of the house, but you may not make it alive')
    print('Good luck on your adventure and try not to be too loud...')


#the cabinet function is a hidden "room" that the user has to have a key to get into 
#they are trapped for a few turns and they can get out if they put in the right passcode
#the user can also escape to the secret room if they go in the down direction
def cabinet():
    print('You are trapped find a way out or die...')
    print('You only get one chance to make this first guess... pick a diretcion and if its the right direction you will be taken somewhere else... if not then youre trapped')
    print('Your direction choices are north, east, south, west, up, or down')
    command = str(input('What would you like to do? ')).upper()
    if command == 'D' or command == 'DOWN':
        print('Youve found a secret passage that you crawl through. It leads you to a secret room in the basement')
        room = 12
    else:
        count = 0
        while count <= 6:
            print('The door wont budge, but there are buttons on it with the letters A, B, and C.')
            print('With the right combination maybe you can get out. However, theres a note saying if you guess wrong 5 times, you will die')
            combination = 'BCA'
            guess = input('Use all three letters only once in each guess. What is your guess?')
            if guess != combination:
                print('Thats wrong')
                count += 1
            else:
                print('Yay you made it out!')
                room = 3
        print('You make it out... barely')       

                
    
#each room has a look function that simply reprints the description and asks for a command from the user
#enterance_room
#the entrance room is where the program begins. The user can go into a few rooms from this one
def entrance_room():
    room = 1
    print('Room Description Enterance Room - Walk in double doors cannot walk back through these doors. There are 6 doors around the room. Four doors on the wall the player is facing (North). And one door on each of the two walls to the East and West. The room is completely empty giving an abandoned feeling.')
    print('Exit Door on the West Wall leads to Side1 - normal exit.')
    print('Exit Door on the East Wall leads to Side2 - normal exit.')
    print('Exit Door North Wall all the way West leads to the living room - normal exit.')
    print('Exit Door North Wall in the middle toward west leads to hallway 1- normal exit.')
    print('Exit Door North Wall in the middle toward east leads to hallway 2 - normal exit.')
    print('Exit Door North Wall all the way East leads to kitchen- normal exit')

    command = str(input('What would you like to do? ')).upper()

    while room == 1:
        if command == 'N' or command == 'NORTH':
            print('You go the direction into hallway 1')
            room = 13
        elif command == 'E' or command == 'EAST':
            print('You go the direction into the east side room')
            room = 3
        elif command == 'W' or command == 'WEST':
            print('You go the direction into the west side room')
            room = 2
        elif command == 'S' or command == 'SOUTH':
            print('The door is locked you cannot go this way. You are still in the entrance room')
            room = 1
        elif command == 'NE' or command == 'NORTHEAST':
            print('You go the direction into the kitchen')
            room = 10 
        elif command == 'NW' or command == 'NORTHWEST':
            print('You go the direction into the living room ')
            room = 4
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 1
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 1
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 1
            print('Room Description Enterance Room - Walk in double doors cannot walk back through these doors. There are 6 doors around the room. Four doors on the wall the player is facing (North). And one door on each of the two walls to the East and West. The room is completely empty giving an abandoned feeling.')
            print('Exit Door on the West Wall leads to Side1 - normal exit.')
            print('Exit Door on the East Wall leads to Side2 - normal exit.')
            print('Exit Door North Wall all the way West leads to the living room - normal exit.')
            print('Exit Door North Wall in the middle toward west leads to hallway 1- normal exit.')
            print('Exit Door North Wall in the middle toward east leads to hallway 2 - normal exit.')
            print('Exit Door North Wall all the way East leads to kitchen- normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 1
        return room


#side1_room
#this room has basically no extra details in it. It's just for show and a distraction for the user
def side1_room():
    room = 2
    print('Room Description Side Room 1- Walk into a single door to see a table along the West Wall and a bookshelf on the South Wall.')
    print('Exit Door on the East Wall (same one the player walked through) - normal exit goes to Entrance')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 2:
        if command == 'N' or command == 'NORTH':
            print('You bump into a wall. Ouch!')
            room = 2
        elif command == 'E' or command == 'EAST':
            print('You go back out of the door back to where you started in the entrance room')
            room = 1
        elif command == 'W' or command == 'WEST':
            print('You go the direction, but only bump into a table with a knife on it')
            room = 2
        elif command == 'S' or command == 'SOUTH':
            print('You bump into a wall. Ouch!')
            room = 2
        elif command == 'NE' or command == 'NORTHEAST':
            print('You bump into a book shelf.')
            room = 2
        elif command == 'NW' or command == 'NORTHWEST':
            print('You bump into a table')
            room = 2
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 2
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 2
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 2
            print('Room Description Side Room 1- Walk into a single door to see a table along the West Wall and a bookshelf on the South Wall.')
            print('Exit Door on the East Wall (same one the player walked through) - normal exit goes to Entrance')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 2
        return room


#side2_room
#this room has a cabinet in it that will get the user stuck unless they put in the right code
def side2_room():
    room = 3
    print('Room Description Side Room2- Walk through a single door and see a large cabinet along the east wall. If you walk into the cabinet you will be trapped for a few “turns” you will simply go back through the cabinet doors to get out. ')
    print('Exit Door along the West Wall (same one the player walked through) goes to Entrance')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 3:
        if command == 'N' or command == 'NORTH':
            print('You bump into a wall. Ouch!')
            room = 3
        elif command == 'E' or command == 'EAST':
            print('You get to a cabinet that has blood stains all over it, but the door is locked. Do you have a key?')
            if 'key' in inventory:
                print('You go into the cabinet...')
                cabinet()
                room = 12
            else:
                print('No key, no entry.')
                room = 3

        elif command == 'W' or command == 'WEST':
            print('You go the direction back to the starting point in the entrance room')
            room = 1
        elif command == 'S' or command == 'SOUTH':
            print('You bump into a wall. Ouch!')
            room = 3
        elif command == 'NE' or command == 'NORTHEAST':
            print('You bump into a wall.')
            room = 3
        elif command == 'NW' or command == 'NORTHWEST':
            print('You bump into a wall')
            room = 3
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 3
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 3
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 3
            print('Room Description Side Room2- Walk through a single door and see a large cabinet along the east wall. If you walk into the cabinet you will be trapped for a few “turns” you will simply go back through the cabinet doors to get out. ')
            print('Exit Door along the West Wall (same one the player walked through) goes to Entrance')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try anotehr direction')
            room = 3
        return room


#livingroom
#the living room is a basic room with a few murder details 
def livingroom():
    room = 4
    print('Room Description Living Room - There is a couch along the East wall and another couch in the center of the room. And a single couch toward the West wall. Two shelves along the west wall. Three doors along the North Wall. ')
    print('Exit Door on the North Wall all the way West leads to bedroom 1 - normal exit')
    print('Exit door in the middle of the North Wall leads to the bathroom - normal exit')
    print('Exit door on North Wall all the way East leads to bedroom 2 - normal exit')

    command = str(input('What would you like to do? ')).upper()


    while room == 4:
        if command == 'N' or command == 'NORTH':
            print('You go the direction past the couch into the second bedroom')
            room = 7
        elif command == 'E' or command == 'EAST':
            print('You bump into a wall')
            room = 4
        elif command == 'W' or command == 'WEST':
            print('You could go this direction, but you stop when you trip over something in the floor, tehen lose directional sense and end up in the first bedroom')
            room = 5
        elif command == 'S' or command == 'SOUTH':
            print('You walk out of the living room back into the entrance room')
            room = 1
        elif command == 'NE' or command == 'NORTHEAST':
            print('You bump into a wall.')
            room = 4
        elif command == 'NW' or command == 'NORTHWEST':
            print('You go the direction jumping over the couch and into the bathroom')
            room = 9
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 4
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 4
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 4
            print('Room Description Living Room - There is a couch along the East wall and another couch in the center of the room. And a single couch toward the West wall. Two shelves along the west wall. Three doors along the North Wall. ')
            print('Exit Door on the North Wall all the way West leads to bedroom 1 - normal exit')
            print('Exit door in the middle of the North Wall leads to the bathroom - normal exit')
            print('Exit door on North Wall all the way East leads to bedroom 2 - normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 4
        return room



#bedroom1
#room just for show and distraction 
def bedroom1():
    room = 5
    print('Room Description Bedroom1 - See a bed in the middle of the room with the head board along the West Wall. A dresser is along the north wall. A door is all the way north on the East Wall.')
    print('Exit Door Along the East Wall leads to Closet 1 - normal exit')
    print('Exit door along the South Wall (same as the one entered in) -normal exit')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 5:
        if command == 'N' or command == 'NORTH':
            print('You bump into a bed. Ouch!')
            room = 5
        elif command == 'E' or command == 'EAST':
            print('You bump into a shelf')
        elif command == 'W' or command == 'WEST':
            print('You bump into a wall')
            room = 5
        elif command == 'S' or command == 'SOUTH':
            print('You go back out of the room into the living room where you began')
            room = 4
        elif command == 'NE' or command == 'NORTHEAST':
            print('You go the direction into the closet')
            room = 6
        elif command == 'NW' or command == 'NORTHWEST':
            print('You bump into a wall')
            room = 5
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 5
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 5
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 5
            print('Room Description Bedroom1 - See a bed in the middle of the room with the head board along the West Wall. A dresser is along the north wall. A door is all the way north on the East Wall.')
            print('Exit Door Along the East Wall leads to Closet 1 - normal exit')
            print('Exit door along the South Wall (same as the one entered in) -normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 5
        return room


#closet1
#this room has a box in it with clues to the murders if the user goes SE
def closet1():
    room = 6
    print('Room Description Closet1 - Bunch of clothes everywhere with a box laying in the floor ( you will be able to see what’s in this box)')
    print('Exit door along the West wall (same on as entered) - normal exit')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 6:
        if command == 'N' or command == 'NORTH':
            print('You bump into a wall. Ouch!')
            room = 6
        elif command == 'E' or command == 'EAST':
            print('Theres a wall there')
            room = 6
        elif command == 'W' or command == 'WEST':
            print('You go back out of the room into the bedroom')
            room = 5
        elif command == 'S' or command == 'SOUTH':
            print('You bump into a wall. Ouch!')
            room = 6
        elif command == 'NE' or command == 'NORTHEAST':
            print('You bump into a wall.')
            room = 6
        elif command == 'NW' or command == 'NORTHWEST':
            print('You bump into a wall')
            room = 6
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You find a box with notes in it that appear to be bloody love letters?')
            print('Basic summary of what you read is that whoevers box this is they murdered all the people who once lived here')
            print('One letter in particular explains that there were bunches of people that went into hiding down in the basement and that those were the \'bad\' people being murdered.')
            inventory.append('key')
            room = 6
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 6
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 6
            print('Room Description Closet1 - Bunch of clothes everywhere with a box laying in the floor ( you will be able to see what’s in this box)')
            print('Exit door along the West wall (same on as entered) - normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try anotehr direction')
            room = 6
        return room


#bedroom2
#this room is a distraction room for the user
def bedroom2():
    room = 7
    print('Room Description Bedroom2 -Bed is along the corner of the North and East Walls and there is a dresser along the South Wall. A door all the way north along the West Wall to the closet')
    print('Exit door along the West wall leads to closet - normal exit')
    print('Exit door along the South Wall (same as entered) - normal exit')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 7:
        if command == 'N' or command == 'NORTH':
            print('You bump into a wall. Ouch!')
            room = 7
        elif command == 'E' or command == 'EAST':
            print('You bump into a dresser but cant open it')
            room = 7
        elif command == 'W' or command == 'WEST':
            print('You bump into a wall')
            room = 7
        elif command == 'S' or command == 'SOUTH':
            print('You go back out of the room')
            room = 4
        elif command == 'NE' or command == 'NORTHEAST':
            print('You bump into a bed.')
            room = 7
        elif command == 'NW' or command == 'NORTHWEST':
            print('You go the direction into the second closet')
            room = 8
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 7
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 7
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 7
            print('Room Description Bedroom2 -Bed is along the corner of the North and East Walls and there is a dresser along the South Wall. A door all the way north along the West Wall to the closet')
            print('Exit door along the West wall leads to closet - normal exit')
            print('Exit door along the South Wall (same as entered) - normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try anotehr direction')
            room = 7
        return room


#closet2
# distraction room 
def closet2():
    room = 8 
    print('Room Description Closet2 - Nothing is in this room, but you can hear something coming from the south wall (you cannot enter)')
    print('Exit door along the East Wall (same as entered) - normal exit')

    command = str(input('What would you like to do? ')).upper()


    while room == 8:
        if command == 'N' or command == 'NORTH':
            print('You bump into a wall. Ouch!')
            room = 8
        elif command == 'E' or command == 'EAST':
            print('You go back out of the room into the bedroom')
            room = 7
        elif command == 'W' or command == 'WEST':
            print('You bump into a wall. Ouch!')
            room = 8
        elif command == 'S' or command == 'SOUTH':
            print('You bump into a wall. Ouch!')
            room = 8
        elif command == 'NE' or command == 'NORTHEAST':
            print('You bump into a wall.')
            room = 8
        elif command == 'NW' or command == 'NORTHWEST':
            print('You bump into a wall')
            room = 8
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 8
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 8
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 8 
            print('Room Description Closet2 - Nothing is in this room, but you can hear something coming from the south wall (you cannot enter)')
            print('Exit door along the East Wall (same as entered) - normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 8
        return room


#bathroom
#this room has a key in it that will be put into the users inventory[] if they go a specific direction
def bathroom():
    room = 9
    print('Room Description Bathroom - To the north is a sink and countertop with the toilet sitting to the West of the counter. A shower spans the entire West Wall. There is a noise coming from inside the counter. ')
    print('Exit door along the South Wall (same as entered) - normal exit')

    command = str(input('What would you like to do? ')).upper()


    while room == 9:
        if command == 'N' or command == 'NORTH':
            print('Theres a toilet there')
            print('Wait theres a key inside of the toilet? You grab it.')
            inventory.append('key')
            room = 9
        elif command == 'E' or command == 'EAST':
            print('Theres a wall there')
            room = 9
        elif command == 'W' or command == 'WEST':
            print('Youre gonna run into a wall')
            room = 9
        elif command == 'S' or command == 'SOUTH':
            print('You go back out of the room into the living room')
            room = 4
        elif command == 'NE' or command == 'NORTHEAST':
            print('Youre gonna run into a wall')
            room = 9
        elif command == 'NW' or command == 'NORTHWEST':
            print('Youre gonna run into a wall')
            room = 9
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 9
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 9
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 9
            print('Room Description Bathroom - To the north is a sink and countertop with the toilet sitting to the West of the counter. A shower spans the entire West Wall. There is a noise coming from inside the counter. ')
            print('Exit door along the South Wall (same as entered) - normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 9
        return room


#kitchen
#ordinary room 
def kitchen():
    room = 10
    print('Room Description Kitchen - Along the South and East Walls there are cabinets and Counters. In the center of the room there is an Island. There are knives all over the island.')
    print('Exit double doors along the North Wall all the way west - normal exit')
    print('Exit door along the South Wall (same as entered) - normal exit')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 10 :
        if command == 'N' or command == 'NORTH':
            print('You go the direction')
        elif command == 'E' or command == 'EAST':
            print('You find the counters')
            room = 10
        elif command == 'W' or command == 'WEST':
            print('Theres a wall there')
            room = 10
        elif command == 'S' or command == 'SOUTH':
            print('You go back out of the room into the entrance room')
            room = 1
        elif command == 'NE' or command == 'NORTHEAST':
            print('You bump into an island.')
            room = 10
        elif command == 'NW' or command == 'NORTHWEST':
            print('You bump into a wall')
            room = 10
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 10
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 10
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 10
            print('Room Description Kitchen - Along the South and East Walls there are cabinets and Counters. In the center of the room there is an Island. There are knives all over the island.')
            print('Exit double doors along the North Wall all the way west - normal exit')
            print('Exit door along the South Wall (same as entered) - normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 10
        return room


#dining_room
def dining_room():
    room = 11
    print('Room Description Dining Room - HUGE oval table spans the entire center of the room with 16 chairs around it.')
    print('Exit double doors along the West Wall - normal exit')
    print('Exit single double doors along the South Wall (same as entered) - normal exit')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 11:
        if command == 'N' or command == 'NORTH':
            print('Youre gonna bump into a wall')
            room = 11
        elif command == 'E' or command == 'EAST':
            print('You get to a huge table')
            room = 11
        elif command == 'W' or command == 'WEST':
            print('You bump into a wall')
            room = 11
        elif command == 'S' or command == 'SOUTH':
            print('You go back out of the room into the kitchen')
            room = 10
        elif command == 'NE' or command == 'NORTHEAST':
            print('You get to a huge table')
            room = 11
        elif command == 'NW' or command == 'NORTHWEST':
            print('You go the direction into the second hallway')
            room = 14
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 11
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 11
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 11
            print('Room Description Dining Room - HUGE oval table spans the entire center of the room with 16 chairs around it.')
            print('Exit double doors along the West Wall - normal exit')
            print('Exit single double doors along the South Wall (same as entered) - normal exit')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 11
        return room


#secret_room
#this is the only way for the user to get out of the house at all 
#there is a new direction in this room so that the user can get out
def secret_room():
    room = 12
    print('Room Description Secret Room - Bunk beds fill the room. There are 6 total. There is light coming from the North West corner of the room ')

    command = str(input('What would you like to do? ')).upper()

   
    while room == 12:
        if command == 'N' or command == 'NORTH':
            print('You bump into a wall. Ouch!')
            room = 12
        elif command == 'E' or command == 'EAST':
            print('You get to a bunk bed')
            room = 12
        elif command == 'W' or command == 'WEST':
            print('You bump into a wall')
            room = 12
        elif command == 'S' or command == 'SOUTH':
            print('You bump into a wall. Ouch!')
            room = 12
        elif command == 'NE' or command == 'NORTHEAST':
            print('You bump into a bunk bed that has a note on it.')
            print('The note reads: Dorthy, I need you to do something for me... meet me at the cabinet at midnight tonight. I think someone is trying to kill you. -Anthony')
            inventory.append('note')
            room = 12
        elif command == 'NW' or command == 'NORTHWEST':
            print('You bump into a wall')
            room = 12
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 12
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 12
        elif command == 'U' or command == 'UP':
            print('You may be getting somewhere. You begin to crawl somewhere, but you can see light')
            out()
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
                    room = 12
            print('Room Description Secret Room - Bunk beds fill the room. There are 6 total. There is light coming from the North West corner of the room ')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 12
        return room


#hallway1
#there is a secret passage in this room that leads to a secret room 
#there is a mirror in this room that if broken you can get to the secret passage
def hallway1():
    room = 13
    print('Room Description Hallway 1 - a single shelf spans the North Wall of the hallway there is a small hallway about a third of the way North through the hallway and a mirror on the wall about two thirds the way north through the hallway.')
    print('Exit door along the South Wall (same as entered) - normal exit')
    print('Exit hallway a third the way down the East Wall - normal exit')
    print('Watch your step though...')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 13:
        if command == 'N' or command == 'NORTH':
            print('You can see paintings in this direction showing a family that looks happy for a house that ended up like this')
            room = 13
        elif command == 'E' or command == 'EAST':
            print('You go into the second hallway through a secret passage')
            room = 14
        elif command == 'W' or command == 'WEST':
            print('You bump into a wall')
            room = 13
        elif command == 'S' or command == 'SOUTH':
            print('You go back out of the room into the entrance room')
            room = 1
        elif command == 'NE' or command == 'NORTHEAST':
            print('You go this direction.')
            room = 13
        elif command == 'NW' or command == 'NORTHWEST':
            print('Theres a large mirror do you wish to break it?')
            mirror = input('y or n?').lower()
            if mirror == 'y':
                print('You go into a secret passage way and FALL')
                room = 12
            elif mirror == 'n':
                print('You walk away')
                room = 13
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 13
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 13
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            room = 13
            print('Room Description Hallway 1 - a single shelf spans the North Wall of the hallway there is a small hallway about a third of the way North through the hallway and a mirror on the wall about two thirds the way north through the hallway.')
            print('Exit door along the South Wall (same as entered) - normal exit')
            print('Exit hallway a third the way down the East Wall - normal exit')
            print('Watch your step though...')
            command = str(input('What would you like to do? ')).upper()
        else:
            print('Try another direction')
            room = 13
        return room


#hallway2
#decoration room 
def hallway2():
    room = 14
    print('Room Description Hallway2 - There are paintings spanning the entire length of the hallway. There is a small hallway two thirds down the West Wall. There are double doors about two thirds the way down the East Wall.')
    print('Exit double doors along the East wall lead to dining room - normal exit')
    print('Exit hallway a third the way down the West Wall - normal exit')
    print('Exit door along the South Wall (same as entered) - normal exit')

    command = str(input('What would you like to do? ')).upper()

    
    while room == 14:
        if command == 'N' or command == 'NORTH':
            print('You can go this direction')
            room = 14
        elif command == 'E' or command == 'EAST':
            print('You bump into a wall')
        elif command == 'W' or command == 'WEST':
            print('You go back into the first hallway through a secret passage')
            room = 13
        elif command == 'S' or command == 'SOUTH':
            print('You go through a secret door but it only gets you back to the entrance')
            room = 1
        elif command == 'NE' or command == 'NORTHEAST':
            print('You can go this direction into the dining room')
            room = 11
        elif command == 'NW' or command == 'NORTHWEST':
            print('You can only see a glimpse of light, so you go back to where you are')
            room = 14
        elif command == 'SE' or command == 'SOUTHEAST':
            print('You bump into a wall. Ouch!')
            room = 14
        elif command == 'SW' or command == 'SOUTHWEST':
            print('You bump into a wall. Ouch!')
            room = 14
        elif command == 'HELP':
            help()
        elif command == 'LOOK':
            print('Room Description Hallway2 - There are paintings spanning the entire length of the hallway. There is a small hallway two thirds down the West Wall. There are double doors about two thirds the way down the East Wall.')
            print('Exit double doors along the East wall lead to dining room - normal exit')
            print('Exit hallway a third the way down the West Wall - normal exit')
            print('Exit door along the South Wall (same as entered) - normal exit')
            command = str(input('What would you like to do? ')).upper()
            room = 14
        else:
            print('Try another direction')
            room = 14
        return room

#this is called when the user chooses the right direction to get out of the house from the secret room
#there are only a few options for the user and most kill the user
def out():
    room = 15
    print('RUN')
    yorn = input('Do you wish to run? y/n?').lower()
    if yorn == 'y':
        print('You run toward the sound of cars and finally make it out of that house')
        print('You later discover that Dorthy lived in the house and she was the one who murdered everyone')
        print('Her lover, Anthony, thought she was being hunted, but in reality she was doing the hunting')
        print('There has been no motive as to why Dorthy did this and teh bodies have never been found')
    elif yorn == 'n':
        print('You might really want to start running')
        print('THERES SOMEONE BEHIND YOU. This is you last chance to run!')
        print('its too late...youre dead')
    else:
        print('no offense but you just died')
    exit()


#main program
#tried to keep this short and simple if just loops while the user is still in a room and is continuing the game
inventory = []
room = 1
continueGame = True
while continueGame == True:
    if room ==  1:
        room = entrance_room()
    elif room == 2:
        room = side1_room()
    elif room == 3:
        room = side2_room()
    elif room == 4:
        room = livingroom()
    elif room == 5:
        room = bedroom1()
    elif room == 6:
        room = closet1()
    elif room == 7:
        room = bedroom2()
    elif room == 8:
        room = closet2()
    elif room == 9:
        room = bathroom()
    elif room == 10:
        room = kitchen()
    elif room == 11:
        room = dining_room()
    elif room == 12:
        room = secret_room()
    elif room == 13:
        room = hallway1()
    elif room == 14:
        room = hallway2()
    else:
        print('Yea, you are definitely lost')