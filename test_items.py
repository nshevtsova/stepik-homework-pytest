import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_available(browser):

    button = None

    try:
        browser.get(link)
        button = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
       
    except:
        pass
    
    assert  button is not None, "'Add to basket' button should be available"
    
    time.sleep(10)