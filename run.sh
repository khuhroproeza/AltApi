#!/bin/sh
rm ./AltScraper/AltScraper/spiders/items.json
(cd ./AltScraper/AltScraper/spiders; scrapy crawl starwars -o items.json)
gunicorn main:app -b :8014 --reload -k uvicorn.workers.UvicornWorker