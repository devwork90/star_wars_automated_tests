from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from base_pages.movies_home_page import BasePage


class LandingPage(BasePage):
    URL = "http://localhost:3000/"
    title_filter_xpath = "//th[normalize-space()='Title']"

    def go_to_landing_page(self):
        self.open(self.URL)

    def is_loaded(self):
        return self.driver.find_element(By.CLASS_NAME, "layout_container__F8gUU").is_displayed()

    def filter_by_by_title(self):
        wait = WebDriverWait(self.driver, 10)
        filter_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.title_filter_xpath))
        )
        filter_element.click()
        # self.driver.find_element(By.XPATH, self.title_filter_xpath).click()

    def get_value_in_last_table_row(self):
        table = self.driver.find_element(By.XPATH, "//table[@class='text-gray-500 table-auto text-3xl font-mono']")
        table.find_element(By.XPATH, "//tbody")
        rows = table.find_elements(By.TAG_NAME, "tr")

        table_data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)
        return table_data

