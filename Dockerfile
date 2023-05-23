FROM python:3.10.10
RUN pip install --upgrade pip  
ENV DOCKERHOME=/home/app/webapp  
ENV PYTHONUNBUFFERED=1
RUN mkdir -p $DOCKERHOME  
COPY . $DOCKERHOME  
WORKDIR $DOCKERHOME
RUN pip install -r requirements.txt  
EXPOSE 8000
ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]