FROM postgres:13.3
RUN apt update && apt install python3 python3-pip postgresql-plpython3-${PG_MAJOR} -y
RUN echo 'CREATE EXTENSION IF NOT EXISTS plpython3u;' > /docker-entrypoint-initdb.d/00-py3.sql
COPY freq_city.sql /docker-entrypoint-initdb.d/99-freq_city.sql