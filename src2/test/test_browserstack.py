# import time
#
# from selenium import webdriver
# from src2.pages.firstpage import FirstPage
# from src2.pages.secondpage import SecondPage
# from src2.pages.productspage import ProductsPage
# from src2.pages.cartpage import CartPage
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
#
#     secondpage.supermarket_select()
#     time.sleep(1)
#     secondpage.kaufland_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 600)")
#     time.sleep(1)
#     secondpage.bauturi_select()
#     time.sleep(1)
#     secondpage.apa_select()
#     time.sleep(1)
#
#
#
#     productspage.apa2l_select()
#     time.sleep(1)
#     productspage.bucati_select()
#     productspage.bucati_select()
#     productspage.bucati_select()
#     time.sleep(1)
#     productspage.adauga_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 600)")
#     time.sleep(1)
#     productspage.carbo_select()
#     time.sleep(1)
#     productspage.apacarb_select()
#     time.sleep(1)
#     productspage.bucati2_select()
#     productspage.bucati2_select()
#     productspage.bucati2_select()
#     time.sleep(1)
#     productspage.adauga2_select()
#     time.sleep(1)
#
#
#     cartpage.cart_select()
#     time.sleep(1)
#     cartpage.minus_select()
#     time.sleep(1)
#     cartpage.minus_select()
#     time.sleep(1)
#     cartpage.banane_select()
#     time.sleep(1)
#     cartpage.plus_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 450)")
#     time.sleep(1)
#     cartpage.mesaj_text()
#     time.sleep(4)
#
#
#
#
