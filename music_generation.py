import os
import pretty_midi

dataset_path = r"C:\Users\dell\OneDrive\Desktop\AI-Music-Generation\dataset"

notes = []

for file in os.listdir(dataset_path):
    if file.endswith(".mid"):
        try:
            midi = pretty_midi.PrettyMIDI(
                os.path.join(dataset_path, file)
            )

            for instrument in midi.instruments:
                for note in instrument.notes:
                    notes.append(note.pitch)

        except:
            pass

print("Total Notes:", len(notes))
print("First 20 Notes:", notes[:20])



    