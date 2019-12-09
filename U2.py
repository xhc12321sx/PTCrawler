from spider.spider import u2spider
import time
import random


if __name__ == "__main__":
    cookie = [
    {
        "domain": "u2.dmhy.org",
        "name": "PHPSESSID",
        "value": "683e9ca68ec7e23ec6d6711d0ab40ab4",
        }, 
        {
            "domain": ".dmhy.org",
            "name": "__cfduid",
            "value": "ddf8e87e35543daaa82a7a8642e93c5ec1575669957",
        }, 
        {
            "domain": "u2.dmhy.org",
            "name": "nexusphp_u2",
            "value": "668a2ede564b45e05daa400b17d288ec983642f1a64626bd79a2ce222aecd5ce624612cbae43aa6b0e7cd0bddd3281a1",
        }
        ]
    print("Setting up browser...")

    a = u2spider(cookie)
    while 1:
        a.parse_page()

        sleeptime = random.randint(10 * 60, 20 * 60)
        print("Next refresh: {0} mins".format(sleeptime/60))
        time.sleep(sleeptime)
