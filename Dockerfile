FROM python:3.9
COPY ./ /code/AiAlira/.
WORKDIR /code/backend/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt