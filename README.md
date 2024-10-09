# Evaluation Metrics

## Setup Instructions

Follow these steps to set up the project on your local machine:

### 1. Create a Virtual Environment

First, create a virtual environment to isolate the project dependencies. You can do this using `python -m venv`:

```bash
# On Windows

```
python -m venv venv
```

# On macOS/Linux
python3 -m venv venv


# Project Setup Instructions

### 2. Install Dependencies

Use the following command to install the required packages from `requirements.txt`:

```
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project directory and add your `GROQ_API_KEY`:

```
GROQ_API_KEY="....API...KEY..."
```

Make sure to replace `....API...KEY...` with your actual API key.

### 4. Run the Evaluation Test

Run the test script `test_rag.py` using the `deepeval` command:

```
deepeval test run test_rag.py
```
