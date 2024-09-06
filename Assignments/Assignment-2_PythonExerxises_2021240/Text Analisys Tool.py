import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def text_analysis(text):
    tokens = word_tokenize(text.lower())

    # Empty words elimination (stop words)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    # word frequence counter
    word_freq = Counter(filtered_tokens)

    # most common word
    most_common_word = word_freq.most_common(1)[0]

    # total number of words
    total_words = sum(word_freq.values())

    # number of unique words
    unique_words = len(word_freq)

    return {
        "total_words": total_words,
        "unique_words": unique_words,
        "most_common_word": most_common_word
    }

if __name__ == "__main__":
    text = input("Introduce the text to analysis: ")
    analysis_result = text_analysis(text)
    print("\nText Analysis:")
    print("Total of words:", analysis_result["total_words"])
    print("Total of unique words:", analysis_result["unique_words"])
    print("The most common word:", analysis_result["most_common_word"][0], "appears", analysis_result["most_common_word"][1], "times.")
