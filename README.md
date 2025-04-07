# Quizdom Application

**Quizdom** is a full-stack quiz application that allows users to register, log in, take quizzes, and view results in real-time. It's built using modern web technologies with a focus on speed, developer experience, and scalability.

---

## 🧱 Tech Stack

### 🧠 Why These Technologies?

- **Backend: [FastAPI](https://fastapi.tiangolo.com/)**  
  FastAPI is a modern, fast (high-performance) web framework for Python. It is ideal for building APIs with automatic documentation, type safety, and excellent async support.

- **Frontend: [React](https://reactjs.org/) + [Vite](https://vitejs.dev/) + [Shadcn UI](https://ui.shadcn.com/)**  
  React is a powerful UI library, and Vite offers blazing-fast development and build tooling. Shadcn UI provides accessible and customizable components built with Tailwind CSS, perfect for quickly building a polished interface.

- **Database: [PostgreSQL](https://www.postgresql.org/)**  
  A powerful, open-source relational database system, PostgreSQL is well-suited for complex queries and handles structured data with ease.

- **Containerization: [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)**  
  These tools help package the application with all dependencies and simplify development, testing, and deployment—ensuring consistent environments across teams and production.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🛠️ Setup & Run

### 1. Clone the repository

```bash
git clone https://your-repo-url.git
cd quizdom
```

### 2. Create a `.env` file at the root

```env
ENVIRONMENT=development
DATABASE_URL=postgresql+psycopg2://postgres:postgres@db:5432/postgres
SECRET_KEY=your_secret_key_here
```

> 💡 `ENVIRONMENT` controls how the backend runs: `development` uses Uvicorn with hot reload, while `production` uses Gunicorn for performance.

---

### 3. Build & start the app

```bash
docker-compose up --build
```

Once started, access:

- 🧠 Backend API: [http://localhost:8000](http://localhost:8000)
- 💻 Frontend UI: [http://localhost:5173](http://localhost:5173)
- 🗃️ PostgreSQL: accessible on `localhost:5432`

---

### 4. Running in Production

To run in production mode:

1. Update your `.env` file:

   ```env
   ENVIRONMENT=production
   ```

2. Rebuild and start containers:

   ```bash
   docker-compose down
   docker-compose up --build
   ```

---

## 📂 Project Structure

```bash
├── backend/                     # Backend source code
│   ├── .env                     # Backend environment variables (local use)
│   ├── alembic/                 # Alembic migrations
│   ├── app/                     # FastAPI app (routes, models, services)
│   ├── alembic.ini             # Alembic config file
│   ├── requirements.txt        # Python dependencies
├── docker/
│   └── backend/                # Backend Docker setup
│       ├── Dockerfile          # Backend Dockerfile
│       └── start.sh            # Startup script for environment-based boot
├── frontend/                   # Frontend source code
│   ├── .env                    # Frontend environment variables
│   ├── .env.template           # Example env for setup
│   ├── src/                    # React + Vite application source
│   └── public/                 # Static assets
├── docker-compose.yml         # Service orchestration (frontend, backend, db)
├── README.md                  # Project overview and setup instructions
└── .gitignore                 # Files to ignore in version control
```

---

## 🧪 Future Improvements

- 🔐 JWT refresh tokens for extended auth sessions
- 📊 Quiz statistics dashboard
- 🛠 Admin panel for quiz/question management
- ☁️ Docker Swarm / Kubernetes deployment support

---

## 👨‍💻 Maintainers

- Jesse James Kigula – [jkigula@icloud.com](mailto:jkigula@icloud.com)
- Ndyabagye Henry – [ndyabagyehenrytusi@gmail.com](mailto:ndyabagyehenrytusi@gmail.com)

---

## 📄 License

MIT – feel free to use and modify.