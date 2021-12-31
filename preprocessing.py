import pandas as pd
import re
import numpy as np

# Done
# shein.csv
# zara.csv
# gucci.csv
# victoriassecret.csv
# chanel.csv
# nike.csv
# adidas.csv
# h&m.csv
# asos.csv
# boohoo.csv

# https://stackoverflow.com/questions/33404752/removing-emojis-from-a-string-in-python
def deEmojify(text):
    regrex_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        u"\U00010000-\U0010ffff"
        u"\u2600-\u2B55"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'',text)

tweets_df = pd.read_csv("Data/Raw Tweet Data/zara.csv", lineterminator='\n')

text = tweets_df['text'].values
text_list = [t.replace(t, deEmojify(t)) for t in text]
text_list
tweets_df['text'] = text_list
tweets_df['brand'] = np.full((len(tweets_df.index)), "zara")

#geo_tweets_df = tweets_df[tweets_df['geo'].notna()]

tweets_df.to_csv('zara_p.csv', index=False) # change brand name
#geo_tweets_df.to_csv('boohoo_geo.csv', index=False) # change brand name

