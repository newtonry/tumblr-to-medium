'''
Tumblr fetching of blog urls
'''

import urllib
import xml.etree.ElementTree


ENTRIES_PER_PAGE = 50  # 50 is the max in the tumblr docs https://www.tumblr.com/docs/en/api/v1

def get_all_blog_links_for_user(user):
    blog_links = []
    current_item = 0

    while True:
        url = get_tumblr_api_url(user, current_item)
        new_links = get_links_from_tumblr_api(url)
        blog_links += new_links
    
        if not len(new_links):  # we've hit the end
            return blog_links

        current_item += ENTRIES_PER_PAGE

def get_tumblr_api_url(user, start):

    query_params = urllib.urlencode({
        'num': ENTRIES_PER_PAGE,
        'start': start
    })
    return "http://%s.tumblr.com/api/read?" % user + query_params

def get_links_from_tumblr_api(url):
    feed_page = urllib.urlopen(url)
    root = xml.etree.ElementTree.parse(feed_page).getroot()
    posts = root.find('posts').findall('post')
    return [post.get('url') for post in posts]
