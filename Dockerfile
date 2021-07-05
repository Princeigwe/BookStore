FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system
#COPY requirements.txt /code/
#RUN pip install -r requirements.txt

COPY . /code/
