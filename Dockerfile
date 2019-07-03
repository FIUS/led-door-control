FROM python:3-alpine

ADD doorControll.py /

RUN python3 -m pip install requests

CMD [ "python -u", "./doorControll.py" ]
