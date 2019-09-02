#!/usr/bin/python
import RPi.GPIO as GPIO
import time, random
GPIO.setmode(GPIO.BOARD)
# Set up the LED pin as an output
led = 37
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)
# Set up the pins that the buttons connect to as inputs
s1 = 11
s2 = 13
GPIO.setup(s1, GPIO.IN)
GPIO.setup(s2, GPIO.IN)
# Set up buzzer
buzzer = 12
GPIO.setup(buzzer, GPIO.OUT)
# Initialise PWM, 1kHz
p = GPIO.PWM(buzzer, 1000)
# Get player names
gameLoop = True
player_1Score = 0
player_2Score = 0
player1 = input("Enter Player 1’s name: ")
player2 = input("Enter Player 2’s name: ")
while gameLoop == True:
    gameLoop = False
    # Wait random number of seconds before turning LED on
    time.sleep(random.uniform(5, 10))
    GPIO.output(led,1)
    startTime = time.time()
    # Loop to wait until a button is pressed
    while GPIO.input(s1) == False and GPIO.input(s2) == False:
        pass
    # Determine which button was pressed
    if GPIO.input(s1) == True:
        print(player1 + " wins!")
        player_1Score += 1
    else:
        print(player2 + " wins!")
        player_2Score += 1
    reactionTime = str(time.time() - startTime)
    print("Reaction time: "+reactionTime+" S")
    # Button was pressed so sound buzzer for 0.5 seconds
    p.start(50) # 50% duty cycle
    time.sleep(0.5)
    p.stop()
    GPIO.output(led, 0)
    playerInput = input("Play again? (y/N): ")
    if playerInput == "y":
        gameLoop = True
    else:
        if player_1Score > player_2Score:
            print("Player 1 is overall winner with ",player_1Score," points")
        elif player_2Score > player_1Score:
            print("Player 2 is overall winner with ",player_2Score," points")
        else:
            print("Game is a draw")
GPIO.cleanup()
