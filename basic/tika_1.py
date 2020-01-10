from tika import parser
parsed = parser.from_file("D:\\Text\\8d\\8D_Classic\\8D_Classic\\65SD BA-Fall time.pptx.pptx")
print(parsed["metadata"]) #To get the meta data of the file
print(parsed["content"])