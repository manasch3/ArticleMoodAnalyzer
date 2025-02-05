from textblob import TextBlob
from newspaper import Article

while True:
    URL = input('Enter The URL ("exit" to quit): ')
    if URL.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    print('\n')
    print("Processing the article...\n")

    try:
        article = Article(URL)  # Assigning URL to article object
        article.download()      # To convert into descript
        article.parse()         # To make it readable by removing HTML in it
        article.nlp()           # To prepare it for NLP

        text = article.text         # Extracting the plain text content from 'article'
        summary = article.summary   # Extracting the summarized text content from 'article'

        text_blob = TextBlob(text)                 # TextBlob Allows to perform sentiment analysis
        text_sentiment = text_blob.sentiment.polarity  # provides value from -1 to 1
        result_t = text_sentiment

        summary_blob = TextBlob(summary)               # TextBlob Allows to perform sentiment analysis
        summary_sentiment = summary_blob.sentiment.polarity  # provides value from -1 to 1
        result_s = summary_sentiment

        print('Sentiment Analysis : Complete Text')
        if -1.00 < result_t < -0.50:
            print(f'{result_t:.2f} - Strongly Negative 😡')
        elif -0.50 < result_t < -0.10:
            print(f'{result_t:.2f} - Negative 😞')
        elif -0.10 < result_t < 0.10:
            print(f'{result_t:.2f} - Neutral 😐')
        elif 0.10 < result_t < 0.50:
            print(f'{result_t:.2f} - Positive 🙂')
        else:
            print(f'{result_t:.2f} - Strongly Positive 😄')

        print('\n')
        print('Sentiment Analysis : Summarized Text')
        if -1.00 < result_s < -0.50:
            print(f'{result_s:.2f} - Strongly Negative 😡')
        elif -0.50 < result_s < -0.10:
            print(f'{result_s:.2f} - Negative 😞')
        elif -0.10 < result_s < 0.10:
            print(f'{result_s:.2f} - Neutral 😐')
        elif 0.10 < result_s < 0.50:
            print(f'{result_s:.2f} - Positive 🙂')
        else:
            print(f'{result_s:.2f} - Strongly Positive 😄')

        print('\n')

    except Exception:
        print('🚫 Invalid URl')