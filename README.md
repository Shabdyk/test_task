1. Автоматизация была реализована в файле [polls/views.py](https://github.com/Shabdyk/test_task/blob/fixture/mysite/polls/views.py) в виде функции data_fixture(). 
   Но функция работает не совсем корректно, так как не воспринимает вложенные данные.
   Как альтернатива в [polls/models.py](https://github.com/Shabdyk/test_task/blob/fixture/mysite/polls/models.py) были созданы модели JSONField, которые забирают эти вложенные данные в виде json-данных.
   
   Попытка довести функцию data_fixture() до ума предпринималась в ветке "fixture_try" в файле [blogs/views.py](https://github.com/Shabdyk/test_task/blob/fixture_try/mysite2/blogs/views.py).
   Удалось отформатировать вводные данные для функции deserialize(), но вылезла ошибка о несоответствии ForeignKey с имеющимися вводными данными.
   И данные с моделями [blogs/models.py](https://github.com/Shabdyk/test_task/blob/fixture_try/mysite2/blogs/models.py) в соответстие привести не удалось.

2. Таблица отобразится при запуске сервера сайта mysite в ветке fixture и при переходе на http://127.0.0.1:8000/ или [по скриншоту](https://lh6.googleusercontent.com/xRxwVmaVVoiU-J7eWO50Uo3FkRQPDeTe2IY0U0E7vz5Wd9qsUNphh6IOsLPTk9_JPmqEoWjUJsZqWQ7ic4Do=w1366-h695)

3. Также фильтрацию по имени пользователя можно увидеть аналогичным образом. Исходный код (фильтрация) находится в [polls/views.py](https://github.com/Shabdyk/test_task/blob/fixture/mysite/polls/views.py) и 
в [polls/forms.py](https://github.com/Shabdyk/test_task/blob/fixture/mysite/polls/forms.py).



P.S.: не успел закомментировать код, так как пытался всё же "добить" data_fixture() из первого задания.
