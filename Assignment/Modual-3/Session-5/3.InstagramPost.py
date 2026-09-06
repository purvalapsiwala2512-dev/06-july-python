class InstagramPost:


    def __init__(self,caption,likes,comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self,comment_text):
        self.comments.append(comment_text)
        self.likes += 1

post = InstagramPost("Sunset vibes",120,["Nice","Awesome view"])
post.add_comment("Looks great")

print("Comments:",post.comments)
print("Updated Likes:",post.likes)