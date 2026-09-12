from aparat import Aparat

username = input("نام کاربری آپارات: ")
password = input("رمز عبور آپارات: ")
target = input("نام کاربری فردی که می‌خواهی دنبال کنی: ")

aparat = Aparat()

if aparat.login(username, password):
    print("ورود موفق بود.")

    aparat.save_session()

    user = aparat.get_user(target)

    if user.follow():
        print("دنبال شد.")
    else:
        print("عملیات دنبال‌کردن ناموفق بود.")
else:
    print("ورود ناموفق بود.")

