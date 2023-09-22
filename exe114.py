import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está disponivel no momento')
else:
    print('Tudo Ok')
    print(site.read(), end=' ')
