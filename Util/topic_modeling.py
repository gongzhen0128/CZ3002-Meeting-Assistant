from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

def topic_summarizer(text):
    summarization = summarize(text, ratio=0.5)
    print (summarization)
    return summarization


text = "BBC News is an operational business division of the British Broadcasting Corporation (BBC) responsible for the gathering and broadcasting of news and current affairs. The department is the world's largest broadcast news organisation and generates about 120 hours of radio and television output each day, as well as online news coverage. The service maintains 50 foreign news bureaus with more than 250 correspondents around the world. James Harding has been Director of News and Current Affairs since April 2013.The department's annual budget is in excess of £350 million; it has 3,500 staff, 2,000 of whom are journalists. BBC News' domestic, global and online news divisions are housed within the largest live newsroom in Europe, in Broadcasting House in central London. Parliamentary coverage is produced and broadcast from studios in Millbank in London. Through the BBC English Regions, the BBC also has regional centres across England, as well as national news centres in Northern Ireland, Scotland and Wales. All nations and English regions produce their own local news programmes and other current affairs and sport programmes.The BBC is a quasi-autonomous corporation authorised by Royal Charter, making it operationally independent of the government, who have no power to appoint or dismiss its director-general, and required to report impartially. As with all major media outlets, though, it has been accused of political bias from across the political spectrum, both within the UK and abroad."
topic_summarizer(text)