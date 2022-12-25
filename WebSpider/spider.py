#!/usr/bin/env python

import requests # HTTP requests to a specified URL
import re       #Regex
import urllib.parse #This module defines a standard interface to break URL strings up in components 
import argparse # UserInput  Handling


#ASCII ART File Path
f = open("art.txt","r")
print(f.read())

# Handling Input from user
def Agrument():
    parse=argparse.ArgumentParser()
    parse.add_argument("-t",dest="target_url",help="Target URL. eg, -t 123abc.com")
    opt=parse.parse_args()
    if not opt.target_url:
        parse.error("[-] Please Enter Target URL ")
    return opt
   
# calling function for user handling   
opt=Agrument()
target=opt.target_url
# Empty list to append 
target_links =[]


print("____________________________________________________\n")
print("[*] Press CTRL + C to Exit.")
print("\n[*] Start Mapping...\n")
print("Target: ",target)
print("____________________________________________________\n")


def extract_link(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', str(response.content))

# crawler Function 
def crawl(url):   
    try:
        href_link = extract_link(url)
        for link in href_link:
            link=urllib.parse.urljoin(url,link)
            # filtering link in scope only
            if '#' in link:
                link=link.split('#')[0]

            if url in link and link not in target_links:
                target_links.append(link)
                print("[+]",link)
                crawl(link) #recurssion
    except KeyboardInterrupt:
        print("[+] Exiting...")

# calling Function
crawl(target)