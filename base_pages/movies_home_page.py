from selenium.webdriver.chrome.webdriver import WebDriver
class BasePage:
    def __init__(self, driver: WebDriver):
        """

        :rtype: object
        """
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    # def get_title(self):
    #     try:
    #         title =  self.driver.title
    #         if not title:
    #             raise ValueError("Page title is empty")
    #         return title
    #     except Exception as e:
    #         print(f"[Error] Failed to get page title: {e}")
    #         return None

