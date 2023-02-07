````
!pip install moviepy

import moviepy.editor as mp
clip = mp.VideoFileClip(r"/NeMo/intro.mkv")
clip.audio.write_audiofile(r"/NeMo/intro.mp3")

````