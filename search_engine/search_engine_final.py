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


# crawls the web starting with the seed_page
# returns index and graph
# removed the depth parameter
# modified in lessons 3 and 6
def crawl_web(seed_page):
    to_crawl = [seed_page]
    crawled = []
    index = {}  # added in lesson 3
    graph = {}  # added in lesson 6 / list of urls that a page links to (out_links)
    while to_crawl:
        page = to_crawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)  # added in lesson 3
            out_links = get_all_links(content)  # added in lesson 6
            graph[page] = out_links  # added in lesson 6
            union(to_crawl, out_links)
            crawled.append(page)
    return index, graph  # returned crawled before


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


def compute_ranks(graph):
    d = 0.8  # damping factor
    numloops = 50  # number of times we're going through the relaxation algorithm
    npages = len(graph)  # number of pages current page links to

    # initialize the same rank value for all pages in the beginning
    ranks = {page: (1.0 / npages) for page in graph}

    """relaxation algorithm:"""
    for i in range(numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:  # check for each node in graph if it links to page
                if page in graph[node]:  # if it does
                    newrank += d * (ranks[node] / len(graph[node]))  # then add its rank value to newrank of the page
            newranks[page] = newrank  # update the ranks for each page
        ranks = newranks  # update the final ranks in each loop
    return ranks


index, graph = crawl_web('https://www.udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)
print ranks
