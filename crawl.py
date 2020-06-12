import bs4
import urllib.request as url


# vintisachdeva17@gmail.com


a="https://www.imdb.com/find?ref_=nv_sr_fn&q="
b="&s=all"
name=input("Enter the movie name")
path=a+name+b

http=url.urlopen(path)

first_page = bs4.BeautifulSoup(http, 'lxml')

tag=first_page.find('td',class_="result_text")

a_tag=tag.find_all('a')

path2="https://m.imdb.com"+a_tag[0]['href']
http2=url.urlopen(path2)
second_page=bs4.BeautifulSoup(http2, 'lxml')

data=second_page.find('p',class_="plot-description")

print("#################################")
print(data.text+"\n")
print("#################################")

