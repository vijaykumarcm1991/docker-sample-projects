# 🚀 Docker Sample Projects  
This repository contains **5 practical, real-world Docker projects** designed for learning containerization, Docker Compose, multi-container applications, and full-stack deployments.  
Each project is fully working and includes Dockerfiles, docker-compose files, and clean folder structures.

---

## 📂 Repository Structure

```
docker-sample-projects/
│
├── project-1-flask-app/
├── project-2-python-mysql/
├── project-3-node-nginx/
├── project-4-wordpress-mysql/
└── project-5-fullstack-react-node-mongo/
```

---

# 📘 **Project Overview**

---

## 🔹 **1. Python Flask App (Single Container)**  
A simple Flask API serving a “Hello from Docker” message.

📁 Folder: `project-1-flask-app/`  
📦 Skills Learned:
- Writing Dockerfiles  
- Working with Python containers  
- Exposing ports  

Run:
```bash
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

---

## 🔹 **2. Python App + MySQL (Docker Compose)**  
A Flask app connecting to a MySQL container using Docker Compose.

📁 Folder: `project-2-python-mysql/`  
📦 Skills Learned:
- Multi-container apps  
- Docker Compose basics  
- Service dependency management  

Run:
```bash
docker compose up --build
```

---

## 🔹 **3. Node.js App with NGINX Reverse Proxy**  
Node.js backend serviced through NGINX running in a separate container.

📁 Folder: `project-3-node-nginx/`  
📦 Skills Learned:
- NGINX reverse proxy  
- Node.js containerization  
- Multi-service networking  

Run:
```bash
docker compose up --build
```

---

## 🔹 **4. WordPress + MySQL (Production Setup)**  
A ready-to-run WordPress site using Docker Compose with persistent MySQL storage.

📁 Folder: `project-4-wordpress-mysql/`  
📦 Skills Learned:
- Handling environment variables  
- WordPress deployment  
- Persistent Docker volumes  

Run:
```bash
docker compose up -d
```

Website URL:  
👉 http://localhost:8080

---

## 🔹 **5. Full Stack MERN: React + Node.js API + MongoDB**  
A complete full-stack application running with three containers.

📁 Folder: `project-5-fullstack-react-node-mongo/`  
📦 Skills Learned:
- Full-stack Docker workflows  
- API + frontend separation  
- Docker networking with MongoDB  

Run:
```bash
docker compose up --build
```

---

# 🛠️ Technologies Used

- Docker  
- Docker Compose  
- Python (Flask)  
- Node.js / Express  
- MySQL  
- MongoDB  
- NGINX  
- React  

---

# 🚀 Next Steps (Optional Enhancements)

If you want, you can extend this repository to include:

- Kubernetes deployment files  
- Jenkins or GitHub Actions CI/CD  
- Helm charts  
- AWS deployment scripts  
- Monitoring using Prometheus + Grafana  

---

# 📄 License
MIT License.

---

# 🙌 Contribution  
Feel free to fork this repository and submit pull requests to improve these sample projects.
