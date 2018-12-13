#I could not provide the iPython output to Mrs. Feeney, due to code and canopy issues. 
from __future__ import print_function
import random

thingsDoneInHallwayA = []
playerItems = []
enteredRooms = []
openedDoors = []
likability = False
flag = True
flag2 = True

def cellB():
    flag2 = True
    print("\nThis cell has one other prisoner in it.")
    flag = True
    while flag == True:
        if 'gold'in playerItems: 
            print('Here, have the chloroform')
        else:    
            print("Ahoy mate, what are you doing here?")
            choice = input("You want the chloroform? \n")
            if choice == 'yes':
                print("You need to get me gold first!")
            else: 
                print("Too bad, so sad")
    
        playerChoice = input("What do you want to do next? \n")
        while flag2 == True:
            if playerChoice in ['exit']:
                hallwayA()
                flag2 = False
            else:
                print("Invalid Command try again.")
                playerChoice = input("What do you want to do next? \n")
                
	
def cellC():
    x=0
    global enteredRooms
    print('You entered cellC')
    if 'cellC' in enteredRooms:
        print('This cell looks vaguely familiar')
    if 'cellC' not in enteredRooms:
        enteredRooms += ['cellC']
	survey = input('What do you want to do?:')
	while x==0:
		if survey in ['survey','search','look']:
			search = input('You found a loose brick. What do you want to do?:')
			if search in ['remove','break'] and 'bar' in playerItems:
				found = input('You found a golden tooth. Do you want to leave the cell or hide?:')
				playerItems += ['gold']
				if found == 'leave':
					x+=1
				elif found == 'hide':
					print('The guard has found you.')
					lose()
				else:
					print ('The value', found , 'is not recognized')
			elif survey in ['exit','leave']:
				x+=1
			else:
				print ('The value', search , 'is not recognized')
		if survey in ['exit','leave']:
		     x+=1
		else:
		     print ('The value', survey , 'is not recognized')
	        if x==1:
	           print('You have now exited cellC and entered hallB')
	           hallB()
		
def cellA():
    y=0
    global enteredRooms
    print('You entered cellA')
    if 'cellA' in enteredRooms:
        print('This cell looks vaguely familiar')
    if 'cellA' not in enteredRooms:
        enteredRooms += ['cellA']  
	while y==0:
		speak = input('A prisoner in cellA approaches you. Do you want to speak with him or leave?:')
		if speak == 'speak':
			rope = input('He offers you a rope if and only if you guess his secret number between one and a million. Do you want to guess or exit?:')
			if rope == 'guess':
				guess = input('What is your guess?:')
				if guess in ['z','Z']:
					print('You guessed my number. Ha Ha Ha! Here is your rope!')
					playerItems += [rope]
					guard = input('A guard is nearby. Do you want to run, hide, or walk?:')
					if guard in [run,walk]:
						y+=1
					elif guard == 'hide':
						print('The guard has found you!')
						lose()
					else:
						print ('The value', guard , 'is not recognized')
				else:
					print('You have not guessed my number correctly. LEAVE YOU DISGRACE!')
					y+=1
			elif rope == 'exit':
					y+=1
			else:
				print ('The value', rope , 'is not recognized')
		elif speak == 'leave':
			y+=1
		else:
			print ('The value', speak , 'is not recognized')
	if y==1:
		print('You have now exited cellA and entered hallA')
		hallA()
			
		

def hallwayA():
    enteredRooms = []
    thingsDoneInHallA = []
    flag = True
    flag3 = True 

    while flag == True:
        if'room' not in enteredRooms:
            print("This is a hallway, illuminated with dim lights. This is a pretty long hallway, with a lot of cobwebs. There is Cell A to your right and Cell B to your left. Suddenly a spider drops down in front of your legs.")
        
        if'room' in enteredRooms:
            print("This hallway looks familiar")
           
        spiderAction = input("What do you want to do?\n")
        while flag3 == True:
            if spiderAction in ["kill spider", "step on spider"]:
                print("The spider has been killed")
                thingsDoneInHallA += ["The spider has been killed"]
                spiderAction = input("What do you want to do now?\n")
            elif "The spider has been killed" in thingsDoneInHallA:
                print("You have killed a potential friend here. You'll be haunted by that spider for the rest of your short life.")
                spiderAction = input("What do you want to do?\n")
            elif spiderAction in ["enter cell b", "go to cell b"]:
                enteredRooms += ["room"]
                #print(enteredRooms)
                cellB()
                flag3 = False
            elif spiderAction == "befriend spider":
                print("The spider, named Spid, which will follow you around now, like a great companion!")
                thingsDoneInHallA += ["The spider is your friend"]
                spiderAction = input("What do you want to do now?\n")
            elif spiderAction in ["go to hallway b", "next hallway"]:
                hallwayB()
                flag3 = False 
            elif spiderAction == 'enter cell a':
                cellA()
                flag3 = False 
            elif spiderAction == "exit":
                print("You can't exit the hallway, you are still in this dim hallway and you can go to cell A, cell B or hallway B ")
                spiderAction = input("What do you want to do now?\n")
            else:
                print("This command is not valid")
                spiderAction = input("Try again: What do you want to do now?\n")
        flag = False 

