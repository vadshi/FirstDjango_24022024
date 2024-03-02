# FirstDjango_24022024
## Инструкция по развертыванию проекта

```
python3 -m venv django_venv
source django_venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## Дополнительно
1. Полезное дополнение для шаблонов Django, автор Baptiste Darthenay
```
ext install batisteo.vscode-django
```
Добавить в `settings.json`:
```
"emmet.includeLanguages": {
      "django-html": "html",
    },
    "files.associations": {
      "*.html": "django-html"
    },
```
