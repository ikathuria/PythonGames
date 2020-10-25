import os
import time

def clearScreen():
  time.sleep(1.5)

  if os.name == 'posix':
    _ = os.system('clear')
  else:
    # for windows platfrom
    _ = os.system('cls')

while (1):
  wel = 'WELCOME TO PYTHON GAMES'
  print('\n', *wel)
  print("\n1. Rock Paper Scissors")
  print("2. Tic-Tac-Toe")
  print("3. War")
  print("4. Blackjack")
  print("5. Exit")
  choice = int(input("Which game do you want to play? (1-5): "))

  if choice == 1:
    os.system("python Rock-Paper-Scissors/game.py")

  elif choice == 2:
    os.system("python Tic-Tac-Toe/game.py")
    
  elif choice == 3:
    os.system("python War/game.py")
    
  elif choice == 4:
    os.system("python BlackJack/game.py")
  
  elif choice == 5:
    print("\nThank You for playing!")
    print("Goodbye!")
    break;
  
  else:
    print("Invalid option! Try again!")
  
  clearScreen()
