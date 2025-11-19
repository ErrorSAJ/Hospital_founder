virtualenv venv 
venv\Scripts\activate
pip install -r requirment.txt
py manage.py migrate 
py manage.py runserver