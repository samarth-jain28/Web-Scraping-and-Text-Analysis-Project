# Data Extraction and NLP #
* __Objective__ - The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables that are explained below.
* __Approch__ - 
  * First, I used the BeautifulSoup library for web scraping, and Pandas for data manipulation.
  * Converted pandas data frame to NumPy array.
  * Then tried to scrape only the first URL.
  * Scrapped the data from the URL and converted it into a string and then in the list of words.
  * Then I decided to create a TextAnalysis class inside the TextAnalysis.py file with constructor declaring all the variables we want.
  * Created 3 class attributes StopWord, PositiveWords, and NegativeWords because they will be used for every URL data.
  * Then created 3 class methods to define these 3 attributes. Opened files containing all Stop Words and appended them to the StopWord list. The same is done for the other two attributes.
  * Then created methods for data extraction, clean data, and others to perform all the tasks we want. Assigned all the attributes in each method.
  * Used exception handling at the time of data extraction.
  * Defined the sequence of methods to be run in construction to ensure that the dependent variables like word count should be assigned first.
  * Created Main.py file, and imported this TextAnalysis class to perform these defined tasks for every URL iteratively.
  * Created a dictionary for results and converted it into an Output.xlsx file.
    
* __To Run the project__ -
  * Download this project, and run - ``` $ pip3 install -r requirements.txt ``` in the terminal.
  * Run Main.py

* __Requirnments__ -
  * All required libraries are mentioned in requirements.txt
  * Libraries used -
    * requests
    * bs4
    * pandas
    * nltk
    * openpyxl
  * Operating System - MacOS
