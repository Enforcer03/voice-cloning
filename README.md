# Voice Cloning with Tortoise-TTS

![image](https://github.com/Enforcer03/voice-cloning/assets/103068685/45e6cace-1b51-4a07-a757-43fe4f98d8cc)



## Description

Tortoise-TTS is an advanced text-to-speech (TTS) library built on the latest deep learning and speech synthesis developments. It utilizes Deep Neural Networks and Vocoders to generate natural-sounding speech. The library allows you to clone the unique characteristics of a speaker's voice by training a model on their speech samples.

Tortoise-TTS offers the following key features:

- **Voice Cloning**: Clone a specific speaker's voice by training a model on their speech data.
- **High-Quality Synthesis**: Generate high-quality synthetic speech with natural intonation and expressiveness.
- **Customizable**: Fine-tune the voice cloning models to match the speaker's voice better.
- **Easy Integration**: Tortoise-TTS is compatible with most Python libraries.

## Directions

To get started with this repository:

1. **Prepare Speech Data**: Firstly, place the speech data files (.wav format) of the desired speaker in the `input` folder of the repository. It is important to note that the .wav files should belong to the same speaker and be in English for optimal performance. It is recommended to have at least two speech samples for better results.

2. **Run the Code**: Open the `tortoise_tts_main.ipynb` file in Colab and ensure the runtime is set to GPU. Execute the code, and it will allow you to upload the .wav files from the `input` folder.

3. **Configure Text and Output**: Within the notebook, you can specify the desired text that you want the cloned voice to speak. Modify the `text` variable to customize the speech output.

4. **Generate Cloned Voice**: After setting the text and output configuration, run the code to generate the cloned voice. Tortoise-TTS will process the speech data and synthesize the speech based on the specified text.

5. **Samples**: Sample inputs and their corresponding outputs are saved in the Input and Output folder, respectively


