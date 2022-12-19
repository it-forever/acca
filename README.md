# acca
Проект по аналитике аудиосодержимого. Краткое содержание смотрите в статье https://habr.com/ru/post/667824/ к январю 2023 здесь будут схемы, документация и работающий код с моделями.

- [Тесты с примерами](./test_code_for_analytics/) - Тут находится тестовый код с примерами запуска и проблемами, которые могут возникнуть при эксплуатации

- [упаковка fasttext](./test_code_for_analytics/fasttext/) - Запуск и использование fasttext используя flask. Неудачный эксперимент, лучше использовать готовый deeppavlov. Исходный код проекта https://github.com/facebookresearch/fastText

- [vosk-server](./vosk-server/) -  чарт для запуска vosk-server, который работает в качестве websocket, в случае kubernetes по факту используется service. Node_port включен для проведения тестов запуска за пределами среды kubernetes. код проекта https://github.com/alphacep/vosk-server

