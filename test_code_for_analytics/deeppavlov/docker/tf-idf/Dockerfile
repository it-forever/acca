FROM deeppavlov/base-cpu:0.17.6
# COPY requirements.txt ./
# 
# RUN pip3 install -r requirements.txt &&\
#     mkdir -p /root/.deeppavlov/downloads/vocabs &&\
#     mkdir -p /root/.deeppavlov/downloads/language_models
WORKDIR /root/.deeppavlov/downloads
RUN pip3 install sortedcontainers kenlm
RUN apt-get update &&\
    apt-get install wget gzip -y &&\
    wget http://files.deeppavlov.ai/datasets/wikipedia/ruwiki.tar.gz && tar xzf ruwiki.tar.gz && rm ruwiki.tar.gz

WORKDIR /root/.deeppavlov/models
RUN wget http://files.deeppavlov.ai/deeppavlov_data/ru_odqa.tar.gz && tar xzf ru_odqa.tar.gz && rm ru_odqa.tar.gz


EXPOSE 5000
COPY ru_ranker_tfidf_wiki.json /root
CMD python -m deeppavlov riseapi /root/ru_ranker_tfidf_wiki.json -d -p 5000