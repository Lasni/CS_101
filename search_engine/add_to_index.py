# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]


# index = [[entry1], [entry2], [entry3],...]
# entry = [keyword1, [url1,count], [url2,count2], [url3,...]]
# checks if the keyword already exists in the index
# adds the url if it does
# adds the entry if it doesn't

index = []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for pair in entry[1]:
                if pair[0] == url:
                    return
            entry[1].append([url, 0])  # do this only after all the pairs have been checked
            return
    index.append([keyword, [[url, 0]]])

# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

# splits the content into a list of words and performs add_to_index(...) on each word
def add_page_to_index(index, url, content):
    content = content.split()
    for word in content:
        add_to_index(index, word, url)


add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')
print index
# >>> [['udacity', ['http://udacity.com', 'http://npr.org']],
# >>> ['computing', ['http://acm.org']]]

add_page_to_index(index, 'fake.text', "This is a test")
# print index
# >>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
# >>> ['test',['fake.text']]]
