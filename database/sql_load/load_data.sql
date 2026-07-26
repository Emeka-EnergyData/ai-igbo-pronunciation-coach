-- ==========================================================
-- 1. Topics
-- ==========================================================

INSERT INTO topics (
    topic_name, 
    description
)
VALUES ( 
    'Foundation', 
    'Core concepts required to begin speaking Igbo.'
);

-- ==========================================================
-- 2. Subtopics
-- ==========================================================

INSERT INTO subtopics (
    topic_id, 
    subtopic_name, 
    description
)
VALUES (
    1,
    'Alphabet',
    'Introduction to the Igbo alphabet and pronunciation.'
);

-- ==========================================================
-- 3. Lessons
-- ==========================================================

INSERT INTO lessons (
    subtopic_id,
    lesson_number, 
    title,
    concept
)
VALUES (
    1, 
    1.1, 
    'Compound Consonants',
    'Compound consonants are two letters written together that produce one single sound. They should not be pronounced separately.'
);

-- ==========================================================
-- 4. Lesson Items
-- ==========================================================

INSERT INTO lesson_items(lesson_id,item_order,item_type,title,explanation,example,audio_path)
VALUES
(1,1,'compound_consonant','CH','Sounds like "ch" in church.','Chukwu','assets/audio/ch.mp3'),
(1,2,'compound_consonant','GB','Implosive sound produced with both lips.','Gbaa','assets/audio/gb.mp3'),
(1,3,'compound_consonant','GH','Soft throat sound.','Aghụghọ','assets/audio/gh.mp3'),
(1,4,'compound_consonant','GW','Sounds like "gw".','Gwam','assets/audio/gw.mp3'),
(1,5,'compound_consonant','KP','Lip popping sound.','Kpọọ','assets/audio/kp.mp3'),
(1,6,'compound_consonant','KW','Sounds like "qu".','Kweere','assets/audio/kw.mp3'),
(1,7,'compound_consonant','NW','Blend N and W together.','Nwa','assets/audio/nw.mp3'),
(1,8,'compound_consonant','NY','Like "ny" in canyon.','Nye','assets/audio/ny.mp3'),
(1,9,'compound_consonant','SH','Like "sh" in ship.','Shịọ','assets/audio/sh.mp3');

-- ==========================================================
-- 5. Exercises
-- ==========================================================

INSERT INTO exercises(lesson_id, exercise_number, title, prompt, expected_answer, hint, audio_path)
VALUES
(1, 1,'Task 1 - Nwa','Say the Igbo word for Child.','Nwa','Blend N and W into one smooth sound.','assets/audio/nw.mp3'),
(1,2,'Task 2 - Kpọọ','Say the Igbo word for Call.','Kpọọ','Use a popping KP sound.','assets/audio/kp.mp3'),
(1,3,'Task 3 - Gbaa','Say the Igbo word for Run.','Gbaa','Press both lips together for GB.','assets/audio/gb.mp3'),
(1,4,'Task 4 - Nye','Say the Igbo word for Give.','Nye','Blend NY smoothly before the vowel.','assets/audio/ny.mp3');