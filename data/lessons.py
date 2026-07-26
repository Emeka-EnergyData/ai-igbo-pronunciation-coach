"""Temporary lesson data for the MVP.
Later this data will be stored in PostgreSQL."""

LESSON_1 = {
    "lesson_id": 1,
    "topic": "Foundation",
    "subtopic": "Alphabet",
    "title": "Compound Consonants",
    "subtitle": "Lesson 1.1",
    "concept": """Compound consonants are two letters written togetherthat produce one single sound. You should NOT pronounce them separately.""",
    "section_title": "The 9 Compound Consonants (Nchịkọta Mgbadọ)",
    "compound_letters": [
        {
            "letter": "CH",
            "sound": "Sounds like 'ch' in church.",
            "example": "Chukwu (God)",
            "audio": None
        },
        {
            "letter": "GB",
            "sound": "Implosive sound produced with both lips.",
            "example": "Gbaa (Run)",
            "audio": None 
        },
        {
            "letter": "GH",
            "sound": "Soft throat sound.",
            "example": "Aghụghọ (Cunning)",
            "audio": None
        }, 
        {
            "letter": "GW",
            "sound": "Sounds like 'gw'.",
            "example": "Gwam (Tell me)",
            "audio": None
        },
        {
            "letter": "KP",
            "sound": "Lip popping sound.",
            "example": "Kpọọ (Call)",
            "audio": None
        },
        {
            "letter": "KW",
            "sound": "Sounds like 'qu'.",
            "example": "Kweere (Agree)",
            "audio": None
        },
        {
            "letter": "NW",
            "sound": "Blend N and W together.",
            "example": "Nwa (Child)",
            "audio": None
        },
        {
            "letter": "NY",
            "sound": "Like 'ny' in canyon.",
            "example": "Nye (Give)",
            "audio": None
        },
        {
            "letter": "SH", 
            "sound": "Like 'sh' in ship.",
            "example": "Shịọ (Refuse)",
            "audio": None }
        ],
    "exercises": [
        {
            "exercise_id": 1,
            "title": "Task 1 - Nwa",
            "prompt": "Say the Igbo word for 'Child'.",
            "expected_answer": "Nwa",
            "hint": "Blend N and W into one smooth sound.",
            "target_audio": None
        }, 
        {
            "exercise_id": 2,
            "title": "Task 2 - Kpọọ",
            "prompt": "Say the Igbo word for 'Call'.",
            "expected_answer": "Kpọọ",
            "hint": "Use a popping KP sound.",
            "target_audio": None
        },
        {
            "exercise_id": 3,
            "title": "Task 3 - Gbaa",
            "prompt": "Say the Igbo word for 'Run'.",
            "expected_answer": "Gbaa",
            "hint": "Press both lips together for GB.",
            "target_audio": None
        },
        {
            "exercise_id": 4,
            "title": "Task 4 - Nye",
            "prompt": "Say the Igbo word for 'Give'.",
            "expected_answer": "Nye",
            "hint": "Blend NY smoothly before the vowel.",
            "target_audio": None
        }
        ]
    }