import tkinter as tk
from tkinter import filedialog, messagebox
from includes import config as cfg
from includes import note

# Function to clear the text box
def clear_text():
    text_box.delete("1.0", tk.END)

# Function to save text to a file
def save_text():
    # Get the content from the Text widget
    text_content = text_box.get("1.0", tk.END).strip()  # Strip any leading/trailing whitespace
    
    # Check if the text box is empty
    if not text_content:
        messagebox.showwarning("Nothing to save", "The text box is empty! Please enter some text to save.")
        return  # Exit the function if the text box is empty
    
    # Open a file dialog to choose where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".np", filetypes=[("NP Files", "*.np"), ("All Files", "*.*")])
    
    if file_path:
        # Save the content to the selected file
        with open(file_path, "w") as file:
            file.write(text_content)
        print(f"File saved to {file_path}")

# Function to play the notes
def play_notes():
    """Get the note sequence and durations from the input and play them."""
    input_sequence = text_box.get("1.0", tk.END)
    # Split the input by spaces
    note_sequence = input_sequence.split()
    
    # Play the sequence of notes
    note.play_sequence(note_sequence)

# Function to export the program for arduino
def export_prog():
    pass

# Set up the GUI
root = tk.Tk()
root.title("NotePlayer  V1.0")
root.geometry("400x600")
root.resizable(False, False)
root.iconbitmap(cfg.ICON_PATH)

# Create menu bar
menu = tk.Menu(root)

# Create the file menu
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New", command=lambda: note.new_file())
file_menu.add_command(label="Save", command=lambda: note.save_file())
file_menu.add_command(label="Load", command=lambda: note.load_file())
file_menu.add_separator()
file_menu.add_command(label="Settings", command=lambda: note.settings())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

# Create About menu
about_menu = tk.Menu(menu, tearoff=0)
about_menu.add_command(label="About", command=lambda: note.about())
menu.add_cascade(label="About", menu=about_menu)

# Create Help menu
help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label="Help", command=lambda: note.help())
menu.add_cascade(label="Help", menu=help_menu)

# Set menu bar to the root window
root.config(menu=menu)

# Add some margin by using padding
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Add a text box with rich capabilities
text_box = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12), relief=tk.SUNKEN, bd=2)
text_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add a button frame below the text box
button_frame = tk.Frame(frame)
button_frame.pack(fill=tk.X, pady=(10, 0))  # Add some space above buttons

# Add buttons in the button frame
play_button = tk.Button(button_frame, text="Play", command=play_notes)
play_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save", command=save_text)
save_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)

export_button = tk.Button(button_frame, text="Export", command=export_prog)
export_button.pack(side=tk.LEFT, padx=5)

# Run the GUI
root.mainloop()