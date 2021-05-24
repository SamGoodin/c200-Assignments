import webbrowser

def egypt(x):
    x1 = x.lower()
    files = "Files/"
    top, bottom = files + "eglyphTOP.jpg", files + "eglyphBOTTOM.jpg"
    imgDict = {
        "a": "eglypha.jpg",
        "b": "eglyphb.jpg",
        "c": "eglyphc.jpg",
        "d": "eglyphd.jpg",
        "g": "eglyphg.jpg",
        "h": "eglyphh.jpg",
        "i": "eglyphi.jpg",
        "j": "eglyphj.jpg",
        "k": "eglyphk.jpg",
        "l": "eglyphl.jpg",
        "m": "eglyphm.jpg",
        "n": "eglyphn.jpg",
        "o": "eglypho.jpg",
        "p": "eglyphp.jpg",
        "q": "eglyphq.jpg",
        "r": "eglyphr.jpg",
        "s": "eglyphs.jpg",
        "t": "eglypht.jpg",
        "u": "eglyphu.jpg",
        "v": "eglyphv.jpg",
        "w": "eglyphw.jpg",
        "x": "eglyphx.jpg",
        "y": "eglyphy.jpg",
        "z": "eglyphz.jpg"
        }
    #Remove letters that don't have a symbol
    name = ""
    for letter in x1:
        for key in imgDict.keys():
            if letter == key:
                name += letter
    s = """<html><head></head>
<body>
<h2 class="text-center">{0} = {1}</h2>
<img src="{2}"><br>""".format(x, name, top)

    for letter in name:
        s += '<img src="{0}"><br>\n'.format(files + imgDict.get(letter))

    s += """<img src="{0}"><br>
</body></html>""".format(bottom)

    return s


plocation = input("Enter location: ")

f = open(plocation, 'w')

name = input("Name: ")

f.write(egypt(name))
f.close()

webbrowser.open_new_tab(plocation)
