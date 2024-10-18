# data_crawl
Python app that crawls a list of URLs to find and download all .txt and .pdf files to a local directory separated into the following classes: main.py, userinput.py, crawler.py, and downloader.py.

Here's an overview of how the code will work:

userinput.py: This will handle user input, asking for the list of URLs and the download directory. It will validate the directory path to ensure it exists.
crawler.py: This will use Scrapy to crawl the URLs provided and identify the .txt and .pdf files.
downloader.py: This will create subdirectories for PDFs and TXTs within the specified download directory and then download the files using Scrapy, with a progress bar using tqdm.
main.py: This will orchestrate the entire process by calling the functions from the other classes.
Assumptions:

You have Python and Scrapy installed. If not, you can install them using pip: pip install scrapy tqdm.
You have a basic understanding of Python and object-oriented programming.
Restrictions:

This code is designed to crawl and download files from publicly accessible URLs. It may not work with websites that require login or have anti-scraping measures.
