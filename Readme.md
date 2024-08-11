# Web-Scraping-and-Text-Analysis-Project

## Objective
The goal of this project is to extract textual data from articles using provided URLs and perform text analysis to compute various metrics.

## Approach

1. **Web Scraping**:
   - Used the `BeautifulSoup` library for web scraping.
   - Extracted data from the first URL and converted it into a string, then a list of words.
  
2. **Data Manipulation**:
   - Converted the extracted data into a pandas DataFrame and further into a NumPy array for manipulation.

3. **Text Analysis**:
   - Created a `TextAnalysis` class inside the `TextAnalysis.py` file.
   - Defined class attributes for `StopWords`, `PositiveWords`, and `NegativeWords` to use across all URL data.
   - Methods were created to:
     - Load stop words, positive words, and negative words from files.
     - Extract, clean, and analyze the text data.
   - Employed exception handling during data extraction.
   - Managed the sequence of methods to ensure dependent variables like word count are assigned first.

4. **Automation**:
   - Created a `Main.py` file that imports the `TextAnalysis` class and performs analysis on each URL iteratively.
   - Results are stored in a dictionary and exported to an `Output.xlsx` file.

## Setup

### Requirements

- Ensure all required libraries are installed by running:
  ```sh
  pip3 install -r requirements.txt ```
### Libraries Used
 - Requests
 - Bs4 (BeautifulSoup)
 - pandas
 - NLTK
 - Openpyxl
### Operating System
 - MacOS
   
### How to Run the Project
 1. **Clone the repository:**
     ```sh
     git clone https://github.com/samarth-jain28/Web-Scraping-and-Text-Analysis-Project/ ```
 2. **Navigate to the project directory:**
     ```sh
     cd Web-Scraping-and-Text-Analysis-Project
     ```
 3. **pip3 install -r requirements.txt:**
     ```sh
      pip3 install -r requirements.txt
     ```
 4. **Run the `Main.py` file to start the analysis:**
     ```sh
      python3 Main.py
     ```
### Output
 - The results will be saved in `Output.xlsx` within the project directory.

### Future Enhancements
 - Add support for additional languages in text analysis.
 - Implement sentiment analysis using machine learning models.

