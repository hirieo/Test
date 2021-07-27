FROM apache/superset:latest

USER root
RUN pip install cockroachdb psycopg2-binary sqlalchemy-cockroachdb

# Switching back to using the `superset` user
USER superset