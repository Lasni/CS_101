"""
Find all URLs in the page html and print them out
"""


# receives a page html and returns next url and the position of the quote after it
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


# receives a url and returns the page html
def get_page(url):
    try:
        from BeautifulSoupTests import BeautifulSoup
        import requests
        response = requests.get(url)
        page = str(BeautifulSoup(response.content))
        return page
    except:
        return ""


# receives a page(string) and returns a list of links on it
def get_all_links(page):
    links = []
    while True:  # loop forever until we get to the break statement
        url, end_pos = get_next_target(page)
        page = page[end_pos:]
        if url:
            links.append(url)
        else:
            break
    return links


# helper function that creates a union of two lists
def union(lst1, lst2):
    for i in lst2:
        if i not in lst1:
            lst1.append(i)


# crawls the web starting with the seed_page until reaching the max_depth value
# returns a list of crawled pages
def crawl_web(seed_page, max_depth):
    to_crawl = [seed_page]
    crawled = []
    next_depth = []
    depth = 0
    while to_crawl and depth <= max_depth:
        page = to_crawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
    return crawled


print(get_all_links(get_page("https://xkcd.com/162/")))

print crawl_web("https://xkcd.com/162/", 10)
