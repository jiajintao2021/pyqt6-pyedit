from cores.static import QssTemplate

qss = QssTemplate() 
qss.tag = 'qwidget'
qss.qss_l = [('background', 'break')]
qss.qss_d = {'backgroud-color': 'blank'}

print(qss.output())


qss = """
    qwidget {
        backgroud-color: blank;
        background: break;
        background1: 0 1 1;
    }
"""

qss = qss.strip()

tag = []
tem_l = []
d = {}
for s in qss:
    if s in [' ', '\n']:
        continue
    tem_l.append(s)
    if s == '{':
        tag = tem_l
        tem_l.clear()
        continue

