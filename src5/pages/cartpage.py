from seleniumpagefactory.Pagefactory import PageFactory


class CartPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "cart": ("XPATH", '/html/body/header/tz-header-box/div/div[1]/tz-cart-box'),
        "mesaj": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[6]/div[2]/div/div/textarea')


    }

    def cart_select(self):
        self.cart.click()


    def mesaj_text(self):
        self.mesaj.send_keys("Intrarea in bloc se face prin spatele acestuia.")