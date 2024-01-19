FROM python:3

WORKDIR /app

RUN apt-get update
RUN apt-get install -y \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./geckodriver

CMD [ "python", "-u", "./main.py" ]