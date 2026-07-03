<img width="1920" height="946" alt="image" src="https://github.com/user-attachments/assets/b7e2832f-9403-41fd-b826-ebfc66692ac7" />
<img width="1920" height="953" alt="image" src="https://github.com/user-attachments/assets/5e3ea568-b036-4d69-993e-1beb68a9e7e4" />
<img width="1920" height="953" alt="image" src="https://github.com/user-attachments/assets/3c5449b8-8179-4f41-bd14-e78fd95b14ee" />
<img width="1920" height="953" alt="image" src="https://github.com/user-attachments/assets/559aec8a-1f85-4fcc-8227-a5ffec74459b" />


# IssuePilot


IssuePilot is an AI-powered bug triage system built to simplify the initial stages of software issue management. Given a bug report, the application analyzes its description, predicts its priority, identifies the most relevant software component, and retrieves similar historical issues using machine learning.

The project combines multiple machine learning models with a **FastAPI** backend and a **React** frontend to provide a complete end-to-end application. The backend is containerized using Docker and hosted on Render, while the frontend is deployed on Vercel.

**Live app:** [issue-pilot-bug-triage.vercel.app](https://issue-pilot-bug-triage.vercel.app)

---

## Motivation

Large software projects often receive hundreds of bug reports. Reviewing each report manually can be repetitive and time-consuming, especially during the initial triage process.

IssuePilot was built to explore how machine learning can automate part of this workflow by assisting developers with issue classification and retrieval, rather than replacing human decision-making.

---

## Features

- Analyze software bug reports from natural language descriptions
- Predict issue priority using a trained machine learning model
- Classify issues into their most likely software component
- Retrieve similar historical issues using text similarity
- View project statistics through a dashboard
- Learn how the prediction system works through the About page
- Fully deployed using Render (backend) and Vercel (frontend)

---

## Machine Learning

IssuePilot uses multiple machine learning models trained on a dataset of **4,515** GitHub issues.

### Priority Prediction
A text classification model predicts the priority level of an incoming issue based on its title and description. The model was trained using **TF-IDF vectorization** combined with **Logistic Regression**, learning relationships between issue descriptions and their priority labels. (~85% accuracy)

### Component Classification
A second Logistic Regression model predicts which software component or module the issue most likely belongs to, helping organize incoming issues before developers begin working on them. (~72% accuracy)

### Similar Issue Retrieval
Instead of training another predictive model, IssuePilot performs semantic retrieval using TF-IDF vectors:

1. The issue description is converted into a TF-IDF vector
2. Cosine similarity is calculated against previously processed issues
3. The most similar historical issues are returned

This helps developers spot duplicate reports or previously solved problems.

---

## Backend

The backend is built with **FastAPI** and exposes REST endpoints used by the frontend. Its responsibilities include:

- loading trained machine learning models
- preprocessing user input
- generating predictions
- retrieving similar issues
- serving dashboard statistics
- returning JSON responses for the frontend

Models are loaded once at application startup using **Joblib** to reduce inference latency.

### API Reference

| Method | Endpoint      | Description                                            |
|--------|---------------|----------------------------------------------------------|
| GET    | `/`             | API status check                                        |
| POST   | `/analyze`      | Submit a `title` + `description`, returns predicted priority, component, and top 3 similar issues |
| GET    | `/dashboard`    | Aggregate stats — total predictions, priority breakdown, model accuracy |
| GET    | `/model-info`   | Metadata about the trained models (type, vectorizer, accuracy) |
| GET    | `/about`        | Project metadata (version, stack, dataset size, features) |
| GET    | `/health`       | Health check — confirms API status and that models are loaded |

**Example request:**
```bash
curl -X POST https://issue-pilot-bug-triage.onrender.com/analyze \
  -H "Content-Type: application/json" \
  -d '{"title": "Login button unresponsive on Safari", "description": "Clicking login does nothing on Safari 17, works fine on Chrome."}'
```

**Example response:**
```json
{
  "priority": "High",
  "component": "Frontend",
  "similar_issues": [
    { "issue_url": "...", "title": "...", "similarity_score": 0.82 }
  ]
}
```

---

## Frontend

The frontend is built with **React** and **Vite**. It communicates with the FastAPI backend through **Axios** and provides a clean interface where users can:

- submit issue descriptions
- view predictions
- browse similar issues
- explore project statistics
- understand how the system works

Routing is handled using **React Router**.

---

## Tech Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React, Vite, Axios, React Router |
| **Backend** | FastAPI, Python, Pandas, NumPy, scikit-learn, Joblib |
| **Machine Learning** | TF-IDF Vectorization, Logistic Regression, Cosine Similarity |
| **DevOps & Deployment** | Docker, Git & GitHub, Render, Vercel |

---

## Project Structure

```text
IssuePilot
│
├── backend
│   ├── app
│   │   ├── routers        # analyze, dashboard, about, health, model_info
│   │   ├── services        # predictor.py, similarity.py
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   ├── ML
│   │   ├── artifacts        # trained model files
│   │   ├── data
│   │   └── training
│   │
│   ├── Dockerfile
│   └── requirements-prod.txt
│
└── frontend
    └── bug-triage
```

---

## Running Locally

### Backend
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements-prod.txt
uvicorn app.main:app --reload
```
Backend runs at `http://localhost:8000`.

### Frontend
```bash
cd frontend/bug-triage
npm install
npm run dev
```
Frontend runs at `http://localhost:5173`.

### With Docker
```bash
docker compose up --build
```

---

## Live Demo

| Service | URL |
|---|---|
| Frontend | https://issue-pilot-bug-triage.vercel.app |
| Backend API | https://issue-pilot-bug-triage.onrender.com |

---

## Future Improvements

- GitHub Issues integration
- User authentication
- Confidence scores for predictions
- Model retraining pipeline
- Improved semantic search using sentence embeddings
- Advanced analytics dashboard

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Maheen Ul Muslim**

GitHub: [github.com/maheen8q](https://github.com/maheen8q)
LinkedIn: [linkedin.com/in/maheen-ul-muslim-463b8135a](https://www.linkedin.com/in/maheen-ul-muslim-463b8135a)
GitHub: https://github.com/maheen8q

LinkedIn: www.linkedin.com/in/maheen-ul-muslim-463b8135a


