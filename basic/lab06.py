with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
  for line in infile:
    for term in line.lower().replace(",", "").replace(".", "").split():
      cleaned_words = term + "\n"
      outfile.write(cleaned_words)