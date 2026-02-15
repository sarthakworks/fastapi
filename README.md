# FastAPI Project

A FastAPI-based web application.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Setup Instructions (New System)

Follow these steps to set up and run the project on a new system:

### 1. Clone the Repository (if applicable)

```bash
git clone <your-repo-url>
cd fastapi
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install fastapi uvicorn
```

### 5. Run the Application

```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

### 6. Access API Documentation

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## Available Endpoints

- `GET /` - Root endpoint (Hello World)
- `GET /health` - Health check endpoint

## Development

- The `--reload` flag enables auto-reload on code changes
- Deactivate virtual environment: `deactivate`

## Troubleshooting

- **Command not found:** Ensure Python is installed and in your PATH
- **Permission denied:** On macOS/Linux, you may need to use `python3` instead of `python`
- **Module not found:** Make sure virtual environment is activated and dependencies are installed