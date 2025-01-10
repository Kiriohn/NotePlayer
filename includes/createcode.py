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