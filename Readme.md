# FastAPI Student CRUD API with JWT Authentication (Dockerized)

A FastAPI application for managing student records with full CRUD (Create, Read, Update, Delete) operations, secured with JWT authentication. The project is fully containerized and published to Docker Hub for easy deployment anywhere.

---

## 🚀 Run Anywhere with Docker

You can run this application on **any platform** (Windows, macOS, Linux) using Docker. No need to install Python or dependencies manually!

### 1. Pull the Docker Image from Docker Hub

```bash
docker pull chandrka54/jwt-dockerize-crud-excercise:latest
```

### 2. Run the Docker Container

```bash
docker run -it -p 8000:8000 chandrka54/jwt-dockerize-crud-excercise:latest
```

- The API will be available at [http://localhost:8000](http://localhost:8000)
- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

#### Notes
- Make sure Docker is installed and running on your system.
- This image is already pushed to Docker Hub and can be run anywhere with Docker support.
- For custom builds, you can use the provided Dockerfile:

```bash
docker build -t chandrka54/jwt-dockerize-crud-excercise:latest .
docker run -d -p 8000:8000 chandrka54/jwt-dockerize-crud-excercise:latest
```

---

## 🔐 JWT Authentication

This API uses JWT (JSON Web Token) for authentication. Only authenticated users can access student CRUD endpoints.

- **Login Endpoint:**
  - `POST /login`
  - Use username: `admin` and password: `admin123` (demo credentials)
  - Returns: `{ "access_token": <token>, "token_type": "bearer" }`

- **How to Use JWT:**
  1. Call `/login` with the credentials to get a JWT access token.
  2. For all protected endpoints, add the following header:
     - `Authorization: Bearer <access_token>`

- **Token Expiry:**
  - Tokens are valid for 30 minutes by default.

---

## 📝 API Endpoints

| Method | Endpoint                 | Description                   | Auth Required |
| ------ | ------------------------ | ----------------------------- | ------------- |
| POST   | `/login`                 | Obtain JWT access token       | No            |
| POST   | `/students/{student_id}` | Create a new student          | Yes           |
| GET    | `/students/{student_id}` | Retrieve student by ID        | Yes           |
| PUT    | `/students/{student_id}` | Update student information    | Yes           |
| DELETE | `/students/{student_id}` | Delete student by ID          | Yes           |
| GET    | `/`                      | View API overview and author  | No            |

---

## 📦 Project Structure

```
JWT_Dockerize_fastAPI_CRUD_Excercise/
├── Dockerfile
├── main.py
├── requirments.txt
├── Readme.md
├── app/
│   ├── main.py
│   ├── auth_utils.py
│   ├── api/
│   │   └── routes.py
│   ├── schemas/
│   │   └── student.py
│   └── services/
│       └── student_service.py
```

---

## 📁 Important Files

### .gitignore
Specifies files and folders to be ignored by git version control. Example:
```
venv/
.env
__pycache__
.dockerignore
.git/
```

### .env
Environment variables for sensitive or environment-specific settings. Example:
```
APP_HOST=0.0.0.0
APP_PORT=8000
SECRET_KEY=your-secret-key
```

### requirments.txt
Python dependencies for the project:
```
fastapi
uvicorn
python-dotenv
python-jose
passlib[bcrypt]
```

### Dockerfile
Builds and runs the FastAPI app in a container:
- Installs dependencies from `requirments.txt`
- Exposes port 8000
- Runs the app with Uvicorn

---

## 🛠️ Local Development (Optional)

If you want to run the app locally (without Docker):

1. Clone the repository:
   ```bash
   git clone https://github.com/Chandrakant-Majumdar/JWT_Dockerize_fastAPI_CRUD_Excercise
   cd fastAPI_CRUD_Excercise/JWT_Dockerize_fastAPI_CRUD_Excercise
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   # On Linux/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirments.txt
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   # or
   python main.py
   ```

---

## 👤 Author

Developed by **Chandrakant Majumdar**

---
