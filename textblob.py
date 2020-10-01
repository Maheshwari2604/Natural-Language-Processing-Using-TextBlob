#pip install textblob
#python -m textblob.download_corpora


>>> from textblob import TextBlob
>>> b = TextBlob('hey i am happy')
>>> b.sentiment
Sentiment(polarity=0.8, subjectivity=1.0)

>>> from textblob import TextBlob
>>> b = textBlob('i am not happy')

print(b.textblob)

>>> for i in b.words:
...     print(i)
... 
i
am
not
happy


>>> b = TextBlob('i am not happ')
>>> b.correct()
TextBlob("i am not happy")

>>> b = TextBlob('enthusium')
>>> b.correct()
TextBlob("enthusiasm")

>>> b = TextBlob('i am not happ')
>>> b.words[3].spellcheck()
[('happy', 0.919831223628692), ('rapp', 0.04219409282700422), ('harp', 0.03375527426160337), ('hasp', 0.004219409282700422)]

>>> b.detect_language()
'en'
>>> bb = TextBlob('أحبك')
>>> bb.detect_language()
'ar'
>>> bb.translate(to='en')
TextBlob("I love you")
>>> c = bb.translate(to='en')
>>> for words, tag in blob.tags:
...     print(words, tags)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'blob' is not defined
>>> for words, tag in b.tags:
...     print(words, tags)
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'tags' is not defined
>>> for words, tag in b.tags:
...     print(words, tag)
... 
i NN
am VBP
not RB
happ JJ
