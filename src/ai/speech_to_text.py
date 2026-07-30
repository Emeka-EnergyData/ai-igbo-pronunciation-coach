import os

os.environ["HF_HUB_OFFLINE"] = "1"
import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_asr():
    return pipeline(
    "automatic-speech-recognition",
    model = "NCAIR1/Igbo-ASR"
)

response = load_asr()

def transcribe_audio(audio_path: str):
    transcribed_text = response(audio_path)
    return transcribed_text["text"]