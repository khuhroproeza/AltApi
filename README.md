# DataScrapingApi
## _Readme Guide_

DataScrapingApi project scraps the data from  [cNet Website](https://www.cnet.com/pictures/star-wars-spaceships-ranked-by-power-speed/2/) to retrieve the data of starwars
aircrafts as per their hyperdrive rating.


## Features

- Scrapy scraper used to scrap the data
- Json used as Database setup
- FastApi to handle Api requests
- Returns List of StarWars Ships as per their hyperdrive rating in ascending or descending order.
- Error handling in case scraping returns error.



## Tech

Dillinger uses a number of open source projects to work properly:

- [FastApi] - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- [Scrapy] - Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages.
- [Uvicorn] - Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.


## Installation


For Installing virtual env

```sh
python3 -m venv envalt
source venv/bin/activate
```

Install the dependencies and start the server.

```sh
cd AltApi
pip3 install -r requirements.txt
./run.sh
```

#### How to use Api

App is hosted on 0.0.0.0 and port=8014

FastApi routes can be accessed by opening:
```sh
http://0.0.0.0:8014/docs
```

Request can be made by clicking the get route and further clicking try it out. Upon clicking "Execute" a get request would be made to the api to fetch the Data. Order of Arrangement can be set by clicking descending boolean value. Default is false.

## WorkFlow

Bash file 
```sh
./run.sh
```

- First locates for any previous items.json file if available the file is deleted.
- Scrapy scraper is started to scrap the data from the link.
- Scraped data is saved in "items.json"
- After scraping is done, FastApi service is initiated.
- After get request initiation, data is cleaned and sent back as json payload.




