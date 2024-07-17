import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ttkbootstrap as ttkb

# Tạo cửa sổ chính
root = ttkb.Window(themename="flatly")
root.title("Biểu Mẫu Nhập Dữ Liệu")
root.geometry("500x450")
root.configure(bg="#f0f0f0")

# Hàm xử lý khi nhấn nút "Gửi"
def submit_data():
    messagebox.showinfo("Thông Báo", "Dữ liệu đã được gửi thành công!")

# Tạo khung thông tin người dùng
user_info_frame = ttk.LabelFrame(root, text="Thông Tin Người Dùng", padding=(10, 10), bootstyle="success")
user_info_frame.pack(fill="both", expand="yes", padx=20, pady=10)

ttk.Label(user_info_frame, text="Tên").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ttk.Entry(user_info_frame, style="TEntry").grid(row=0, column=1, padx=10, pady=5)
ttk.Label(user_info_frame, text="Họ").grid(row=0, column=2, padx=10, pady=5, sticky="w")
ttk.Entry(user_info_frame, style="TEntry").grid(row=0, column=3, padx=10, pady=5)
ttk.Label(user_info_frame, text="Chức Danh").grid(row=0, column=4, padx=10, pady=5, sticky="w")
ttk.Combobox(user_info_frame, values=["Mr", "Ms", "Dr"], style="TCombobox").grid(row=0, column=5, padx=10, pady=5)

ttk.Label(user_info_frame, text="Tuổi").grid(row=1, column=0, padx=10, pady=5, sticky="w")
ttk.Spinbox(user_info_frame, from_=18, to=100, style="TSpinbox").grid(row=1, column=1, padx=10, pady=5)
ttk.Label(user_info_frame, text="Quốc Tịch").grid(row=1, column=2, padx=10, pady=5, sticky="w")
ttk.Entry(user_info_frame, style="TEntry").grid(row=1, column=3, padx=10, pady=5)

# Tạo khung trạng thái đăng ký
registration_frame = ttk.LabelFrame(root, text="Trạng Thái Đăng Ký", padding=(10, 10), bootstyle="success")
registration_frame.pack(fill="both", expand="yes", padx=20, pady=10)

ttk.Checkbutton(registration_frame, text="Hiện đang đăng ký", bootstyle="round-toggle-success").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ttk.Label(registration_frame, text="Số khóa học đã hoàn thành").grid(row=0, column=1, padx=10, pady=5, sticky="w")
ttk.Spinbox(registration_frame, from_=0, to=50, style="TSpinbox").grid(row=0, column=2, padx=10, pady=5)
ttk.Label(registration_frame, text="Số học kỳ").grid(row=0, column=3, padx=10, pady=5, sticky="w")
ttk.Spinbox(registration_frame, from_=0, to=10, style="TSpinbox").grid(row=0, column=4, padx=10, pady=5)

# Tạo khung điều khoản và điều kiện
terms_frame = ttk.LabelFrame(root, text="Điều Khoản và Điều Kiện", padding=(10, 10), bootstyle="success")
terms_frame.pack(fill="both", expand="yes", padx=20, pady=10)

ttk.Checkbutton(terms_frame, text="Tôi chấp nhận các điều khoản và điều kiện.", bootstyle="round-toggle-success").pack(padx=10, pady=5, anchor="w")

# Nút gửi dữ liệu
submit_button = ttk.Button(root, text="Gửi dữ liệu", command=submit_data, bootstyle="success")
submit_button.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
