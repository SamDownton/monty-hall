'''
Created on 2 Jun 2016

@author: samuel.downton
'''

import random

def hide_the_car(num_of_doors):
    doors = []
    for i in xrange(num_of_doors):
        doors.append(0)
        i += 1
    doors[random.randint(0,len(doors))-1] = 1
    # print doors
    return doors

def pick_a_door(doors):
    rand = random.randint(0,len(doors)-1)
    # print "choice door", rand
    return rand


def leave_door_shut(doors, door):
    choose = []
    if doors[door] == 1: 
        for i in xrange(len(doors)):
            if i != door:
                choose.append(i)
        return choose[random.randint(0, len(choose)-1)]
    else:
        for i in xrange(len(doors)):
            if doors[i] == 1:
                the_door = i
        return the_door
    

def play_quietly(num_doors):
    doors = hide_the_car(num_doors)
    door = pick_a_door(doors)
    shut_door = leave_door_shut(doors, door)
    # print "switched door", doors[shut_door]
    if doors[shut_door] == 1:
        return 1
    else: 
        return 0
    
def play_loads_of_times(time_to_play, num_doors):
    i = 0
    results = []
    while i < time_to_play:
        result = play_quietly(num_doors)
        results.append(result)
        i += 1
    percent_times_one = (float(sum(results)) / float(time_to_play)) * 100
    print percent_times_one, "% of games won"
    
def play_interactively():
    play = True
    while play:
        num_doors = int(raw_input("How many doors would you like to play with? : "))     
        doors = hide_the_car(num_doors)
        print "Please choose the door you think contains the prize ( 0 -", len(doors) - 1, "):"
        door = int(raw_input())
        closed_door = leave_door_shut(doors, door)
        print "Goats have been revealed behind all the doors, except for your door, number", door
        print "and door number", closed_door, ". Would you like to swap or keep your original choice (S/K)? "
        choice = raw_input()
        for i in xrange(len(doors)):
            if doors[i] == 1:
                prize_location = i
        validate = False
        while not validate:
            if choice == "S" or choice =="K":
                validate = True
            else:
                choice = raw_input("You must select \"S\" or \"K\"")
        if choice == "S":
            door = closed_door
        if doors[door] == 1:
            print "Congratulations! You Win!"
        else:
            print "You lose! The prize was behind door number", prize_location
        validate = False
        continue_ = raw_input("Would you like to play again? (Y/N)")
        while not validate:       
            if continue_ == "Y" or continue_ == "N":
                validate = True
            else:
                continue_ = raw_input("You must enter \"Y\" or \"N \"")
        if continue_ == "N":
            play = False
        
def start_up():
    validated = False
    choice = raw_input("Please enter 1 to play interactively or 2 to run a bulk simulation: ")
    while not validated:
        if int(choice) == 1 or int(choice) == 2 or int(choice) == 3:
            validated = True
        else:
            choice = int(raw_input("You must enter 1 or 2! :"))
    if choice == 1:
        play_interactively()
    else:
        num_of_plays = int(raw_input("Enter number of times to play: "))
        num_of_doors = int(raw_input("Enter number of doors in game (2+): "))
        play_loads_of_times(num_of_plays, num_of_doors) 
         

if __name__ == '__main__':
    start_up()



            
    