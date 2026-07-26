# Database Design

## Overview

The Asụsụ AI database is designed to evolve alongside the application. Rather than building every database table at the beginning, the project follows a phased approach where each phase introduces only the tables required for that stage of development.

This approach keeps the MVP simple, makes development easier to manage, and provides a clear roadmap for future features.

---

# Database Evolution

The database is divided into three phases:

1. Curriculum Database (MVP)
2. Learning Platform Database
3. AI Tutor & RAG Database

Each phase builds on the previous one.

---

# Phase 1: Curriculum Database (Current MVP)

## Goal

Create a curriculum engine capable of delivering structured lessons to learners.

At this stage, the application focuses entirely on educational content. There are no user accounts, learner progress, or AI conversation features.

## Tables

- Topics
- Subtopics
- Lessons
- Lesson Items
- Exercises

## Responsibilities

- Organise the learning roadmap.
- Store lesson content.
- Store lesson explanations.
- Store audio references.
- Store practice exercises.
- Deliver lesson data to the Streamlit application.

## Entity Relationship Diagram

```text
                    ┌──────────────────┐
                    │      topics      │
                    ├──────────────────┤
                    │ topic_id (PK)    │
                    │ topic_name       │
                    │ description      │
                    └────────┬─────────┘
                             │ 1
                             │
                             │
                             │ ∞
               ┌─────────────▼──────────────┐
               │          subtopics         │
               ├────────────────────────────┤
               │ subtopic_id (PK)           │
               │ topic_id (FK)              │
               │ subtopic_name              │
               │ description                │
               └─────────────┬──────────────┘
                             │ 1
                             │
                             │
                             │ ∞
                 ┌───────────▼─────────────┐
                 │ lessons                 │
                 ├─────────────────────────┤
                 │ lesson_id (PK)          │
                 │ subtopic_id (FK)        │
                 │ lesson_number           │
                 │ title                   │
                 │ concept                 │
                 └──────────┬───────┬──────┘
                            │1      │1
                            │       │
                           ∞│      ∞│
           ┌────────────────▼─┐ ┌───▼──────────────┐
           │ lesson_items     │ │ exercises        │
           ├──────────────────┤ ├──────────────────┤
           │ item_id (PK)     │ │ exercise_id (PK) │
           │ lesson_id (FK)   │ │ lesson_id (FK)   │
           │ item_order       │ │ exercise_number  │
           │ item_type        │ │ title            │
           │ title            │ │ prompt           │
           │ explanation      │ │ expected_answer  │
           │ example          │ │ hint             │
           │ audio_path       │ │ audio_path       │
           └──────────────────┘ └──────────────────┘
```

## Table Descriptions

### Topics

Stores the highest level of the curriculum.

Examples:

- Foundation
- Grammar
- Conversation
- Listening

Each topic contains multiple subtopics.

---

### Subtopics

Stores the learning sections inside each topic.

Example:

Foundation

- Alphabet
- Pronunciation

Each subtopic contains one or more lessons.

---

### Lessons

Stores the individual lessons presented to the learner.

Each lesson contains:

- Lesson number
- Lesson title
- Lesson concept

A lesson acts as the parent record for both teaching content and exercises.

---

### Lesson Items

Stores the teaching content inside a lesson.

Rather than creating separate tables for vowels, consonants, grammar rules and greetings, all lesson content is stored in one flexible table.

Current examples include:

- CH
- GB
- KP

Each lesson item stores:

- Title
- Explanation
- Example
- Audio path

This allows future lessons to reuse the same table without modifying the database schema.

---

### Exercises

Stores all practice activities belonging to a lesson.

Each exercise contains:

- Exercise title
- Prompt
- Expected answer
- Hint
- Target audio

These exercises are displayed immediately after the lesson content.

---

## Relationships

The curriculum follows a simple hierarchical structure.

```text
One Topic
        ↓
Many Subtopics

One Subtopic
        ↓
Many Lessons

One Lesson
        ↓
Many Lesson Items

One Lesson
        ↓
Many Exercises
```

Relationship Summary

| Parent | Child | Relationship |
|---------|--------|-------------|
| Topics | Subtopics | One-to-Many |
| Subtopics | Lessons | One-to-Many |
| Lessons | Lesson Items | One-to-Many |
| Lessons | Exercises | One-to-Many |

---

# Phase 2: Learning Platform Database

## Goal

Transform the curriculum into a personalised learning platform.

Instead of only displaying lessons, the application now remembers each learner's progress and performance.

## Planned Tables

- Users
- Lesson Progress
- Exercise Attempts
- AI Feedback

## Responsibilities

- User authentication.
- Save completed lessons.
- Track learner progress.
- Store AI pronunciation scores.
- Store learner self-ratings.
- Store human verification.
- Resume learning from the last completed lesson.

---

# Phase 3: AI Tutor & RAG Database

## Goal

Enable intelligent tutoring and real conversational practice.

This phase introduces Retrieval-Augmented Generation (RAG) and AI-powered conversations using the curriculum as the application's knowledge base.

## Planned Tables

- Documents
- Document Chunks
- Embeddings
- Conversation History
- Conversation Memory
- Audio Library

## Responsibilities

- Store curriculum documents.
- Split lessons into searchable chunks.
- Store vector embeddings.
- Retrieve relevant lesson content during conversations.
- Store conversation history.
- Maintain conversation memory.
- Manage professionally recorded native-speaker audio.

---

# Development Timeline

```text
Phase 1
Curriculum Engine
│
├── Topics
├── Subtopics
├── Lessons
├── Lesson Items
└── Exercises

        │
        ▼

Phase 2
Learning Platform
│
├── Users
├── Lesson Progress
├── Exercise Attempts
└── AI Feedback

        │
        ▼

Phase 3
AI Tutor & RAG
│
├── Documents
├── Document Chunks
├── Embeddings
├── Conversation History
├── Conversation Memory
└── Audio Library
```

---

## Design Philosophy

The database is intentionally developed in phases.

Rather than attempting to build every feature upfront, each phase introduces only the tables required to support the application's current functionality.

This incremental approach keeps the MVP manageable, simplifies development, and allows the database to grow naturally as new features are added.