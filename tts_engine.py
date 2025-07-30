from transformers import VitsModel, AutoTokenizer
import torch
import soundfile as sf

model = VitsModel.from_pretrained("facebook/mms-tts-vie")
tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-vie")

def text_to_speech(text, output_path="output.wav"):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        output = model(**inputs)
        waveform = output.waveform[0]  # Truy cập waveform từ output
        sf.write(output_path, waveform.cpu().numpy(), samplerate=model.config.sampling_rate)
    return output_path
