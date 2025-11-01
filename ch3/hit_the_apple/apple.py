import tkinter as tk
from PIL import Image, ImageTk

# Create the main application window
root = tk.Tk()
root.title("Image at Top-Left")

# Load the image
image_path = 'apple.png'  # Replace with your image path
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Create a label to hold the image
label = tk.Label(root, image=photo)
label.image = photo  # Keep a reference to avoid garbage collection
label.pack(side='left', anchor='n')  # Pack the label to the left and top

# Start the GUI event loop
root.mainloop()