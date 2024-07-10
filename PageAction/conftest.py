import pytest
from selenium import webdriver
from Utility.Readdata import Readdata


@pytest.fixture()
def setup(browser):
    global driver
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Readdata.base_url())
    act_title = driver.title
    if act_title == "Selenium Practice - Student Registration Form":
        assert True
    else:
        driver.save_screenshot(r"C:\Users\chiya\PycharmProjects\HybridFramwork\Screenshots\WrongTitle.png")
        assert False
        driver.quit()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")




@pytest.hookimpl(tryfirst=True)
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Platform",None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
    metadata['Created By'] = 'Prasanna'


