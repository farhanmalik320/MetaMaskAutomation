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
  current_url = driver.get("https://pancakeswap.finance/?chainId=1")
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
    words=["your phrase words"]

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

def addnetwork():

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

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn--rounded.btn-primary")))
    git_it = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

    time.sleep(5)

def selectnetwork():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "chip__left-icon")))

    driver.find_element(By.CLASS_NAME, 'chip__left-icon').click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "network-dropdown-content--link")))

    driver.find_element(By.CLASS_NAME, 'network-dropdown-content--link').click()

    time.sleep(5)

    options = driver.find_elements(By.CLASS_NAME, 'settings-page__content-item-col')

    # This should print 16
    print(len(options))

    # Start the loop
    for i in range(7, len(options)):
        options[7].click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "chip__left-icon")))

    driver.find_element(By.CLASS_NAME, 'chip__left-icon').click()

    time.sleep(5)

    # select network
    networks = driver.find_elements(By.CLASS_NAME, 'color-indicator__inner-circle')
    networks[2].click()

    time.sleep(5)

    # Open the metamask
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')


def pancakeswap():

    driver.switch_to.window(driver.window_handles[1])
    # driver.get('chrome-extension://{}/popup.html'.format(EXTENSION_ID))

    # CLick on metamask button
    connect_btn = driver.find_element(By.XPATH, "//div[contains(text(),'Connect Wallet')]").click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='portal-root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/img[1]")))

    connect_btn = driver.find_element(By.XPATH, "//body/div[@id='portal-root']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/img[1]").click()

    time.sleep(5)
    EXTENSION_ID = 'nkbihfbeogaeaoehlefnkodbefgpgknn'

    driver.switch_to.window(driver.window_handles[0])

    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'.format(EXTENSION_ID))

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
    # NextButton
    next = driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn--rounded.btn-primary")))
    # connect button
    connect_wallet = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

    time.sleep(2)
    # change it to pancake swap
    driver.switch_to.window(driver.window_handles[1])

    # click on trade from menu
    driver.find_element(By.CSS_SELECTOR,
                        'div.sc-80277dc0-0.leLMTT.ggzm1z0._1nzuaz71yo._1nzuaz71zq:nth-child(2) div.sc-80277dc0-2.nZpXm:nth-child(1) nav.sc-80277dc0-1.PiKAT div.sc-b492d839-1.sc-32d5f017-0.gEMDyZ.fOPopv:nth-child(1) div.ggzm1z0._1nzuaz710._1nzuaz72 div.sc-b492d839-1.sc-32d5f017-0.cdfIDa.fOPopv div.sc-b492d839-1.EYAtR:nth-child(1) div.sc-b492d839-1.gEMDyZ > div.sc-437c0afe-0.iFWbsi').click()

    time.sleep(5)

    print("Test Case Completed successfully")

    driver.quit()

setURL()
MetaMaskSetup()
#addnetwork()
#selectnetwork()
pancakeswap()



























