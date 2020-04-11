# Data_Insights


In this blog I will explain on how we can leverage technology for fetching meaningful insights from the freely available data over the internet (which can help corporates/people/banks etc.). In the read me section, I will explain about few things related to attached code snippet which works on 3 steps: getting the data, formatting the data and analysing the data .

To summarize, we need to work on the following three step approach:-

1. How to get data : I will be sharing few sources and ways of getting the data. It can be either with the help of web scraping (i.e. fetching data from the website's source code) or using their free api (if available) or it can be from a reliable source from where we can download the data. 

1.1 Using API: If a website has its free API, we can use that to fetch the required data. Generally, the developers page will give you the information if they have an API. For example for Twitter: https://developer.twitter.com/en/apply-for-access.
Some websites does not have a free api. If we want to fetch news from such websites, we need to pay a periodical subscription fee.
1.2 Webscraping: Webscraping is technique of fetching data from a website source code. This can be done by hitting the target website's source code and getting the information. The complexity involved in this process may vary from website to website, as it all depends on it's source code. For example: few websites are static in nature, It is easier to fetch data from such websites as the source code is in a simple HTML/CSS/Bootstrap. On the other hand some website involves logging first. In such cases we need to make use of selenium webdriver. Also, after logging in we may need to click on a button, so wherever any human intervention is required for running the website, a webdriver like selenium is required for loading the required page on the website. In the code attached for reference, I am taking data from google.com. For webscraping data from google: first of all we need to write the name of the product/company etc to fetch the data related to that. Then we press enter and so on. For this case, I am making use of selenium webdriver in Python.
1.3 Kaggle: Nowadays a lot of free data is avilable on Kaggle in the form of csv's. These csv's can be directly imported in python and data can be manipulated based on the requirements using various python packages like pandas and can be used for further analysis.


2.Converting the data into the required format, based on the requirement : Usually the required format is in json. As json format can be used easily for further consumption like showing on the UI, saving it in the database. In the attached example DataInsights_from_Google.py : I am creating a word cloud of the adjectives fetched from the reviews data from google for the input company/product. Benefits of creating a word cloud is that we can easily see the adjectives drawn from the reviews/comments. It is quite user friendly.


3.Deriving significant insights from the data: There can be a lot of ways of finding meaningful insights from the filtered data using various python libraries which provides ways for doing different statistical analysis. For example we can create a wordcloud, or we can show the data in terms of a report with graphs and charts.

