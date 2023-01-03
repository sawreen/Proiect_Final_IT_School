from seleniumpagefactory.Pagefactory import PageFactory


class ProductsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "bardar": ("XPATH", '//*[@id="product-8217418"]/div/div'),
        "plus": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[5]/div[2]/button'),
        "adauga": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "backhora": ("XPATH", '/html/body/div[2]/main/div[1]/div/div/div/div/a[3]'),
        "vin": ("XPATH", '/html/body/div[2]/main/tz-widget-market/div/div/div/div/div/a[1]'),
        "taraboste": ("XPATH", '//*[@id="product-8217340"]/div/div'),
        "adauga2": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "plus2": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[5]/div[2]/button'),
        "novak": ("XPATH", '//*[@id="product-8217357"]/div/div'),
        "plus3": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[5]/div[2]/button'),
        "adauga3": ("XPATH", ' /html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button')


    }



    def bardar_select(self):
        self.bardar.click()


    def plus_select(self):
        self.plus.click()

    def adauga_select(self):
        self.adauga.click()

    def backhora_select(self):
        self.backhora.click()

    def vin_select(self):
        self.vin.click()

    def taraboste_select(self):
        self.taraboste.click()

    def adauga2_select(self):
        self.adauga2.click()

    def plus2_select(self):
        self.plus2.click()


    def novak_select(self):
        self.novak.click()



    def plus3_select(self):
        self.plus3.click()



    def adauga3_select(self):
        self.adauga3.click()