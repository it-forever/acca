FROM deeppavlov/base-cpu:0.17.6
# COPY requirements.txt ./
# 
# RUN pip3 install -r requirements.txt &&\
#     mkdir -p /root/.deeppavlov/downloads/vocabs &&\
#     mkdir -p /root/.deeppavlov/downloads/language_models
WORKDIR /root/.deeppavlov/downloads/vocabs
RUN pip3 install sortedcontainers kenlm
RUN apt-get update &&\
    apt-get install wget gzip -y &&\
    wget http://files.deeppavlov.ai/deeppavlov_data/vocabs/russian_words_vocab.dict.gz &&\
    gzip -d russian_words_vocab.dict.gz

WORKDIR /root/.deeppavlov/downloads/language_models
RUN wget http://files.deeppavlov.ai/lang_models/ru_wiyalen_no_punkt.arpa.binary.gz &&\
    gzip -d ru_wiyalen_no_punkt.arpa.binary.gz

EXPOSE 5000
COPY levenshtein_corrector_ru.json /root
CMD python -m deeppavlov riseapi /root/levenshtein_corrector_ru.json -d -p 5000