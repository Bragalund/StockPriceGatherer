FROM alpine:latest

ENV RUNTIME_PACKAGES python3 py3-pip libxslt libxml2 git curl libpq
ENV BUILD_PACKAGES build-base libxslt-dev libxml2-dev libffi-dev python3-dev openssl-dev postgresql-dev

ENV PYTHONUNBUFFERED=1

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

RUN apk add --no-cache ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
  pip install git+https://github.com/scrapy/scrapy.git \
              git+https://github.com/scrapy/scrapyd.git \
              git+https://github.com/scrapy/scrapyd-client.git \
              git+https://github.com/scrapinghub/scrapy-splash.git \
              simplejson \
              psycopg2 && \
  curl -sSL https://github.com/scrapy/scrapy/raw/master/extras/scrapy_bash_completion >> /root/.bashrc && \
  apk del ${BUILD_PACKAGES} && \
  rm -rf /root/.cache

ADD ./scrapyd.conf /etc/scrapyd/
ADD ./scrapyd.conf scrapyd.conf
ADD ./scrapyd.conf ~/.scrapyd.conf

# EXPOSE 6800

CMD ["scrapyd"]