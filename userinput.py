import os

class UserInput:
    def url_input(self):
        """
        Requests a list of URLs from the user, separated by commas.
        Returns a list of URLs.
        """
        while True:
            urls = input("Please enter a list of URLs to crawl, separated by commas: ")
            url_list = [url.strip() for url in urls.split(',')]
            if all(url_list):  # Check if any entries are empty
                break
            else:
                print("Invalid input. Please ensure all URLs are valid and separated by commas.")
        return url_list

    def directory_input(self):
        """
        Requests a directory path from the user.
        Validates the path and prompts for retry if invalid.
        Returns the validated directory path.
        """
        while True:
            data_path = input("Please enter the directory path to store the data: ")
            if os.path.isdir(data_path):
                break
            else:
                print("Error: The directory does not exist.")
        return data_path
