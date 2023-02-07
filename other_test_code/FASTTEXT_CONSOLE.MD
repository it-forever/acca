fasttext supervised


````
__label__parazite Эт самое
__label__parazite Это самое
__label__parazite Ну вот
__label__parazite Вот
__label__parazite Ну
__label__parazite Ээээ
__label__parazite эээ
__label__norma Любить
__label__norma Жить
__label__norma Творить
````

Обучаем модель

./fasttext supervised -input train.txt -output model

Создаем новый файл с словами

````
один
два
эт самое
````

Запускаем тест

./fasttext predict model.bin test.txt


Увеличиваем эпохи:

fasttext supervised -input train.txt -output model -epoch 100
fasttext supervised -input train.txt -output model -epoch 100



Проверяем работу

fasttext predict model.bin test.txt