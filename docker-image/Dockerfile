FROM alpine:3.6

ENV FLASK_APP=catalog
ENV FLASK_DEBUG=true
ENV PYTHONPATH=/udacity/

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
    ca-certificates \
  && pip install \
     sqlalchemy \
     flask \
  && rm -rf /var/cache/apk/*

RUN mkdir -p /udacity/catalog/

WORKDIR /udacity

COPY resources/setup.py .
COPY resources/catalog/ catalog/

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]