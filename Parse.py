import tempfile
import subprocess
import os
'''
File parser, takes in code in a language and runs it
'''

def run_command(filename, contents):
    fileext = filename.split(".")[1]
    scriptFile = tempfile.NamedTemporaryFile(delete=False)
    scriptFile.write(str.encode(contents))
    scriptFile.close()
    scriptFileLocation = scriptFile.name
    language = {
        "js": run_js(scriptFileLocation),
        "py": "one",
        "clj": "two",
    }
    language.get(fileext, "clj")

def run_js(scriptFileLocation):
    return os.popen('node '+ scriptFileLocation).read()
