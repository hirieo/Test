docker-compose exec cockroachdb cockroach sql --insecure -e "create database superset; create user superset_user; grant all on database superset to superset_user;"
docker-compose exec superset superset db upgrade
docker-compose exec superset superset fab create-admin --username admin --firstname Superset --lastname Admin --email admin@superset.com --password admin
docker-compose exec superset superset init