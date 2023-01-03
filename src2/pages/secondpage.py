from seleniumpagefactory.Pagefactory import PageFactory


class SecondPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "supermarket": ("XPATH", '/html/body/div[2]/main/div/tz-widget-partner-types/div/div[2]/div/tz-dynamic-carousel/div/section/ul/li[2]/a/div[2]'),
        "kaufland": ("XPATH", '/html/body/div[2]/main/tz-partners/div/div[2]/div[1]/a'),
        "bauturi": ("XPATH", '/html/body/div[2]/main/tz-widget-partner-departments/div/div/div/div/div/div/div/div/div/a[8]'),
        "apa": ("XPATH", '/html/body/div[2]/main/div[3]/div/div/div/div/div/a[1]')

    }


    def supermarket_select(self):
        self.supermarket.click()

    def kaufland_select(self):
        self.kaufland.click()


    def bauturi_select(self):
        self.bauturi.click()


    def apa_select(self):
        self.apa.click()
