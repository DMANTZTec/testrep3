fw=open('sample.txt','w')
fw.write('writing some text to my sample file\n')
fw.write('I like bacon\n')
fw.close()

fr=open('sample.txt','r')
text=fr.read()
print(text)
fr.close()

#download files from web

from urllib import request
google_url="sample.txt"
def download_stock_data(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n")
    dest_url=google_url
    fx=open(dest_url,'w')
    for line in lines:
        fx.write(line+"\n")
download_stock_data(google_url)