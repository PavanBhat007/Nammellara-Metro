from flask_login import login_user, current_user
new_user = 'a'
login_user(new_user)
print(current_user)