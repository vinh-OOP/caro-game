import tkinter as tk
from tkinter import messagebox

class CaroGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Cờ Ca-rô (Vinh-OOP)")
        
        # 1. Khởi tạo dữ liệu
        self.turn = 'X' # Lượt đi hiện tại
        self.buttons = [] # Mảng lưu các nút bấm (Button widget)
        
        # Tạo lưới 3x3 button
        for r in range(3):
            row_buttons = []
            for c in range(3):
                # Tạo một nút bấm
                btn = tk.Button(
                    self.root, 
                    text="", 
                    font=("Arial", 20, "bold"),
                    width=6, height=3,
                    # Lưu ý: Dùng lambda để truyền tham số r, c vào hàm
                    command=lambda r=r, c=c: self.on_click(r, c)
                )
                # Đặt nút lên giao diện dạng lưới (grid)
                btn.grid(row=r, column=c)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def on_click(self, r, c):
        # Hàm này chạy khi người chơi bấm vào nút ở dòng r, cột c
        current_btn = self.buttons[r][c]

        # Nếu ô còn trống thì mới cho đánh
        if current_btn['text'] == "":
            # 1. Cập nhật giao diện (hiện X hoặc O)
            current_btn['text'] = self.turn
            
            # Thêm màu cho đẹp (X màu xanh, O màu đỏ)
            if self.turn == 'X':
                current_btn['fg'] = 'blue'
            else:
                current_btn['fg'] = 'red'

            # 2. Kiểm tra thắng thua ngay lập tức
            if self.check_winner():
                messagebox.showinfo("Kết thúc", f"Chúc mừng! Người chơi {self.turn} đã thắng!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Kết thúc", "Hòa rồi!")
                self.reset_board()
            else:
                # 3. Đổi lượt
                self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        # Lấy text từ các nút để kiểm tra (tương tự bản Console)
        b = [[self.buttons[r][c]['text'] for c in range(3)] for r in range(3)]

        # Kiểm tra hàng ngang, dọc
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] and b[i][0] != "": return True
            if b[0][i] == b[1][i] == b[2][i] and b[0][i] != "": return True
        
        # Kiểm tra chéo
        if b[0][0] == b[1][1] == b[2][2] and b[0][0] != "": return True
        if b[0][2] == b[1][1] == b[2][0] and b[0][2] != "": return True
        
        return False

    def check_draw(self):
        # Kiểm tra hòa: Nếu không còn nút nào trống
        for r in range(3):
            for c in range(3):
                if self.buttons[r][c]['text'] == "":
                    return False
        return True

    def reset_board(self):
        # Xóa hết bàn cờ để chơi ván mới
        for r in range(3):
            for c in range(3):
                self.buttons[r][c]['text'] = ""
        self.turn = 'X'

# Chạy chương trình
if __name__ == "__main__":
    root = tk.Tk() # Tạo cửa sổ chính
    game = CaroGUI(root)
    root.mainloop() # Vòng lặp giữ cửa sổ luôn hiển thị