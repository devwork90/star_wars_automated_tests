from base_pages.landing_page import LandingPage
from base_pages.movie_details_page import MovieDetailsPage
from base_pages.select_movie_page import SelectedMoviePage
from utilities.custome_logger import Log_Maker

logger = Log_Maker.log_gen()


def test_landing_page(driver):
    logger.info("====================Test_01_landing_page==========")
    """
    test function for landing page
    """
    landing = LandingPage(driver)
    landing.go_to_landing_page()
    assert landing.is_loaded()


def test_landing_title(driver):
    logger.info("====================Test_02_landing_page_title=====")
    landing = LandingPage(driver)
    landing.go_to_landing_page()
    # assert landing.get_title() == "localhost:3000"


def test_value_in_last_table_row(driver):
    logger.info("====================Test_03_Table filtering=========")
    landing = LandingPage(driver)
    landing.go_to_landing_page()
    landing.filter_by_by_title()
    table_data = landing.get_value_in_last_table_row()

    # Assertion statement for the last value in the last row
    expected_title = "The Phantom Menace"
    last_row = table_data[-1]
    actual_movie_title = last_row[0].strip()
    assert actual_movie_title == expected_title


def test_movie_search_and_selection(driver):
    logger.info("====================Test_04_Movie Selection=========")
    # "The Empire Strikes Back"
    landing = LandingPage(driver)
    landing.go_to_landing_page()
    selected = SelectedMoviePage(driver)
    movie_details_page = selected.get_movie_table_row_by_value("The Empire Strikes Back")
    assert movie_details_page is not None


def test_the_empire_strike_back_have_wookie(driver):
    logger.info("====================Test_05 Item verification=========")
    landing = LandingPage(driver)
    landing.go_to_landing_page()
    selected = SelectedMoviePage(driver)
    selected.get_movie_table_row_by_value("The Empire Strikes Back")

    # Assertion statement for the species item
    movie_details_page = MovieDetailsPage(driver)
    items = movie_details_page.get_movie_listed_items_by_header_names("layout_lists__rBjPn", "Species")
    assert 'Wookie' in items


def test_the_phantom_menance_planets_does_not_have_camino(driver):
    logger.info("====================Test_06 Item verification=========")
    landing = LandingPage(driver)
    landing.go_to_landing_page()
    selected = SelectedMoviePage(driver)
    selected.get_movie_table_row_by_value("The Phantom Menace")

    movie_details_page = MovieDetailsPage(driver)
    items = movie_details_page.get_movie_listed_items_by_header_names("layout_lists__rBjPn", "Planets")
    assert 'Camino' not in items
