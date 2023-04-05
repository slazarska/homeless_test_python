# UI автотесты для сайта проекта [Ночлежка](https://homeless.ru//)
![image](homeless_test_python/resources/img/homeless_mainpage.png)

## :open_book: Содержание:
- [Technology Stack](#автотесты-написаны-с-использованием)
- [Кратко о проекте](#in-a-nutshell-about-the-project)
- [Checks are implemented](#heavy_check_mark-checks-are-implemented)
- Tests launch:
  - [Jenkins](#-remote-launch-via-jenkins])
  - [Local](#computer-local-launch )
- Reporst:
  - [Allure](#bar_chart-test-reports-available-in-allure)
  - [BrowserStack](#-browserstack)
  - [Telegram](#-telegram)
- [Allure TestOps](#briefcase-intergation-with-allure-testops)
- [Video](#movie_camera-test-run-video-example)


## Автотесты написаны с использованием:
<div>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/python.png" title="Python" alt="Python" width="40" height="40"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/pycharm.png" title="PyCharm" alt="PyCharm" width="40" height="40"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/pytest.png" title="Pytest" alt="Pytest" width="40" height="40"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/selene.png" title="Selene" alt="Selene" width="40" height="40"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/Jenkins.png" title="Jenkins" alt="Jenkins"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/selenoid.png" title="Selenoid" alt="Selenoid" width="40" height="40"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/Allure_Report.png" title="Allure Report" alt="Allure Report"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/AllureTestOps.png" title="AllureTestOps" alt="AllureTestOps"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/Jira.png" title="Jira" alt="Jira" width="40" height="40"/>
<img src="https://github.com/slazarska/homeless_test_python/blob/main/homeless_test_python/resources/img/icons/Telegram.png" title="Telegram" alt="Telegram"/>
</div>

## Кратко о проекте:
- [x] Паттерны `Page Object` и `Application Manager`
- [x] Self-documenting code
- [x] Параметризация
- [x] Удаленный запуск тестов, используя Jenkins и Selenoid
- [x] `Allure Reports` с приложением тест артефактов: логи, скриншоты, запись экрана
- [x] Интеграция с `Allure TestOps`
- [x] Интеграция с `Jira`
- [x] Отправка результатов тестовых прогонов в `Telegram`

## Список проверок, реализованных в автотестах:

- [X] - Открытие главной страницы сайта
- [X] - Переход на страницу пожертвований с главной страницы
- [X] - Дефолтное состояние страницы пожертвований
- [X] - Проверка возможностей выбора различных форм и сумм пожертвований
- [X] - Проверка заполнения полей в форме для отправки пожертвований

## Удаленный запуск через [Jenkins](https://jenkins.autotests.cloud/job/slazarska-py-diplom-ui/):

Для запуска тестов из Jenkins:
1. Нажмите кнопку "Собрать сейчас"

## Запуск тестов локально:

1. Склонируйте репозиторий
2. Установите Poetry (`poetry install`)
3. Откройте проект в PyCharm, установите Python Interpreter
4. Создайте .env файл в папке проекта по образцу (sample)
5. Запустите тесты в PyCharm или в командной строке:
```bash
pytest . --alluredir allure-results/
```

## Пример видеозаписи прохождения теста:
![video]()
<br><br>
## Скриншоты:
#### *Selenoid используется для реализации протокола Selenium.::*
![image]()
<br />
<br />
#### *Jenkins используется в качестве CI системы*
![image]()
<br /> 
<br />
#### *Allure Reports подключен для формирования отчетов о прохождении тестов:*
![image]()
![image]()
<br />
<br />
#### *Allure TestOps используется в качестве Тест Менеджмент системы:*
![image]()
![image]()
![image]()
<br />
<br />
#### *Настроена интеграция Test Ops с Jira:*
![image]()
<br /> 
<br />
#### *Настроено автоматическое оповещение о результатах запуска тестов в Jenkins в Telegram-чат с помощью бота:*
![image]()
<br />
<br />

Благодарности :pray:<br/>
:green_heart: <a target="_blank" href="https://qa.guru">qa.guru</a><br/>
:purple_heart: <a target="_blank" href="https://sites.google.com/view/qasisters/">QA sisters</a><br/>