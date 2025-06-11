# CI/CD Pipeline using GitHub Actions with FastAPI

This project demonstrates how to implement a complete CI/CD pipeline using GitHub Actions. Since the core objective is to understand the CI/CD pipeline therfore a simple FastAPI app is chosen that returns a Fibonacci series for a given number of terms. The CI/CD Workflow includes code build, testing, and Docker image deployment to Docker Hub.

## 📂 Project Structure

```
CICD_PIPELINE_USING_GITHUB_ACTIONS/
├── .gitignore                # Specifies files and directories to be ignored by Git (e.g., __pycache__, .env, myenv/)
├── .dockerignore            # Specifies files and directories to be ignored by Docker (e.g., myenv/, __pycache__)
├── app_fastapi.py           # FastAPI application with Fibonacci endpoints
├── requirements.txt         # Python dependencies
├── test_cases.py            # Unit tests for the FastAPI application
├── README.md                # Project documentation
├── myenv/                   # Python virtual environment (not pushed to repo)
└── .github/
    └── workflows/
        └── CICD.yaml        # GitHub Actions workflow file for CI/CD pipeline
```

## 🚀 FastAPI Application Overview

- **Endpoint `/`** — Health check
- **Endpoint `/fibonacci/{n}`** — Returns the first `n` terms of the Fibonacci sequence

## 🔄 GitHub Actions CI/CD Workflow

The `.github/workflows/CICD.yaml` file contains two jobs:

1. **Build & Test**
   - Triggered on push and pull requests to the `main` branch
   - Installs dependencies using `requirements.txt`
   - Runs tests defined in `test_cases.py`

2. **Deploy**
   - On successful testing, builds a Docker image
   - Pushes the image to Docker Hub

> GitHub Secrets required:
> - `DOCKER_USERNAME`
> - `DOCKER_PASSWORD`

## 🧪 Local Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/shakeeluetp1041/cicd-auto-build-test-deploy-pipeline.git
cd CICD_PIPELINE_USING_GITHUB_ACTIONS
```

2. **Create and activate a virtual environment**

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the FastAPI app**

```bash
uvicorn app_fastapi:app --reload
```

5. **Test the endpoint**

Open your browser or use curl to visit:

```
http://127.0.0.1:8000/fibonacci/10
```

## ⚙️ Steps to Trigger CI/CD Pipeline

1. Push any code change to the `main` branch or create a pull request
2. GitHub Actions will automatically:
   - Install dependencies
   - Run tests
   - Build and deploy Docker image to Docker Hub

> Make sure to configure GitHub secrets with your DockerHub credentials.

## 🐳 Using Dockerized App

1. **Pull image from Docker Hub**

```bash
docker pull shakeelahmed1041(write-your-dockerhub-username)/fibonacci-fastapi:latest
```

2. **Run the container**

```bash
docker run -d -p 8000:8000 shakeelahmed1041(write-your-dockerhub-username)/fibonacci-fastapi:latest
```

3. **Access the app**

Open browser at: `http://localhost:8000/fibonacci/5`

## 📌 Project Requirements

- Python 3.7+
- Git & GitHub account
- Docker & Docker Hub account
- GitHub Actions enabled
- Internet connection

## 🛠️ End-to-End Pipeline Setup Summary

- Clone the repository
- Create and activate virtual environment
- Install dependencies via `requirements.txt`
- Create `.github/workflows/CICD.yaml` with build, test, deploy jobs
- Write test cases in `test_cases.py`
- Push code or create pull requests to trigger CI/CD
- Docker image is pushed to Docker Hub upon successful pipeline

This project provides a complete CI/CD template with FastAPI and GitHub Actions integrated with Docker deployment.
