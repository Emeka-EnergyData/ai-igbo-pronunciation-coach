# Project Planning Architecture

## SCOPE

### Project Goal

Build a voice-first, AI-powered web application that teaches beginners conversational Igbo through challenge-based learning inspired by Exercism.

The MVP is not about teaching everything in Igbo. It is about proving that the learning model works.

### Target Users

- Beginners who want to learn Igbo.
- Nigerians in the diaspora.
- Nigerians who understand Igbo but lack confidence speaking it.
- Non-Igbo speakers interested in learning.

## Core Features (Must Have)

### 1. Lesson Mode

Learners can browse a roadmap of lessons.
Each lesson contains:

- Explanation
- Examples
- Audio
- 3-4 concept exercises
- Boss Challenge

### 2. Challenge Mode

The same exercises appear in a guided learning path.
Features:

- Progressive unlocking
- One new concept at a time
- Continuous review of previous concepts

### 3. Voice Learning

Learners can:

- Listen to native pronunciation
- Record themselves
- Receive feedback

### 4. AI Tutor

Learners can:

- Ask lesson questions
- Receive grammar explanations
- Get hints
- Understand mistakes

### 5. User Progress

Track:

- Completed exercises
- Current challenge
- XP
- Lesson completion

### 6. Database

Store:

- Lessons
- Exercises
- Audio
- Users
- Progress
- Learning Path

### Not Included in Version 1

These are intentionally postponed:

- Yoruba lessons
- Hausa lessons
- Conversation mode
- Pronunciation scoring
- Multiplayer
- Community contributions
- Mobile app & Offline mode
- Adaptive learning
- Teacher dashboard

## Post-MVP (Out of Scope for V1)

- Gamification heavy features (Streaks, Achievements, Leaderboards)
- Yoruba / Hausa tracks
- Live free-form AI conversation Mode
- Mobile Native Apps (IOS/Andriod) & Offline Mode
- Teacher Dashboard / Community Audio Uploads

## System Structure

``` text
                         USER
                           │
                           ▼
                  Streamlit Frontend
                           │
                           ▼
                   Learning Engine
                           │
           ┌────────────────────────────────┐
           ▼                                ▼
        PostgreSQL                      AI Services                         
           │                                │
           ▼                      ┌─────────┼───────────┐       
     Lesson Data                  ▼         ▼           ▼     
                                 RAG      OpenAI LLM   Whisper STT         
```

## Design Database

### Goal

Design the database structure that will support the application's learning experience.

### Objectives

- Identify the core entities.
- Define relationships between entities.
- Plan how user progress will be stored.
- Plan how lesson content will be stored.
- Plan how exercises will be stored.
- Plan how challenge progression will be stored.
- Plan how native audio will be linked.
- Plan how AI/RAG data will be stored.
- Create an Entity Relationship Diagram (ERD).

### Deliverables

- Database schema
- ER Diagram
- Table relationships

### Initial Project Structure

```text
Asusu-AI/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── app/ # Streamlit application
│
├── learning_engine/ # Learning logic
│
├── ai/ # AI services
│
├── database/ # Database models & queries
│
├── data/ # curriculum / seed data
│
├── assets/
│ ├── audio/
│ └── images/
│
├── tests/
│
├── docs/
│ ├── product.md
│ ├── roadmap.md
│ ├── curriculum.md
│ ├── architecture.md
│ ├── database.md
│ ├── ai.md
│ └── deployment.md
│
└── docker/
```