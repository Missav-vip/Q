from instabot import Bot

# Login ke Instagram
bot = Bot()
bot.login(username='mrobotfx', password='$22dolar')

# Mengambil pengikut dari akun target
target_account = 'cristiano'  # Ganti dengan nama akun target
target_users = bot.get_user_followers(target_account)

# Tentukan jumlah pengikut yang ingin diikuti (misalnya 50 pertama)
target_count = 50  # Ganti dengan jumlah yang Anda inginkan
users_to_follow = target_users[:target_count]  # Ambil 50 pengikut pertama

# Follow pengguna dari akun yang ditargetkan
bot.follow_users(users_to_follow)

# Cek berapa banyak orang yang di-follow
print(f"Total following: {bot.get_total_following()}")
