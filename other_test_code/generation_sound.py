import gtts
from playsound import playsound
tts = gtts.gTTS("Простой тест синтеза речи",lang="ru")

tts.save("./test.mp3")
