from instabot import Bot
import time

# Membuat instance bot
bot = Bot()

# Login ke Instagram
bot.login(username="username_anda", password="password_anda")

# Fungsi untuk follow pengguna berdasarkan lokasi atau bahasa
def follow_users_from_country(language_code, country_name, amount=50):
    print(f"Following users from {country_name} with language code {language_code}")
    
    # Anda bisa mengikuti pengguna berdasarkan bahasa dan lokasi yang ditargetkan
    users = bot.search_users_by_location(country_name, amount=amount)  # Ganti dengan lokasi dan nama negara yang sesuai
    bot.follow_users(users)

# Fungsi untuk memberikan like pada postingan dalam bahasa atau lokasi tertentu
def like_posts_from_country(language_code, country_name, amount=100):
    print(f"Liking posts from {country_name} in language {language_code}")
    
    # Gunakan filter pencarian berdasarkan negara atau bahasa
    posts = bot.search_posts(language_code, country_name)  # Ganti dengan pencarian berbasis negara atau bahasa
    bot.like_posts(posts, amount=amount)

# Fungsi untuk follow pengguna yang mengikuti akun influencer atau brand Jepang/Korea
def follow_users_from_influencer(influencer_usernames, amount=50):
    print(f"Following users who follow {', '.join(influencer_usernames)}")
    for username in influencer_usernames:
        followers = bot.get_user_followers(username)
        bot.follow_users(followers[:amount])

# Fungsi untuk unfollow non-followers
def unfollow_non_followers():
    print("Unfollowing users who are not following back")
    bot.unfollow_non_followers()

# Fungsi untuk menambah pengikut aktif dari pengguna Jepang dan Korea
def add_active_followers():
    # Daftar influencer atau akun Jepang/Korea yang relevan
    influencer_usernames = ['influencer_japan', 'influencer_korea']  # Ganti dengan username influencer

    # Menargetkan bahasa dan negara
    follow_users_from_country('ja', 'Japan', amount=50)  # Follow pengguna di Jepang (bahasa Jepang)
    like_posts_from_country('ja', 'Japan', amount=100)  # Like postingan dari Jepang
    follow_users_from_country('ko', 'Korea', amount=50)  # Follow pengguna di Korea (bahasa Korea)
    like_posts_from_country('ko', 'Korea', amount=100)  # Like postingan dari Korea
    
    # Mengikuti pengikut influencer Jepang/Korea
    follow_users_from_influencer(influencer_usernames, amount=50)
    
    # Unfollow non-followers
    unfollow_non_followers()

# Memulai bot
if __name__ == '__main__':
    add_active_followers()
    print("Bot started successfully!")
