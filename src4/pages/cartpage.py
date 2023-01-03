from seleniumpagefactory.Pagefactory import PageFactory


class CartPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "cart": ("XPATH", '/html/body/header/tz-header-box/div/div/tz-cart-box/div[1]/div[1]'),
        "plus": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[2]/tz-cart-dialog-opener/div/div/div[2]/div[2]/div[1]/div[3]/button'),
        "plus2": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[3]/tz-cart-dialog-opener/div/div/div[2]/div[2]/div[1]/div[3]/button'),
        "plus3": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[4]/tz-cart-dialog-opener/div/div/div[2]/div[2]/div[1]/div[3]/button'),
        "plus4": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[5]/tz-cart-dialog-opener/div/div/div[2]/div[2]/div[1]/div[3]/button'),
        "mesaj": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[6]/div[2]/div/div/textarea')


    }

    def cart_select(self):
        self.cart.click()

    def plus_select(self):
        self.plus.click()

    def plus2_select(self):
        self.plus2.click()

    def plus3_select(self):
        self.plus3.click()

    def plus4_select(self):
        self.plus4.click()

    def mesaj_text(self):
        self.mesaj.send_keys("Puteti lasa produsele portarului de la intrarea in cladirea de birouri, dupa ce sunati la interfon")