FROM postgres:13.3
RUN apt update && apt install -y postgresql-plpython3-${PG_MAJOR}
RUN echo 'CREATE EXTENSION IF NOT EXISTS plpython3u;' > /docker-entrypoint-initdb.d/init-plpython.sql