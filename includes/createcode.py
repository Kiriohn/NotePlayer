# Generate the arduino code for the melody

def export_code(notes, durations):
    # Generate the melody array (C-style)
    melody_array = "int Melody[] = {"
    melody_array += ", ".join(f"NOTE_{note}" for note in notes)  # Adding NOTE_ to each note
    melody_array += "};\n"

    # Generate the note durations array (C-style)
    durations_array = "int NoteDurations[] = {" + ", ".join(map(str, durations)) + "};\n"

    # Calculate the melody length (C-style)
    melody_length = f"int MelodyLength = sizeof(Melody) / sizeof(Melody[0]);\n"

    # Combine everything into one string
    result = melody_array + durations_array + melody_length

    return result

def new_export(notes, durations):
    """
    Generates Arduino code for a melody using the provided notes and durations.

    Args:
        notes (list of str): List of notes.
        durations (list of int): List of durations corresponding to the notes.

    Returns:
        str: Arduino code as a string.
    """
    # Create the melody array
    melody_array = "int Melody[] = {"
    melody_array += ", ".join(f"NOTE_{note}" for note in notes)  # Adding NOTE_ to each note
    melody_array += "};\n"

    # Generate the note durations array (C-style)
    durations_array = "int NoteDurations[] = {" + ", ".join(map(str, durations)) + "};\n"

    # Calculate the melody length (C-style)
    melody_length = f"int MelodyLength = sizeof(Melody) / sizeof(Melody[0]);\n"

    # Rest of the Code
    rest_code = """#define SPK_pin 8  // Speaker pin

// Function to play a note
void playNote(int frequency, int duration) {{
  if (frequency == 0) {{
    delay(duration);  // Rest (no sound)
  }} else {{
    tone(SPK_pin, frequency, duration);  // Generate tone
    delay(duration);  // Wait for the note's duration
  }}
}}

// Function to play a melody
void playMusic(int notes[], int durations[], int length) {{
  for (int i = 0; i < length; i++) {{
    playNote(notes[i], durations[i]);  // Play each note
    delay(50);  // Short pause between notes
  }}
}}

void setup() {{
  pinMode(SPK_pin, OUTPUT);  // Set speaker pin as output
  playMusic(melody, durations, melodyLength);  // Play the melody
}}

void loop() {{
  // Nothing here
}}
"""

    # Combine everything into one string
    arduino_code = melody_array + durations_array + melody_length + rest_code

    return arduino_code