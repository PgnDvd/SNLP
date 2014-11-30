import pycurl

from StringIO import StringIO


b = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://text-processing.com/api/sentiment/')
c.setopt(pycurl.POSTFIELDS, "text=great")
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
result = b.getvalue()
print(result)
