# 🚀 Churn Prediction App (MLOps Edition)

A full-stack Machine Learning application that predicts customer churn using **TensorFlow/Keras**. This project is containerized with **Docker** and developed within a **WSL 2** environment on Windows.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **ML Framework:** TensorFlow, Keras, Scikit-learn
* **Deployment:** Streamlit
* **Infrastructure:** Docker, WSL 2 (Ubuntu)

---

## 🏗️ Project Structure
* `app.py`: Streamlit frontend and prediction logic.
* `churn_model.keras`: Trained deep learning model.
* `scaler.pkl`: Pre-processing scaler for feature normalization.
* `Dockerfile`: Instructions for containerizing the app.
* `requirements.txt`: Python dependencies.

---

## 🚀 How to Run Locally

### 1. Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on Windows.
* WSL 2 enabled with Ubuntu integration.
