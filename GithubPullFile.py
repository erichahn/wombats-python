from bottle import route, run
import urllib.request
import json
import Parse

'''
Pull a file from github, using tokens
'''


@route('/bot/<code>')
def get_bot_code(code):
    file = urllib.request.urlopen("https://raw.githubusercontent.com/XenthisX/bot/master/bots/bot.clj").read()
    print(code)
    if (code == 'js'):
        file = urllib.request.urlopen("https://raw.githubusercontent.com/erichahn/wombats-python/master/bots/bottest.js")
        extension = "bottest.js"
    elif(code == 'py'):
        file = urllib.request.urlopen("https://raw.githubusercontent.com/erichahn/wombats-python/master/bots/bottest.py")
        extension = "bottest.py"
    return Parse.run_command(extension, file.read())


run(host='localhost', port=8080, debug=True);