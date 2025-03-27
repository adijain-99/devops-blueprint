# What Does This App Do?

Imagine a magical school where we keep track of all students. Our User Service is like a super-smart librarian who can:

- Show you a list of all students
- Find a specific student by their unique ID
- Always tell you if the system is working perfectly

### Technical Features

- RESTful API for user management
- Containerized application
- Kubernetes-ready deployment
- Built with Python and Flask
- Includes health check endpoint

### Prerequisites: 

- Docker (🐳 Version 20.10+)
- Kubernetes (Minikube recommended)
- Python 3.9+
- Git
- Stable internet connection

## Local setup

### 1. Clone the Repository

```
git clone <your-repository-url>
cd services/user-service

```

### 2. Local Python Development

```
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application locally
python app.py

```

### 3. Docker Build and Run

```
# Build the image
docker build -t user-service:v1 .

# Verify image is created
docker images | grep user-service


# Run container locally
docker run -p 5000:5000 user-service:v1

# Access the service
# Open browser: http://localhost:5000/users

```

### 4. Kubernetes Deployment

```
# Start Minikube
minikube start

# Load Docker image to Minikube
minikube image load user-service:v1

# Apply Kubernetes Deployments
kubectl apply -f user-deployment.yaml
kubectl apply -f user-service.yaml

# Check deployments
kubectl get deployments
kubectl get services

```

### 5. Accessing the Service

```
# Open service in browser
minikube service user-service

OR

# Forward port to access service
kubectl port-forward service/user-service 5000:80

```


