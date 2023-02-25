from textblob import TextBlob
b = TextBlob("I havv goood speelimg")
b = b.correct()
print(b)