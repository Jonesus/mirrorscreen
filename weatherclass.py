import xml.etree.ElementTree as ET
from urllib.request import urlopen
import dryscrape
from bs4 import BeautifulSoup
import textwrap


class weatherobj:
    
    '''
    Class used to fetch weatherdata for mirror.
    
    Includes methods for updating sunrise and sunset, fetching latest
    weather observation and fetching a forecast for next 15 hours.
    '''
    
    def __init__(self):
        
        # Fetch data from OpenWeatherMap and parse into usable XML
        
        self.defaulthtml = urlopen("http://api.openweathermap.org/data/2.5/" + \
                       "weather?q=Helsinki,fi&units=metric&mode=xml" + \
                       "&appid=9540e786751fb775e2f1bf34065b3af7", timeout = 5).read()
        
        self.defaulthtmlstring = self.defaulthtml.decode('utf-8')
        self.currentxml = ET.fromstring(self.defaulthtmlstring)
        
        
        
    def get_rise_set(self):
        
        # Sets today's sunrise and sunset time
        
        self.sunrise = self.currentxml[0][2].attrib["rise"][11:-3]
        self.sunset = self.currentxml[0][2].attrib["set"][11:-3]
    
    
    
    def get_current(self):
        
        # Returns a list of current temperature, wind speed and picture for weather
    
        html = urlopen("http://api.openweathermap.org/data/2.5/" + \
                       "weather?q=Helsinki,fi&units=metric&mode=xml" + \
                       "&appid=9540e786751fb775e2f1bf34065b3af7", timeout = 5).read()
        htmlstring = html.decode('utf-8')
        currentxml = ET.fromstring(htmlstring)
        
        self.sunrise = self.currentxml[0][2].attrib["rise"][11:-3]
        self.sunset = self.currentxml[0][2].attrib["set"][11:-3]
        
        temp = currentxml[1].attrib["value"]
        wspd = currentxml[4][0].attrib["value"]
        picno = currentxml[8].attrib["icon"]
        
        return [picno + ".bmp", temp + "°", wspd]
        
    
    
    def get_forecast(self):
        
        # Returns a two dimensional list with forecast for 15 hours forward and
        # pictures for weather conditions
        
        html = urlopen("http://api.openweathermap.org/data/2.5/" + \
                       "forecast?q=Helsinki,fi&units=metric&mode=xml" + \
                       "&appid=9540e786751fb775e2f1bf34065b3af7", timeout = 5).read()
        
        htmlstring = htmlstring = html.decode('utf-8')
        forecastxml = ET.fromstring(htmlstring)
        out = []
        
        for i in range(1,6):
            time = forecastxml[4][i].attrib["to"][11:-3]
            temp = forecastxml[4][i][4].attrib["value"]
            timesymbol = "d" if int(self.sunrise[:2])+2 <= int(time[:2]) <= int(self.sunset[:2])+2 else "n"
            picno = forecastxml[4][i][0].attrib["var"][:2] + timesymbol
            
            out.append([picno + ".bmp", time + " " + temp + "°"])
            
        return out
    
    
    
    def get_events(self):
        
        # Returns a list of every event in minnenyt.fi's website minus ongoing movies
        
        # Following code by Sharuzzaman Ahmat Raslan from StackOverflow:
        ###
        
        # make sure you have xvfb installed
        dryscrape.start_xvfb()
        
        
        # set up a web scraping session
        sess = dryscrape.Session()
        
        # we don't need images
        sess.set_attribute('auto_load_images', False)
        
        # visit homepage and search for a term
        sess.visit('http://www.minnenyt.fi/#main-open/tanaan/')
        response = sess.body()
        soup = BeautifulSoup(response)
        
        ###
        # end
        
        
        event = soup.find('div',{'class':'event-info'})
        
        eventlist = [["" for x in range(15)] for y in range(500)]
        
        runner = 0
        
        while event != None:
            wrap = textwrap.wrap(event.h2.text, width = 50)
            if len(wrap) == 1:
                wrap.append(" ")
            elif len(wrap) >= 3:
                wrap[1] = wrap[1][:47]
                wrap[1] += "..."
            eventlist[runner][0] = wrap[0]
            eventlist[runner][1] = wrap[1]
            
            if event.p != None:
                wrap = textwrap.wrap(event.p.text, width = 40)
                for i in range(len(wrap)):
                    try:
                        eventlist[runner][i+2] = wrap[i]
                    except:
                        eventlist[runner][i] += "..."
                        break
            else:
                wrap = []
                
            eventtext = event.parent.find('div',{'class':'date'}).text
            if len(wrap) <= 13:
                eventlist[runner][len(wrap)+2] = eventtext if eventtext[0] != " " \
                                                else eventtext[1:]
            else:
                eventlist[runner][14] = eventtext if eventtext[0] != " " \
                                                else eventtext[1:]
            
            event = event.find_next('div',{'class':'event-info'})
            runner += 1
            
        filteredlist = [event for event in eventlist if event[0] != ""]
        
        lenrange = len(filteredlist)
        x = 0
        while x < lenrange:
            filteredlist[x] = [line for line in filteredlist[x]]
            for line in filteredlist[x]:
                if ("Elokuvat" in line) or ("elokuva" in line):
                    del filteredlist[x]
                    lenrange -= 1
                    x -= 1
            x += 1        
            
            
            
        return filteredlist
        


# Debugging prints not in use
'''
old = []
        
saa = weatherobj()
    
lista = saa.get_current()


for alkio in lista:
    for rivi in alkio:
        print(rivi)
    print()
'''     

        
        
        
        
        