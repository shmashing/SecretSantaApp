import os
import sys

#app_name = sys.argv[0]
app_name = raw_input("Name of app? ")

os.makedirs(app_name + '/templates/' + app_name)
os.makedirs(app_name + '/static/' + app_name)

os.mkdir(app_name + '/static/' + app_name + '/css')
os.mkdir(app_name + '/static/' + app_name + '/javascript')
os.mkdir(app_name + '/static/' + app_name + '/images')

####################################################
#	Create __init__.py file
####################################################
file = open('__init__.py', 'w+')
file.close()


####################################################
#	Create urls.py file
####################################################
file = open(app_name + '/urls.py', 'w+')
file.write('from django.conf.urls import url\n')
file.write('from . import views\n\n')

file.write('urlpatterns = [\n')
file.write("  url(r'^$', views.index),\n")
file.write(']\n')
file.close()


####################################################
#	Create Index.html file
####################################################
file = open(app_name + '/templates/' + app_name + '/index.html', 'w+')

file.write('<!DOCTYPE html>\n\n')
file.write('<html>\n')
file.write('<head>\n')
file.write('  <meta charset="utf-8">\n')
file.write('  <title>BLANK_TITLE</title>\n')
file.write('  <meta name="description" content="BLANK DESCRIPTION">\n')
file.write('  {% load static %}\n')
file.write('  <link rel="stylesheet" href="{% static '+"'"+app_name+"/css/main.css'"+'%}" media="screen" title="no title"  charset="utf-8">\n')
file.write('</head>\n')
file.write('<body>\n')
file.write('</body>\n')
file.write('</html>')
file.close()

####################################################
#	Create styles.css file
####################################################
file = open(app_name + '/static/' + app_name + '/css/main.css', 'w+')

file.write('* {\n')
file.write('    margin: 0px;\n')
file.write('    padding: 0px;\n')
file.write('}')
file.close()

####################################################
#	update views.py file
####################################################
file = open(app_name + '/views.py', 'a')

file.write('def index(request):\n')
file.write('    return render(request, "' + app_name + '/index.html")')


####################################################
#	update main settings.py file
####################################################
current_path = os.getcwd()
current_dir = []

runner = len(current_path) - 1
place_holder = len(current_path)

while(runner >= 0):
  if(current_path[runner] == '/'):
    current_dir.append(current_path[runner:place_holder])
    place_holder = runner

  runner -= 1
 

current_dir = current_dir[1][1:]

file = open('../../' +current_dir + '/' +current_dir +'/settings.py', 'r')

lines = file.readlines()
for i in range(len(lines)):
  if (lines[i] == 'INSTALLED_APPS = [\n'):
    lines.insert(i+1, "\n    'apps." + app_name + "',\n")

file.close()

file = open('../../' +current_dir + '/' +current_dir +'/settings.py', 'w')
for line in lines:
  file.write(line)


####################################################
#	update main urls.py file
####################################################

file = open('../../' +current_dir + '/' +current_dir +'/urls.py', 'r')

lines = file.readlines()
for i in range(len(lines)):
  if (lines[i] == 'from django.conf.urls import url\n'):
    lines[i] = lines[i][0:-1] + ', include\n'
  elif (lines[i] == 'urlpatterns = [\n'):
    lines.insert(i+1, "\n    url(r'^/" + app_name+ "', include('apps."+app_name+".urls')),\n")

file.close()

file = open('../../' +current_dir + '/' +current_dir +'/urls.py', 'w')
for line in lines:
  file.write(line)

