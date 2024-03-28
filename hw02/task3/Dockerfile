FROM python:3.11

RUN apt-get update && apt-get install -y texlive-latex-base

RUN pip install -U --index-url https://test.pypi.org/simple/ --no-deps slatgen==0.2.0

ADD example.py app/example.py
ADD assets/example.jpeg app/assets/example.jpeg
ADD gen.sh app/gen.sh
WORKDIR app/
RUN chmod +x gen.sh

ENTRYPOINT ./gen.sh