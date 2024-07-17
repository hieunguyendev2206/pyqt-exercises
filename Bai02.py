import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import messagebox

# Function to show a message when buttons are clicked
def button_clicked(button_name):
    messagebox.showinfo("Button Clicked", f"{button_name} đã được nhấn.")

# Tạo cửa sổ chính
root = ttkb.Window(themename="cosmo")
root.title("AtarBals Modern Antivirus")
root.geometry("800x500")
root.configure(bg="white")

# Tạo thanh bên
sidebar = ttkb.Frame(root, bootstyle="primary", width=200)
sidebar.pack(side=LEFT, fill=Y)

# Thêm các nhãn vào thanh bên
sections = ["Trạng thái", "Cập nhật", "Cài đặt", "Chia sẻ phản hồi", "Mua Premium", "Trợ giúp"]
for section in sections:
    label = ttkb.Label(sidebar, text=section, bootstyle="inverse-primary", anchor="w", padding=10, font=("Helvetica", 12, "bold"))
    label.pack(fill=X, pady=5)

# Thêm nút "Quét ngay" vào thanh bên
scan_now_button = ttkb.Button(sidebar, text="Quét ngay", bootstyle="success-outline", command=lambda: button_clicked("Quét ngay"))
scan_now_button.pack(pady=20, padx=10)

# Tạo khu vực nội dung chính
main_content = ttkb.Frame(root, bootstyle="light")
main_content.pack(side=RIGHT, expand=True, fill=BOTH)

# Thêm nhãn tiêu đề
title_label = ttkb.Label(main_content, text="Quét", font=("Helvetica", 24, "bold"), bootstyle="light", foreground="black")
title_label.pack(pady=20)

# Thêm nhãn phụ đề
subtitle_label = ttkb.Label(main_content, text="Premium sẽ luôn miễn phí. Bạn chỉ cần nhấn nút.", font=("Helvetica", 12), bootstyle="light", foreground="black")
subtitle_label.pack(pady=10)

# Tạo khung cho các nút
button_frame = ttkb.Frame(main_content, bootstyle="light")
button_frame.pack(pady=20)

# Thêm các nút vào khu vực nội dung chính
buttons = [("Quét nhanh", "primary"), ("Bảo vệ web", "primary"), ("Cách ly", "primary"), ("Quét toàn bộ", "primary"), ("Cập nhật đơn giản", "primary")]
for button_text, style in buttons:
    button = ttkb.Button(button_frame, text=button_text, bootstyle=f"{style}-outline", width=15, command=lambda bt=button_text: button_clicked(bt))
    button.pack(side=LEFT, padx=10, pady=10)

# Thêm nhãn trạng thái
status_label = ttkb.Label(main_content, text="Nhận Premium để bật: {Bảo vệ web}, {Quét toàn bộ}, {Cập nhật đơn giản}", font=("Helvetica", 12), bootstyle="light", foreground="purple")
status_label.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
