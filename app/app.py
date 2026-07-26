import streamlit as st
# ----------------------------------# Page Configuration# ----------------------------------
st.set_page_config( page_title="Asụsụ AI", page_icon=" ", layout="wide")

st.title("Compound Consonants")
# ----------------------------------# Lesson Introduction# ----------------------------------
st.info("""### Concept
Compound consonants are **two letters written together** that produce **one single sound**.
You should NOT pronounce the letters separately.""")

# ----------------------------------# Compound Consonants# ----------------------------------
st.header ("""The 9 Compound Consonants (Nchikota Mgbado)""")
st.write("""""")
compound_letters = [ 
    {
        "letter": "CH", 
        "sound": "Sounds like 'ch' in church.", 
        "example": "Chukwu (God)"
    },
    {
        "letter": "GB", 
        "sound": "Implosive sound produced with both lips.", 
        "example": "Gbaa (Run)" 
    }, 
    {
        "letter": "GH",
        "sound": "Soft throat sound.",
        "example": "Aghụghọ (Cunning)" 
    }, 
    {   "letter": "GW",
        "sound": "Sounds like 'gw'.",
        "example": "Gwam (Tell me)"
    }, 
    {   "letter": "KP",
        "sound": "Lip popping sound.",
        "example": "Kpọọ (Call)" 
    }, 
    {   "letter": "KW",
        "sound": "Sounds like 'qu'.",
        "example": "Kweere (Agree)" 
    }, 
    {   "letter": "NW", 
        "sound": "Blend N and W together.", 
        "example": "Nwa (Child)"
    }, 
    {   "letter": "NY", 
        "sound": "Like 'ny' in canyon.", 
        "example": "Nye (Give)" 
    }, 
    { 
        "letter": "SH", 
        "sound": "Like 'sh' in ship.", 
        "example": "Shịọ (Refuse)" 
    }
    ]

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

exercises = [
    {
        "title": "Task 1 - Nwa",
        "prompt": "Say the Igbo word for 'Child'.",
        "guide": "Blend N and W into one smooth sound."
    },
    {
        "title": "Task 2 - Kpọọ",
        "prompt": "Say the Igbo word for 'Call'.",
        "guide": "Use a popping KP sound."
    },
    {
        "title": "Task 3 - Gbaa",
        "prompt": "Say the Igbo word for 'Run'.",
        "guide": "Press both lips together for GB."
    },
    {
        "title": "Task 4 - Nye",
        "prompt": "Say the Igbo word for 'Give'.",
        "guide": "Blend NY smoothly before the vowel."
    }
]

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