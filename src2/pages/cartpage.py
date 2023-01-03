from seleniumpagefactory.Pagefactory import PageFactory


class CartPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "cart": ("XPATH", '/html/body/header/tz-header-box/div/div[1]/tz-cart-box/div[1]/div[1]'),
        "minus": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[3]/tz-cart-dialog-opener/div/div/div[2]/div[2]/div[1]/div[1]'),
        "banane": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]'),
        "plus": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[4]/tz-cart-dialog-opener/div/div/div[2]/div[2]/div[1]/div[3]/button'),
        "mesaj": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[5]/div[2]/div/div/textarea')



    }

    def cart_select(self):
        self.cart.click()


    def minus_select(self):
        self.minus.click()

    def banane_select(self):
        self.banane.click()


    def plus_select(self):
        self.plus.click()

    def mesaj_text(self):
        self.mesaj.send_keys("Bananele sa fie cat mai verzi!")

