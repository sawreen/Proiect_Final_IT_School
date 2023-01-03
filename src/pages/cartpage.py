from seleniumpagefactory.Pagefactory import PageFactory


class CartPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "cart": ("XPATH", '/html/body/header/tz-header-box/div/div[1]/tz-cart-box/div[1]/div[1]/div[1]'),
        "tacamuri": ("XPATH", '/html/body/tz-cart/div/div[1]/div[1]/div[4]/div[2]/div[1]/div/div[2]/div'),
        "ultimprodus": ("XPATH", '/html/body/tz-cart/div/div[1]/div[1]/div[4]/div[1]/div[2]/div[4]/div[2]/div[2]/div[2]'),
        "mesaj": ("XPATH", '/html/body/tz-cart/div/div/div[1]/div[5]/div[2]/div[2]/div/textarea')


    }

    def cart_select(self):
        self.cart.click()

    def tacamuri_select(self):
        self.tacamuri.click()

    def ultimprodus_select(self):
        self.ultimprodus.click()

    def mesaj_text(self):
        self.mesaj.send_keys("Apel atunci cand se pleaca catre livrarea produsului. Multumesc.")