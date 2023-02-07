from vosk import Model, KaldiRecognizer
import wave
import json

'''
this script reads a mono wav file (inFileName) and writes out a json file (outfileResults) with the speech to text conversion results.  It then writes out another json file (outfileText) that only has the "text" values.
'''

inFileName = 'C:\\Users\\xxx\\pyenv\\NLP\\inputfiles\\COURSE\\M1S3-Mono.wav'
outfileResults = 'C:\\Users\\xxx\\pyenv\\NLP\\inputfiles\\COURSE\\M1S3-Results.json'
outfileText = 'C:\\Users\\xxx\\pyenv\\NLP\\inputfiles\\COURSE\\M1S3-Text.json'

wf = wave.open(inFileName, "rb")

# initialize a str to hold results
results = ""
textResults = []

# build the model and recognizer objects.
model = Model(r"C:\Users\xxx\pyenv\NLP\model")
recognizer = KaldiRecognizer(model, wf.getframerate())
recognizer.SetWords(True)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        recognizerResult = recognizer.Result()
        results = results + recognizerResult
        # convert the recognizerResult string into a dictionary  
        resultDict = json.loads(recognizerResult)
        # save the 'text' value from the dictionary into a list
        textResults.append(resultDict.get("text", ""))

##    else:
##        print(recognizer.PartialResult())
        
# process "final" result
results = results + recognizer.FinalResult()
resultDict = json.loads(recognizer.FinalResult())
textResults.append(resultDict.get("text", ""))

# write results to a file
with open(outfileResults, 'w') as output:
    print(results, file=output)

# write text portion of results to a file
with open(outfileText, 'w') as output:
    print(json.dumps(textResults, indent=4), file=output)