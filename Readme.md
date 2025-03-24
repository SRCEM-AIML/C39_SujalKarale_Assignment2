# **StudentProject - Multi-App Django Project with Docker & Jenkins**

## **📌 Project Overview**
StudentProject is a **multi-app Django web application** designed to demonstrate **static views and templates**. This project is containerized using **Docker** and automated with **Jenkins CI/CD**.

---
## **🚀 Features**
- Multi-app Django project (**app1 & app2**).
- No database, only **static views & templates**.
- **Dockerized** for easy deployment.
- **CI/CD pipeline** using Jenkins.
- **Automated Docker image push** to Docker Hub.

---
## **📌 Project Structure**
```
StudentProject/
│── app1/                  # First Django app (homepage)
│── app2/                  # Second Django app (sample page)
│── StudentProject/        # Main Django project settings
│── templates/             # HTML templates
│── Dockerfile             # Docker configuration
│── Jenkinsfile            # CI/CD pipeline script
│── docker-compose.yml     # Docker Compose setup
│── requirements.txt       # Python dependencies
│── manage.py              # Django management script
│── README.md              # Project documentation
```

---
## **📌 1️⃣ Prerequisites**
Ensure you have the following installed:
- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/downloads)
- [Jenkins](https://www.jenkins.io/download/)

---
## **📌 2️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/StudentProject.git
cd StudentProject
```

---
## **📌 3️⃣ Run the Project Locally**
### ✅ **Using Python**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
# venv\Scripts\activate  # For Windows
pip install -r requirements.txt
python manage.py runserver
```
Access the application at **http://127.0.0.1:8000/**

---
## **📌 4️⃣ Run with Docker**
### ✅ **Build and Run Container**
```bash
docker build -t studentproject .
docker run -p 8000:8000 studentproject
```
Access **http://localhost:8000/**

---
## **📌 5️⃣ Deploy Using Docker Compose**
```bash
docker-compose up -d
```

---
## **📌 6️⃣ Push to Docker Hub**
### ✅ **Login & Push Docker Image**
```bash
docker login
docker tag studentproject yourdockerhubusername/studentproject:latest
docker push yourdockerhubusername/studentproject:latest
```

---
## **📌 7️⃣ Automate with Jenkins**
### ✅ **Jenkins Pipeline Setup**
1. **Go to Jenkins Dashboard → New Item → Pipeline**.
2. **Select 'Pipeline script from SCM'**.
3. **Enter your GitHub Repository URL**.
4. **Set Branch as 'main'**.
5. **Script Path: `Jenkinsfile`**.
6. **Click 'Save' and 'Build Now'**.

### ✅ **Jenkinsfile for CI/CD**
```groovy
pipeline {
    agent any
    environment {
        IMAGE_NAME = "yourdockerhubusername/studentproject"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/yourusername/StudentProject.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-credentials', variable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u yourdockerhubusername --password-stdin'
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }
    }
}
```

---
## **📌 8️⃣ Access the Application**
- **Local**: http://127.0.0.1:8000/
- **Docker**: http://localhost:8000/
- **Jenkins**: http://localhost:8080/

---
## **📌 9️⃣ Cleanup (Optional)**
### ✅ **Stop and Remove Containers**
```bash
docker stop studentproject
docker rm studentproject
```

### ✅ **Remove Docker Image**
```bash
docker rmi studentproject
```

### ✅ **Remove Unused Docker Data**
```bash
docker system prune -a
```

---
## **📌  🔥 Final Notes**
This project automates deployment using **Docker & Jenkins**. For any issues, create a GitHub issue or contact the maintainer.

💡 **Happy Coding! 🚀**