import wikipediaapi

wiki = wikipediaapi.Wikipedia('zh')
pages = ['Python', 'Ruby', 'Java', 'Scala', 'Haskell', 'Lua', 'JavaScript']
for page in pages:
    page_content = wiki.page(page)
    print(page_content.title)
    print(page_content.summary)
    print(page_content.text)