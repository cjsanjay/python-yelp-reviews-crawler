import urllib2
import urllib
import re,random,time
import os 
from BeautifulSoup import BeautifulSoup,Comment
from pyquery import PyQuery as pq
from lxml import etree
from datetime import datetime
import json
from selenium import webdriver
browser = webdriver.Firefox()  
    
#crawler script to crawl and collect page urls
#uses input file generated from get_yelp_Data.py
#output in reviews folder
def fetchPages():
    in_file=open("yelp_data_final","r")
    data=in_file.read()
    json_data=json.loads(data)
    for each_d in json_data:       
        print "processed id:",each_d['id']
        if each_d['id']>297:
            url=each_d['url']            
            browser.get(url)
            html_doc=browser.page_source
            index = random.randint(20, 60)
            time.sleep(index)
            try:
                soup = BeautifulSoup(html_doc)
                html_data=str(soup)
                out_file=open("reviews/"+str(each_d['id'])+".txt","w")
                bs=BeautifulSoup(html_data)
                mydivs = bs.findAll("div", { "class" : "review-content" })
                for each_mydiv in mydivs:
                    try:
                        out_file.write(str(each_mydiv.text).encode('utf-8'))  
                        out_file.write("\n")        
                    except:                        
                        continue    
                out_file.close()
            except:
                print "skipping :",each_d['id']
                continue

fetchPages()                
