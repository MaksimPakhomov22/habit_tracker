## <a id="title1">Трекер полезных привычек</a>
Для корректной работы необходимо:
-----------------------------------------

- Установить виртуальное окружение ```venv```:
```shell
python3 -m venv venv
```
- Запустить вирутальное окружение:
```shell
source venv/bin/activate
```
- Установить необходимые зависимости из файла ```requirements.txt```:
```shell
- pip install -r requirements.txt
```
- Создайте файл ```.env``` и внесите в него все данные по образцу из файла ```.env.sample```.
- Запустите миграции:
```shell
python manage.py migrate
```
- Создайте ```cуперпользователя```:
```shell
python manage.py csu
```
- Установить и запустите ```redis```.
- Запустить проект
- В виртуальном окружении проекта запустить celery worker командой:
```shell
celery -A config worker -l INFO
```
- В виртуальном окружении проекта запустить celery beat командой:
```shell
celery -A config beat -l info -S django
```

Логика работы системы
---------------------
Пользователь создает себе список полезных привычек. За каждую полезную привычку необходимо себя вознаграждать или сразу
после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше 2 минут.
Создание места и действия для привычки реализованы отдельными эндпоинтами.
После создания новой привычки, если привычка не является приятной, автоматически создается периодическая задача, которая
отправляет уведомление на телеграм бота с периодичностью выполнения привычки (по
умолчанию каждый день) в формате "Я буду <ДЕЙСТВИЕ> в <ВРЕМЯ> в <МЕСТО>". Время указывается соответствующее времени
создания привычки.

Валидация
---------

- Исключен одновременный выбор связанной привычки и указания вознаграждения.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

Права доступа
-------------

- Ко всем действиям имеет доступ только авторизованный пользователь.
- К получению, изменению и удалению привычки имеет доступ только персонал или создатель привычки.
- К получению списка всех публичных привычек имеют доступ все авторизованные пользователи.
