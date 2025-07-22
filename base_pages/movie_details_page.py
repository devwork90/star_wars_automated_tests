from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MovieDetailsPage:
    def __init__(self, driver):
        self.find_elements = None
        self.driver = driver

    def get_movie_listed_items_by_header_names(self, parent_div_class, target_h1_text):
        """
        Get all child divs inside the parent
        :param parent_div_class:
        :param target_h1_text:
        :return:
        """
        wait = WebDriverWait(self.driver, 10)

        print("Looking for: ", target_h1_text)

        # Wait for the parent container to be present
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, parent_div_class)))

        child_divs = self.driver.find_elements(By.CSS_SELECTOR, f"div.{parent_div_class} > div")
        print("Found child divs: ", len(child_divs))

        for div in child_divs:
            try:
                h1 = div.find_element(By.TAG_NAME, "h1")
                print("Found h1:", h1.text)
                if h1.text.strip() == target_h1_text:
                    ul = div.find_element(By.TAG_NAME, "ul")
                    li_elements = ul.find_elements(By.TAG_NAME, "li")
                    results = [li.text.strip() for li in li_elements]
                    print("Returning items: ", results)
                    return results
            except Exception as e:
                print("Error in loop:", e)
                continue

        print("No matching h1 found.")
        return []
