FROM python:3

ADD doorControll.py /

RUN python3 -m pip install requests

CMD [ "python", "./doorControll.py" ]