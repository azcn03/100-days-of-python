class User :
    def __init__(ding, id, username):
        #self in this case user_1,. iid you can name that attribute however you like, id is the name of the argument passed
        #also it can be named differently, not need to be self
        ding.iid = id
        ding.uusername = username
        ding.followers = 0
        ding.following = 0

    def follow(ding, the_other_user):
        the_other_user.followers += 1
        ding.following += 1


user_1 = User("001", "A")
user_2 = User("002", "B")

user_1.follow(user_2)

print(user_1.following)

# We can't do that, constructor NEEDS the arguments
# user_2 = User()
# user_2.iid = "002"
# user_2.uusername = "B"

