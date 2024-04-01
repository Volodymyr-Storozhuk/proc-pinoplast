# pull official base image
FROM python:3.11-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create directory for the www user
RUN mkdir -p /home/www

# create the www user
RUN addgroup --system www && adduser --system --group www

# create the appropriate directories
ENV HOME=/home/www
ENV APP_HOME=/home/www/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
RUN apt-get update && \
    apt-get install -y gnupg2 curl && \
    apt-get install -y --no-install-recommends netcat

# Add Microsoft SQL Server driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev libgssapi-krb5-2

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt $APP_HOME
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R www:www $APP_HOME

# copy entrypoint.sh
# COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /home/www/web/entrypoint.sh
RUN chmod +x /home/www/web/entrypoint.sh

# change to the app user
USER www

# run entrypoint.sh
ENTRYPOINT ["/home/www/web/entrypoint.sh"]
