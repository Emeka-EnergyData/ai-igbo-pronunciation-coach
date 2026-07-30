from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

class PronunciationFeedback(BaseModel):
    transcription: str = Field(description="The exact Igbo text transcribed from the learner's speech.")
    score: int = Field(description="An overall pronunciation score from 0 to 10.")
    correct: bool = Field(description="Whether the learner's pronunciation is considered correct.")
    pronunciation_feedback: str = Field(description="A concise overall assessment of the learner's pronunciation.")
    mistake: str = Field(description="Describe the main pronunciation mistake the learner made. If there is no mistake, explain what they did well.")
    next_tip: str = Field(description="Provide one practical tip the learner can apply on the next attempt.")
    encouragement: str = Field(description="A short, positive, encouraging message to motivate the learner.")
    sound_focus: str = Field(description="The specific Igbo sound, letter, or compound letter the learner should focus on improving, such as 'gb', 'kp', 'sh', or 'ch'.")
    confidence: float = Field(description="The AI's confidence in its assessment, from 0.0 to 1.0.")
    explanation: str = Field(description="A brief teaching explanation describing why the pronunciation was correct or incorrect and how the target sound is produced.")
    
def generate_feedback(expected_answer: str, transcription: str) -> PronunciationFeedback:
    
    system_instruction = """
    You are an expert, warm, and encouraging Igbo language tutor
    Your job is to evaluate a learner's spoken attempt (transcription) against the expected target word/phrase.
    Guidelines:
    1. Compare the 'transcription' against the 'expected_answer'.
    2. Account for slight phonetic speech-to-text variations or accent quirks, but catch missing dots/tones if obvious.
    3. 'score' must be an integer from 0 to 10.
    4. 'correct' should be True if score >= 7, otherwise False.
    5. 'mistake': Explain specifically what went wrong phonetically or grammatically (or 'None' if correct).
    6. 'next_tip': Provide 1 actionable tip on how to shape the mouth, tongue, or pitch for this sound.
    7. 'encouragement': Give a short, upbeat phrase in English or Igbo (e.g., 'Daalụ!', 'Keep it up!')."""

    prompt = f"""
        Expected Igbo Answer: ```{expected_answer}``` 
        Learner Transcription: ```{transcription}```
        Evaluate the my attempt and return structured feedback."""
    
    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents = prompt,
        config = types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        response_mime_type="application/json",
                        response_schema=PronunciationFeedback,
                        temperature=0.2
                    )
    )

    if response.parsed:
        return response.parsed
    else: 
        return PronunciationFeedback(
                transcription=transcription,
                score=5,
                correct=False,
                pronunciation_feedback="Could not parse detailed feedback.",
                mistake="Evaluation formatting error.",
                next_tip="Try recording again clearly.",
                encouragement="Ndo! Let's try one more time.",
                sound_focus= "",
                confidence = 0,
                explanation= "")
    