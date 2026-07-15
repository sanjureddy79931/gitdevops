FROM python:3.13.12

WORKDIR /newapp

COPY add.py sub.py numbers.csv calc.sh mul.py div.py .

RUN chmod +x calc.sh

ENTRYPOINT ["./calc.sh"]
