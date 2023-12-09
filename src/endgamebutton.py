#import tkinter as tk
#from tkinter import messagebox

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Game App")

        # Create a button that ends the game
        self.end_game_button = tk.Button(root, text="End Game", command=self.end_game)
        self.end_game_button.pack(pady=20)

    def end_game(self):
        # Display a message box to confirm ending the game
        result = messagebox.askquestion("End Game", "Are you sure you want to end the game?")
        if result == "yes":
            print("Game Ended")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()