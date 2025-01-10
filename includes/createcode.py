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
    # Note definitions
    note_definitions = '''
#define NOTE_0 0
    
#define NOTE_C0  16
#define NOTE_CS0 17
#define NOTE_D0  18
#define NOTE_DS0 19
#define NOTE_E0  21
#define NOTE_F0  22
#define NOTE_FS0 23
#define NOTE_G0  25
#define NOTE_GS0 26
#define NOTE_A0  28
#define NOTE_AS0 29
#define NOTE_B0  31

#define NOTE_C1  33
#define NOTE_CS1 35
#define NOTE_D1  37
#define NOTE_DS1 39
#define NOTE_E1  41
#define NOTE_F1  44
#define NOTE_FS1 46
#define NOTE_G1  49
#define NOTE_GS1 52
#define NOTE_A1  55
#define NOTE_AS1 58
#define NOTE_B1  62

#define NOTE_C2  65
#define NOTE_CS2 69
#define NOTE_D2  73
#define NOTE_DS2 78
#define NOTE_E2  82
#define NOTE_F2  87
#define NOTE_FS2 93
#define NOTE_G2  98
#define NOTE_GS2 104
#define NOTE_A2  110
#define NOTE_AS2 117
#define NOTE_B2  123

#define NOTE_C3  131
#define NOTE_CS3 139
#define NOTE_D3  147
#define NOTE_DS3 156
#define NOTE_E3  165
#define NOTE_F3  175
#define NOTE_FS3 185
#define NOTE_G3  196
#define NOTE_GS3 208
#define NOTE_A3  220
#define NOTE_AS3 233
#define NOTE_B3  247

#define NOTE_C4  262
#define NOTE_CS4 277
#define NOTE_D4  294
#define NOTE_DS4 311
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_FS4 370
#define NOTE_G4  392
#define NOTE_GS4 415
#define NOTE_A4  440
#define NOTE_AS4 466
#define NOTE_B4  494

#define NOTE_C5  523
#define NOTE_CS5 554
#define NOTE_D5  587
#define NOTE_DS5 622
#define NOTE_E5  659
#define NOTE_F5  698
#define NOTE_FS5 740
#define NOTE_G5  784
#define NOTE_GS5 831
#define NOTE_A5  880
#define NOTE_AS5 932
#define NOTE_B5  988

#define NOTE_C6  1047
#define NOTE_CS6 1109
#define NOTE_D6  1175
#define NOTE_DS6 1245
#define NOTE_E6  1319
#define NOTE_F6  1397
#define NOTE_FS6 1480
#define NOTE_G6  1568
#define NOTE_GS6 1661
#define NOTE_A6  1760
#define NOTE_AS6 1865
#define NOTE_B6  1976

#define NOTE_C7  2093
#define NOTE_CS7 2217
#define NOTE_D7  2349
#define NOTE_DS7 2489
#define NOTE_E7  2637
#define NOTE_F7  2794
#define NOTE_FS7 2960
#define NOTE_G7  3136
#define NOTE_GS7 3322
#define NOTE_A7  3520
#define NOTE_AS7 3729
#define NOTE_B7  3951

#define NOTE_C8  4186
#define NOTE_CS8 4435
#define NOTE_D8  4699
#define NOTE_DS8 4978
#define NOTE_E8  5274
#define NOTE_F8  5588
#define NOTE_FS8 5920
#define NOTE_G8  6272
#define NOTE_GS8 6645
#define NOTE_A8  7040
#define NOTE_AS8 7459
#define NOTE_B8  7902
'''

    # Create the melody array
    melody_array = "int Melody[] = {"
    melody_array += ", ".join(f"NOTE_{note}" for note in notes)  # Adding NOTE_ to each note
    melody_array += "};\n"

    # Generate the note durations array (C-style)
    durations_array = "int NoteDurations[] = {" + ", ".join(map(str, durations)) + "};\n"

    # Calculate the melody length (C-style)
    melody_length = f"int MelodyLength = sizeof(Melody) / sizeof(Melody[0]);\n"

    # Rest of the Code
    rest_code = """#define SPK_pin 3  // Speaker pin

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
  playMusic(Melody, NoteDurations, MelodyLength);  // Play the melody
}}

void loop() {{
  // Nothing here
}}
"""

    # Combine everything into one string
    arduino_code = note_definitions + melody_array + durations_array + melody_length + rest_code

    return arduino_code