# 📚 Quizdom – Full Stack Quiz Application

**Quizdom** is a modern, full-stack quiz application that allows users to:

- Register and log in
- Take quizzes
- View results in real time

Built with speed, developer experience, and scalability in mind using cutting-edge technologies.

---

## 🧱 Tech Stack

### 🔧 Backend
- **[FastAPI](https://fastapi.tiangolo.com/)**  
  Fast, async-ready Python web framework with automatic documentation and type safety.

### 🎨 Frontend
- **[React](https://reactjs.org/)** + **[Vite](https://vitejs.dev/)** + **[Shadcn UI](https://ui.shadcn.com/)**  
  High-performance UI development with accessible and elegant components built using Tailwind CSS.

### 🗃️ Database
- **[PostgreSQL](https://www.postgresql.org/)**  
  Robust relational database system suited for structured data and advanced querying.

### 📦 Containerization
- **[Docker](https://www.docker.com/)** & **[Docker Compose](https://docs.docker.com/compose/)**  
  Ensure reproducible environments for development, testing, and production deployment.

---

## 🚀 Getting Started

### ✅ Prerequisites

Ensure the following are installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ Setup & Run

### 1️⃣ Clone the Repository

```bash
git clone https://your-repo-url.git
cd quizdom
```

### 2️⃣ Configure Environment Files

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
```

### 3️⃣ Root Environment Configuration

Create a `.env` file at the root with:

```env
ENVIRONMENT=development
DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/postgres
SECRET_KEY=your_secret_key_here
REACT_APP_API_URL=http://localhost:8000
```

> 💡 Use `development` for hot-reload via Uvicorn, `production` for Gunicorn performance.

---

### 4️⃣ Build & Start the App

```bash
docker-compose up --build
```

Access the services:

- 🧠 Backend: [http://localhost:8000](http://localhost:8000)
- 💻 Frontend: [http://localhost:5173](http://localhost:5173)
- 🗃️ PostgreSQL: `localhost:5432` (user: `postgres`, password: `postgres`)

---

## 🏗️ Running in Production

### 🔧 1. Update Environment

Edit `.env`:

```env
ENVIRONMENT=production
DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/postgres
REACT_APP_API_URL=http://your-domain.com:8000
```

### 🔁 2. Rebuild & Start

```bash
docker-compose down -v
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
```

### 🌐 3. Access Production Endpoints

```bash
Frontend: http://localhost:3000
Backend API: http://localhost:8000
```

### 🧰 4. Management Commands

```bash
# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Full cleanup (remove volumes too)
docker-compose down -v
```

---

## 🗂️ Project Structure

```bash
├── backend/
│   ├── .env                  # Local backend config
│   ├── alembic/              # DB migrations
│   ├── app/                  # FastAPI app (routes, models, etc.)
│   ├── alembic.ini           # Migration config
│   └── requirements.txt      # Backend dependencies
├── docker/
│   └── backend/
│       ├── Dockerfile        # Backend Dockerfile
│       └── start.sh          # Boot script (env-aware)
├── frontend/
│   ├── .env                  # Local frontend config
│   ├── .env.template         # Setup template
│   ├── src/                  # React + Vite app
│   └── public/               # Static assets
├── docker-compose.yml        # Main service configuration
├── README.md                 # Project overview
└── .gitignore                # Git exclusion list
```

---

## ✨ Key Features

- ✅ User Authentication
- 🧩 Quiz Creation & Management
- 📈 Real-Time Results
- 🐳 Containerized Deployment
- ♻️ Hot-Reload for Development

---

## 🔮 Planned Improvements

- 🔐 JWT Refresh Tokens
- 📊 Quiz Statistics Dashboard
- 🧑‍💼 Admin Panel
- ☁️ Docker Swarm / Kubernetes Deployment Support

---

## 👨‍🔧 Maintainers

- **Jesse James Kigula** – [jkigula@icloud.com](mailto:jkigula@icloud.com)  
- **Ndyabagye Henry** – [ndyabagyehenrytusi@gmail.com](mailto:ndyabagyehenrytusi@gmail.com)

---

## 📄 License

**MIT** – free to use, modify, and distribute.