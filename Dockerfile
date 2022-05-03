FROM python:3
COPY . /NotesApp
CMD python NotesApp/manage.py runserver