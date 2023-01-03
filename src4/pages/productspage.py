from seleniumpagefactory.Pagefactory import PageFactory


class ProductsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "typec": ("XPATH", '//*[@id="product-10039939"]/div/div'),
        "adauga": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "lightning": ("XPATH", '//*[@id="product-10039935"]/div/div'),
        "adauga2": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "backmobi": ("XPATH", '/html/body/div[2]/main/div[1]/div/div/div/div/a[3]'),
        "auto": ("XPATH", '/html/body/div[2]/main/tz-widget-market/div/div/div/div/div/a[4]'),
        "chargerauto": ("XPATH", '//*[@id="product-10039943"]/div/div'),
        "adauga3": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "backmobi2": ("XPATH", '/html/body/div[2]/main/div[1]/div/div/div/div/a[3]'),
        "suportauto": ("XPATH", '/html/body/div[2]/main/tz-widget-market/div/div/div/div/div/a[15]'),
        "gravity": ("XPATH", '//*[@id="product-10040384"]/div/div'),
        "adauga4": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button')



    }

    def typec_select(self):
        self.typec.click()

    def adauga_select(self):
        self.adauga.click()

    def lightning_select(self):
        self.lightning.click()

    def adauga2_select(self):
        self.adauga2.click()

    def backmobi_select(self):
        self.backmobi.click()

    def auto_select(self):
        self.auto.click()

    def chargerauto_select(self):
        self.chargerauto.click()

    def adauga3_select(self):
        self.adauga3.click()

    def backmobi2_select(self):
        self.backmobi2.click()

    def suportauto_select(self):
        self.suportauto.click()

    def gravity_select(self):
        self.gravity.click()

    def adauga4_select(self):
        self.adauga4.click()


