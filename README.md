# Trello Clone – Scaler AI Labs Assignment

## Overview
A Trello-like Kanban board built as part of the Scaler AI Labs SWE Intern assignment.

## Tech Stack
- Frontend: Next.js (App Router), TypeScript, Tailwind CSS
- Backend: FastAPI, SQLAlchemy
- Database: SQLite
- Drag & Drop: @hello-pangea/dnd

## Features
- Board with lists and cards
- Drag & drop lists and cards
- Create, edit, and reorder cards
- Checklist with completion status
- Persistent backend storage

## Setup Instructions

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
