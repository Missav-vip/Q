from instabot import Bot

# Login ke Instagram
bot = Bot()
bot.login(username='mrobotfx', password='$22dolar')

# Target akun untuk di-follow
target_account = 'target_account_name'  # Ganti dengan nama akun target Anda
target_users = bot.get_users_following(target_account)

# Follow pengguna dari akun yang ditargetkan
bot.follow_users(target_users)

# Cek berapa banyak orang yang di-follow
print(f"Total following: {bot.get_total_following()}")
