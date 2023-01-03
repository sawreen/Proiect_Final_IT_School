# import time
#
# from selenium import webdriver
# from src5.pages.firstpage import FirstPage
# from src5.pages.secondpage import SecondPage
# from src5.pages.productspage import ProductsPage
# from src5.pages.cartpage import CartPage
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
#     secondpage.restaurante_select()
#     time.sleep(1)
#     secondpage.mcdonalds_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 450)")
#     time.sleep(1)
#     secondpage.happy_select()
#     time.sleep(1)
#
#
#
#     productspage.hamburger_select()
#     time.sleep(1)
#     productspage.adauga_select()
#     time.sleep(1)
#     productspage.mcpuisor_select()
#     time.sleep(1)
#     productspage.adauga2_select()
#     time.sleep(1)
#     productspage.cartofi_select()
#     time.sleep(1)
#     productspage.mare_select()
#     time.sleep(1)
#     productspage.adauga3_select()
#     time.sleep(1)
#     productspage.bauturi_select()
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 9700)")
#     time.sleep(1)
#     productspage.sprite_select()
#     time.sleep(1)
#     productspage.adauga4_select()
#     time.sleep(1)
#
#
#     cartpage.cart_select()
#     driver.execute_script("window.scrollTo(0, 900)")
#     time.sleep(1)
#     cartpage.mesaj_text()
#     time.sleep(4)
#
#
