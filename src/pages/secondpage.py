from seleniumpagefactory.Pagefactory import PageFactory


class SecondPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "restaurante": ("XPATH", '/html/body/div[2]/main/div/tz-widget-partner-types/div/div[2]/div/tz-dynamic-carousel/div/section/ul/li[1]/a/div[2]'),
        "filter": ("XPATH", '/html/body/div[2]/main/tz-partners-filters/div/div/div[2]/tz-filters-dialog/div'),
        "burger":("XPATH",'/html/body/tz-dialog/div[1]/div/div[2]/div/tz-filters-dialog/div/div[1]/div[2]/div[2]/div[2]/label'),
        "livrare_tazz":("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-filters-dialog/div/div[1]/div[1]/div[2]/div[11]/label'),
        "aplica":("XPATH", '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-filters-dialog/div/div[2]/button')

    }

    def restaurante_select(self):
        self.restaurante.click()

    def filter_select(self):
        self.filter.click()


    def burger_select(self):
        self.burger.click()

    def livraretazz_select(self):
        self.livrare_tazz.click()


    def aplica_click(self):
        self.aplica.click()