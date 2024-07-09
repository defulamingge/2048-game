import game

# This is the main function that runs the game.
def main():
    while True:
        grid = game.initialize_grid()
        while True:
            game.print_grid(grid)
            
            if game.check_win(grid):
                print("Congratulations! You've reached 2048!")
                break
            if game.check_game_over(grid):
                print("Game over! No more moves left.")
                break

            move = input("Enter move (w/a/s/d) or 'q' to quit: ").strip().lower()
            if move == 'q':
                print("Thanks for playing!")
                return
            if move not in ['w', 'a', 's', 'd']:
                print("Invalid input! Please enter w, a, s, or d.")
                continue

            initial_grid = [row[:] for row in grid]
            if move == 'w':
                grid = game.move_up(grid)
            elif move == 'a':
                grid = game.move_left(grid)
            elif move == 's':
                grid = game.move_down(grid)
            elif move == 'd':
                grid = game.move_right(grid)

            if grid != initial_grid:
                game.add_random_two(grid)
            else:
                print("No valid move! Try a different direction.")


if __name__ == "__main__":
    main()
