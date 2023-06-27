import requests
from lib.cmdargspars import CmdArgsParse
from lib.log import Log

def check_url():
    Log.info('testing connections')
    args = CmdArgsParse().cmdargs()
    try:
        response = requests.get(args.url)
        if response.status_code == 200:
            Log.info("connected success")
            return 1
    except:
        Log.warning('unable to connect')
        return 0


