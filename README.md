📰 Article Sentiment Analyzer

🚀 Overview

The Article Sentiment Analyzer is a Python-based project that extracts and analyzes the sentiment of any online article using TextBlob and Newspaper3k. It provides sentiment analysis for both the complete text and the summarized text of the article.

📌 Features

-  ✅  Extracts article content from any given URL.
-  ✅  Summarizes the article using NLP techniques.
-  ✅  Performs Sentiment Analysis on both the full text and summary.
-  ✅  Provides a sentiment score ranging from -1 to 1.
-  ✅  Displays emoji-based sentiment results.
-  ✅  Loop-based system to analyze multiple articles until user exits.

📦 Libraries Used

-  🔥  TextBlob - For sentiment analysis.
-  🔥  Newspaper3k - For web scraping and NLP-based text extraction.

🎯 How It Works

- ⚡  The user enters an article URL
- ⚡  The script downloads and extracts the article content
- ⚡  It summarizes the article using NLP
- ⚡  Sentiment analysis is performed on both the full article text and the summarized text
- ⚡  The sentiment score is displayed along with emoji-based feedback
- ⚡  The user can analyze multiple articles until they type "exit"

🔧 Usage Instructions

-  🔹 Run the script
-  🔹 Enter a valid article URL when prompted
-  🔹 View the sentiment results
-  🔹 Enter another URL or type "exit" to quit

🛠 Error Handling

-  ⚠️  If an invalid URL is entered, the script displays "Invalid URL"
-  ⚠️  If the article fails to download or parse, an error message is shown

📜 Example Output

-  User enters the URL of an article.
  
   The program processes it and returns the sentiment results:

   Sentiment Analysis: Complete Text

   Score: 0.45 - Positive 🙂

   Sentiment Analysis: Summarized Text

   Score: 0.30 - Positive 🙂

🤝 Contributing

-  Want to improve this project? Feel free to fork and submit a pull request!

🌟 Acknowledgments

-  Thanks to TextBlob and Newspaper3k for making text analysis easy!

Happy Coding! 🎉
