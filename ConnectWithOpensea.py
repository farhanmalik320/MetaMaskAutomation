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
  current_url = driver.get("https://testnets.opensea.io/")
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
    words=["your phrase"]

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

    time.sleep(3)

    options = driver.find_elements(By.CLASS_NAME, 'settings-page__content-item-col')

    # This should print 16
    print(len(options))

    # Start the loop
    for i in range(7, len(options)):
        options[7].click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, "chip__left-icon")))

    driver.find_element(By.CLASS_NAME, 'chip__left-icon').click()

    time.sleep(3)

    # select network
    networks = driver.find_elements(By.CLASS_NAME, 'color-indicator__inner-circle')
    networks[2].click()


def connectwallet():

    # switch to uniswap
    driver.switch_to.window(driver.window_handles[1])

    # CLick on metamask button
    wallet_btn = driver.find_element(By.XPATH, "//i[contains(text(),'account_balance_wallet')]").click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'MetaMask')]")))

    metamask_btn = driver.find_element(By.XPATH, "//span[contains(text(),'MetaMask')]").click()

    time.sleep(5)

    driver.switch_to.window(driver.window_handles[0])

    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
    # NextButton
    next = driver.find_element(By.CLASS_NAME, 'btn-primary').click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn--rounded.btn-primary')))

    connect_wallet = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

    time.sleep(2)
    # change it to opensea
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(5)

    # time.sleep(5)

    # accpet_sign= driver.find_element(By.XPATH,"//button[contains(text(),'Accept and sign')]").click()

    #time.sleep(5)

    #driver.switch_to.window(driver.window_handles[0])

    #driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')

    #time.sleep(5)

    #switch_network = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

def purchaseNFT():
    # open the NFT
    driver.get(
        'https://testnets.opensea.io/assets/goerli/0xf4910c763ed4e47a585e2d34baa9a4b611ae448c/13453191221977235658492620070148485862678800902474289814882130172116165722113')

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dqdDEM')))

    # Click on add to cart
    driver.find_element(By.CLASS_NAME, 'dqdDEM').click()

    time.sleep(2)

    add_to_cart_btn=driver.find_elements(By.CLASS_NAME, 'NavItem--withIcon')
    add_to_cart_btn[1].click()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CLASS_NAME,'ikQpYW')))

    complete_purchase= driver.find_element(By.CLASS_NAME,'ikQpYW').click()

    time.sleep(10)

    # change to metmask
    driver.switch_to.window(driver.window_handles[0])

    # Open the metamask
    driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn--rounded.btn-primary')))

    confirm_button = driver.find_element(By.CSS_SELECTOR, '.btn--rounded.btn-primary').click()

    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])

setURL()
MetaMaskSetup()
#addnetwork()
selectnetwork()
connectwallet()
purchaseNFT()



























