FROM python:3.10-slim

WORKDIR /app

COPY degree.py .
COPY test_degree.py .

RUN pip install pytest

CMD ["pytest", "-v"]
