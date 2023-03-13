#SNAKE AND LADDER GAME IN PYTHON

import random

# Define the Snake and Ladder board as a dictionary
board = {
    3: 17,
    7: 11,
    13: 5,
    19: 2,
    21: 9,
    27: 1,
    31: 19,
    33: 15,
    37: 23,
    43: 29,
    47: 37,
    49: 32,
    51: 11,
    53: 9,
    55: 7,
    57: 28,
    59: 38,
    61: 18,
    63: 45,
    67: 48,
    69: 39,
    73: 53,
    75: 28,
    79: 59,
    81: 30,
    87: 33,
    91: 20,
    93: 13,
    97: 67,
    99: 26
}

# Define the main game loop
def play_game():
    # Initialize the player's position to 0
    player_position = 0
    
    # Main game loop
    while True:
        # Roll the dice
        input("Press Enter to roll the dice...")
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}!")
        
        # Update the player's position based on the dice roll
        player_position += dice_roll
        
        # Check if the player has won
        if player_position >= 100:
            print("Congratulations! You won!")
            break
        
        # Check if the player has landed on a Snake or Ladder
        if player_position in board:
            new_position = board[player_position]
            if new_position > player_position:
                print(f"You landed on a ladder! You move from {player_position} to {new_position}")
            else:
                print(f"You landed on a snake! You move from {player_position} to {new_position}")
            player_position = new_position
        
        # Print the player's current position
        print(f"You are now at position {player_position}")
        
# Start the game
play_game()
