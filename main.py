from successwithielts.scrap_links import LinkGrabber
from successwithielts.scrap_vocab import VocabGrabber
import pandas as pd

if __name__ == '__main__':
    url = "https://successwithielts.com/podcast#transcripts"
    # with LinkGrabber(headless=False) as lg:
    #     lg.collect_links(url)

    links_df = pd.read_csv('data/link/links_data.csv')
    with VocabGrabber(headless=True) as vg:
        for index, row in links_df.iterrows():
            # if index <= 27:
            #     continue
            vg.get_vocab_list(row['href'], row['header'])
            break
