
#x description="download a website with a HTTP get"
#x pre={
url="https://www.example.org"
#x }

#x step={
import urllib.request
content = urllib.request.urlopen(url).read()
#x }

print(content)
