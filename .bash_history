cd /app && apt install nano git --yes && pip3 install -e git+https://github.com/django-oscar/django-oscar.git@151dc05395865ec0f51cdd45be9970a1bbea2f0c#egg=django-oscar
./manage.py 
./manage.py show_urls
./manage.py shell_plus
./manage.py runserver 0.0.0.0:8000
