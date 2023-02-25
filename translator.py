from textblob import TextBlob
b = TextBlob("Hi")
b = b.translate(from_lang = 'en' , to="tg")
print(b)

