from selenium import webdriver
import time
import requests

# insert the websites page number
maximumPages = 8

driver = webdriver.Chrome()

link = 'insert your link here'

scrollAmount = 500


def navigateToLink(url):
    driver.get(url)
    s = 0
    for i in range(5):
        s += scrollAmount
        driver.execute_script("window.scrollTo(0, %s);" % s)
        time.sleep(2)


navigateToLink(link)

streams = []
pageNumber = 1
i = 1
for index in range(100):
    try:
        driver.switch_to.frame(i)
    except:
        print(i)

        pageNumber += 1
        if pageNumber == maximumPages + 1:
            break

        newlink = link + '{}/'.format(pageNumber)
        print(newlink)
        navigateToLink(newlink)
        i = 1
        continue
    try:
        element = driver.find_element_by_tag_name('audio')
    except:
        continue

    source = element.get_attribute('src')
    source = source[:-1]
    streams.append(source)
    print(source)
    driver.switch_to.default_content()

    i += 1

print(streams)

downloadIndex = 1
for url in streams:
    r = requests.get(url)
    open('Chapter %s.mp3' % downloadIndex, 'wb').write(r.content)
    downloadIndex += 1
