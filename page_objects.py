from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from  resizeimage import resizeimage
from pdiffer import pdiff, assert_images_similar
import os
import time

class landing_page_model():


    def __init__(self,driver):

        self.driver = driver


    def go_to_google(self):
        self.driver.get('https://www.google.com')
        self.driver.get_screenshot_as_file(os.getcwd() + '/screenshot.png')


    def verify_landing_page_ui(self):
        cwd = os.getcwd()
        assert_images_similar(cwd + '/base_line.png',cwd + '/screenshot.png',threshold=10000)
        pass
