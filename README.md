# acca
Проект по аналитике аудиосодержимого. Краткое содержание смотрите в статье https://habr.com/ru/post/667824/ к январю 2023 здесь будут схемы, документация и работающий код с моделями.

- [Тесты с примерами](./test_code_for_analytics/) - Тут находится тестовый код с примерами запуска и проблемами, которые могут возникнуть при эксплуатации

- [упаковка fasttext](./test_code_for_analytics/fasttext/) - Запуск и использование fasttext используя flask. Неудачный эксперимент, лучше использовать готовый deeppavlov. Исходный код проекта https://github.com/facebookresearch/fastText

- [vosk-server](./vosk-server/) -  чарт для запуска vosk-server, который работает в качестве websocket, в случае kubernetes по факту используется service. Node_port включен для проведения тестов запуска за пределами среды kubernetes. код проекта https://github.com/alphacep/vosk-server

        Собраны следующие образы:

        - itforever/vosk-server-small:0.22  - мобильный датасет при запуске потребляет 150 мб
        
        - itforever/vosk-server:0.0-ru - 0.10 модель, лучше использовать более новую.

        - itforever/vosk-server:0.22 - 0.22 модель, потребляет 4,1 Гб озу, при нагрузке +10% идет прирост. 2 часовой подкаст транскибировала 1 час (задействовалось ровно 1 ядро процессора).

- [deeppavlov](./test_code_for_analytics/deeppavlov/) - сборки deeppavlov:

        - [автокорректор](./test_code_for_analytics/deeppavlov/docker/levenshtein_corrector_ru/) - требуется наличие 5 гб озу для работы приложения

        Пример работы tf-idf:

        

        - [автокорректор](./test_code_for_analytics/deeppavlov/docker/tf-idf/) - требуется наличие 5 гб озу для работы приложения.

        Пример работы корректора:

        ````
        curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\"Гвазди\",\"таршер\"]}"

        [["гвозди"],["торшер"]]
        ````

- [natasha](./test_code_for_analytics/natasha/slovnet/) - это библиотека Python для моделирования НЛП на основе глубокого обучения для русского языка. Можно запускать в виде контейнеров. Сборка тривиальна.

- ``whisper`` (https://github.com/openai/whisper) - показал хороший результат, но затратный по ресурсам. На модели medium расшифровка 2х часовой аудиозаписи, занимает 50 минут, но расставляет знаки пунктуации. Сравнение с vosk ознакомьтесь с статьей https://alphacephei.com/nsh/2023/01/15/whisper-finetuning.html





