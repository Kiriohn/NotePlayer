import tkinter as tk
from tkinter import filedialog, messagebox
from includes import config as cfg
from includes import note
from includes import createcode

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

# Function to load a .np file into the text box
def load_file():
    file_path = filedialog.askopenfilename(title="Open .np File", filetypes=(("NP files", "*.np"), ("All files", "*.*")))
    
    if file_path:  # Ensure the user selected a file
        try:
            # Open and read the .np file
            with open(file_path, 'r') as file:
                content = file.read()
                text_box.delete(1.0, tk.END)  # Clear existing content in text box
                text_box.insert(tk.END, content)  # Insert content from the file into the text box
        except Exception as e:
            print(f"Error reading file: {e}")

# Function to play the notes
def play_notes():
    """Get the note sequence and durations from the input and play them."""
    input_sequence = text_box.get("1.0", tk.END)
    # Split the input by spaces
    note_sequence = input_sequence.split()

    # Play the sequence of notes
    note.play_sequence(note_sequence)

# Function to extract notes and durations from the input data
def extract_notes_and_durations(input_data):
    # Split the input string into a list of elements
    elements = input_data.split()
    
    # Initialize two empty lists for notes and durations
    notes = []
    durations = []
    
    # Iterate over the elements, taking two at a time (note, duration)
    for i in range(0, len(elements), 2):
        note = elements[i]
        duration = int(elements[i + 1])  # Convert the duration to integer
        notes.append(note)
        durations.append(duration)
    
    return notes, durations

# Export
def export():
    # Get content from the text box
    code_content = text_box.get("1.0", tk.END).strip()

    # Check if the code snippet is empty
    if not code_content:
        messagebox.showwarning("Nothing to export", "Please enter some notes to export.")
        return  # Exit the function if the code snippet is empty

    # enable code snippet text box
    code_text.config(state=tk.NORMAL)
    
    notes, durations = extract_notes_and_durations(text_box.get("1.0", tk.END))

    code_text.insert(tk.END, createcode.new_export(notes, durations))

    # disable code snippet text box
    code_text.config(state=tk.DISABLED)

# Function to copy the code snippet to the clipboard
def copy_code():
    root.clipboard_clear()
    root.clipboard_append(code_text.get("1.0", tk.END))
    # display status message for a few seconds
    status["text"] = "Code snippet copied to clipboard"
    root.after(2000, lambda: status.config(text="NotePlayer v1.0"))


def open_about_page():
    """Creates and displays the About Page."""
    about_window = tk.Toplevel()
    about_window.title("About")
    about_window.geometry("400x300")
    about_window.resizable(False, False)
    about_window.iconbitmap(cfg.ICON_PATH)

    # Add a label for the About Page content
    about_content = (
        "About NotePlayer\n\n"
        "This application is designed using Python and Tkinter.\n"
        "It is a simple tool used to preview the tone frequency\n" 
        "used in programming Arduino or any microcontroller projects.\n\n\n"
        "NotePlayer © 2025 by Ed John Roxas is licensed under CC BY-NC-SA 4.0 \n"
    )
    about_label = tk.Label(about_window, text=about_content, justify="left", padx=10, pady=10)
    about_label.pack(fill="both", expand=True)

    # Add a close button
    close_button = tk.Button(about_window, text="Close", command=about_window.destroy)
    close_button.pack(pady=10)

def open_help_page():
    """Creates and displays the Help Page."""
    help_window = tk.Toplevel()
    help_window.title("Help")
    help_window.geometry("400x300")
    help_window.resizable(False, False)
    help_window.iconbitmap(cfg.ICON_PATH)

    # Add a label for the Help Page content
    help_content = (
        "How to Use:\n\n"
        "1. Input Notes\n"
        "   - Enter notes and durations in the format:\n"
        "     C4 150 E4 75 G4 150\n\n"
        "2. Preview Notes\n"
        "   - Press Play to preview the melody directly in the application.\n\n"
        "3. Generate Code\n"
        "   - Click Generate Code to create Arduino-compatible code.\n\n"
        "4. Save/Load Files\n"
        "   - Use the File menu to save your melody or load a saved one.\n\n"
        "5. Copy Code\n"
        "   - Click Copy to copy the generated code to the clipboard.\n\n"
    )
    help_label = tk.Label(help_window, text=help_content, justify="left", padx=10, pady=10)
    help_label.pack(fill="both", expand=True)

    # Add a close button
    close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
    close_button.pack(pady=10)


# Set up the GUI
root = tk.Tk()
root.title("NotePlayer  V1.0")
root.geometry("600x800")
root.resizable(False, False)
root.iconbitmap(cfg.ICON_PATH)

# Create menu bar
menu = tk.Menu(root)

# Create the file menu
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Save", command=save_text)
file_menu.add_command(label="Load", command=load_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

menu.add_command(label="About", command=open_about_page)

menu.add_command(label="Help", command=open_help_page)

# Set menu bar to the root window
root.config(menu=menu)

# Add some margin by using padding
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Add a text box with rich capabilities
text_box = tk.Text(frame, wrap=tk.WORD, font=("Arial", 12), relief=tk.SUNKEN, bd=2, height=10)
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

export_button = tk.Button(button_frame, text="Export", command=export)
export_button.pack(side=tk.LEFT, padx=5)

# Add a code snippet frame below the buttons
code_frame = tk.Frame(frame)
code_frame.pack(fill=tk.X, pady=(10, 0))  # Add some space above the code snippet

# Add a code snippet label
code_label = tk.Label(code_frame, text="Code Snippet:")
code_label.pack(side=tk.TOP)

# Add a code snippet text box
code_text = tk.Text(code_frame, wrap=tk.WORD, font=("Arial", 10), relief=tk.SUNKEN, bd=2, height=10)
code_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
code_text.config(state=tk.DISABLED)  # Disable editing of the code snippet

# Add a button frame below the code snippet
button_frame2 = tk.Frame(code_frame)
button_frame2.pack(fill=tk.X, pady=(0, 10))  # Add some space below the buttons

# Add a copy button for the code snippet
copy_button = tk.Button(button_frame2, text="Copy", command=copy_code)
copy_button.pack(side=tk.LEFT, padx=5)

# Add a status bar at the bottom
status = tk.Label(root, text="NotePlayer v1.0", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

# Run the GUI
root.mainloop()