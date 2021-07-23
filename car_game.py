command = ""
started = False
print("Type 'help' to get the commands!")
while True :
    command = input(">").lower()
    if command == 'start':
        if started:
            print("Car already started!")
        else:
            started = True
            print("The car started...")
    elif command == "stop" :
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help" :
        print("""
start - to start the car
stop - to stop the car
quit - to quit 
            """)
    elif command == 'quit':
        break
    else:
        print("Sorry I don't understand that!")

