import tkinter as tk

# Create a window
window = tk.Tk()
window.title("My First GUI")
window.geometry("400x300")

# Add a label
label = tk.Label(window, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
def on_click():
    label.config(text="Button Clicked!")

button = tk.Button(window, text="Click Me!", command=on_click)
button.pack(pady=20)

# Run the application
window.mainloop()
