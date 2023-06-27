from lib.log import *
from lib.cmdargspars import CmdArgsParse
from lib import connect
from lib import crawl
from main import core
import sys


def start():
    args = CmdArgsParse().cmdargs()
    print(logo)

    Log.info("Starting...")
    if connect.check_url() == 0:
        sys.exit()
    if args.payload == 'full':
        payloads = core().read_payload_list()
        for payload in payloads:
            if args.single:
                core.main(args.url, args.proxy, args.user_agent, payload,
                          args.cookie, args.method)
            else:
                Log.info("Crawling...")
                urls = crawl.crawl(args.url)
                for url in urls:
                    core.main(url, args.proxy, args.user_agent, payload, args.cookie, args.method)

    elif args.payload is None:
        payload = core.generate(2)
        if args.single:
            core.main(args.url, args.proxy, args.user_agent, payload,
                      args.cookie, args.method)
        else:
            Log.info("Crawling...")
            urls = crawl.crawl(args.url)
            for url in urls:
                core.main(url, args.proxy, args.user_agent, payload,
                          args.cookie, args.method)
    else:

        if args.single:
            core.main(args.url, args.proxy, args.user_agent, args.payload,
                      args.cookie, args.method)
        else:
            Log.info("Crawling...")
            urls = crawl.crawl(args.url)
            for url in urls:
                core.main(url, args.proxy, args.user_agent, args.payload,
                          args.cookie, args.method)



if __name__ == "__main__":
    start()
