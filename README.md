# Evaluation Metrics Project

## Overview

The Evaluation Metrics Project is a tool designed to assess and analyze various metrics using the Groq API and DeepEval framework. This project aims to provide insights into [specific metrics or goals of your project].

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- pip (Python package installer)
- A Groq API key

## Installation

Follow these steps to set up the Evaluation Metrics Project:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/evaluation-metrics.git
   cd evaluation-metrics
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## Configuration

1. Create a `.env` file in the project root directory.

2. Add your Groq API key to the `.env` file:
   ```
   GROQ_API_KEY="your_actual_api_key_here"
   ```

3. Replace `your_actual_api_key_here` with your actual Groq API key.

## Testing

To run the evaluation tests:

```bash
deepeval test run test_rag.py
```
