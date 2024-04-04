FROM python:3.11

WORKDIR /Assigment

COPY . /Assigment/

RUN pip install -r/Assigment/requirements.txt

RUN python train.py

CMD ["python", "test.py"]