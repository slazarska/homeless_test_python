from homeless_test_python.model import app


def test_open_main_page():
    app.mainpage.open_main_page()
    app.mainpage.check_main_page_is_opened()
