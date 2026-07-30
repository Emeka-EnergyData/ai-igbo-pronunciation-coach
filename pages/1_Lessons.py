import streamlit as st
from src.learning_engine.lesson_service import load_lesson
from streamlit_mic_recorder import mic_recorder
from src.audio.recorder import save_audio
from src.ai.speech_to_text import transcribe_audio
from src.ai.feedback_service import generate_feedback

lesson = load_lesson(1)

exercises = lesson["exercises"]
# ----------------------------------# Page Configuration# ----------------------------------
st.set_page_config( page_title="Asụsụ AI", page_icon=" ", layout="wide")

st.title(lesson["lesson"]["title"])
# ----------------------------------# Lesson Introduction# ----------------------------------
st.info(lesson["lesson"]["concept"])

# ----------------------------------# Compound Consonants# ----------------------------------
st.header ("The 9 Compound Consonants (Nchịkọta Mgbadọ)")
st.write("""""")
compound_letters = lesson["compound_letters"]
st.divider()
st.header("Learn the Sounds")
for item in compound_letters:
    with st.container():
        col1, col2 = st.columns([1,4])
        with col1:
            st.subheader(item["title"])
        with col2:
            st.write(item["explanation"])
            st.write(f"**Example:** {item['example']}")
            st.audio(item["audio_path"])
        st.divider()

# ----------------------------------
# Exercises
# ----------------------------------

st.header("Exercises")

exercises = lesson["exercises"]

for i, exercise in enumerate(exercises):

    with st.expander(exercise["title"], expanded= True):

        st.write(f"### {exercise['prompt']}")

        st.info(f"💡 Hint: {exercise['hint']}")

        st.audio(exercise["audio_path"])

        # Mic Setup
        audio = mic_recorder(
            start_prompt="Start Recording",
            stop_prompt="Stop Recording",
            key=f"recorder_{i}")
        
        # Save Audio
        if audio:
            file_path = save_audio(audio, f"exercise_{i}.wav")
            st.success("Recording saved successfully!")
            
        # Audio Playback
        if audio:
            st.audio(file_path)

        #Submit Audio
        if st.button(
            "Submit Answer",
            key=f"submit_{i}"
        ):
            with st.spinner("Listening and analysing your pronunciation..."):
                text = transcribe_audio(file_path)
                
            feedback = generate_feedback(expected_answer=exercise["expected_answer"], transcription=text)
            
            st.success("Placeholder AI Feedback")

            st.write(f"**Transcription:** {feedback.transcription}")

            st.write(f"**Score:** {feedback.score}/10")

            st.write(f"**Correct:** {feedback.correct}")

            st.write(f"**Feedback:** {feedback.pronunciation_feedback}")

            st.write(f"**Mistake:** {feedback.mistake}")

            st.write(f"**Next Tip:** {feedback.next_tip}")

            st.write(f"**Encouragement:** {feedback.encouragement}")

            confidence = st.slider(
                "How confident are you?",
                1,
                5,
                3,
                key=f"confidence_{i}"
            )

            st.write(f"Your confidence: ⭐ {confidence}/5")

            verified = st.checkbox(
                "A teacher or native speaker confirmed my answer.",
                key=f"verified_{i}"
            )

            if verified:
                st.success("✔ Human verification recorded")

st.divider()

col1,col2 = st.columns(2)

with col1:
    st.button("⬅ Previous Lesson")

with col2:
    st.button("Next Lesson ➜")