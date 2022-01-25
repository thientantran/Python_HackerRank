from html.parser import HTMLParser

class CustomHTMLParse(HTMLParser):
    def handle_attrs(self, attrs):
        for attrsPair in attrs:
            # print(f"-> {attrsPair[0]} > attrsPair[1]")
            print('->',attrsPair[0],'>',attrsPair[1]) 
    
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs)
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs)
        
n = int(input())
html=""
for i in range(n):
    html+=input().strip()
    html+="\n"

customHTMLParser = CustomHTMLParse()
customHTMLParser.feed(html)
customHTMLParser.close()
