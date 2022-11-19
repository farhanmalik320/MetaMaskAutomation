from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options= ChromeOptions()
chrome_options.add_extension("meta.crx")

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s, options=chrome_options)

chrome_options= ChromeOptions()
chrome_options.add_extension("meta.crx")

def setURL():
  #open the url in the browser
  current_url = driver.get("https://google.com")
  driver.maximize_window()

def MetaMaskSetup():

    driver.switch_to.window(driver.window_handles[0])

    # clicking on get started button
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "first-time-flow__button")))
    get_started_button = driver.find_element(By.CLASS_NAME, "first-time-flow__button")
    get_started_button.click()

    # clicking on i agree button
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "page-container__footer-button")))
    i_agree = driver.find_element(By.CLASS_NAME, "page-container__footer-button")
    i_agree.click()

    # clicking on import wallet button
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "first-time-flow__button")))
    import_wallet = driver.find_element(By.CLASS_NAME, "first-time-flow__button")
    import_wallet.click()

    i=0
    j=0
    length=12
    words=["Your phrase" ]

    while i<12:
        #Seedphrasefirstword
        driver.find_element(By.ID, "import-srp__srp-word-" + str(i)).send_keys(words[j])
        i+=1
        j+=1

    # passwordfield
    driver.find_element(By.ID, "password").send_keys("Farhan@1234")

    # confirmpassword
    driver.find_element(By.ID, "confirm-password").send_keys("Farhan@1234")

    # clickoncheckbox
    driver.find_element(By.ID, "create-new-vault__terms-checkbox").click()

    # importbutton
    driver.find_element(By.CLASS_NAME, "create-new-vault__submit-button").click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "first-time-flow__button")))

    # alldonebutton
    get_started_button = driver.find_element(By.CLASS_NAME, "first-time-flow__button")
    get_started_button.click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "chip__left-icon")))

    # network dropdown
    click_network = driver.find_element(By.CLASS_NAME, 'chip__left-icon').click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "network__add-network-button")))

    # click on addnetwork
    add_network = driver.find_element(By.CLASS_NAME, 'network__add-network-button').click()

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "form-field__input")))
    # add the text on all the required fields on add network page

    network_name = driver.find_elements(By.CLASS_NAME, 'form-field__input')
    network_name[0].send_keys('Mumbai Testnet')
    network_name[1].send_keys('https://rpc-mumbai.maticvigil.com/')
    network_name[2].send_keys('80001')
    network_name[3].send_keys('MATIC')
    network_name[4].send_keys('https://mumbai.polygonscan.com/')

    save_btn = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

def transferfunds():

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.currency-display-component__text')))

    time.sleep(1)
    amount = driver.find_element(By.CSS_SELECTOR, '.currency-display-component__text').text
    print(amount)

    time.sleep(5)
    # select the send button
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#asset/MATIC')

    amount = driver.find_element(By.CSS_SELECTOR, '.currency-display-component__text').text
    print(amount)

    time.sleep(2)

    if str(amount) > str(0):
        driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#send')
        driver.find_element(By.CLASS_NAME, 'ens-input__wrapper__input').is_displayed()
        driver.find_element(By.CLASS_NAME, 'ens-input__wrapper__input').send_keys('0x1dBe3C8444f225f86F225f52F24a8298850aAA27')
        time.sleep(2)

        driver.find_element(By.CLASS_NAME, 'unit-input__input').send_keys('0.01')

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn--rounded.btn-primary")))

        next_btn = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn--rounded.btn-primary")))

        confirm_button = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

        time.sleep(5)

        transactions = driver.find_elements(By.CLASS_NAME, 'transaction-list-item')
        transactions[0].click()

        explorer = driver.find_element(By.CLASS_NAME, 'btn-link').click()

setURL()
MetaMaskSetup()
transferfunds()


























