-- ==========================================================
--  DATABASE
-- PostgreSQL Schema
--
-- Dataset: Olist Brazilian E-commerce Public Dataset
-- Purpose: Data Analysis & Business Intelligence Portfolio
-- Database: PostgreSQL
-- ==========================================================


/*
Description
-----------
This schema contains the core relational tables required for
analyzing sales performance, customer behavior, seller
performance, product trends, payments, and customer reviews
from the Olist Brazilian E-commerce dataset.

*/

-- ==========================================================
-- 1. Topics
-- ==========================================================

CREATE TABLE topics (
    topic_id SERIAL PRIMARY KEY,
    topic_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- ==========================================================
-- 2. Subtopics
-- ==========================================================

CREATE TABLE subtopics (
    subtopic_id SERIAL PRIMARY KEY,

    topic_id INTEGER NOT NULL,

    subtopic_name VARCHAR(100) NOT NULL,

    description TEXT,

    CONSTRAINT fk_topic
        FOREIGN KEY (topic_id)
        REFERENCES topics(topic_id)
        ON DELETE CASCADE
);

-- ==========================================================
-- 3. Lessons
-- ==========================================================


CREATE TABLE lessons (
    lesson_id SERIAL PRIMARY KEY,

    subtopic_id INTEGER NOT NULL,

    lesson_number DECIMAL(3,1) NOT NULL,

    title VARCHAR(200) NOT NULL,

    concept TEXT NOT NULL,

    CONSTRAINT fk_subtopic
        FOREIGN KEY (subtopic_id)
        REFERENCES subtopics(subtopic_id)
        ON DELETE CASCADE
);

-- ==========================================================
-- 4. Lesson Items
-- ==========================================================

CREATE TABLE lesson_items (
    item_id SERIAL PRIMARY KEY,

    lesson_id INTEGER NOT NULL,

    item_order INTEGER NOT NULL,

    item_type VARCHAR(50) NOT NULL,

    title VARCHAR(100) NOT NULL,

    explanation TEXT,

    example TEXT,

    audio_path TEXT,

    CONSTRAINT fk_lesson
        FOREIGN KEY (lesson_id)
        REFERENCES lessons(lesson_id)
        ON DELETE CASCADE
);

-- ==========================================================
-- 5. Exercises
-- ==========================================================

CREATE TABLE exercises (
    exercise_id SERIAL PRIMARY KEY,

    lesson_id INTEGER NOT NULL,

    exercise_number INTEGER NOT NULL,

    title VARCHAR(100) NOT NULL,

    prompt TEXT NOT NULL,

    expected_answer TEXT,

    hint TEXT,

    audio_path TEXT,

    CONSTRAINT fk_lesson
        FOREIGN KEY (lesson_id)
        REFERENCES lessons(lesson_id)
        ON DELETE CASCADE
);

