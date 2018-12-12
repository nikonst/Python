import requests
import xml.sax

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        self.isInTitle = False

    def startElement(self, tagName, attrs):
        if tagName == "slideshow":
            print("Slide show title -> " + attrs['title'])
        elif tagName == "slide":
            self.slideCount += 1
        elif tagName == "item":
            self.itemCount += 1
        elif tagName == "title":
            self.isInTitle = True

    def endElement(self, tagName):
        if tagName == "title":
            self.isInTitle = False

    def characters(self, chars):
        if self.isInTitle:
            print("Title " + chars)

    def startDocument(self):
        print("About to start")

    def endDocument(self):
        print("About to end")

def main():
    # create a new content handler for the SAX parser
    handler = MyContentHandler()

    # use the Requests lib to get XML data from the server
    # Requests auto-decodes our content
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    print(result.text)

    xml.sax.parseString(result.text, handler)

    print("There were {0} slide elements".format(handler.slideCount))
    print("There were {0} item elements".format(handler.itemCount))

if __name__ == "__main__":
    main()

