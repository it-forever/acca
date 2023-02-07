
import wave
import audioop

inFileName = 'C:\\Users\\jsing\\pyenv\\NLP\\inputfiles\\NOAGENDA\\NA-1348-2021-05-20-cut60-120.wav'
outFileName = 'C:\\Users\\jsing\\pyenv\\NLP\\inputfiles\\NOAGENDA\\NA-1348-2021-05-20-cut60-120-Mono.wav'

# read input file and write mono output file
try:
    # open the input and output files
    inFile = wave.open(inFileName,'rb')
    outFile = wave.open(outFileName,'wb')
    # force mono
    outFile.setnchannels(1)
    # set output file like the input file
    outFile.setsampwidth(inFile.getsampwidth())
    outFile.setframerate(inFile.getframerate())
    # read
    soundBytes = inFile.readframes(inFile.getnframes())
    print("frames read: {} length: {}".format(inFile.getnframes(),len(soundBytes)))
    # convert to mono and write file
    monoSoundBytes = audioop.tomono(soundBytes, inFile.getsampwidth(), 1, 1)
    outFile.writeframes(monoSoundBytes)
    
except Exception as e:
    print(e)
    
finally:
    inFile.close()
    outFile.close()