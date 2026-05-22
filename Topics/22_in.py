spam_word1 = "subscribe"
spam_word2 = "click link" #click link both should be there
spam_word3 = "buy"
spam_word4 = "offer"

text = input("Enter the text: ")

if(spam_word1 in text or spam_word2 in text or spam_word3 in text or spam_word4 in text):
    print("This is a spam message.")
else:
    print("This is not a spam message.")