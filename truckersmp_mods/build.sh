pip3 install --no-cashe-dir -r requirements.txt


python3 manage.py collectstatic --noinput
python3 manage.py migrate