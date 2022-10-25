from bs4 import BeautifulSoup
import requests

def get_soup():
    url = 'https://in.search.yahoo.com/search;_ylt=AwrPrUd4UFZjU4UZ7E26HAx.;_ylc=X1MDMjExNDcyMzAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZAMEbl9yc2x0AzAEbl9zdWdnAzAEb3JpZ2luA2luLnNlYXJjaC55YWhvby5jb20EcG9zAzAEcHFzdHIDBHBxc3RybAMwBHFzdHJsAzYEcXVlcnkDcHl0aG9uBHRfc3RtcAMxNjY2NjAxMDg0?p=jobs&fr=sfp&iscqry=&fr2=sb-top-search'
    c = requests.get(url).content
    soup = BeautifulSoup(c, 'html.parser')
    return soup

if __name__ == '__main__':
    soup = get_soup()

    for div in soup.findAll('span'):
        if div.has_attr('class'):
            div_class = div['class']
            if 'fc-obsidian' in div_class:
                print(div.text)

'''
"c"	"BBupper"	"bblower"
"155"	\N	\N
"155"	\N	\N
"141.4"	\N	\N
"140.35"	\N	\N
"145.45"	\N	\N
"142.2"	\N	\N
"137.15"	\N	\N
"139.8"	\N	\N
"137.75"	\N	\N
"145"	\N	\N
"144.65"	\N	\N
"138.15"	\N	\N
"132.1"	\N	\N
"133.5"	\N	\N
"133.5"	\N	\N
"127.3"	\N	\N
"128.05"	\N	\N
"124.05"	\N	\N
"125.75"	\N	\N
"132"	"154.85"	"120.97"
"132"	"151.93"	"121.58"
"127.4"	"148.55"	"122.2"
"128.9"	"147.91"	"121.59"
"125.35"	"147.5"	"120.5"
"125.4"	"145.92"	"120.08"
"130"	"144.65"	"120.13"
"129"	"144.12"	"119.84"
"126.85"	"143.11"	"119.56"
"127.45"	"142.33"	"119.31"
"122.1"	"139.78"	"119.57"

'''