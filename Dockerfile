FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --trusted-host pypi.python.org --no-cache-dir

COPY app/ .

ENV MONGO_URI mongodb+srv://userReadOnly:7ZT817O8ejDfhnBM@minichallenge.q4nve1r.mongodb.net/
ENV API_PORT 8080

EXPOSE 8080
RUN ls
ENTRYPOINT [ "python", "app.py" ]