import time
time.localtime()

class Comment():
    def __init__(self, likes=0, dislikes=0):
            self.username = input("Adını gir: ")
            self.text = input("Yorumu gir: ")
            self.likes = likes
            self.dislikes = dislikes
            self.hour = time.localtime().tm_hour
            self.min = time.localtime().tm_min
            self.sec = time.localtime().tm_sec


comment1 = Comment()
comment2 = Comment()
comment3 = Comment()
comment4 = Comment()
comment5 = Comment()


liste = [comment1, comment2, comment3, comment4, comment5]

for c in liste:
    print(f"\n{c.username} - Yorum: {c.text} - Likes: {c.likes} - Dislikes: {c.dislikes} - Time: {c.hour , c.min , c.sec} ")





























