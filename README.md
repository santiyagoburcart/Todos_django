For install source in windows

install python3 and install git bash

open CMD and type command
"pip install virtualenv"
mkvirtualenv <name for environment>
source <name for environment>\scripts\activate
git clone https://github.com/santiyagoburcart/Todos_django.git
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 8000




and install in  ubuntu 
pip install virtualenv
virtualenv <name for environment>
source <name for environment>/bin/activate
git clone https://github.com/santiyagoburcart/Todos_django.git
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 8000