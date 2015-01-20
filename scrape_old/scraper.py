from bs4 import BeautifulSoup
from urllib2 import urlopen
import cPickle as pickle
from multiprocessing.dummy import Pool

def download_link(link):
    print 'reading', link
    return urlopen(link).read()

def parallel_pickle(obj):
    print 'dumping', obj[1], obj[0][250:300]
    pickle.dump(obj[0], open(obj[1], 'wb'))

def better_get():
    html = urlopen("http://www.jropinion.com/413431355").read()
    print 'downloaded main page'
    soup = BeautifulSoup(html)
    posts = soup.find_all('div', attrs={'class':'content'})[0]
    links = map(lambda x: x.find_all('a', href=True)[0]['href'], posts.find_all('h4'))
    p = Pool(4)
    raw_html = p.map(download_link, links)
    p.close()
    p.join()
    del p
    print 'downloaded subpages'
    names = map(lambda x: x+'.pkl', map(lambda x: ''.join(''.join(x[285:300]).split(' ')[:2]), raw_html)) 
    objs = zip(raw_html, names)
    p = Pool(4)
    p.map(parallel_pickle, objs)
    p.close()
    del p
    print 'saved subpages'
    pages = map(lambda x: BeautifulSoup(x), raw_html)
    return pages

def get_text(posts):
    content_list = map(lambda x: x.find_all('div', {'class': "blog-post-body section"}), posts)
    post_contents = map(lambda x: x[0].find_all('div', {'class': 'content'})[0].get_text(), content_list)
    print 'got contents'
    return post_contents

def get_names(posts):
    titles =  map(lambda x: x.find_all('meta', {'property': 'og:title'})[0].get('content'), posts)
    print 'got titles'
    return titles

def wrapper():
    posts = better_get()
    text = get_text(posts)
    titles = get_names(posts)
    posts = zip(titles, text)
    posts = map(lambda x: x[1].encode('ascii', 'ignore').replace("\n", ""), posts)
    print 'pickling posts'
    pickle.dump(posts, open('scraped_contents.pkl', 'wb'))
    return posts

if __name__ == '__main__':
    wrapper()
 