def yourCell():
	#this allows us to use global variables, so that the events in each cell are not independent of one another
	global playerItems
    	global enteredRooms
   	global openedDoors
	
	#sets me up to be able to break  my while loop later
    	exitRoom = False
	
    	cellItems = ['pillow','pillowcase']
    	print('Your hands shake as you pace around your cramped cell')
    	print('The cell bars are tight and close, but they look weak.')
    	while exitRoom == False:
		#allows the user to choose what they want to do
        	userAction = input('What would you like to do? ')
		
		#different outcomes for different choices
        	if userAction == 'slide through bars' and 'bar' in playerItems:
           		print('You slip through the bars, holding the bar.')
			#this way, you can't just leave the cell -- keeps track of where you've been
            		openedDoors += ['yourCell']
            		exitRoom = True
        	elif userAction == 'pick up pillow':
            		print('You picked up the pillow')
            		playerItems += ['pillow']
            		exitRoom = False
		#allows for user error to be fixed	
        	else:
            		userAction = input('Not a valid action.  Try Again! ')
    	if 'yourCell' in openedDoors:
        	hallA()  
	
def hallB():
	#global variable usage is key to make sure the game runs continuously
    	global playerItems
    	global enteredRooms
    	global openedDoors
    	exitRoom = False
	
	#need this to see where we have been for other rooms' purposes
    	enteredRooms += ['hallB']
    	
	#nice opening monolouge to let the user understand their surroundings
    	print('The hall is dark and musty, lit by a single torch on the stone walls.')
    	print('There are 3 doors, one on the east (door 1), one on the west (door 2), and one directly south of you (door 3).')
    	print('Their is a door directly north of you that is guarded by a tall, dark man in leather armor.')
    
    	#using the same while loop as in yourCell()
    	while exitRoom == False:
        	
		#eliminates the guard as an issue before the user is ready to confront
        	action = input('Would you like to confront the guard? (yes or no)')
    
    		#when they want to confront
        	if action == 'yes':
            	   print('As you approach the guard, he turns to face you.')
            	   print('He lifts his hood and stands up straight to confront you.')
            	   choice = input('What are you doing out of your cell?(looking to barter or looking to fight)')
            
	    	#makes sure the use chooses a valid response
            	while choice != 'looking to barter' and choice != 'looking to fight':
                	choice = input('Invalid response (looking to barter or looking to fight):')
        
            	while choice == 'looking to barter':
                	print('The guard takes a step towards you.')
                	barter = input('I am listening. Go on, what do you have for me?:')
         		
			#makes sure they barter what they have
                	while barter not in playerItems:
                    		print('You can not barter something you do not have.')
                    		barter = input('Invalid response (looking to barter or looking to fight):') #second chance
                
			#the two incorrect barter choices
                	if barter == 'gold' and 'gold' in playerItems or barter == 'pillow' and 'gold' in playerItems:
                    		print('You think I want some old ' + barter + '?')
                    		response = input('The guard reaches for his sword. You must now fight or surrender.') 
                    		if response == 'surrender':
                        		print('You surrender yourself to the guard.')
                        		print('He yells for other guards. You have failed.')
                        		lose()	#this way we don't get stuck in loops
                    		if response == 'fight':
                        		choice = 'looking to fight' #break the loop
                
                	elif barter == 'spider' and 'spider' in playerItems:
                    		playerItems -= [barter]
                    		print('The guards eyes water at the look of the spider.')
                    		print('You notice the guards sunken eyes and hollow cheeks.')
                    		print('He looks like he has not eaten for days.')
                    		print('You take one look at your spider friend. He gives you a little nod as if to say "It will be okay".')
                    		print('You hand your little buddy over and turn away as you hear the deafening crunch of the ultimate sacrifice.')
                    		win() #don't get stuck in loops
            
            	while choice == 'looking to fight':
                	print('Your hands sweat as you think of what you should use to defend yourself.')
                	weapon = input('What do you use to defend yourself?')
			#makes sure that we use a weapon I have coded for
                	while weapon != 'chloroform' and weapon != 'bar' or weapon not in playerItems:
                            weapon = input('Invalid choice, try a different item: ')
                
			#basic if statement of the conditions to win
                	if weapon == 'chloroform' and 'chloroform' in playerItems and 'rope' in playerItems:
                    		print('You knock the guard out with your rag and leave him tied up against the wall.')
		    		playerItems =- 'chloroform'
		    		playerItems -='rope'
                    		win()
            
                	elif weapon == 'bar' and 'rope' not in playerItems:
                    		print('You successfully strike the guard and drop the bar to the ground with a resounding clang.')
                    		print('Your hand is turning the door handle when your legs are knocked out from under you.')
                    		print('Your head is spinning as you look up and see the guard kneeling over you, calling out for help.')
                    		print('The other guards come quickly to his aid.')
                    		lose()
                	elif weapon == 'bar' and 'rope' in playerItems:
                    		print('You successfully strike the guard and drop the bar to the ground with a resounding clang.')
                   		print('You tie the guard up and leave him leaning against the stone wall')
		    		playerItems -= 'bar'
		    		playerItems -= 'rope'
                    		win()
        #if you chose not to confront the guard, you can just go to one of the other rooms        
        if action == 'no':
		move = input('Which door would you like to enter?(door 1, door 2, or door 3): ')
            	if move == 'door 1':
                	cellD()
                	exitRoom = True
           	elif move == 'door 2':
                	cellC()
                	exitRoom = True
            	elif move == 'door 3':
                	hallA()
                	exitRoom = True
		elif action == 'quit':
			quit()
		#gives the option to quit the game instead of continue playing	
		elif action == 'quit':
		  quit()
        #making usre we have valid inputs
        elif action not in ['yes', 'no', 'quit']:
            	print('Invalid option, please try again.')
        	
