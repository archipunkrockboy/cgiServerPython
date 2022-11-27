import cgi
import sys
import os
import inspect
import xml.etree.ElementTree as ET
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import db

form = cgi.FieldStorage()

galleries_xml = form.getfirst('xml_file')

if galleries_xml is not None:
    root = ET.fromstring(galleries_xml.decode("utf-8"))
    success_cnt = 0
    for child in root:
        gallery = {}
        for a_ch in child:
            if a_ch.tag == 'name':
                gallery['name'] = a_ch.text
            if a_ch.tag == 'city':
                gallery['city'] = a_ch.text
            if a_ch.tag == 'country':
                gallery['country'] = a_ch.text

        if ('name' in gallery) and ('city' in gallery) and ('country' in gallery):
            db.add_gallery(gallery['name'], gallery['city'], gallery['country'])
            success_cnt += 1
print('Content-type:text/html\n')
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Добавление данных</title>
</head>
<body>
<label>Данные загружены!</label>
</body>
</html>''')