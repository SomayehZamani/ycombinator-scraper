# ycombinator Scraper
This is a python repository aims to scrape list of ycombinator's companies and save them in a .csv file

This repositroy srcapes companies' information in two steps; 1)at the first step it searches for available webpages of companies on the ycombinator website and saves urls of valid webpages to scrape information from each of them later on. 2) at the second step, for each valid url it extracts interesting information of the related company( e.g. name, location, foundation year, etc.)

## Install

To run this source code please install required libraries
```shell
 pip install -r requirements.txt 
```
## Usage

You can scrape and save information of companies with id numbers in range [start id, end id] using the following command line:
```shell
	python main.py --sid <start id> --eid <end id>
```
For example, if you want to scrape information of companies with id in range [5, 10] you can run the command line below :

```shell
	python main.py --sid 5 --eid 10
```

This command first saves valid urls of companies with id in range [start id, end id] to working_urls_{start id}-{end id}.csv file and then extracts and saves information to yclist_{number of companies}.csv file


You can also do these two steps separately by running the following command lines:

```shell
	python get_urls.py --sid <start id> --eid <end id>
```

This command saves valid urls of companies with id in range [start id, end id] to working_urls_{start id}-{end id}.csv file

```shell
	python scrape.py -path <path of working urls>
```

This command extracts information of companies and saves them to yclist_{number of companies}.csv file
