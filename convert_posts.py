from tumblr_read import get_all_blog_links_for_user
from medium_import import open_medium_import_for_links


username = raw_input("What's your tumblr username: ")
xsrf_token = raw_input("What's the xsrf token from medium?: ")

blog_links = get_all_blog_links_for_user(username)
open_medium_import_for_links(blog_links[::-1], xsrf_token)  # reversing here, so we can post in order of age