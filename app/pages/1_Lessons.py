from learning_engine.lesson_service import load_lesson
import streamlit as st


lesson = load_lesson(1)
# ----------------------------------# Page Configuration# ----------------------------------
st.set_page_config( page_title="Asụsụ AI", page_icon=" ", layout="wide")

st.title(lesson["title"])
# ----------------------------------# Lesson Introduction# ----------------------------------
st.info(lesson["concept"])

# ----------------------------------# Compound Consonants# ----------------------------------
st.header (lesson["section_title"])
st.write("""""")
compound_letters = lesson["compound_letters"]
st.divider()
st.header("Learn the Sounds")
for item in compound_letters:
    with st.container():
        col1, col2 = st.columns([1,4])
        with col1:
            st.subheader(item["letter"])
        with col2:
            st.write(item["sound"])
            st.write(f"**Example:** {item['example']}")
            st.button(
                " Play Audio",
                key=item["letter"]
                )
        st.divider()

# ----------------------------------
# Exercises
# ----------------------------------

st.header("Exercises")

exercises = lesson["exercises"]

for i, exercise in enumerate(exercises):

    with st.expander(exercise["title"], expanded=(i == 0)):

        st.write(f"### {exercise['prompt']}")

        st.info(f"💡 Hint: {exercise['guide']}")

        st.button(
            "🔊 Play Target Audio",
            key=f"audio_{i}"
        )

        st.write("🎤 Record your answer")

        st.button(
            "Start Recording",
            key=f"start_{i}"
        )

        st.button(
            "Stop Recording",
            key=f"stop_{i}"
        )

        if st.button(
            "Submit Answer",
            key=f"submit_{i}"
        ):

            st.success("Placeholder AI Feedback")

            st.metric(
                "AI Score",
                "4 / 5 ⭐"
            )

            st.write("""
Great pronunciation!

✅ Your compound consonant was clear.

Keep practising the vowel sound.
""")

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