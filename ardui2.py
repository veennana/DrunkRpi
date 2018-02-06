import time
import serial



ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=5)
PIN_final=0
BAC = 0 #BAC reading from arduino

relay=0 #Variable controlling ignition
game_total=0.0#total scores during game
score2 = 0 #individual score for game REMOVE after adding game to code


def class_drunk(float_BAC):#if BAC reaches 0.05 or above consistently for 10 seconds
    relay=0
    float_BAC2 =float_BAC*0.1 
    print("BAC detected to be %0.2f! Ignition is now locked. Simulating test")%float_BAC2
    time.sleep(7)
    class_game(game_total)
    
def class_game(game_total):#start game
    
    from Mouse_Trap_New import game_intro, variables.dodged
    class_game_result(game_total,variables.dodged)

def class_game_result(game_total, variables.dodged):

    print(variables.dodged)
	
    if variables.dodged>=14 and variables.dodged<=19:
        game_total = game_total+0.5
        
    elif variables.dodged>=20:
        game_total = game_total+1 #1 if cycle per game
		print("You have passed the sobriety test, ignition is now enabled")
        class_longnodrunk()
	
	else:
		class_game2(game_total)
		
def class_game2(game_total):

	score2=int(input("Enter score sa 2nd game: "))
	
    if score2>=14 and score2<=19:
        game_total = game_total+0.5
        
    elif score2>=20:
        game_total = game_total+1 #1 if cycle per game

    if game_total == 1:
        time.sleep(3)
        print("You have passed the sobriety test, ignition is now enabled")
        time.sleep(5)
        class_longnodrunk()
    else:
        time.sleep(3)
        print("You have failed the sobriety test, proceeding to protocol")
        time.sleep(5)
        class_gsm()
        
def class_gsm():
        time.sleep(2)
        ser.write('1')
        while 1:
            if ser.in_waiting > 0:
                PIN_old = ser.readline()
                PIN_new = PIN_old.split()
                PIN_int = [int(i) for i in PIN_new]
                PIN_final=PIN_int[0]
                print(PIN_final)
                try1(PIN_final)
        
def try1(PIN_final):
        guess=int(input("Enter 5-digit code sent via mobile: "))
        pinConfirm(3,guess,PIN_final)

def try2(PIN_final):
        guess=int(input("Enter 5-digit code sent via mobile: "))
        pinConfirm(2,guess,PIN_final)

def try3(PIN_final):
        guess=int(input("Enter 5-digit code sent via mobile: "))
        pinConfirm(0,guess,PIN_final)
        
def class_longnodrunk():
		relay=0
                sensor_mode()
        
def class_longdrunk():
		relay=1
                sensor_mode()

def pinConfirm(tries,inputfromText,PIN_final):
        
        
        if inputfromText != PIN_final: 
        
                        if tries==3:
                                print("PIN is incorrect! 2 tries left")
                                try2(PIN_final)
                        if tries==2:
                                print("PIN is incorrect! 1 try left")
                                try3(PIN_final)
                        elif tries==0:
                                print("PIN is incorrect! You have reached the maximum number of tries. Please wait for the lockdown period to finish")
                                
        elif inputfromText == PIN_final:
             
                        print("PIN validation successful! Vehicle ignition system has been enabled")
                        class_longnodrunk()
                        
def sensor_mode():

    while 1:
            if ser.in_waiting > 0:
                BAC_old = ser.readline()
                BAC_new = BAC_old.split()
                BAC_int = [int(i) for i in BAC_new]
                BAC_final=BAC_int[0]
                print(BAC_final)
				
                if BAC_final < 5:
                    BAC=BAC_final*0.01
                    print(BAC_final)
					
                elif BAC_final >=5 and BAC_final <=10:
                 
                    class_drunk(BAC_final*0.1)
					
                else:
                    print("BAC data unrecognizable")

sensor_mode()