def cellD():
	global playerItems
	global enteredRooms
	global openedDoors
	global likability
	exitRoom = False
	cellItems = []

	if not("cD" in enteredRooms):
		enteredRooms += ["cD"]
		print("This cell is dark just like the rest of them. Before you stands to tall figure.")
		print("One to your left, the other to your right.")
		print("The one to your right barks, 'Hey what are you doing in here?'")
		print("How do you respond.")
		print("You are hiding from the guard or you are trying to escape the prison?")
		response = raw_input("Hide or Escape: ")
		while response != "Hide" and response != "Escape":
		  response = raw_input("Invalid Option, Hide or Escape: ")
		if response == "Hide":
			likability = True
			print('The one to your left says, "We can sympathize with that. That guard has been a pain to everyone around here."')
		else:
			print('The one on your right scoffs, "Ha. Your trying to escape this prison, fat chance."')
			print('The one on your left chimes in, "Well, he has made it this far. Who is to say he cannot."')
			print('The one on your right says, "Maybe your right. Maybe he can do it. But will he take us with him?"')
			print('Will you try to free these prisoners?')
			response = raw_input('Yes or No: ')
			while response != "Yes" and response != "No":
			 response = raw_input("Invalid Option, Yes or No: ")
			if response == "Yes":
				likability = True
				print('The one on your right shouts, "Alright, nice. Hey, any information you need, we both got it."')
			else:
				print("The one on your right menacingly says, Wrong answer bub. You'll have to make it up to us now.")
				print('The one on your left says, "Why not leave that little pillow case we see you dragging around."')
				playerItems.remove("pillowcase")
				cellItems += ["pillowcase"]
				print("You don't think you can take a two on one fight. You drop your pillow case in the room.")
				print("Without it, you can only carry two items.")

	else:
		print("This is the cell with the two mysterious figures in it. It hasn't changed much since you left.")
		if likability == True:
			print("The prisoner on your right says, Hey it's good to see you again.")
			print('The prisoner on your left says, "What do you need?"')
		else:
			print('The prisoner on your right says, "You got a lotta nerve comming back here."')
			print('The prisoner on your left nods in agreement')

	if len(playerItems) > 2:
		if not("pillowcase" in playerItems):
			while len(playerItems) > 2:
				print("You currently cannot hold more than two items. Which one will you drop")
				for item in playerItems:
				    print(item)
				item = raw_input()
				while not(item in playerItems):
					item = raw_input("Invalid object, try another: ")
				playerItems.remove(item)
				cellItems += [item]
				print("You dropped" + item)

	while exitRoom == False:
		action = raw_input("What do you want to do?  ")
		if action in ['survey', 'look', 'search']:
			if len(cellItems) == 0:
				print("You look around the cell and find it is still dark. It also does not contain anything of note.")
			else:
				print("You look around the cell and find it is still dark. There are some things on the floor you might")
				print("be able to take.")
		elif action in ['take', 'pick up']:
			if len(cellItems) == 0:
				print("There are no items to pick up.")
			else:
				for item in cellItems:
					print(item)
				item = raw_input("Take what? ")
				while not(item in cellItems):
					item = raw_input("Invalid object, try another: ")
				if item != 'pillowcase':
					playerItems += [item]
					print("You added " + item + " to your inventory")
					if len(playerItems) > 2:
						if not("pillowcase" in playerItems):
							while len(playerItems) > 2:
								print("You currently cannot hold more than two items. Which one will you drop")
								for item in playerItems:
									print(item)
								item = raw_input()
								while not(item in playerItems):
									item = raw_input("Invalid object, try another: ")
								playerItems.remove(item)
								cellItems += [item]
								print("You dropped " + item)
				else:
					if likability == False:
						print('The prisoner on your right growls at you.')
						print('You may want to reconsider taking that.')
					else:
						playerItems += [item]
						print("You added " + item + " to your inventory")

		elif action in ['drop', 'put down']:
			if len(playerItems) > 0:
				print("Which item will you drop")
				for item in playerItems:
					print(item)
				item = raw_input()
				while not(item in playerItems):
					item = raw_input("Invalid object, try another: ")
				playerItems.remove(item)
				cellItems += [item]
				print("You dropped " + item)
			else:
				print("You have nothing on you to drop.")

		elif action in ['give', 'gift']:
			if len(playerItems) == 0:
				print("You cannot give something you don't have")
			else:
				print("Which item will you give")
				for item in playerItems:
					print(item)
				item = raw_input()
				if item != 'pillow':
					print("The prisoner on your left looks at you funny.")
					print("He says, That's not something we need.")
				else:
					playerItems.remove(item)
					print("The prisoner on your right says, Really, you'd give that to us?")
					print('The prisoner on your left says, "Now we can both have something to sleep on.')
					print('Our deepest gratitude."')
					likability = True

		elif action in ['talk', 'chat']:
			if likability == False:
				print('The one on your left says, "Find us in a kinder mood first."')
			else:
				print("Talk about what?")
				print("accross, diagonal, next to, guard, you two")
				question == raw_input()
				while not(question in ['accross', 'diagonal', 'next to', 'guard', 'you two']):
					print("Not a valid option, try again")
					question = raw_input()
				if question == 'accross':
					print('The one on your right says, "There used to be a guy in that cell.')
					print('He just disappeared one day though. Might of been something to do')
					print("with his obsession with shiny things. Wouldn't be shocked if he left")
					print('something shiny in his cell."')
				elif question == 'diagonal':
					print('The one on your left says, "Now that guy there is a tough one.')
					print("He's super possessive of his things. It'd take something very valuable")
					print('to make him give something up."')
				elif question == 'next to':
					print('The one on your right says, "That guy is looney.')
					print("He's a real pain, and he won't stop saying " + str(z) + " in his sleep.")
				elif question == 'guard':
					print('The one on your left says, "The guard standing out there is a toughie.')
					print('I would challeng him unless I had a good game plan. Although, I have heard')
					print('he takes bribes."')
				else:
					print('The one on your right says, "Us? We both got caught in the crime together.')
					print("You don't need to know more than that.")
		elif action in ['leave', 'exit']:
			exitRoom = True
		else:
			print("Invalid action, try another")
	print("You left the cell and entered the hallway. The guard stands nearby.")
	hallB()
   	
               
def startGame():
    print('Welcome to Prison Break')
    raw_input('Press enter to start the game. ')
    yourCell()
    
def lose():   
	print('You have lost the game.')

def win():
	print('You have won the game!')
	
def quit():
	print('You have quit the game!')
