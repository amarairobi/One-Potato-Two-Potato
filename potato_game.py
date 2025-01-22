import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

class PotatoGame:
    def __init__(self):
        self.head = None
        self.current = None

    def create_players(self, n):
        self.head = Node(0)
        self.current = self.head
        for i in range(1, n):
            self.current.nxt = Node(i)
            self.current = self.current.nxt
        self.current.nxt = self.head
        self.current = self.head

    def eliminate_next(self, k):
        for j in range(k-1):
            self.current = self.current.nxt
        eliminated = self.current.nxt.data
        self.current.nxt = self.current.nxt.nxt
        return eliminated

    def get_winner(self):
        return self.current.data

class PotatoGameGUI:
    def __init__(self, root):
        self.root = root
        self.game = PotatoGame()
        self.n = 0
        self.k = 0
        self.players = []
        self.create_widgets()

    def create_widgets(self):
        # input fields for n and k
        tk.Label(self.root, text="N:",font=("Helvetica", 12)).pack()
        self.n_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.n_entry.pack()

        tk.Label(self.root, text="K:", font=("Helvetica", 12)).pack()
        self.k_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.k_entry.pack()

        # start button
        self.start_button = tk.Button(self.root, text="Start",font=("Helvetica", 12), command=self.start_game)
        self.start_button.pack()

        # text widget for messages
        self.text_widget = tk.Text(self.root, height=10, width=40,font=("Helvetica", 12))
        self.text_widget.pack()
        
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

    def start_game(self):
        # see if n and k are valid
        try:
            self.n = int(self.n_entry.get())
            self.k = int(self.k_entry.get())
            if not (1 < self.n < 12 and self.k >= 1):
                raise ValueError
        except ValueError:
            messagebox.showinfo("Invalid Input", "N must be 2-11 and K >= 1.")
            return

        # to start up the game
        self.game.create_players(self.n)
        self.players = list(range(self.n))

   
        self.display_players()


        self.eliminate_button = tk.Button(self.root, text="Eliminate", command=self.eliminate_player)
        self.eliminate_button.pack()

        # display game start message
        self.text_widget.insert(tk.END, f"Game started. N={self.n}, K={self.k}\n")
    

    
    def display_players(self):
        import math  
        # to clear previous icons and display current players
        self.canvas.delete("all")
        cx, cy = 200, 200
        radius = 150
        num_players = len(self.players)

        for i, player in enumerate(self.players):
            angle = 2 * math.pi * i / num_players
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            self.canvas.create_text(x, y, text=str(player), font=("Helvetica", 14), fill="black")



    def eliminate_player(self):
        if len(self.players) == 2:
            # to display the winner
            winner = self.game.get_winner()
            messagebox.showinfo("Winner", f"The winner is: Player {winner}!")
            self.reset_game()
            return

        eliminated = self.game.eliminate_next(self.k)
        self.players.remove(eliminated)
        self.text_widget.insert(tk.END, f"Player {eliminated} eliminated.\n")
        self.display_players()

    def reset_game(self):
        # resetting the user interface for the next game
        self.players.clear()
        self.text_widget.delete("1.0", tk.END)
        self.eliminate_button.destroy()

# initializing the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Potato Game")
    app = PotatoGameGUI(root)
    root.mainloop()
