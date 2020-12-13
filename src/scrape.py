# Importing all necessery packages
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error
import pandas as pd
from tqdm import tqdm
import re
import argparse


def get_urls(path ):
    temp_urls = pd.read_csv(path)
    temp_urls.columns = ["index", "links"]
    urls = temp_urls["links"].values.tolist()
    return urls



def scrape(urls_path):
    '''
    Parmas:

        urls_path: path to the csv file containing list of valid urls of companies' page on the ycombinator
    Output:
        a csv file containing list of companies' information
    '''

    
    csv_titles = ["NAME",
                  "FOUNDATION YEAR",
                  "SIZE",
                  "LOCATION",
                  "BATCH",
                  "SHORT DESC",
                  "LONG DESC",
                  ]

    result = pd.DataFrame(columns=csv_titles)
    data=[]
    urls = get_urls(urls_path)
    with tqdm(total = len(urls)) as pbar:
        for url in urls:
            request = requests.get(url)
            text = request.text
            soup = BeautifulSoup(text, "html.parser")

            # we refer to html file of one of companies to find class name of each part
            # by referring we found that
            #  #company's name is mentioned by h1 tag and class='heavy'
            #  #short description is mentioned by h3 tag
            #  #long description is mentioned by p tag


            name = (soup.find("div", {"h1", "heavy"})).get_text(strip=True)
            short_description = (soup.find("h3").get_text(strip=True))
            long_description = (soup.find("p").get_text(strip=True))

            #The other information are under class="highlight-box"
            details = (soup.find(("div"), ("highlight-box"))).get_text(strip=True)
            #Here we extract information from details using regular expression since all companies'
            # detail follow this expression style
            # e.g CircuitHubFounded2012Team Size30LocationLondon, United Kingdom
            match_obj = re.match(r'(.*)Founded(\d*)Team Size(\d*)Location(.*)', details, re.M | re.I)

            year = match_obj.group(2)
            size = match_obj.group(3)
            location = match_obj.group(4)
            # batch is mentioned by class = pill pill-orange
            batch = (soup.find(("span"), ("pill pill-orange"))).get_text(strip=True)
            dict = {
                "NAME": name,
                "FOUNDATION YEAR": year,
                "SIZE": size,
                "LOCATION": location,
                "BATCH": batch,
                "SHORT DESC": short_description,
                "LONG DESC": long_description,
                }
            data.append(dict)
            pbar.update(1)
    #save result
    result= result.append(pd.DataFrame.from_records(data, columns=dict.keys()))
    result.to_csv("yclist_{}.csv".format(str(len(urls))))
    print(" The result has been saved to ", "yclist_{}.csv".format(str(len(urls))))
    
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Scrape companies\' info ...')
    parser.add_argument('-p', '--path', required=True, 
                   help='path to the companies\' urls')
    
    args = parser.parse_args()
    scrape(args.path)

