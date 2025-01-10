import pygame
import numpy as np
import time

# Define the note frequencies as integers
notes = {
    "C0": 16, "CS0": 17, "D0": 18, "DS0": 19, "E0": 21, "F0": 22, "FS0": 23,
    "G0": 25, "GS0": 26, "A0": 28, "AS0": 29, "B0": 31,
    
    "C1": 33, "CS1": 35, "D1": 37, "DS1": 39, "E1": 41, "F1": 44, "FS1": 46,
    "G1": 49, "GS1": 52, "A1": 55, "AS1": 58, "B1": 62,

    "C2": 65, "CS2": 69, "D2": 73, "DS2": 78, "E2": 82, "F2": 87, "FS2": 93,
    "G2": 98, "GS2": 104, "A2": 110, "AS2": 117, "B2": 123,

    "C3": 131, "CS3": 139, "D3": 147, "DS3": 156, "E3": 165, "F3": 175, "FS3": 185,
    "G3": 196, "GS3": 208, "A3": 220, "AS3": 233, "B3": 247,

    "C4": 262, "CS4": 277, "D4": 294, "DS4": 311, "E4": 330, "F4": 349, "FS4": 370,
    "G4": 392, "GS4": 415, "A4": 440, "AS4": 466, "B4": 494,

    "C5": 523, "CS5": 554, "D5": 587, "DS5": 622, "E5": 659, "F5": 698, "FS5": 740,
    "G5": 784, "GS5": 831, "A5": 880, "AS5": 932, "B5": 988,

    "C6": 1047, "CS6": 1109, "D6": 1175, "DS6": 1245, "E6": 1319, "F6": 1397, "FS6": 1480,
    "G6": 1568, "GS6": 1661, "A6": 1760, "AS6": 1865, "B6": 1976,

    "C7": 2093, "CS7": 2217, "D7": 2349, "DS7": 2489, "E7": 2637, "F7": 2794, "FS7": 2960,
    "G7": 3136, "GS7": 3322, "A7": 3520, "AS7": 3729, "B7": 3951,

    "C8": 4186, "CS8": 4435, "D8": 4699, "DS8": 4978, "E8": 5274, "F8": 5588, "FS8": 5920,
    "G8": 6272, "GS8": 6645, "A8": 7040, "AS8": 7459, "B8": 7902
}


# Initialize the mixer
pygame.mixer.init()

def generate_wave(frequency, duration=0.5, sample_rate=44100, amplitude=4096):
    """Generate a sine wave for a specific frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t) * amplitude
    wave = wave.astype(np.int16)  # Convert to 16-bit signed integers
    
    # Convert to stereo by duplicating the mono signal
    stereo_wave = np.stack((wave, wave), axis=-1)
    
    return stereo_wave

def play_note(frequency, duration=500):
    """Play a note with a specific frequency (integer) and duration in milliseconds."""
    duration_seconds = duration / 1000.0  # Convert duration from milliseconds to seconds
    wave = generate_wave(frequency, duration_seconds)
    sound = pygame.sndarray.make_sound(wave)
    sound.play(-1)  # Play the sound looped until the time is up
    time.sleep(duration_seconds)
    sound.stop()

def play_sequence(note_sequence):
    """Play a sequence of notes with their respective durations."""
    idx = 0
    while idx < len(note_sequence):
        note = note_sequence[idx]
        # If it's a note name, get the frequency
        frequency = get_frequency_from_note_name(note)
        if frequency:
            idx += 1
            duration = int(note_sequence[idx])  # The next item is the duration in ms
            print(f"Playing {note} ({frequency} Hz) for {duration} ms")
            play_note(frequency, duration)
            time.sleep(0.05)  # Small delay between notes
        else:
            print(f"Invalid note name: {note}")
        idx += 1

def get_frequency_from_note_name(note_name):
    """Retrieve the frequency from the note name."""
    for name, frequency in notes.items():
        if name == note_name:
            return frequency
    return None