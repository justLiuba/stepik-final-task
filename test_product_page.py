from pages.product_page import ProductPage
import pytest 

@pytest.mark.parametrize('offer', ["?promo=offer0", "?promo=offer1", "?promo=offer2",
"?promo=offer3", "?promo=offer4", "?promo=offer5", "?promo=offer6", "?promo=offer7", "?promo=offer8", "?promo=offer9"]) 
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{offer}"
    page = ProductPage(browser, link)
    page.open()                      
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_goods_name_in_the_success_message()
    page.should_be_right_price_in_success_message()
