import time


from selenium import webdriver
from src.pages.firstpage import FirstPage
from src.pages.secondpage import SecondPage
from src.pages.productspage import ProductsPage
from src.pages.cartpage import CartPage

def test_1():
    driver = webdriver.Chrome('E:/PycharmProjects/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.get("https://tazz.ro/")
    driver.maximize_window()
    time.sleep(1)

    firstpage = FirstPage(driver)
    secondpage = SecondPage(driver)
    productspage = ProductsPage(driver)
    cartpage = CartPage(driver)

    firstpage.cookies_select()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 800)")
    time.sleep(1)
    firstpage.iasi_select()
    time.sleep(1)
    firstpage.adresa_select()
    time.sleep(1)
    firstpage.adressadd_select()
    time.sleep(1)
    firstpage.locatie_text()
    time.sleep(1)
    firstpage.locatie_select()
    time.sleep(1)
    firstpage.confirm_select()
    time.sleep(1)
    firstpage.detalii_text()
    time.sleep(1.5)
    firstpage.acasa_select()
    time.sleep(1)
    firstpage.save_select()
    time.sleep(1)



    secondpage.restaurante_select()
    time.sleep(1.5)
    secondpage.filter_select()
    time.sleep(1)
    secondpage.burger_select()
    time.sleep(1)
    secondpage.livraretazz_select()
    time.sleep(1)
    secondpage.aplica_click()
    time.sleep(1)


    productspage.salsa_select()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 900)")
    time.sleep(1)
    productspage.quesadilla_select()
    time.sleep(1)
    productspage.vita_select()
    time.sleep(1)
    productspage.adauga_select()
    time.sleep(1)
    productspage.concarne_select()
    time.sleep(1)
    productspage.adauga_select()
    time.sleep(1)


    cartpage.cart_select()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 450)")
    time.sleep(2)
    cartpage.tacamuri_select()
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 150)")
    time.sleep(1.5)
    cartpage.ultimprodus_select()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(1)
    cartpage.mesaj_text()
    time.sleep(3)







