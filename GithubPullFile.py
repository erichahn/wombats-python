from bottle import route, run
import urllib.request
import json
import Parse

'''
Pull a file from github, using tokens
'''


@route('/bot/<code>')
def get_bot_code(code):
    file = urllib.request.urlopen("https://raw.githubusercontent.com/XenthisX/bot/master/bot.clj").read()
    if (code == 'test'):
        file = urllib.request.urlopen("https://raw.githubusercontent.com/erichahn/wombats-python/master/bottest.js")
    return Parse.run_command("bottest.js", file)



run(host='localhost', port=8080, debug=True);