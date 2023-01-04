from seleniumpagefactory.Pagefactory import PageFactory


class SecondPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "bauturitutun": ("XPATH", '/html/body/div[2]/main/div/tz-widget-partner-types/div/div[2]/div/tz-dynamic-carousel/div/section/ul/li[3]/a'),
        "hora": ("XPATH", '/html/body/div[2]/main/tz-partners/div/div[2]/div[4]/a'),
        "tarie": ("XPATH", '/html/body/div[2]/main/tz-widget-market/div/div/div/div/div/a[2]')




    }


    def bauturitutun_select(self):
        self.bauturitutun.click()

    def hora_select(self):
         self.hora.click()


    def tarie_select(self):
        self.tarie.click()


