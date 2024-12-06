from instabot import Bot
import time

# Membuat instansi bot
bot = Bot()

# Login ke Instagram
username = 'mrobotfx'  # Ganti dengan username Anda
password = '$22dolar'  # Ganti dengan password Anda
bot.login(username=username, password=password)

# Menargetkan followers dari akun tertentu
target_username = 'claudyafx'  # Ganti dengan akun yang ingin Anda targetkan
bot.follow_users(bot.get_users_following(target_username))

# Menargetkan followers dari hashtag tertentu
target_hashtag = 'fashion'  # Ganti dengan hashtag yang relevan
media = bot.get_hashtag_medias(target_hashtag, amount=50)  # Ambil 50 post terakhir dengan hashtag tersebut
user_ids = bot.get_media_likers(media)  # Dapatkan pengguna yang menyukai postingan
bot.follow_users(user_ids)

# Cek berapa banyak orang yang di-follow
print(f"Total following: {bot.get_total_following()}")

# Tunggu beberapa detik untuk menghindari deteksi sebagai bot
time.sleep(2)

# Logout setelah selesai
bot.logout()
