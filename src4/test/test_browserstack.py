# import time
#
# from selenium import webdriver
# from src4.pages.firstpage import FirstPage
# from src4.pages.secondpage import SecondPage
# from src4.pages.productspage import ProductsPage
# from src4.pages.cartpage import CartPage
#
#
# def test_1():
#     driver = webdriver.Chrome('E:/PycharmProjects/chromedriver.exe')
#     driver.implicitly_wait(10)
#     driver.get("https://tazz.ro/")
#     driver.maximize_window()
#     time.sleep(1)
#
#     firstpage = FirstPage(driver)
#     secondpage = SecondPage(driver)
#     productspage = ProductsPage(driver)
#     cartpage = CartPage(driver)
#
#
#     firstpage.cookies_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 800)")
#     time.sleep(1)
#     firstpage.iasi_select()
#     time.sleep(1)
#     firstpage.adresa_select()
#     time.sleep(1)
#     firstpage.adressadd_select()
#     time.sleep(1)
#     firstpage.locatie_text()
#     time.sleep(1)
#     firstpage.locatie_select()
#     time.sleep(1)
#     firstpage.confirm_select()
#     time.sleep(1)
#     firstpage.detalii_text()
#     time.sleep(1.5)
#     firstpage.acasa_select()
#     time.sleep(1)
#     firstpage.save_select()
#     time.sleep(1)
#
#
#     secondpage.mall_select()
#     time.sleep(1)
#     secondpage.mobiup_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 400)")
#     time.sleep(1)
#     secondpage.cabludate_select()
#     time.sleep(1)
#
#
#
#     productspage.typec_select()
#     time.sleep(1)
#     productspage.adauga_select()
#     time.sleep(1)
#     productspage.lightning_select()
#     time.sleep(1)
#     productspage.adauga2_select()
#     time.sleep(1)
#     productspage.backmobi_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 500)")
#     time.sleep(1)
#     productspage.auto_select()
#     time.sleep(1)
#     productspage.chargerauto_select()
#     time.sleep(1)
#     productspage.adauga3_select()
#     time.sleep(1)
#     productspage.backmobi2_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 800)")
#     time.sleep(1)
#     productspage.suportauto_select()
#     time.sleep(1)
#     productspage.gravity_select()
#     time.sleep(1)
#     productspage.adauga4_select()
#     time.sleep(1)
#
#
#
#     cartpage.cart_select()
#     time.sleep(1)
#     cartpage.plus_select()
#     time.sleep(1)
#     cartpage.plus2_select()
#     time.sleep(1)
#     cartpage.plus3_select()
#     time.sleep(1)
#     cartpage.plus4_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 600)")
#     time.sleep(1)
#     cartpage.mesaj_text()
#     time.sleep(4)
#
#
#
#
#
#
#
#
