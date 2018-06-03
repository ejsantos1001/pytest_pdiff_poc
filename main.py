from .page_objects import *
import pytest


@pytest.fixture
def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    return webdriver.Chrome(chrome_options=chrome_options)

def test_iam_a_test(create_driver):
    driver = create_driver
    landing_page = landing_page_model(driver)
    landing_page.go_to_google()
    landing_page.verify_landing_page_ui()

def test_iam_another_test():
    print('test')
