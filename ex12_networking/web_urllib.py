import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://vantrant.github.io/library-app/darkmode.js')
for line in fhand:
    print( line.decode().strip() )