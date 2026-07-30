# AI Igbo Pronunciation Coach

> **Current Status:** MVP Complete | Preparing for Deployment

## Overview

An AI-powered language learning application focused on helping learners practice Igbo pronunciation. Learners listen to native pronunciations, record their own speech, and receive AI-generated feedback to improve their speaking confidence.

This project combines speech recognition, large language models, and educational software design into an interactive learning experience.

## Features

### Implemented
- Lesson-based pronunciation practice
- Native Igbo audio playback
- Voice recording
- Local Igbo speech recognition
- AI-generated pronunciation feedback
- Streamlit user interface
- PostgreSQL-backed lesson management

### In Progress

- Application deployment
- User interface improvements
- Performance optimization

### Planned

- Learner progress tracking
- Personalized learning
- Improved pronunciation assessment
- Conversation practice
- Vocabulary and grammar modules

## Tech Stack
- Python
- Streamlit
- PostgreSQL
- SQLAlchemy
- Pydantic
- Hugging Face Transformers
- Google Gemini API

## Project Structure

```text
.
├── app.py
├── assets/
├── docs/
├── pages/
├── src/
│ ├── ai/
│ ├── audio/
│ ├── database/
│ └── learning_engine/
├── tests/
└── requirements.txt
```

## Documentation

- [Product Vision](docs/product.md)
- [Development Roadmap](docs/roadmap.md)
- [Curriculum](docs/architecture.md)
- [System Architecture](docs/architecture.md)
- [Database Design](docs/database.md)
- [AI Pipeline](docs/ai.md)

## AI Workflow

```text
User
   │
   ▼
Streamlit Interface
   │
   ▼
Audio Recording
   │
   ▼
Igbo Speech-to-Text
   │
   ▼
AI Feedback Service
   │
   ▼
Pronunciation Feedback
```

## Product Vision

The long-term vision of this project is to become an intelligent Igbo language learning platform that combines AI, speech recognition, and personalized learning to help preserve and promote the Igbo language.

## Installation

Clone the repository:

```bash
git clone https://github.com/Emeka-EnergyData/ai-igbo-pronunciation-coach.git
```

Navigate into the project:

```bash
cd ai-igbo-pronunciation-coach
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Roadmap

- [x] MVP pronunciation practice application
- [ ] Deploy application
- [ ] Improve pronunciation evaluation
- [ ] Learner progress tracking
- [ ] RAG-powered language explanations
- [ ] Conversation practice
- [ ] Mobile-friendly interface
      
## License

This project is intended for educational and research purposes.
> **Note**: Audio assets used during development are not included in this repository because they are not redistributable. Replace them with your own recordings before deployment.

