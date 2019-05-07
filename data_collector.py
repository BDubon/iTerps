import requests as r
import json
import csv

"""
 C O U R S E S
-- KEYS -- 
'course_id' - str (INSTXXX)  X
'semester' - str (numbers)
'name' -str                  X
'dept_id' - str
'department' - str
'credits' - str              X
'description' - str          X
'grading_method' - list
'gen_ed' - list              X
'core' - list
'relationships' - dict
    'coreqs'
    'prereqs'                X
    'formerly'
    'restrictions'
    'additional_info'
    'also_offered_as'
    'credit_granted_for'
'sections' - list

url = 'https://api.umd.io/v0/courses?dept_id=INST'

data = r.get(url)
jData = json.loads(data.content)
with open('other/courses.csv', 'w', newline='') as csvFile:
    headers = ['id', 'course_id', 'name', 'slug', 'description', 'credits', 'prereqs', 'gen_ed']
    writer = csv.DictWriter(csvFile, fieldnames=headers)
    writer.writeheader()
    id = 1
    for item in jData:
        courseID = item['course_id']
        name = item['name']
        credit = item['credits']
        prereqs = dict(item['relationships'])
        pre = prereqs['prereqs']
        if pre is None:
            pre = 'None'
        desc = item['description']
        if desc is None:
            desc = 'Not Available'
        gen = item['gen_ed']
        if len(gen) == 0:
            gen = 'None'
        else:
            gen = gen[0]

        row = {'id': id, 'course_id': courseID, 'name': name, 'slug': courseID, 'description': desc,
               'credits': credit, 'prereqs': pre, 'gen_ed': gen}

        writer.writerow(row)
        id += 1
"""

# PROFESSOR'S DATA

with open('other/professors.csv', 'r') as pf:
    next(pf)
    wFile = open('other/professor2.csv', 'w', newline='')
    headers = ['prof_ID', 'first_name', 'last_name', 'title', 'email', 'phone_number', 'office', 'slug', 'picture']
    writer = csv.DictWriter(wFile, fieldnames=headers)
    writer.writeheader()
    for line in pf:
        line = line.strip()
        lineList = line.split(',')
        profID = lineList[0]
        firstN = lineList[1]
        lastN = lineList[2]
        title = lineList[3]
        email = lineList[4]
        phone = lineList[5]
        office = lineList[6]
        slug = firstN + '-' + lastN
        pic = lineList[8]
        courses = lineList[9]

        row = {'prof_ID': profID, 'first_name': firstN, 'last_name': lastN, 'title': title, 'email': email,
               'phone_number': phone, 'office': office, 'slug': slug, 'picture': pic}
        writer.writerow(row)




