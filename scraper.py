from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

STARTURL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(STARTURL)
time.sleep(10)
def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planetdata = []
    for i in range(0,202):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs = {"class", "exoplanet"}):
            litags = ultag.find_all("li")
            templist = []
            for index,litags in enumerate(litags):
                if index == 0:
                    templist.append(litags.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(litags.contents[0])
                    except:
                        templist.append("")
            planetdata.append(templist)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerow(headers) 
        csvwriter.writerows(planetdata)
scrape()