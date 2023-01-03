from seleniumpagefactory.Pagefactory import PageFactory


class ProductsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "salsa": ("XPATH", '/html/body/div[2]/main/tz-partners/div/div[2]/div[2]/div[2]'),
        "quesadilla": ("XPATH", '//*[@id="#subcategory-226886"]'),
        "vita": ("XPATH", '//*[@id="subcategory-226886-product-5173924"]/div/div'),
        "adauga": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "concarne": ("XPATH", '//*[@id="subcategory-226886-product-5173926"]/div/div')



    }


    def salsa_select(self):
        self.salsa.click()

    def quesadilla_select(self):
        self.quesadilla.click()

    def vita_select(self):
        self.vita.click()

    def adauga_select(self):
        self.adauga.click()

    def concarne_select(self):
        self.concarne.click()

    def adauga_select(self):
        self.adauga.click()




