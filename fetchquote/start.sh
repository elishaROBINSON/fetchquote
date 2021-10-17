cd /code/fetchquote
python /code/fetchquote/manage.py migrate --noinput
python /code/fetchquote/manage.py runserver 0.0.0.0:8000 &
celery -A fetchquote beat  -l info