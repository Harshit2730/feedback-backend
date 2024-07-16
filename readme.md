## FeedAnalyzer

### Setup 

1. DB setup \
goto database.py and change the username, password, db name according to your local environment.

2. Installations \
recommended to use virtual environment and run below commands

        pip install -r requirements.txt
        python -m textblob.download_corpora  

### Running of app
To start the app in development, use the below command

    fastapi dev app/main.py
