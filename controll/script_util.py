from gensim.summarization import summarize, keywords
from translate import Translator


def get_summary(text):
       return summarize(text)


def get_keywords(text):
       return keywords(text)


def get_translation(text, target):
       translator = Translator(to_lang=target)
       return translator.translate(text)
