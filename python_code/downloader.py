# downloader.py
import os
from tqdm import tqdm
from crawler import Crawler
from userinput import UserInput
import scrapy

class Downloader:
    def __init__(self):
        self.crawler = Crawler()
        self.user_input = UserInput()
        self.data_path = self.user_input.directory_input()

    def directory_create(self):
        """
        Creates directories for pdf and txt files.
        Returns the paths to the created directories.
        """
        path_to_pdf_files = os.path.join(self.data_path, "pdf_files")
        os.makedirs(path_to_pdf_files, exist_ok=True)
        path_to_txt_files = os.path.join(self.data_path, "txt_files")
        os.makedirs(path_to_txt_files, exist_ok=True)
        return path_to_pdf_files, path_to_txt_files

    def the_download(self):
        """
        Downloads the .pdf and .txt files using Scrapy and tqdm for progress tracking.
        """
        path_to_pdf_files, path_to_txt_files = self.directory_create()

        pdf_list = self.crawler.get_pdf_list()
        for url in tqdm(pdf_list, desc="Downloading PDFs"):
            file_name = url.split("/")[-1]
            file_path = os.path.join(path_to_pdf_files, file_name)
            scrapy.Request(url, callback=self.save_file, meta={'file_path': file_path})

        txt_list = self.crawler.get_txt_list()
        for url in tqdm(txt_list, desc="Downloading TXTs"):
            file_name = url.split("/")[-1]
            file_path = os.path.join(path_to_txt_files, file_name)
            scrapy.Request(url, callback=self.save_file, meta={'file_path': file_path})

    def save_file(self, response):
        """
        Saves the downloaded file to the specified path.
        """
        with open(response.meta['file_path'], 'wb') as f:
            f.write(response.body)
