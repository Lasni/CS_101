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
    index = {}  # added this
    while to_crawl and depth <= max_depth:
        page = to_crawl.pop()
        if page not in crawled:
            content = get_page(page)
            union(next_depth, get_all_links(content))
            add_page_to_index(index, page, content)  # added this
            crawled.append(page)
        if not to_crawl:
            to_crawl, next_depth = next_depth, []
            depth += 1
    return index  # returned crawled before


# index = [[entry1], [entry2], [entry3],...]
# entry = [keyword1, [url1, url2, url3,...]]
# checks if the keyword already exists in the index
# adds the url if it does
# adds the entry if it doesn't
# Modified to work with a dictionary instead of a list
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]


# splits the content into a list of words and performs add_to_index(...) on each word
def add_page_to_index(index, url, content):
    content = content.split()
    for word in content:
        add_to_index(index, word, url)


# checks if an entry with the keyword in the index exists and returns the list of urls
# returns an empty list if nothing is found
# Modified to work with a dictionary instead of a list
def lookup(index, keyword):
    try:
        return index[keyword]
    except:
        return None


# increments the count for the corresponding url link
def record_user_click(index, keyword, url):
    urls = lookup(index, keyword)  # returns a list of lists ([url, count] pairs)
    if urls:
        for entry in urls:  # for each pair check if it matches the url
            if entry[0] == url:
                entry[1] += 1  # increment the pair's count if it does


