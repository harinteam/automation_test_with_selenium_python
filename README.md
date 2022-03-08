# automation_test_with_selenium_python
learn automation test with selenium python


# test scenario automation we want to try :
  - Given us google home page
  - when we search for "remote worker id"
  - Then we should see search result of "remote worker id"
  - 
# Step by step :

  - Install python on you mac 
  - install venv in vscode : piython3 -m venv yourvenvname
  - install web driver manager : pip install webdriver-manager
  - install selenium, on you mac terminal type : pip install selenium
  - import webdriver :
    ### selenium 4
      from selenium import webdriver
      from selenium.webdriver.chrome.service import Service
      from webdriver_manager.chrome import ChromeDriverManager
      from webdriver_manager.utils import ChromeType

      driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
      
      ![import selenium chrome driver](https://i.ibb.co/bsDkdzB/carbon.png)
      
      
