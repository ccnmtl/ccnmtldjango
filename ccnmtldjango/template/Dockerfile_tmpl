FROM ccnmtl/django.base
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# install node stuff
COPY package.json /node/
RUN cd /node && npm install && touch /node/node_modules/sentinal

# build virtualenv and run tests
ADD wheelhouse /wheelhouse
RUN /ve/bin/pip install --no-index -f /wheelhouse -r /wheelhouse/requirements.txt \
    && rm -rf /wheelhouse && touch /ve/sentinal
WORKDIR /app
COPY . /app/
RUN VE=/ve/ MANAGE="/ve/bin/python manage.py" NODE_MODULES=/node/node_modules/ make

EXPOSE 8000
ADD docker-run.sh /run.sh
ENV APP ${package}
ENTRYPOINT ["/run.sh"]
CMD ["run"]
