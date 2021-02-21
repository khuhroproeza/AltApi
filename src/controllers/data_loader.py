import json
import sys
from natsort import natsorted


def json_loader(reverse_list: bool = False):

    data_path = sys.path[0] + "/AltScraper/AltScraper/spiders/items.json"
    data_crafts = None

    try:
        with open(data_path, "r") as json_file:
            data_crafts = json.loads(json_file.read())
    except OSError as err:
        error = "Data not scraped, or path:{0} not set properly".format(data_path)
        return [error]
    except ValueError:
        error = "Could not get the values"
        return [error]
    except:
        error = "Unexpected error:", sys.exc_info()[0]
        return [error]
    try:
        data_crafts = data_crafts[0]["names"]
    except:
        return ["Scrapped file Empty"]
    return natsorted(data_crafts, reverse=reverse_list)
