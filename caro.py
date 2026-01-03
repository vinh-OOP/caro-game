import tkinter as tk
from tkinter import messagebox

class CaroGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CARO")
        
        self.turn = 'X' 
        self.buttons = []
        
       
        for r in range(3):
            row_buttons = []
            for c in range(3):
               
                btn = tk.Button(
                    self.root, 
                    text="", 
                    font=("Arial", 20, "bold"),
                    width=6, height=3,
                    
                    command=lambda r=r, c=c: self.on_click(r, c)
                )
                
                btn.grid(row=r, column=c)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def on_click(self, r, c):
       
        current_btn = self.buttons[r][c]

       
        if current_btn['text'] == "":
          
            current_btn['text'] = self.turn
            
            
            if self.turn == 'X':
                current_btn['fg'] = 'blue'
            else:
                current_btn['fg'] = 'red'

            if self.check_winner():
                messagebox.showinfo("Kết thúc", f"Chúc mừng! Người chơi {self.turn} đã thắng!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Kết thúc", "Hòa rồi!")
                self.reset_board()
            else:
                self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        
        b = [[self.buttons[r][c]['text'] for c in range(3)] for r in range(3)]

        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] and b[i][0] != "": return True
            if b[0][i] == b[1][i] == b[2][i] and b[0][i] != "": return True
        
       
        if b[0][0] == b[1][1] == b[2][2] and b[0][0] != "": return True
        if b[0][2] == b[1][1] == b[2][0] and b[0][2] != "": return True
        
        return False

    def check_draw(self):
        for r in range(3):
            for c in range(3):
                if self.buttons[r][c]['text'] == "":
                    return False
        return True

    def reset_board(self):
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]['text'] = ""
        self.turn = 'X'

if __name__ == "__main__":
    root = tk.Tk() 
    game = CaroGUI(root)
    root.mainloop() 