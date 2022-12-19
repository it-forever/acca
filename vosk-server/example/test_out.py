#!/usr/bin/env python3

import asyncio
import websockets
import sys

async def run_test(uri):
    async with websockets.connect(uri) as websocket:

        proc = await asyncio.create_subprocess_exec(
                       'ffmpeg', '-nostdin', '-loglevel', 'quiet', '-i', sys.argv[1],
                       '-ar', '16000', '-ac', '1', '-f', 's16le', '-',
                       stdout=asyncio.subprocess.PIPE)

        await websocket.send('{ "config" : { "sample_rate" : 16000 } }')

        while True:
            data = await proc.stdout.read(8000)

            if len(data) == 0:
                break

            await websocket.send(data)
            print (await websocket.recv())

        await websocket.send('{"eof" : 1}')
        print (await websocket.recv())

        await proc.wait()

asyncio.run(run_test('ws://192.168.51.203:32532'))

# run python3 test_ffmpeg.py /home/user/test-audio.wav
#  python3 test_out.py /home/user/test-audio.wav | grep text
#   "text" : "так я записываю тестовую статью для определения речи текст и проверки грамматики"
#   "text" : "мы часто слышим утверждение о том что наши данные собираются обрабатываются в интеллектуальных системах"
#   "text" : "так могут использоваться полученные данные никто не знает при этом мы видим разные мнения действия кто-то начнёт сейчас скрывать и быть более сдержанным другие наоборот пытаются заявить о себе"
#   "text" : "мы постоянно находимся на тонкой грани между правильным и неправильным применением технологии в мир мы можем анализировать текст речи для улучшения качества жизни людей исправление дефектов произношения улучшение ораторских качеств"
#   "text" : "мы можем использовать записанные данные для возможности выявления предпочтений к различным товарам и услугам"
#   "text" : "но конечно возможности выявления стороны который выбирает пользователь на правильное или 