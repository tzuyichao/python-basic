from summa import keywords
from summa import summarizer

text = """Automatic summarization is the process of reducing a text document with a \
computer program in order to create a summary that retains the most important points \
of the original document. As the problem of information overload has grown, and as \
the quantity of data has increased, so has interest in automatic summarization. \
Technologies that can make a coherent summary take into account variables such as \
length, writing style and syntax. An example of the use of summarization technology \
is search engines such as Google. Document summarization is another."""

print("keyword:")
print("-"*40)
print(keywords.keywords(text))
print("-"*40)
print("summarize:")
print("-"*40)
print(summarizer.summarize(text))
print("-"*40)