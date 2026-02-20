FROM eclipse-temurin:8-jdk

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN rm -f /usr/bin/python /usr/bin/pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

WORKDIR /app

COPY requirements.txt .

RUN pip --no-cache-dir install --break-system-packages -r requirements.txt

COPY . .

CMD ["python", "main.py"]
