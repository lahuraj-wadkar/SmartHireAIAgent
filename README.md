# 🚀 Smart Hire AI Agent

An AI-powered Technical Interview Simulator built using **Python**, **Ollama**, and **Llama 3**. The system conducts technical interviews, evaluates answers using a Large Language Model (LLM), generates feedback, assigns scores, and creates detailed interview reports.

---

## 📌 Project Objective

The objective of this project is to help students and professionals practice technical interviews using an AI-powered evaluation system.

This project demonstrates:

- Generative AI
- AI Agents
- LLM Integration
- Prompt Engineering
- Memory Management
- Automatic Answer Evaluation
- Report Generation
- Local LLM Deployment using Ollama

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Ollama | Local LLM runtime |
| Llama 3 | Interview evaluation model |
| Requests | API communication |
| SQLite3 | Local data storage |
| Datetime | Timestamp generation |
| Text Files | Interview report storage |

---

## 📂 Project Structure

```text
SmartHire_AI_Agent/
│
├── main.py
├── interview_agent.py
├── LLMengine.py
├── questions.py
├── report_generator.py
│
└── reports/
    └── Generated Interview Reports
```

---

## 🎯 Features

- Full Technical Interview Mode
- Topic-wise Interview Mode
- AI-based Answer Evaluation
- Automatic Score Calculation
- Interview Memory Management
- Detailed Feedback Generation
- Report Generation with Timestamp
- Local Execution using Ollama

---

## 📚 Supported Interview Topics

The question bank currently contains questions from:

- Python
- C++
- Machine Learning
- Deep Learning
- Tkinter
- SQL
- RAG (Retrieval Augmented Generation)
- AI Agents

Example Question:

```python
{
    "topic": "Python",
    "question": "Explain the difference between list, tuple and set in Python."
}
```

---

## 🔄 Project Workflow

```text
Student Starts Application
          │
          ▼
       main.py
          │
          ▼
 Student Enters Details
          │
          ▼
 Selects Interview Mode
          │
          ▼
 Questions Loaded from questions.py
          │
          ▼
 Student Answers Question
          │
          ▼
 interview_agent.py
 Creates Evaluation Prompt
          │
          ▼
 llm_engine.py
          │
          ▼
 Ollama API
          │
          ▼
 Llama3 Model
          │
          ▼
 Evaluation + Score
          │
          ▼
 Report Generation
          │
          ▼
 report_generator.py
          │
          ▼
 Report Saved in reports/
```

---

# 📄 Module Description

## 1. main.py

Main entry point of the application.

### Responsibilities

- Displays project header
- Collects student information
- Displays interview menu
- Starts interview sessions
- Generates final report

### Important Functions

#### print_header()

Displays project information.

#### show_menu()

Displays menu options.

```text
1. Start Full Interview
2. Exit
3. Start Topic-wise Interview
```

#### get_available_topics()

Returns available interview topics.

#### start_interview()

Starts and manages the complete interview.

#### main()

Controls overall application flow.

---

## 2. questions.py

Contains the interview question bank.

### Responsibilities

- Stores topic-wise questions
- Allows easy expansion of question sets
- Supplies questions during interviews

Example:

```python
{
    "topic": "Python",
    "question": "Explain the difference between list, tuple and set."
}
```

---

## 3. interview_agent.py

Core AI Agent implementation.

### Class

```python
MarvellousInterviewAgent
```

### Responsibilities

- Prompt Generation
- Interview Evaluation
- Score Calculation
- Feedback Generation
- History Management
- Final Report Generation

### Important Attributes

```python
self.student_name
self.history
self.conversation
self.total_score
```

### Key Functions

#### evaluate_answer(topic, question, answer)

Creates a structured prompt and sends it to 