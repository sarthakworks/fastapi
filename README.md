# FastAPI Project

A FastAPI-based web application.

## Project Structure

The application is organized using FastAPI's router system for better code organization:

```
fastapi/
├── main.py              # Application entry point, includes routers
├── routes_get.py        # All GET endpoints (/, /greet, /hello, /weather)
├── routes_post.py       # All POST endpoints (/person)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

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
pip install fastapi uvicorn httpx
```

### 5. Run the Application

**Option 1: Using python directly**
```bash
python main.py
```

**Option 2: Using uvicorn with auto-reload**
```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

### 6. Access API Documentation

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

## Available Endpoints

### GET Endpoints

- `GET /` - Root endpoint (Hello World)
- `GET /greet?first_name={name}&last_name={name}` - Greet with query parameters
  - Example: `http://127.0.0.1:8000/greet?first_name=Sarthak&last_name=Bansal`
- `GET /hello/{fname}/{lname}` - Greet with path parameters
  - Example: `http://127.0.0.1:8000/hello/Sarthak/Bansal`
- `GET /weather?city={city_name}` - Get current weather for a city (uses free Open-Meteo API)
  - Example: `http://127.0.0.1:8000/weather?city=Delhi`
  - Example: `http://127.0.0.1:8000/weather?city=London`
  - Returns: temperature, wind speed, weather code, and timestamp

### POST Endpoints

- `POST /person` - Add a person with JSON body
  - Request Body:
    ```json
    {
      "fname": "Sarthak",
      "lname": "Bansal",
      "age": 25
    }
    ```

## Testing POST Requests in Browser

The easiest way to test POST requests is using FastAPI's built-in **interactive API documentation**:

### Method 1: Swagger UI (Recommended)

1. Start your FastAPI application
2. Open your browser and navigate to: `http://127.0.0.1:8000/docs`
3. Find the **POST /person** endpoint in the list
4. Click on it to expand
5. Click the **"Try it out"** button
6. Enter your JSON data in the request body field:
   ```json
   {
     "fname": "Sarthak",
     "lname": "Bansal",
     "age": 25
   }
   ```
7. Click **"Execute"** to send the request
8. View the response below

### Method 2: Browser Console (JavaScript)

Open your browser's Developer Console (Press F12) and run:

```javascript
fetch('http://127.0.0.1:8000/person', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    fname: 'Sarthak',
    lname: 'Bansal',
    age: 25
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## Development

- The `--reload` flag enables auto-reload on code changes
- Deactivate virtual environment: `deactivate`

## Troubleshooting

- **Command not found:** Ensure Python is installed and in your PATH
- **Permission denied:** On macOS/Linux, you may need to use `python3` instead of `python`
- **Module not found:** Make sure virtual environment is activated and dependencies are installed