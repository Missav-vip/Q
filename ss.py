import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Masukkan data akun Instagram
InstaID = input("Masukkan username/email/nomor telepon Instagram Anda: ")
InstaPass = input("Masukkan password Instagram Anda: ")
InstaTag = input("Masukkan username target Instagram (tanpa @): ")

nFollowers = 500000  # Jumlah pengikut yang akan diikuti

chrome_driver_path = "./chromedriver.exe"  # Path ke chromedriver Anda

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

CookiesText = "Consenti cookie essenziali e facoltativi"
FollowText = "Segui"

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        self.driver.implicitly_wait(5)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        # Klik tombol menerima cookies
        self.driver.find_element(By.XPATH, "//button[text()='" + CookiesText + "']").click()

        # Login dengan username dan password yang diberikan
        ID = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        ID.send_keys(InstaID)

        Pass = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        Pass.send_keys(InstaPass)

        time.sleep(random.randint(3, 5))  # Penundaan acak
        Pass.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(random.randint(5, 10))  # Penundaan acak
        self.driver.get(f"https://www.instagram.com/{InstaTag}/followers")

    def follow(self):
        modal = self.driver.find_element(By.CSS_SELECTOR, 'button._acan._acap._acas')
        FCount = 0
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'div div button')

        for x in buttons:
            if x.text == FollowText and FCount < nFollowers:
                # Delay acak sebelum mengikuti
                time.sleep(random.randint(2, 5))  # Penundaan acak untuk meniru pengguna manusia
                x.click()
                FCount += 1

            # Mengecek batas pengikut
            if FCount >= nFollowers:
                print(f"Sudah mengikuti {nFollowers} pengguna, berhenti untuk sementara.")
                break

            # Jangan lupa untuk scroll agar lebih natural
            if random.choice([True, False]):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(random.randint(3, 7))  # Penundaan acak setelah scroll

        # Jika sudah mencapai batas pengikut yang diinginkan
        if FCount >= nFollowers:
            print(f"Selesai mengikuti {nFollowers} pengguna.")

    def randomize_actions(self):
        # Fungsi untuk menambahkan variasi dalam aktivitas
        current_hour = time.localtime().tm_hour
        if current_hour > 6 and current_hour < 10:
            time.sleep(random.randint(10, 15))  # Variasi waktu pagi
        else:
            time.sleep(random.randint(20, 30))  # Variasi waktu siang/malam

    def advanced_logic(self):
        # Logika Cerdas untuk menyerupai manusia
        actions = [
            "like", "comment", "follow", "unfollow", "scroll", "search", "watch_story", "like_photo", 
            "unlike_photo", "comment_photo", "report", "open_profile", "send_message", "accept_message", 
            "open_dms", "post_photo", "update_profile", "change_password", "block_user", "view_profile"
        ]
        action = random.choice(actions)
        if action == "like":
            self.like_action()
        elif action == "comment":
            self.comment_action()
        elif action == "follow":
            self.follow_action()
        elif action == "scroll":
            self.scroll_action()
        elif action == "search":
            self.search_action()
        elif action == "watch_story":
            self.watch_story()
        elif action == "like_photo":
            self.like_photo()
        elif action == "open_profile":
            self.open_profile()
        elif action == "send_message":
            self.accept_message()
        elif action == "open_dms":
            self.open_dms()
        elif action == "post_photo":
            self.post_photo()

    def like_action(self):
        # Like beberapa postingan secara acak
        print("Melakukan like pada postingan")
        time.sleep(random.randint(5, 10))  # Delay acak untuk like

    def comment_action(self):
        # Memberikan komentar acak pada postingan
        comments = ["Keren!", "Wow, amazing!", "Bagus sekali!", "Love it!"]
        comment = random.choice(comments)
        print(f"Meninggalkan komentar: {comment}")
        time.sleep(random.randint(5, 10))  # Delay acak untuk komentar

    def unfollow_action(self):
        # Unfollow akun secara acak
        print("Melakukan unfollow secara acak")
        time.sleep(random.randint(5, 10))  # Delay acak untuk unfollow

    def scroll_action(self):
        # Melakukan scroll pada halaman
        print("Melakukan scroll pada halaman")
        time.sleep(random.randint(5, 10))  # Delay acak untuk scroll

    def search_action(self):
        # Mencari akun atau tagar
        print("Mencari akun atau tagar secara acak")
        time.sleep(random.randint(5, 10))

    def watch_story(self):
        # Menonton story dari orang lain
        print("Menonton story orang lain")
        time.sleep(random.randint(5, 10))

    def like_photo(self):
        # Like foto secara acak
        print("Melakukan like foto secara acak")
        time.sleep(random.randint(5, 10))

    def unlike_photo(self):
        # Unlike foto secara acak
        print("Melakukan unlike foto")
        time.sleep(random.randint(5, 10))

    def comment_photo(self):
        # Memberikan komentar pada foto secara acak
        comments = ["Great shot!", "Nice pic!", "This is amazing!", "So beautiful!"]
        comment = random.choice(comments)
        print(f"Meninggalkan komentar pada foto: {comment}")
        time.sleep(random.randint(5, 10))

    def report_action(self):
        # Melaporkan akun atau konten
        print("Melaporkan akun atau konten")
        time.sleep(random.randint(5, 10))

    def open_profile(self):
        # Membuka profil pengguna lain
        print("Membuka profil pengguna lain")
        time.sleep(random.randint(5, 10))

    def send_message(self):
        # Mengirim pesan secara acak
        print("Mengirim pesan secara acak")
        time.sleep(random.randint(5, 10))

    def accept_message(self):
        # Menerima pesan
        print("Menerima pesan")
        time.sleep(random.randint(5, 10))

    def open_dms(self):
        # Membuka DM untuk melihat pesan
        print("Membuka Direct Messages")
        time.sleep(random.randint(5, 10))

    def post_photo(self):
        # Mengunggah foto secara acak
        print("Mengunggah foto secara acak")
        time.sleep(random.randint(5, 10))

    def update_profile(self):
        # Mengubah profil
        print("Mengubah profil secara acak")
        time.sleep(random.randint(5, 10))

    def change_password(self):
        # Mengubah password secara acak
        print("Mengubah password")
        time.sleep(random.randint(5, 10))

    def block_user(self):
        # Memblokir pengguna secara acak
        print("Memblokir pengguna")
        time.sleep(random.randint(5, 10))

    def view_profile(self):
        # Melihat profil secara acak
        print("Melihat profil pengguna lain")
        time.sleep(random.randint(5, 10))

    def targeted_following(self):
        # Menargetkan followers dari negara Korea dan Jepang
        target_locations = ["Korea", "Japan"]
        print(f"Menargetkan pengikut dari negara: {random.choice(target_locations)}")
        time.sleep(random.randint(5, 10))  # Delay acak untuk simulasi berpindah negara

# Inisialisasi dan jalankan bot
Bot = Bot()
Bot.login()
Bot.find_followers()
Bot.follow()
Bot.advanced_logic()
Bot.randomize_actions()
Bot.targeted_following()
Bot.driver.quit()
