import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import LEFT

# Create the main window
root = ttkb.Window(themename="flatly")
root.title("Frame Recorder")
root.geometry("600x300")
root.configure(bg="#e7f0fd")  # Background color set to light blue

# Create and place the title label
title_label = ttkb.Label(root, text="Frame Recorder", font=("Helvetica", 24, "bold"), bootstyle="info")
title_label.pack(pady=20)

# Create and place the FPS input label and entry
fps_frame = ttkb.Frame(root, bootstyle="light")
fps_frame.pack(pady=10)

fps_label = ttkb.Label(fps_frame, text="create an", font=("Helvetica", 12), bootstyle="light")
fps_label.pack(side=LEFT, padx=5)

fps_entry = ttkb.Entry(fps_frame, width=10, bootstyle="light")
fps_entry.pack(side=LEFT, padx=5)
fps_entry.insert(0, "100")  # Default FPS value

fps_suffix_label = ttkb.Label(fps_frame, text="fps video", font=("Helvetica", 12), bootstyle="light")
fps_suffix_label.pack(side=LEFT, padx=5)

# Create and place the buttons
button_frame = ttkb.Frame(root, bootstyle="light")
button_frame.pack(pady=20)

pause_button = ttkb.Button(button_frame, text="Pause", bootstyle="primary-outline")
pause_button.pack(side=LEFT, padx=10)

start_button = ttkb.Button(button_frame, text="Start", bootstyle="success-outline")
start_button.pack(side=LEFT, padx=10)

end_button = ttkb.Button(button_frame, text="End", bootstyle="danger-outline")
end_button.pack(side=LEFT, padx=10)

# Create and place the status label
status_label = ttkb.Label(root, text="Recording Paused", font=("Helvetica", 12), bootstyle="info")
status_label.pack(pady=20)

# Run the application
root.mainloop()
