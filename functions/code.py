def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age*365*24*60*60
    print(f"Your age in seconds is {age_seconds}")


user_age_in_seconds()


def add_friend():
    friends = ["Mansur", "Ali"]

    friends_name = input("Enter your friends name: ")
    friends = friends+[friends_name]
    print(friends)


add_friend()
