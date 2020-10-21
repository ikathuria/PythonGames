import os

while (1):
  print("1. Rock Paper Scissors")
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
    os.system("python Blackjack/game.py")
  
  elif choice == 5:
    print("Thank You for playing!")
    print("Goodbye!")
    break;
  
  else:
    print("Invalid option! Try again!")
