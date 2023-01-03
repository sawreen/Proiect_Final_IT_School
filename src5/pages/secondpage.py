from seleniumpagefactory.Pagefactory import PageFactory


class SecondPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "restaurante": ("XPATH", '/html/body/div[2]/main/div/tz-widget-partner-types/div/div[2]/div/tz-dynamic-carousel/div/section/ul/li[1]/a'),
        "mcdonalds": ("XPATH", '/html/body/div[2]/main/tz-partners/div/div[2]/div[2]/a'),
        "happy": ("XPATH", '//*[@id="#subcategory-521232"]')


    }


    def restaurante_select(self):
        self.restaurante.click()

    def mcdonalds_select(self):
        self.mcdonalds.click()

    def happy_select(self):
        self.happy.click()


