FROM python:3.9

WORKDIR /feedalyzer

COPY ./requirements.txt /feedalyzer/requirements.txt

RUN pip install -m textblob.download_corpora

RUN pip install -m nltk.downloader stopwords

RUN pip install --no-cache-dir --upgrade -r /feedalyzer/requirements.txt

COPY ./app /feedalyzer/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]