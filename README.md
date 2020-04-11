# Data_Insights

In this blog I will explain about how we can leverage technology for fetching meaningful insights from the freely available data over the internet (which can help corporates/people/banks etc.). In the read me section, I will explain about few things related to attached code snippet.

I will be explaining on the following:

1. How to get data : I will be sharing different sources and ways of getting the data either with the help of web scraping (i.e. fetching data from the website's source code) or using their free api (if available). 

1.1 Using API: If a webisite has its free API, we can use that to fetch the required data. Generally, the developers page will give you the information if they have an API. For example for Twitter: https://developer.twitter.com/en/apply-for-access

1.2 Webscraping: Webscraping is technique of fetching data from a website source code. This can be done by hitting the target website's source code and getting the information. The complexity involved in this process may vary from website to website. For example: few websites are static in nature. It is easier to fetch data from such websites. On the other hand some website involves logging first. In such cases we need to make use of selenium webdriver. Also, after logging in we may need to click on a button, so wherever any human intervention is required for running the website, webdriver like selenium is required. In the code attached for reference, I am taking data from google.com. For webscraping data from google: first of all we need to write the name of the product/company etc to fetch the data related to that. Then we press enter and so on. For this case, I am making use of selenium webdriver in Python.

1.3 Kaggle: Nowadays a lot of free data is avilable on Kaggle in the form of csv's. These csv's can be directly imported in python and data can be manipulated based on the requirements using various python packages like pandas and can be used for further analysis.

2.Converting the data into the required format, based on the requirement : Usually the required format is in json. As json format can be used easily for further consumption like showing on the UI, saving it in the database.
In the attached example DataInsights_from_Google.py : I am creating a word cloud of the adjectives fetched from the reviews data from google for the input company/product. 


3.Finding miningfull insights from the data: There can be a lot of ways of finding meaningful insights from the filtered data using various python libraries which provides ways for doing different statistical analysis. For example we can create a wordcloud, or we can show the data in terms of a report with graphs and charts.

