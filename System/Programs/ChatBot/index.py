import chatty
import Data

print("Welcome to Python OS chat bot. Type 'exit' to stop chat bot. WARNING this is a very basic bot.")
while True:
    UserInput = input("User: ").lower()
    if UserInput == "exit":
        exit()
    
    print(f"{Data.bots_name}: {chatty.Ask_Bot(UserInput)}")