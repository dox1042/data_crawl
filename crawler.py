import scrapy
from scrapy_playwright.page import PageMethod
from userinput import UserInput

class Crawler(scrapy.Spider):
    name = "file_crawler"

    def __init__(self):
        super().__init__()
        user_input = UserInput()
        self.start_urls = user_input.url_input()
        self.txt_list = []
        self.pdf_list = []

    async def parse(self, response):
        """
        Parses the response and extracts URLs of .txt and .pdf files.
        """
        await response.page.wait_for_selector("body")  # Wait for page to load

        self.txt_list.extend(response.xpath("//a[contains(@href, '.txt')]/@href").getall())
        self.pdf_list.extend(response.xpath("//a[contains(@href, '.pdf')]/@href").getall())

        # For complex structures, inspect the page and adjust the XPath expressions
        # Example:
        # self.txt_list.extend(response.xpath("//div[@id='content']//a[contains(@href, '.txt')]/@href").getall())

    def get_txt_list(self):
        """
        Returns the list of .txt file URLs.
        """
        return self.txt_list

    def get_pdf_list(self):
        """
        Returns the list of .pdf file URLs.
        """
        return self.pdf_list
