import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base.setup import WebDriverSetup

class VocabGrabber(WebDriverSetup):
    def __init__(self, headless=False):
        super().__init__(headless=headless)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_vocab_list(self, url, topic):
        self.get(url)
        try:
            close_button = WebDriverWait(self, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 't-popup__close-wrapper.t-popup__block-close-button')))
            close_button.click()
        except TimeoutException:
            pass
        try:
            vocabs = WebDriverWait(self, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='t013__text t-text t-text_md']/ul/li")))

            part_1 = self.find_element(By.XPATH, "(//div[@class='t004'])[1]/div/div/div")
            part_1_text = part_1.get_attribute('textContent')

            vocab_list = []
            for i in range(len(vocabs)):
                vocab = {'Topic': topic, 'vocabs': vocabs[i].text.strip()}
                vocab_list.append(vocab)

            df = pd.DataFrame(vocab_list)
            df.to_csv(f'data/{topic}_vocab.csv', index=False)
            df = pd.DataFrame([{
                'Topic': topic, 'Def': part_1_text
            }])
            df.to_csv(f'data/{topic}_def.csv', index=False)



        except Exception as e:
            print(e)
