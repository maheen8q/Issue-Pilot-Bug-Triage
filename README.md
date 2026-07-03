<img width="1920" height="946" alt="image" src="https://github.com/user-attachments/assets/b7e2832f-9403-41fd-b826-ebfc66692ac7" />
<img width="1920" height="953" alt="image" src="https://github.com/user-attachments/assets/5e3ea568-b036-4d69-993e-1beb68a9e7e4" />
<img width="1920" height="953" alt="image" src="https://github.com/user-attachments/assets/3c5449b8-8179-4f41-bd14-e78fd95b14ee" />
<img width="1920" height="953" alt="image" src="https://github.com/user-attachments/assets/559aec8a-1f85-4fcc-8227-a5ffec74459b" />
#  IssuePilot

IssuePilot is an AI-powered bug triage system built to simplify the early stages of software issue management. Instead of manually reading every bug report, the application analyzes an issue description and predicts its priority, identifies the most relevant software component, and recommends similar issues from a historical dataset.

The project combines machine learning models with a FastAPI backend and a React frontend to provide a complete end-to-end application that can be used through a simple web interface.

---

##  Motivation

Large software projects often receive hundreds of bug reports. Reviewing each report manually can be repetitive and time-consuming, especially during the initial triage process.

IssuePilot was built to explore how machine learning can automate part of this workflow by assisting developers with issue classification and retrieval rather than replacing human decision-making.

---

##  Features

* Analyze software bug reports from natural language descriptions.
* Predict issue priority using a trained machine learning model.
* Classify issues into their most likely software component.
* Retrieve similar historical issues using text similarity.
* View project statistics through a dashboard.
* Learn how the prediction system works through the About page.
* Fully deployed using Render (backend) and Vercel (frontend).

---

##  Machine Learning

IssuePilot uses multiple machine learning models trained on GitHub issue data.

### Priority Prediction

A text classification model predicts the priority level of an incoming issue based on its title and description.

The model was trained using **TF-IDF vectorization** combined with **Logistic Regression**, allowing it to learn relationships between issue descriptions and their priority labels.

---

### Component Classification

A second text classification model predicts which software component or module the issue most likely belongs to.

This helps organize incoming issues before developers begin working on them.

---

### Similar Issue Retrieval

Instead of training another predictive model, IssuePilot performs semantic retrieval using TF-IDF vectors.

When a new issue is submitted:

* the issue description is converted into a TF-IDF vector,
* cosine similarity is calculated against previously processed issues,
* the most similar historical issues are returned.

This helps developers identify duplicate reports or previously solved problems.

---

## ⚙️ Backend

The backend is built with **FastAPI** and exposes REST API endpoints used by the frontend.

Its responsibilities include:

* loading trained machine learning models,
* preprocessing user input,
* generating predictions,
* retrieving similar issues,
* serving dashboard statistics,
* returning JSON responses for the frontend.

The models are loaded once during application startup using Joblib to reduce inference time.

---

##  Frontend

The frontend is built with **React** and **Vite**.

It communicates with the FastAPI backend through Axios and provides a clean interface where users can:

* submit issue descriptions,
* view predictions,
* browse similar issues,
* explore project statistics,
* understand how the system works.

Routing is handled using React Router.

---

## 🛠 Tech Stack

### Frontend

* React
* Vite
* Axios
* React Router

### Backend

* FastAPI
* Python
* Pandas
* NumPy
* scikit-learn
* Joblib

### Machine Learning

* TF-IDF Vectorization
* Logistic Regression
* Cosine Similarity

### Deployment

* Vercel (Frontend)
* Render (Backend)

---

##  Project Structure

```text
IssuePilot
│
├── backend
│   ├── app
│   │   ├── routers
│   │   ├── services
│   │   └── main.py
│   │
│   ├── ML
│   │   ├── artifacts
│   │   ├── data
│   │   └── training
│   │
│   └── requirements-prod.txt
│
└── frontend
    └── bug-triage
```

---

## 🚀 Running Locally

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements-prod.txt

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend/bug-triage

npm install

npm run dev
```

---

##  Live Demo

**Frontend**

https://issue-pilot-bug-triage.vercel.app

**Backend API**

https://issue-pilot-bug-triage.onrender.com

---

##  Future Improvements

* GitHub Issues integration
* User authentication
* Confidence scores for predictions
* Model retraining pipeline
* Improved semantic search using sentence embeddings
* Advanced analytics dashboard

---

##  Author

**Maheen Ul Muslim**


GitHub: https://github.com/maheen8q

LinkedIn: www.linkedin.com/in/maheen-ul-muslim-463b8135a


