FROM python:3

ADD doorControll.py /

RUN python3 -m pip install requests
RUN python3 -m pip install threading

CMD [ "python", "./doorControll.py" ]