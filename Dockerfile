#pull official python base image
FROM python:3.11.4-slim-buster

#Set working directory
WORKDIR /usr/src/StationService

#environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat

#install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/StationService/entrypoint.sh
RUN chmod +x /usr/src/StationService/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/StationService/entrypoint.sh"]


# COPY requirements.txt /code/
# RUN pip install -r requirements.txt

# EXPOSE 8000

# CMD ["gunicorn", "--chdir", "StationService", "--bind", ":8000", "StationService.wsgi:application"]