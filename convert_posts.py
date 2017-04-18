from tumblr_read import get_all_blog_links_for_user
from medium_import import open_medium_import_for_links


username = raw_input("What's your tumblr username: ")
xsrf_token = raw_input("What's the xsrf token from medium?: ")
offset = raw_input("Any offset(how many of these have you migrated before)?: ") or 0

blog_links = get_all_blog_links_for_user(username)

if offset: 
    blog_links = blog_links[:-int(offset) + 1]
blog_links = blog_links[::-1] # reversing here, so we can post in order of age

open_medium_import_for_links(blog_links, xsrf_token)  