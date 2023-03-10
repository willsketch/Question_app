FROM python:3.9.16
COPY api /api
COPY app /app
COPY out /out
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "api.main:app" "--host=0.0.0.0"]
