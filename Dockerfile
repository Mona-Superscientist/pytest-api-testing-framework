FROM python:latest

RUN set -x \
    && apt-get update && \
    apt-get install -y \
    libfreetype6-dev \
    default-libmysqlclient-dev \
    clamav

RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["sh", "-c", "sleep 30 ; pytest"]

