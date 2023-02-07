history | grep curl
 1007  curl -X POST -H 'Content-Type: application/json'      --data "[\"Which baking dish is best to bake a banana bread?\", \"Why not put knives in the dishwasher?\"]"      'http://localhost:8000/predict'
 1017  curl http://fasttext-serving.it-forever.ru/health
 1018  curl -X POST -H 'Content-Type: application/json'      --data "[\"Which baking dish is best to bake a banana bread?\", \"Why not put knives in the dishwasher?\"]"      'http://172.17.0.3:8000/predict'
 1019  curl -X POST -H 'Content-Type: application/json'      --data "[\"Молоток гвозди?\", \"Пойдем гулять?\"]"      'http://172.17.0.3:8000/predict'
 1020  curl -X POST -H 'Content-Type: application/json'      --data "[\"Молоток гвозди?\", \"Пойдем гулять?\"]"      'http://172.17.0.3:8000/predictions'
 1021  curl -X POST -H 'Content-Type: application/json'      --data "["Пойдем гулять?"]"      'http://172.17.0.3:8000/predict'
 1022  curl -X POST -H 'Content-Type: application/json'      --data "[\"Молоток гвозди?\", \"Пойдем?\"]"      'http://172.17.0.3:8000/representations'
 1135  curl "https://api.nlpcloud.io/v1/en_core_web_lg/entities" -H "Authorization: Token " -H "Content-Type: application/json" -X POST -d '{"text":"John Doe has been working for Microsoft in Seattle since 1999."}'
 1136  curl "https://api.nlpcloud.io/v1/ru_core_web_lg/entities" -H "Authorization: Token " -H "Content-Type: application/json" -X POST -d '{"text":"Алексей молодец или нет?"}'
 1140  curl -X POST -H 'Content-Type: application/json'      --data "[\"Тест гвозди?\", \"Пойдем?\"]"      'http://192.168.50.102:5005/model'
 1191  curl -X POST -H 'Content-Type: application/json'      --data "[\"Молоток гвозди?\", \"Пойдем?\"]"      'http://127.0.0.1:8080'
 1192  curl -X POST -H 'Content-Type: application/json'      --data "Тестовое предложение"      'http://127.0.0.1:8080'
 1193  curl -X POST -H 'Content-Type: application/json'      --data "{Тестовое предложение}"      'http://127.0.0.1:8080'
 1194  curl -X POST -H 'Content-Type: application/json'      --data "[\"Молоток гвозди?\"]"      'http://127.0.0.1:8080'
 1195  curl -X POST -H 'Content-Type: application/json'      --data "[\"Hello\"]"      'http://127.0.0.1:8080'
 1196  curl -X POST -H 'Content-Type: application/json'      --data "[\"Молоток гвозди?\"]"      'http://127.0.0.1:8080'
 1197  curl -X POST -H 'Content-Type: application/json'      --data "[\"Hello\"]"      'http://127.0.0.1:8080'
 1198  curl -X POST -H 'Content-Type: application/json'      --data "[\"Молоток\"]"      'http://127.0.0.1:8080'
 1199  curl https://speller.yandex.net/services/spellservice.json/checkText?text=синхрафазатрон+в+дубне
 1209  curl -X POST -H 'Content-Type: application/json'      --data "[\"Тест гвозди?\", \"Пойдем?\"]"      'http://192.168.50.102:5005/model'
 1349  curl http://httpbin.org/get
 1352  curl http://slovnet-morph.it-forever.ru/
 1513  curl -X POST -H 'Content-Type: application/json'      --data "[\"Молоток\"]"      'http://127.0.0.1:8080'
 1673  curl -X POST    -H "Authorization: Bearer "    --data-binary "@/home/atkachenko/Yandex.Disk/SIBSAU/My_project/test_audio/zaika1.ogg"    "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?folderId=b1gsmuql7j7dnha9krfq&lang=ru-RU"
 1692  curl -L --request POST     --url https://voice.mcs.mail.ru/asr     --header 'Authorization: Bearer ARNwprvy2mkZUpd9s95SVUVkbkJcztMK9wbdhLx9r71Fv1zKu'     --header 'Content-Type: audio/wave'     --data-binary '/home/atkachenko/Yandex.Disk/SIBSAU/My_project/test_audio/zaika1.wav'
 1694  curl -L --request POST     --url https://voice.mcs.mail.ru/asr     --header 'Authorization: Bearer ARNwprvy2mkZUpd9s95SVUVkbkJcztMK9wbdhLx9r71Fv1zKu'     --header 'Content-Type: audio/wave'     --data-binary '@zaika1.wav'
 1696  curl -X POST -H 'Content-Type: application/json'      --data "[\"Тест гвозди?\", \"Пойдем?\"]"      'http://fasttext-serving.it-forever.ru/representations'
 1697  curl -X POST -H 'Content-Type: application/json'      --data "[\"Пойдем?\"]"      'http://fasttext-serving.it-forever.ru/predictions'
 1698  curl -X POST -H 'Content-Type: application/json'      --data "[\"Тест гвозди?\", \"Пойдем?\"]"      'http://fasttext-serving.it-forever.ru/representations'
 1700  curl -X POST -H 'Content-Type: application/json'      --data "x:[харошо]"      'https://corrector.it-forever.ru/model'
 1701  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\"Гвазди\"]}"
 1702  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\"Гвазди\",\"малатак\"]}"
 1703  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\"Гвазди\",\"лоппа\"]}"
 1704  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\"Гвазди\",\"лопа\"]}"
 1705  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\"Гвазди\",\"таршер\"]}"
 1706  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\"Гвазди\ и таршер\"]}"
 1707  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":["Гвазди и таршер"]}"
 1708  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{"x":["Гвазди и таршер"]}"
 1709  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d {"x":["Гвазди и таршер"]}
 1710  curl -X POST "http://corrector.it-forever.ru/model" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"x\":[\"Гвазди\",\"таршер\"]}"
 2001  history | grep curl

curl -X POST "http://slovnet-syntax.it-forever.ru" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"head\":[\"Гвазди\"]}"

