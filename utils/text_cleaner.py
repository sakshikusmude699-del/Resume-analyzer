import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download("stopwords")
    nltk.download("punkt")
    stop_words = set(stopwords.words("english"))
