from IPython import display
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from selenium.webdriver import ActionChains

import requests
import bs4
import tkinter
import webbrowser

def open_url(url):
    #Open the URL in a browser
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    return

def create_popup(url):
    root = tkinter.Tk()
    text = "Product is now AVAILABLE!"

    label = tkinter.Label(root, text=text)
    label.pack()

    test = tkinter.Button(root, text="Click me!",
              command = open_url(url))
    test.pack()
    root.test = test

    quit = tkinter.Button(root, text="QUIT", command = root.destroy)
    quit.pack()

    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

    return



# driver.get(url)

# Maximize the browser window
# driver.maximize_window()


# accept_buttons = driver.find_elements_by_xpath("//div[@class='meta-blue-text']")
def fetch_prettify(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    prettified_soup = soup.prettify()
    return prettified_soup

# display.display(prettified_soup)
def parse_and_check(url, prettified_soup):
    #i = 0
    #while (("We’re sorry this item is not available" in prettified_soup) and (i < 2)):
    while "We’re sorry this item is not available" in prettified_soup:
        print("product was not available. Sleeping for a while!")
        sleep(500)
        #i += 1
        continue
    create_popup(url)

def main():
    url = 'https://abbottstore.com/infant-and-child/similac/similac-pro-advance/similac-pro-advance-infant-formula-ready-to-feed-1341/similac-pro-advance-infant-formula-ready-to-feed-1-qt-bottle-case-of-6-64248.html'
    prettified_soup = fetch_prettify(url)

    parse_and_check(url, prettified_soup)

    return()


if __name__ == "__main__":
    main()
