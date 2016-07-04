def compute_ranks(graph):
    d = 0.8  # damping factor
    numloops = 10  # number of times we're going through the relaxation algorithm
    npages = len(graph)  # number of pages we can go to from the current page

    # initialize the same rank value for all pages in the beginning
    ranks = {}
    for page in graph:
        ranks[page] = 1.0 / npages

    """relaxation algorithm:"""
    for i in range(numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:  # check for each node in graph if it links to page
                if page in graph[node]:  # if it does then add its rank value to newrank of the page
                    newrank += d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank  # update the ranks for each page
        ranks = newranks  # update the final ranks
    return ranks
