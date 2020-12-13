from get_urls import check_and_save_availabel_urls
from scrape import scrape
import argparse


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Checking valid urls ...')
    parser.add_argument('-s', '--sid', required=True, 
                   help='start id for checking validity of companies\' urls')
    parser.add_argument('-e', '--eid', required=True, 
                   help='end id for checking validity of companies\' urls')

    args = parser.parse_args()
    check_and_save_availabel_urls(int(args.sid), int(args.eid))
    urls_path = "working_urls_{}-{}.csv".format(str(args.sid), str(args.eid))
    scrape(urls_path)
    

