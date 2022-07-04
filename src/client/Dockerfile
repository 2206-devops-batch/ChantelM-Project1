FROM python:3.8.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN export FLASK_APP=app
RUN export FLASK_ENV=production

COPY . .

EXPOSE 5000

# CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["flask", "run", "--host=0.0.0.0"]