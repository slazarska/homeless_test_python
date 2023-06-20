# UI автотесты для сайта проекта [Ночлежка](https://homeless.ru//)
![image](homeless_test_python/resources/img/screenshots/homeless_mainpage.png)

## Содержание:
- [Technology Stack](#автотесты-написаны-с-использованием)
- [О проекте](#о-проекте)
- [Список проверок, реализованных в автотестах:](#список-проверок-реализованных-в-автотстах)
- Запуск тестов:
  - [Jenkins](#удаленный-запуск-через-jenkins)
  - [Локально](#запуск-тестов-локально)
- Интеграции и отчетность:
  - [Allure Report](#allure-report-подключен-для-формирования-отчетов-о-прохождении-тестов)
  - [Allure TestOps](#allure-testOps-используется-в-качестве-Тест-Менеджмент-системы)
  - [Jira](#настроена-интеграция-TestOps-с-Jira)
  - [Telegram](#настроено-автоматическое-оповещение-о-результатах-удаленного-запуска-тестов-в-Telegram-чат)
- [Video](#пример-записи-экрана-при-прохождения-теста)


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

## О проекте:

- [x] Паттерны `Page Object` и `Application Manager`
- [x] Self-documenting code
- [x] Параметризация
- [x] Запуск тестов с использованием Jenkins и Selenoid
- [x] `Allure Reports` с приложением логов, скриншотов, записей экрана
- [x] Интеграция с `Allure TestOps`
- [x] Интеграция с `Jira`
- [x] Отправка результатов тестовых прогонов в `Telegram`

## Список проверок, реализованных в автотестах:

- [X] - Открытие главной страницы сайта
- [X] - Переход на страницу пожертвований с главной страницы
- [X] - Дефолтное состояние страницы пожертвований
- [X] - Проверка возможностей выбора различных форм и сумм пожертвований
- [X] - Проверка заполнения полей в форме для отправки пожертвований

## Удаленный запуск через [Jenkins](https://jenkins.autotests.cloud/job/Students/job/slazarska-py-diplom-ui/):

Для запуска тестов из Jenkins:
1. Нажмите кнопку "Собрать сейчас"

![image](homeless_test_python/resources/img/screenshots/jenkins_run.png)

## Запуск тестов локально:

1. Склонируйте репозиторий
2. Установите Poetry (`poetry install`)
3. Откройте проект в PyCharm, установите Python Interpreter
4. Создайте .env файл в папке проекта по образцу (sample)
5. Запустите тесты в PyCharm или в командной строке:
```bash
pytest . --alluredir allure-results/
```

## Allure Report подключен для формирования отчетов о прохождении тестов:
![image](homeless_test_python/resources/img/screenshots/allure_report_2.png)
![image](homeless_test_python/resources/img/screenshots/allure_report_1.png)
<br />
<br />
> Для получения отчета в Allure Report при локальном запуске введите в командной строке:
```bash
allure serve .\allure-results
```

## Allure TestOps используется в качестве Тест Менеджмент системы:
![image](homeless_test_python/resources/img/screenshots/testops_1.png)
![image](homeless_test_python/resources/img/screenshots/testops_0.png)
<br />
<br />
## Настроена интеграция TestOps с Jira:
![image](homeless_test_python/resources/img/screenshots/jira.png)
<br /> 
<br />
## Настроено автоматическое оповещение о результатах удаленного запуска тестов в Telegram-чат:
![image](homeless_test_python/resources/img/screenshots/bot.png)
<br />
<br />
## Пример записи экрана при прохождения теста:
![video](homeless_test_python/resources/img/screenshots/video.gif)
<br><br>

Благодарности :pray:<br/>
:green_heart: <a target="_blank" href="https://qa.guru">qa.guru</a><br/>
:purple_heart: <a target="_blank" href="https://sites.google.com/view/qasisters/">QA sisters</a><br/>