import numpy as np
from tensorflow.keras.models import load_model
import pretty_midi

model = load_model(
    r"C:\Users\dell\OneDrive\Desktop\AI-Music-Generation\train_model.py\music_model.h5",
    compile=False
)

# Seed sequence
seed = [56,60,63,63,60]

generated_notes = []

for _ in range(50):
    x = np.array(seed).reshape(1, 5, 1)
    prediction = model.predict(x, verbose=0)

    next_note = int(prediction[0][0])

    generated_notes.append(next_note)

    seed.append(next_note)
    seed = seed[1:]

# Create MIDI
midi = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=0)

start = 0

for note_num in generated_notes:
    note = pretty_midi.Note(
        velocity=100,
        pitch=max(0, min(127, note_num)),
        start=start,
        end=start + 0.5
    )
    instrument.notes.append(note)
    start += 0.5

midi.instruments.append(instrument)
midi.write("ai_generated_music.mid")

print("AI music generated successfully!")