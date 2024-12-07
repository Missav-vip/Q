from instabot import Bot

# Login ke Instagram
bot = Bot()
bot.login(username='mrobotfx', password='$22dolar')

# Target akun untuk di-follow
target_account = 'cristiano'  # Ganti dengan nama akun target Anda
target_users = bot.get_users_following(target_account)

# Tentukan jumlah pengikut yang ingin diikuti (misalnya 50 pertama)
target_count = 100000  # Ganti dengan jumlah yang Anda inginkan
users_to_follow = target_users[:target_count]  # Ambil 50 pengikut pertama

# Follow pengguna dari akun yang ditargetkan
bot.follow_users(users_to_follow)

# Cek berapa banyak orang yang di-follow
print(f"Total following: {bot.get_total_following()}")
