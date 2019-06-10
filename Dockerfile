FROM python:3

ADD doorControll.py /

RUN pip install requests
RUN pip install threading

CMD [ "python", "./doorControll.py" ]