
# přidej selenium a importuj webdriver

from selenium import webdriver

# zadej stránku ze které chceš získat data
url = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch'

# nainstaluj webdriver na prohlížeč který používáš a přejdi na stránku
browser = webdriver.Edge(r"C:\Users\Tomi\msedgedriver.exe")
browser.get(url)
# klikni na souhlasím
browser.find_element_by_xpath('//*[@id="consent-page"]/div/div/div/div[2]/div[2]/form/button').click()

# ukaž cenu tbc na internetu a poté ji napiš do konsole
tbc_value = (browser.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').get_attribute("textContent"))
print(tbc_value)
browser.quit()


