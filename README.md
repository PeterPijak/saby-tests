<h2>UI Автотесты на Python с применением фреймворка Pytest и Selenium</h2>

> **Статус проекта:**
> Публичный проект: https://saby.ru/
> 
> 🟢 Поддерживается (активный) 

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Selenium

## Тест-кейсы, которые автоматизировали
* Авторизация на saby.ru
* Пртоверка кнопок для авторизации 
* Проверка ячеек логина и пароля

## Детали реализации

1. Опции браузера вынесены в отдельные фикстуры `homepage.py` и `login_page.py`
2. Отчет по тестам реализован в отдельном ini файле `pytetst.ini`

## Локальный запуск тестов (из терминала)
1. Скачать проект
2. Перейти через терминал в директорию проекта
3. Выполнить команды:

Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

4. Устанавливаем фреймворки

``` markdown
python3 -m pip3 install selenium
```

``` markdown
python3 -m pip3 install pytest
```

5. Запускаем
``` markdown
pytest tests/test_homepage.py
pytest tests/test_login.py
```
6. Запускаем отчет по тестам с помощью bash
``` markdown
pytest
```

## Ожидаемый результат
Получаем отчет о прохождении тестов.

## Автор

 Gulamov Peter([@PetyaPijack](https://t.me/PetyaPijack))
