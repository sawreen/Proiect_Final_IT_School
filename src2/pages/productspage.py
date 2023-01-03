from seleniumpagefactory.Pagefactory import PageFactory


class ProductsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "apa2l": ("XPATH", '//*[@id="subcategory-803160-product-14068707"]/div/div'),
        "bucati": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[5]/div[2]/button'),
        "adauga" :("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "carbo" :("XPATH", '//*[@id="#subcategory-803165"]'),
        "apacarb" :("XPATH", '//*[@id="subcategory-803165-product-14068786"]/div/div'),
        "bucati2" :("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[1]/div[3]/div[5]/div[2]/button'),
        "adauga2" :("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button')




    }

    def apa2l_select(self):
        self.apa2l.click()


    def bucati_select(self):
        self.bucati.click()


    def adauga_select(self):
        self.adauga.click()

    def carbo_select(self):
        self.carbo.click()


    def apacarb_select(self):
        self.apacarb.click()


    def bucati2_select(self):
        self.bucati2.click()


    def adauga2_select(self):
        self.adauga2.click()

