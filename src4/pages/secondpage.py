from seleniumpagefactory.Pagefactory import PageFactory


class SecondPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "mall": ("XPATH", '/html/body/div[2]/main/div/tz-widget-partner-types/div/div[2]/div/tz-dynamic-carousel/div/section/ul/li[4]/a'),
        "mobiup": ("XPATH", '/html/body/div[2]/main/tz-partners/div/div[2]/div[6]/a'),
        "cabludate": ("XPATH", '/html/body/div[2]/main/tz-widget-market/div/div/div/div/div/a[3]')




    }


    def mall_select(self):
        self.mall.click()

    def mobiup_select(self):
         self.mobiup.click()


    def cabludate_select(self):
        self.cabludate.click()