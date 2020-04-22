from flask import request
res = request.get("https://www.goodreads.com/book/review_counts.json", params={"key": "hrazhMWTLAAWHuamZu3Sw", "isbns": "9781632168146"})
print(res.json())