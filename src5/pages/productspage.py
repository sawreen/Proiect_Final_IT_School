from seleniumpagefactory.Pagefactory import PageFactory


class ProductsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {


        "hamburger": ("XPATH", '//*[@id="subcategory-521232-product-9827589"]/div/div'),
        "adauga": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "mcpuisor": ("XPATH", '//*[@id="subcategory-521232-product-9827591"]/div/div'),
        "adauga2": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "cartofi": ("XPATH", '//*[@id="#subcategory-502025"]'),
        "mare": ("XPATH", '//*[@id="subcategory-502025-product-9574494"]/div/div'),
        "adauga3": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button'),
        "bauturi": ("XPATH", '//*[@id="#subcategory-502027"]'),
        "sprite": ("XPATH", '//*[@id="subcategory-502027-product-9574505"]/div/div'),
        "adauga4": ("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-product-dialog/div/div[2]/div/div/button')




    }


    def hamburger_select(self):
        self.hamburger.click()

    def adauga_select(self):
        self.adauga.click()

    def mcpuisor_select(self):
        self.mcpuisor.click()

    def adauga2_select(self):
        self.adauga2.click()

    def cartofi_select(self):
        self.cartofi.click()

    def mare_select(self):
        self.mare.click()

    def adauga3_select(self):
        self.adauga3.click()

    def bauturi_select(self):
        self.bauturi.click()

    def sprite_select(self):
        self.sprite.click()

    def adauga4_select(self):
        self.adauga4.click()



