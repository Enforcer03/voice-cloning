import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F

import IPython

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

# This will download all the models used by Tortoise from the HuggingFace hub.
tts = TextToSpeech()


text = input("Enter the text You intend to clone: ")
print("You entered: ", text)

CUSTOM_VOICE_NAME = input("Enter the name of your clone: ")
print("You entered: ", CUSTOM_VOICE_NAME)
# preset is the speed of the clone voice
preset = "fast"
import os
from tkinter import Tk, filedialog

def upload_files():
    custom_voice_folder = f"tortoise-tts/tortoise/voices/{CUSTOM_VOICE_NAME}"
    os.makedirs(custom_voice_folder, exist_ok=True)
    root = Tk()
    root.withdraw()
    files = filedialog.askopenfiles()
    for i, file in enumerate(files):
        file_data = file.read()
        with open(os.path.join(custom_voice_folder, f'{i}.wav'), 'wb') as f:
            f.write(file_data)
        file.close()

# Call the function to upload files
upload_files()

# Generating speech with the custom voice.
voice_samples, conditioning_latents = load_voice(CUSTOM_VOICE_NAME)
gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents,
                          preset=preset)
torchaudio.save(f'generated-{CUSTOM_VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)
