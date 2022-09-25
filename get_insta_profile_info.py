# Importing InstagramUser from instagramy package
from instagramy import InstagramUser

user = InstagramUser(str(input('Enter instagram profile username: ')))

print('UserName = ', user.username)
print('FullName = ', user.fullname)
print('Biography = ', user.biography)
print('No of followers = ', user.number_of_followers)
print('No of followings = ', user.number_of_followings)
print('No of Posts = ', user.number_of_posts)
print('Is Private = ', user.is_private)

