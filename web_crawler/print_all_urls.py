"""
Find all URLs in the page html and print them out
"""


# receives a page html and returns next url and the position of the quote after it
def get_next_target(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


# receives a url and returns the page html
def get_page(url):
    try:
        from bs4 import BeautifulSoup
        import requests
        response = requests.get(url)
        page = str(BeautifulSoup(response.content))
        return page
    except:
        return


# receives a page(string), prints out the urls and updates the page in each step
def print_all_links(page):
    while True:  # loop forever until we get to the break statement
        url, end_pos = get_next_target(page)
        page = page[end_pos:]
        if url:
            print(url)
        else:
            break


print_all_links(get_page("https://xkcd.com/162/"))