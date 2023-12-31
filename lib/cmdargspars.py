import argparse
from lib.log import agent


class CmdArgsParse:
    def cmdargs(self):
        parser = argparse.ArgumentParser()
        parser.description = "Detect XSS vulnerability in Web Applications "
        parser.add_argument("-u", dest="url", type=str, help="target URL (e.g. \"http://www.site.com/vuln.php?id=1\")",
                            required=True)
        parser.add_argument("-p", dest="payload", metavar="PAYLOAD", help="payload for test", default=None)
        parser.add_argument("--cookie", dest="cookie", help="HTTP cookie header value (e.g. \"PHPSESSID=a8d127e..\")",
                            default='''{"ID":"1094200543"}''', metavar="")
        parser.add_argument("--referer", dest="referer", help="HTTP referer header value")
        parser.add_argument("--method", metavar="",
                            help="Method setting(s): \n\t0: GET\n\t1: POST\n\t2: GET and POST (default)", default=2,
                            type=int)
        parser.add_argument("--data", dest="postdata", help=" Data string to be sent through POST ")
        parser.add_argument("--timeout", default=5, help="Connection timeout（default.. 5s）")
        parser.add_argument("--single", metavar="", help="Single scan. No crawling just one address")
        parser.add_argument("--proxy", help="Use a http proxy to connect to the target URL（e.g. \"127.0.0.1:8080\"）",
                            default=None)
        parser.add_argument("--user-agent", metavar="", help="Request user agent (e.g. Chrome/2.1.1/...)",
                            default=agent)
        return parser.parse_args()
