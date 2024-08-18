FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN python -m pip install sphinx
RUN pip install sphinx-rtd-theme

EXPOSE 5000

CMD ["python3","run.py"]
