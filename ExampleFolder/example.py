""" Module to test out sciter functionnalities, playground.

https://sciter.com/tutorial-learn-sciters-html-components-in-5-minutes/
https://pypi.org/project/PySciter/
https://github.com/sciter-sdk/pysciter

How to install pysciter ?
1) Download : https://sciter.com/download/. 
2) Place the sciter.dll in windows/System32 on Windows, check online if it is on other OS.
3) pip install pysciter
Thats good
"""

import sciter

if __name__ == "__main__":
    frame = sciter.Window(ismain=True, uni_theme=True)
    frame.load_file("ExampleFolder/hello.htm")
    frame.expand()
    frame.run_app()