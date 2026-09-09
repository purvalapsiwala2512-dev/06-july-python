from insta_utils import like_count
from insta_utils import comment_count


current_likes = 120
current_comments = 15

current_likes= like_count(current_likes,5)
current_comments =comment_count(current_comments,2)

print("Updated Likes:",current_likes)
print("Updated Comments:",current_comments)