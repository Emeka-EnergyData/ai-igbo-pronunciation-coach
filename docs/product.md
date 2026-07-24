# AI-IGBO-LANGUAGE-LEARNING-ASSISTANT

> A voice-first AI-powered platform for learning Nigerian languages through challenge-based learning. It contains 135 tracks. 108 exercises and 27 subtopics

## Vision

The aim is to help learners become confident enough to hold everyday conversations in Nigerian languages, starting with **Igbo**.

Instead of memorizing thousands of vocabulary words, learners build confidence through small, interactive challenges that gradually increase in difficulty.

The learning experience is inspired by **Exercism**:

- Learn a concept
- Practice with a few guided exercises
- Complete a challenge
- Reuse previous concepts throughout future challenges

## Learning Philosophy

- One new concept at a time.
- Learn by speaking.
- Constant review.
- Small wins build confidence.
- AI acts as a personal tutor.
- Focus on communication rather than memorization.

## MVP Roadmap

## Phase 0 - Project Planning

**Goal**
Define the project before writing code.

### Tasks

- [✔] Define MVP scope
- [✔] Design system architecture
- [✔] Design database
- [✔] Create project structure
- [✔] Initialize Git repository

## Phase 1 - Curriculum Design

**Goal**
Design the learning roadmap.

### Lessons

- [ ] Foundations
- [ ] Words
- [ ] Sentences
- [ ] Communication
- [ ] Conversation
- [ ] Mastery

### Phase 2 - Lesson Mode

Browse the curriculum by concept.

Each lesson contains

- Explanation
- Native Audio
- Examples
- Explanation Exercises
- AI Tutor
- Exercise 1
- Exercise 2
- Exercise 3
- Boss Challenge

Purpose:
Study a topic whenever you need it.

### Phase 3 - Challenge Mode

The same lessons and exercise are presented in a progressive order.

Example

- Challenge 1 -> Foundations Exercise 1
- Challenge 2 -> Words Exercise 1
- Challenge 3 -> Sentences Exercise 1
- Challenge 4 -> Foundations Exercise 2
- Challenge 5 -> Communication Exercise 1
- Challenge 6 -> Words Exercise 2

...
Each challenge intoduces at most **one new concept** while reinforcing previously learned material

## Phase 4 - Database

**Goal:**
Store all learning content and user progress.

### Tables

- [ ] Lessons
- [ ] Challenges
- [ ] Challenge Types
- [ ] Vocabulary
- [ ] Grammar Notes
- [ ] Users
- [ ] User Progress

## Phase 5 - User Interface

**Goal:**
Build the application.

### Pages

- [ ] Home
- [ ] Lesson
- [ ] Challenge
- [ ] Progress
- [ ] Settings

## Phase 6 - Voice Features

**Goal:**
Enable voice-first learning.

### Features

- [ ] Play native audio
- [ ] Record learner audio
- [ ] Speech-to-text
- [ ] Answer checking

## Phase 7 - AI Tutor

**Goal**
Provide intelligent guidance.

### Features

- [ ] Explain mistakes
- [ ] Grammar explanations
- [ ] Give hints
- [ ] Encourage learners
- [ ] Suggest lesson review

## Phase 8 - RAG

**Goal**
Use your lesson content to power AI explanations.

### Features

- [ ] Embeddings
- [ ] Vector database
- [ ] Lesson retrieval
- [ ] Context-aware AI responses

---

## Phase 9 - Deployment

**Goal**
Publish the application.

### Tasks

- [ ] Docker
- [ ] PostgreSQL
- [ ] Deploy application
- [ ] Testing
- [ ] Documentation

---

# Future Features

- AI conversation mode
- Pronunciation scoring
- Yoruba track
- Hausa track
- Additional Nigerian languages
- Mobile app
- Offline mode
- Teacher dashboard
- Community audio contributions
- Adaptive learning
- Daily challenges

---

# Design Principles

Every feature should follow these rules:
1. Introduce only **one new concept** per challenge.
2. Reuse previously learned concepts in future challenges.
3. If a learner struggles, guide them back to the relevant lesson.
4. Build confidence before pursuing perfection.
5. Prioritize everyday communication over memorizing large vocabulary lists.

---

# Tech Stack (Planned)

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** PostgreSQL (+ pgvector when RAG is added)
- **AI:** OpenAI APIs (or equivalent models)- **Speech-to-Text:** Whisper (or another STT model)
- **Vector Search:** pgvector (MVP)
- **Deployment:** Docker + Hugging Face Spaces / Cloud