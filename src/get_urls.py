# Importing all necessery packages
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error
import pandas as pd
from tqdm import tqdm

import argparse



def check_and_save_availabel_urls(start_id, end_id):
    
    '''
    Parmas:

        start_id: start point of id interval that we check for validity
        end_id  : end point of id interval that we check for validity

        [start_id,end_id] is a Id interval that we check their availabilities on the ycombinator website

    Output:
        a csv file containing list of valid urls of companies' page on the ycombinator
    '''
    cheking_ulrs = ["https://www.ycombinator.com/companies/" + str(id) for id in range(start_id,end_id+1)]
    ULRS_PATH = "working_urls_{}-{}.csv".format(str(start_id), str(end_id))


    #check if each url is valid and the http request returns 200 code
    working_urls=[]
    with tqdm(total = len(cheking_ulrs)) as pbar:
        for i, url in enumerate(cheking_ulrs):
            try:
                pbar.update(1)
                _ = urllib.request.urlopen(url)
            except urllib.error.HTTPError as e:
              # Return code error 
              print('iter{} - HTTPError: {}'.format(i, e.code))
            except urllib.error.URLError as e:
              # Url error
              print('iter{} - URLError: {}'.format(i, e.reason))
            else:
              # url is ok
              working_urls.append(url)
    df_working_urls = pd.DataFrame(working_urls)
    #since this process is time consuming we save its result
    df_working_urls.to_csv(ULRS_PATH)

    
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Checking valid urls ...')
    parser.add_argument('-s', '--sid', required=True, 
                   help='start id for checking validity of companies\' urls')
    parser.add_argument('-e', '--eid', required=True, 
                   help='end id for checking validity of companies\' urls')

    args = parser.parse_args()
    check_and_save_availabel_urls(int(args.sid), int(args.eid))
