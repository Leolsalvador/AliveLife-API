FROM python:3.10

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["sh", "/entrypoint.sh"]
