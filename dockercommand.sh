docker run -it --name data-management --rm --network data-management-nw -v C:\Users\vivek\Research\data\retail_db_json:/retail_db_json -e BASE_DIR=/retail_db_json -e DB_HOST=a4c9cde62db3 -e DB_PORT=5432 -e DB_NAME=retail_db -e DB_USER=retail_user -e DB_PASS=anuragpostgres data-management python /data-management/app/app.py departments,categories