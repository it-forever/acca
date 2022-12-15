FROM gitlab.it-forever.ru:5050/external/image-external/image-base-fasttext-model-rus:0.0
# FROM ubuntu:22.04
# COPY ./cc.ru.300.bin /cc.ru.300.bin downloads for https://fasttext.cc/docs/en/crawl-vectors.html
RUN apt-get update && apt-get install -y python3-pip git && pip install flask && apt-get clean && rm -rf /var/lib/apt/lists/* 
RUN git clone https://github.com/facebookresearch/fastText.git &&\
   cd fastText &&\
   pip install .
WORKDIR /ft_server
COPY ./ft_server /ft_server
EXPOSE 8000
ENTRYPOINT python3 server.py