'''
Medium related logic
'''

import os
import urllib

def open_medium_import_for_links(links, xsrf_token):
    for link in links:
        print "Opening %s" % link
        medium_import_url = get_medium_import_url(link, xsrf_token)
        open_link_in_chrome(medium_import_url)

        user_input = None
        while user_input is not 'y':
            user_input = raw_input("Type 'y' when you're done importing the current article: ")

def get_medium_import_url(entry_link, xsrf_token):
    return "https://medium.com/p/import-story?" + urllib.urlencode({
        'xsrf': xsrf_token,
        'importUrl': entry_link
    })

def open_link_in_chrome(link):
    os.system('/usr/bin/open -a "/Applications/Google Chrome.app" "%s"' % link)  # path may vary here
