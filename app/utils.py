from textblob import TextBlob
from nltk.corpus import stopwords


data=None

def init(value):
    global data 
    data = value

def get_stats():
    
    temp = 0 # a temporary variable to get sum of polarity whic will be used later to get average
    pos_sent=0
    neg_sent=0
    neu_sent=0
    total=0
    average_sentiment=0

    for i in data:
        stats_data=[]

        if i.polarity>0:
            pos_sent+=1
        elif i.polarity<0:
            neg_sent+=1
        else:
            neu_sent+=1
        total+=1
        temp +=i.polarity
    if total!=0:
        average_sentiment = temp/total 
    

    return {
        "overall_sentiment": round(average_sentiment,2),
        "positive_rating" :pos_sent,
        "negative_rating" :neg_sent,
        "neutral_rating" :neu_sent,
        "total_count" :total
    }

def get_word_count():

    combined_data=""
    for i in data:
        combined_data+=i.feedback.lower()+" "

    dataset = TextBlob(combined_data)
    tokens = set(dataset.words)
    stop=set(stopwords.words("english"))
    tokens = tokens -stop

    word_count={}
    for i in tokens:
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1
    word_count_list=[]
    for i in word_count:
        word_count_list.append({
            'key':i,
            'value' :word_count[i]
        })
    return word_count_list
    

    
def get_trend():
    trend=list()
    for i in data:
        trend.append({'x':i.polarity, 'y':i.subjectivity})
    return trend