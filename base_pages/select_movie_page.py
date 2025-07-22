from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_pages.landing_page import LandingPage
from base_pages.movie_details_page import MovieDetailsPage


class SelectedMoviePage(LandingPage):
    def get_movie_table_row_by_value(self, search_text):
        # Wait for the table to be present
        table = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//table[contains(@class, 'table-auto')]")
            )
        )

        # add visibility wait it is needed
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(table)
        )

        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            for cell in cells:
                if search_text.lower() in cell.text.strip().lower():
                    cell.click()
                    # return True  # Only return after click
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CLASS_NAME, "layout_main__IC0zG")  # customize this
                        )
                    )
                    return MovieDetailsPage(self.driver)
        return None
        # return False  # Only return False if nothing matched