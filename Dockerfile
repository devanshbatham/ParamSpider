### Dockerfile
FROM python:3.8-alpine
RUN apk update && apk upgrade && \
    apk add --no-cache bash git

RUN git clone https://github.com/devanshbatham/ParamSpider
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r ParamSpider/requirements.txt

ENTRYPOINT ["python", "ParamSpider/paramspider.py", "--domain", "hackerone.com"]