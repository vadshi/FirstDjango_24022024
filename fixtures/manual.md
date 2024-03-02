### Выгрузить данные из БД
```
python manage.py dumpdata MainApp --indent 4 > ./fixtures/MainApp.json
```

### Загрузить данные в БД
```
python manage.py loaddata ./fixtures/MainApp.json
```