# Data_Insights

In this blog I will explain, how we can leverage technology for fetching useful insights from the freely available data. Basically we can build up models which can help corporates/people/banks in making decisions from the free available data over the internet. In the read me section I will explaining about things and showing that with the help of code examples.

I will be explaining on the following:

How to get data : I will be sharing few sources and ways of getting the data either with the help of web scraping (i.e. fetching data from the website's source code) or using their free api (if available). 
1.1 Using API: If a webisite has its free API, we can use that to fetch the reuired data. Generally, the developers page will give you the information they have an API. 

1.2 Webscraping: Webscraping is technique of fetching the data from a website from its source code. This can be done by hitting the target website's source code and getting the information. This complexity involved in this process may vary from website to website. For example: few websites are static in nature. It is easier to fetch data from such websites. On the other hand some website involves logging first. In such cases we need to make use of selenium. Also, after logging in we may need to click on a button, so wherever any human intervention is required for running the website, selenium can be very useful.
In the code attached for reference, I am taking data from google.com. For webscraping data from google:
first of all we need to write the name of the product/company etc to fetch the data related to that. Then we press enter.
For all that I am making use of selenium webdriver in Python.


1.3 Kaggle: Nowadays a lot of free data is avilable on Kaggle in the form of csv's. These csv's can be directly imported in python and data can be manipulated based on the requirements using various python packages like pandas.

2. Converting the data into the required format, based on the requirement : Usually the required format is in json. As json format can be used easily for further consumption like showing on the UI, saving it in the database.

3. Finding miningfull insights from the data: There can be a lot of ways of finding meaningful insights from the filtered data using various python libraries which provides ways for doing different statistical analysis. For example we can create a wordcloud, or we can show the data in terms of a report with graphs and charts.
