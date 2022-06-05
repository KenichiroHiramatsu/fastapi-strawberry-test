FROM tiangolo/uvicorn-gunicorn:python3.8

COPY requirements.txt /tmp/requirements.txt

# RUN python3 -m venv .venv
# RUN source .venv/bin/activate

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY main.py .
COPY ./app /app
