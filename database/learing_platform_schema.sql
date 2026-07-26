-- ==========================================================
-- 6. Exercise Attempts
-- ==========================================================

CREATE TABLE exercise_attempts (
    attempt_id SERIAL PRIMARY KEY,

    exercise_id INTEGER NOT NULL,

    user_answer TEXT,

    ai_score NUMERIC(4,2),

    self_rating INTEGER,

    human_verified BOOLEAN DEFAULT FALSE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_exercise
        FOREIGN KEY (exercise_id)
        REFERENCES exercises(exercise_id)
        ON DELETE CASCADE
);