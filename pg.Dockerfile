FROM postgres:13.3
RUN apt update && apt install python3 python3-pip postgresql-plpython3-${PG_MAJOR} -y
COPY ./database.sql /docker-entrypoint-initdb.d/py3.sql
