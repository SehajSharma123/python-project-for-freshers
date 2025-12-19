news = input("Enter news text: ").lower()

fake_keywords = ["breaking", "shocking", "unbelievable", "click"]

flag = False
for word in fake_keywords:
    if word in news:
        flag = True

if flag:
    print("Result: This news may be FAKE.")
else:
    print("Result: This news seems GENUINE.")
