{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyND9wnBtZG4OgsVQ9Z36ggJ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DiegoQuiroz-AI/AI_A2024_002_2021240/blob/main/Text_Analysis_Tool.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LgwyGMgMhGp2",
        "outputId": "314eae3e-cb28-45e2-d8d5-89c2de181e9c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "[nltk_data] Downloading package punkt to /root/nltk_data...\n",
            "[nltk_data]   Package punkt is already up-to-date!\n",
            "[nltk_data] Downloading package stopwords to /root/nltk_data...\n",
            "[nltk_data]   Package stopwords is already up-to-date!\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Introduce the text to analysis: repeat repeat repeat repeat I am repeating to test the code\n",
            "\n",
            "Text Analysis:\n",
            "Total of words: 7\n",
            "Total of unique words: 4\n",
            "The most common word: repeat appears 4 times.\n"
          ]
        }
      ],
      "source": [
        "import nltk\n",
        "from nltk.tokenize import word_tokenize\n",
        "from nltk.corpus import stopwords\n",
        "from collections import Counter\n",
        "\n",
        "nltk.download('punkt')\n",
        "nltk.download('stopwords')\n",
        "\n",
        "def text_analysis(text):\n",
        "    tokens = word_tokenize(text.lower())\n",
        "\n",
        "    # Empty words elimination (stop words)\n",
        "    stop_words = set(stopwords.words('english'))\n",
        "    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]\n",
        "\n",
        "    # word frequence counter\n",
        "    word_freq = Counter(filtered_tokens)\n",
        "\n",
        "    # most common word\n",
        "    most_common_word = word_freq.most_common(1)[0]\n",
        "\n",
        "    # total number of words\n",
        "    total_words = sum(word_freq.values())\n",
        "\n",
        "    # number of unique words\n",
        "    unique_words = len(word_freq)\n",
        "\n",
        "    return {\n",
        "        \"total_words\": total_words,\n",
        "        \"unique_words\": unique_words,\n",
        "        \"most_common_word\": most_common_word\n",
        "    }\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    text = input(\"Introduce the text to analysis: \")\n",
        "    analysis_result = text_analysis(text)\n",
        "    print(\"\\nText Analysis:\")\n",
        "    print(\"Total of words:\", analysis_result[\"total_words\"])\n",
        "    print(\"Total of unique words:\", analysis_result[\"unique_words\"])\n",
        "    print(\"The most common word:\", analysis_result[\"most_common_word\"][0], \"appears\", analysis_result[\"most_common_word\"][1], \"times.\")"
      ]
    }
  ]
}