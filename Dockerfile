FROM python:3.10.5-slim-bullseye
WORKDIR /docker

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy in the source code
COPY . .

CMD ["python3", "-m", "flask", "--app", "flask_api", "run","--host","0.0.0.0"]