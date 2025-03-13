FROM python:3.9

# Choose a UID and GID (e.g., 1001)
ARG APP_UID=1001
ARG APP_GID=1001

RUN groupadd -r --gid $APP_GID appgroup && useradd -r -u $APP_UID -g appgroup appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser:appgroup /app

USER appuser

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["python", "app.py"]
