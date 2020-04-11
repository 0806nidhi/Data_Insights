from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import datetime
import pandas as pd
import nltk
from collections import defaultdict
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import sys, os


class Scrapper_Google(object):

    def __init__(self):        
        return None

    def ScrapWeb(self, companyName):
        print('Starting Scrapper.. fetching results from google.com...')
        print('Fetching results from google.com...')
        pd.set_option('display.max_columns', 10)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
        Result = []
        company_name = companyName
        no_of_reviews = 150

# -------------------------------------------------------------------------------------------- Extracting google reviews
        try:
            print('Getting reviews...')
            reviews, time_stamp = self.extract_google_reviews(driver, company_name, no_of_reviews)
            Result.extend(reviews)

# ------------------------------------------------------------------ Fetching and saving list of adjectives from reviews
            print('parsing...', )
            reviewsDf = pd.DataFrame(Result)
            TimeStampDf = pd.DataFrame(time_stamp)
            TimeStampDf.columns = ['Time Stamp']
            reviewsDf.columns = ['google_review']
            reviewsDf['review_adjectives'] = reviewsDf['google_review'].apply(self.pick_adjectives)
            consolidated_adjectives = reviewsDf['review_adjectives'].str.cat(sep=' ')
            try:
                n = int(len(consolidated_adjectives) / 2)
                if(n>400):
                    word_cloud = WordCloud(width=n, height=n, relative_scaling='auto',
                                           background_color='white').generate(consolidated_adjectives)
                else:
                    word_cloud = WordCloud(background_color='white').generate(consolidated_adjectives)
                print('saving word cloud in png format...', )
                dt = datetime.datetime.now().isoformat().replace(".", "").replace(":", "")
                print(cpath+path)
                img = company_name + "-Google_" + "reviews" + dt +".png"
                word_cloud.to_file(img)
            except:
                img = ""
                print("Not enough words for creating word cloud.")
            result = pd.concat([reviewsDf, TimeStampDf], ignore_index=True, axis=1)
            print(result)
            result.rename(columns={0: 'Review', 1: 'Adjectives', 2:'Time Stamp'}, inplace=True)
            arr=[]
            totalReview={}
            result = result.dropna()
            for index, row in result.iterrows():
                dict={}                
                if(row[0] == ''):
                    dict["text"] = ''
                else:
                    dict["text"] = row[0].replace('"', '')
                if(row[1] == ''):
                    dict["title"] = ''
                else:
                    dict["title"] = row[1]
                if(row[2] == ''):
                    dict["time"] = ''
                else:
                    dict["time"] = row[2]
                arr.append(dict)
            totalReview["reviews"] = arr
            if "aggregateReview" not in totalReview:                
                totalReview["aggregateReview"] = 0
            totalReview["imagePath"] = img
            print(totalReview)
            result.to_csv(company_name + '-Google_reviews.csv', sep=',')
                
        except TimeoutException:
            print("TimeoutException : Could not find results on google.com")
            raise ("TimeoutException : Could not find results on google.com")
        except Exception as e:
            print(str(e)+' :Error')
            raise Exception(str(e))
        return totalReview

    def pick_adjectives(self, row):
        adj_keys = ['JJ', 'JJR', 'JJS']
        token_words = nltk.word_tokenize(row)
        token_dict = dict(nltk.pos_tag(token_words))
        modified_token_dict = defaultdict(list)
        for k, v in token_dict.items():
            modified_token_dict[v].append(k)
        adjectives = list(map(modified_token_dict.get, adj_keys))
        adjectives = [x for x in adjectives if x is not None]
        adjectives_str = ' '.join(str(item) for sublist in adjectives for item in sublist)
        return adjectives_str

    def extract_google_reviews(self, driver, company_name, no_of_reviews):
        driver.get('https://www.google.com')
        driver.find_element_by_name('q').send_keys(company_name)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()
        count = 0
        reviews = []
        # ratings = []
        time_stamp = []
# ---------------------------------------------------------------------- Checking if Google has reviews for this company
        if(driver.find_elements_by_link_text("View all Google reviews") != []):
            driver.find_elements_by_link_text("View all Google reviews")[0].click()
        elif(driver.find_elements_by_link_text("1 Google review") != []):
            driver.find_elements_by_link_text("1 Google review")[0].click()
        elif(driver.find_elements_by_link_text("2 Google reviews") != []):
            driver.find_elements_by_link_text("2 Google reviews")[0].click()
        elif(driver.find_elements_by_link_text("3 Google reviews") != []):
            driver.find_elements_by_link_text("3 Google reviews")[0].click()
        elif(driver.find_elements_by_link_text("4 Google reviews") != []):
            driver.find_elements_by_link_text("4 Google reviews")[0].click()
        elif(driver.find_elements_by_link_text("5 Google reviews") != []):
            driver.find_elements_by_link_text("5 Google reviews")[0].click()
        elif(driver.find_elements_by_link_text("6 Google reviews") != []):
            driver.find_elements_by_link_text("6 Google reviews")[0].click()
        elif(driver.find_elements_by_link_text("7 Google reviews") != []):
            driver.find_elements_by_link_text("7 Google reviews")[0].click()
        elif(driver.find_elements_by_link_text("8 Google reviews") != []):
            driver.find_elements_by_link_text("8 Google reviews")[0].click()
        elif(driver.find_elements_by_link_text("9 Google reviews") != []):
            driver.find_elements_by_link_text("9 Google reviews")[0].click()
        else:
            print("Google don't have reviews for this company")
            raise Exception('No Reviews')
        # exit()
        all_reviews = WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.gws-localreviews__google-review')))
        while len(all_reviews) < no_of_reviews:
            driver.execute_script('arguments[0].scrollIntoView(true);', all_reviews[-1])
            WebDriverWait(driver, 5, 0.25).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class$="activityIndicator"]')))
            all_reviews = driver.find_elements_by_css_selector('div.gws-localreviews__google-review')
            count = count + 1
            if count == no_of_reviews:
                print("google has the following number of reviews only")
                print(len(all_reviews))
                break
        # soup = BeautifulSoup(driver.page_source, "html.parser")
        for review in all_reviews:
            try:
                full_text_element = review.find_element_by_css_selector('span.review-full-text')
                time = review.find_element_by_css_selector('span.dehysf')
                # rating_text = review.find_element_by_css_selector('span.aria-label')
            except:
                full_text_element = review.find_element_by_css_selector('span[class^="r-"]')
                time = review.find_element_by_css_selector('span.dehysf')
                rating_text = review.find_element_by_css_selector('span[class^="fTKmHE99XE4__star fTKmHE99XE4__star-s"]')
            ratings.append(rating_text.get_attribute('aria-label'))
            reviews.append(full_text_element.get_attribute('textContent'))
            time_stamp.append(time.get_attribute('textContent'))
        return reviews, time_stamp

start = datetime.datetime.now()
#for Testing
SR = Scrapper_Google()
c = SR.ScrapWeb("namdhari fresh hsr layout")
print(c)
end = datetime.datetime.now()
diff = end - start
print("Time taken :", diff.total_seconds(), ' seconds')
