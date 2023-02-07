from os import path
from pydub import AudioSegment

# files                                                                         
src = "./test.mp3"
dst = "./test.wav"

# start time in seconds
startTime = 0.0
# end time in seconds
endTime = 3600.0

# create audiosegment                                                            
sound = AudioSegment.from_mp3(src)
# cut it to length
cut = sound[startTime * 1000:endTime * 1000]
# export sound cut as wav file
cut.export(dst, format="wav")
