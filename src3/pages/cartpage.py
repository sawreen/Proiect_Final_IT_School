from seleniumpagefactory.Pagefactory import PageFactory


class CartPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "cart": ("XPATH", '/html/body/header/tz-header-box/div/div/tz-cart-box/div[1]'),
        "adauga": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[5]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]'),
        "mesaj": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[6]/div[2]/div/div/textarea')


    }

    def cart_select(self):
        self.cart.click()

    def adauga_select(self):
        self.adauga.click()


    def mesaj_text(self):
        self.mesaj.send_keys("Apel cu 15 minute inainte de livrare. Multumesc!")
