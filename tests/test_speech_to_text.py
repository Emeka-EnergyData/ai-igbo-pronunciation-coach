from src.ai.speech_to_text import transcribe_audio

transcript = transcribe_audio("assets/23_Master.wav")

print(transcript)