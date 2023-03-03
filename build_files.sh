# build the project
# pip install -r requirements.txt
pip -m pip install -r requirements.txt

# Make migration
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

# Collect static
python3.9 manage.py collectstatic --noinput --clear