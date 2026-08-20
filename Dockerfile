FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY task_manager.py .
COPY test_task_manager.py .

RUN python -m pytest

CMD ["python", "task_manager.py"]