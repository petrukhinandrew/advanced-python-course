FROM python:3.11

RUN apt-get update && apt-get install -y texlive-latex-base

RUN pip install --index-url https://test.pypi.org/simple/ --no-deps slatgen

ADD example.py app/example.py
ADD gen.sh app/gen.sh
WORKDIR app/
RUN chmod +x gen.sh

ENTRYPOINT ./gen.sh