from seleniumpagefactory.Pagefactory import PageFactory


class FirstPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {

        "cookies": ("XPATH", '/html/body/tz-cookie-consent/div/div[2]'),
        "iasi": ('XPATH', "//a[@href='https://tazz.ro/iasi/oras']"),
        "adaugaadresa": ("XPATH", '/html/body/header/tz-header-box/div/div[1]/tz-address-box/div[1]/div[1]'),
        "adresaadd": (
            "XPATH", '/html/body/header/tz-header-box/div/div[1]/tz-address-box/div[1]/div[2]/div[2]/div/div[1]'),
        "locatie": ("XPATH",
                    '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-search/div[1]/div[1]/input'),
        "locatiselect": ("XPATH",
                         '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-search/div[1]/div[2]/div/div[2]/div[1]'),
        "confirm": ("XPATH",
                    '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-map/div/div[3]/div[2]'),
        "detalii": ("XPATH",
                    '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-map/div/div[2]/div[2]/div/div[2]/textarea'),
        "acasa": ("XPATH",
                  '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-map/div/div[2]/div[2]/div/div[4]/div[1]'),
        "save": ("XPATH",
                 '/html/body/tz-dialog/div[1]/div/div[2]/div/tz-address-dialog/div/tz-address-dialog-map/div/div[2]/div[2]/div/div[5]/div')

    }



    def cookies_select(self):
        self.cookies.click()

    def iasi_select(self):
        self.iasi.click()

    def adresa_select(self):
        self.adaugaadresa.click()

    def adressadd_select(self):
        self.adresaadd.click()

    def locatie_text(self):
        self.locatie.send_keys("strada Anastasie Panu 2")

    def locatie_select(self):
        self.locatiselect.click()

    def confirm_select(self):
        self.confirm.click()

    def detalii_text(self):
        self.detalii.send_keys("scara D, bloc C3, etaj 12, interfon 48")

    def acasa_select(self):
        self.acasa.click()

    def save_select(self):
        self.save.click()