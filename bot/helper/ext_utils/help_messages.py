mirror = """<b>Kirim tautan bersama dengan baris perintah atau </b>

/cmd tautan

<b>Dengan membalas tautan/file</b>:

/cmd -n nama baru -e -up tujuan unggah

<b>CATATAN:</b>
1. Perintah yang dimulai dengan <b>qb</b> HANYA untuk torrent."""

yt = """<b>Kirim tautan bersama dengan baris perintah</b>:

/cmd tautan
<b>Dengan membalas tautan</b>:
/cmd -n nama baru -z kata sandi -opt x:y|x1:y1

Periksa semua <a href='https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md'>SITUS</a> yang didukung di sini
Periksa semua opsi api yt-dlp dari <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a> ini atau gunakan <a href='https://t.me/mltb_official_channel/177'>script</a> ini untuk mengonversi argumen cli menjadi opsi api."""

clone = """Kirim tautan Gdrive|Gdot|Filepress|Filebee|Appdrive|Gdflix atau path rclone bersama dengan perintah atau dengan membalas tautan/rc_path menggunakan perintah.
Gunakan -sync untuk menggunakan metode sinkronisasi di rclone. Contoh: /cmd rcl/rclone_path -up rcl/rclone_path/rc -sync"""

new_name = """<b>Nama Baru</b>: -n

/cmd tautan -n nama baru
Catatan: Tidak berfungsi dengan torrent"""

multi_link = """<b>Beberapa tautan hanya dengan membalas tautan/file pertama</b>: -i

/cmd -i 10(jumlah tautan/file)"""

same_dir = """<b>Beberapa tautan dalam direktori unggah yang sama hanya dengan membalas tautan/file pertama</b>: -m

/cmd -i 10(jumlah tautan/file) -m nama folder (multi pesan)
/cmd -b -m nama folder (bulk-pesan/file)"""

thumb = """<b>Thumbnail untuk tugas saat ini</b>: -t

/cmd tautan -t tg-link-pesan (dokumen atau foto)"""

split_size = """<b>Ukuran pemisahan untuk tugas saat ini</b>: -sp

/cmd tautan -sp (500mb atau 2gb atau 4000000000)
Catatan: Hanya mb dan gb yang didukung atau tulis dalam byte tanpa satuan!"""

upload = """<b>Tujuan Unggah</b>: -up

/cmd tautan -up rcl/gdl (Untuk memilih konfigurasi rclone/token.pickle, remote & path/ gdrive id atau Tg id/username)
Anda bisa langsung menambahkan path unggahan: -up remote:dir/subdir atau -up (Gdrive_id) atau -up id/username
Jika DEFAULT_UPLOAD adalah `rc`, Anda bisa menggunakan up: `gd` untuk mengunggah menggunakan alat gdrive ke GDRIVE_ID.
Jika DEFAULT_UPLOAD adalah `gd`, Anda bisa menggunakan up: `rc` untuk mengunggah ke RCLONE_PATH.

Jika Anda ingin menambahkan path atau gdrive secara manual dari konfigurasi/token Anda (diunggah dari usetting), tambahkan mrcc: untuk rclone dan mtp: sebelum path/gdrive_id tanpa spasi.
/cmd tautan -up mrcc:main:dump atau -up mtp:gdrive_id atau -up b:id/@username/pm(leech oleh bot) atau -up u:id/@username(leech oleh pengguna) atau -up m:id/@username(leech campuran)

Jika Anda ingin menentukan apakah menggunakan token.pickle atau akun layanan, Anda bisa menambahkan tp:gdrive_id atau sa:gdrive_id atau mtp:gdrive_id.
DEFAULT_UPLOAD tidak mempengaruhi perintah leech.
"""

user_download = """<b>Unduh Pengguna</b>: tautan

/cmd tp:tautan untuk mengunduh menggunakan token.pickle pemilik jika akun layanan diaktifkan.
/cmd sa:tautan untuk mengunduh menggunakan akun layanan jika akun layanan dinonaktifkan.
/cmd tp:gdrive_id untuk mengunduh menggunakan token.pickle dan file_id jika akun layanan diaktifkan.
/cmd sa:gdrive_id untuk mengunduh menggunakan akun layanan dan file_id jika akun layanan dinonaktifkan.
/cmd mtp:gdrive_id atau mtp:tautan untuk mengunduh menggunakan token.pickle pengguna yang diunggah dari usetting
/cmd mrcc:remote:path untuk mengunduh menggunakan konfigurasi rclone pengguna yang diunggah dari usetting"""

rcf = """<b>Flag Rclone</b>: -rcf

/cmd tautan|path|rcl -up path|rcl -rcf --buffer-size:8M|--drive-starred-only|key|key:value
Ini akan menggantikan semua flag lainnya kecuali --exclude
Periksa semua <a href='https://rclone.org/flags/'>RcloneFlags</a>."""

bulk = """<b>Unduhan Massal</b>: -b

Bulk dapat digunakan melalui pesan teks dan dengan membalas file teks yang berisi tautan yang dipisahkan dengan baris baru.
Anda hanya bisa menggunakannya dengan membalas pesan (teks/file).
Contoh:
tautan1 -n nama baru -up remote1:path1 -rcf |key:value|key:value
tautan2 -z -n nama baru -up remote2:path2
tautan3 -e -n nama baru -up remote2:path2
Balas ke contoh ini dengan perintah ini -> /cmd -b(bulk) atau /cmd -b -m nama folder
Anda bisa menetapkan awal dan akhir dari tautan dalam bulk seperti seed, dengan -b start:end atau hanya akhir dengan -b :end atau hanya awal dengan -b start.
Awal default adalah dari nol (tautan pertama) hingga tak terhingga."""

rlone_dl = """<b>Unduhan Rclone</b>:

Perlakukan path rclone persis seperti tautan
/cmd main:dump/ubuntu.iso atau rcl (Untuk memilih konfigurasi, remote, dan path)
Pengguna dapat menambahkan rclone mereka sendiri dari pengaturan pengguna
Jika Anda ingin menambahkan path secara manual dari konfigurasi Anda, tambahkan mrcc: sebelum path tanpa spasi
/cmd mrcc:main:dump/ubuntu.iso"""

extract_zip = """<b>Ekstrak/Zip</b>: -e -z

/cmd tautan -e kata_sandi (untuk mengekstrak yang dilindungi kata sandi)
/cmd tautan -z kata_sandi (untuk zip yang dilindungi kata sandi)
/cmd tautan -z kata_sandi -e (untuk mengekstrak dan zip yang dilindungi kata sandi)
Catatan: Ketika ekstrak dan zip ditambahkan dengan perintah, ekstrak akan dilakukan terlebih dahulu dan kemudian zip, jadi selalu ekstrak terlebih dahulu"""

join = """<b>Gabungkan File Terpisah</b>: -j

Opsi ini hanya akan berfungsi sebelum ekstrak dan zip, jadi sebagian besar akan digunakan dengan argumen -m (samedir)
Dengan Membalas:
/cmd -i 3 -j -m nama folder
/cmd -b -j -m nama folder
Jika Anda memiliki tautan (folder) yang memiliki file terpisah:
/cmd tautan -j"""

tg_links = """<b>Tautan TG</b>:

Perlakukan tautan seperti tautan langsung lainnya
Beberapa tautan memerlukan akses pengguna, jadi pastikan Anda menambahkan USER_SESSION_STRING untuk itu.
Tiga jenis tautan:
Publik: https://t.me/channel_name/message_id
Pribadi: tg://openmessage?user_id=xxxxxx&message_id=xxxxx
Super: https://t.me/c/channel_id/message_id
Rentang: https://t.me/channel_name/first_message_id-last_message_id
Contoh Rentang: tg://openmessage?user_id=xxxxxx&message_id=555-560 atau https://t.me/channel_name/100-150
Catatan: Tautan rentang hanya akan berfungsi dengan membalas perintah ke tautan tersebut"""

sample_video = """<b>Video Sampel</b>: -sv

Buat video sampel untuk satu video atau folder video.
/cmd -sv (ini akan mengambil nilai default yaitu durasi sampel 60 detik dan durasi bagian 4 detik).
Anda bisa mengontrol nilai-nilai tersebut. Contoh: /cmd -sv 70:5(durasi-sampel:durasi-bagian) atau /cmd -sv :5 atau /cmd -sv 70."""

screenshot = """<b>Tangkapan Layar</b>: -ss

Buat hingga 10 tangkapan layar untuk satu video atau folder video.
/cmd -ss (ini akan mengambil nilai default yaitu 10 foto).
Anda bisa mengontrol nilai ini. Contoh: /cmd -ss 6."""

seed = """<b>Seed Bittorrent</b>: -d

/cmd tautan -d rasio:waktu_seed atau dengan membalas file/tautan
Untuk menentukan rasio dan waktu seed, tambahkan -d rasio:waktu.
Contoh: -d 0.7:10 (rasio dan waktu) atau -d 0.7 (hanya rasio) atau -d :10 (hanya waktu) di mana waktu dalam menit"""

zip_arg = """<b>Zip</b>: -z kata_sandi

/cmd tautan -z (zip)
/cmd tautan -z kata_sandi (zip yang dilindungi kata sandi)"""

qual = """<b>Tombol Kualitas</b>: -s

Jika kualitas default ditambahkan dari opsi yt-dlp menggunakan opsi format dan Anda perlu memilih kualitas untuk tautan tertentu atau tautan dengan fitur multi tautan.
/cmd tautan -s"""

yt_opt = """<b>Opsi</b>: -opt

/cmd tautan -opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{"ffmpeg": ["-threads", "4"]}|wait_for_video:(5, 100)
Catatan: Tambahkan `^` sebelum bilangan bulat atau pecahan, beberapa nilai harus numerik dan beberapa string.
Seperti playlist_items:10 bekerja dengan string, jadi tidak perlu menambahkan `^` sebelum angka, tetapi playlistend hanya bekerja dengan bilangan bulat sehingga Anda harus menambahkan `^` sebelum angka seperti contoh di atas.
Anda juga dapat menambahkan tuple dan dict. Gunakan tanda kutip ganda di dalam dict."""

convert_media = """<b>Konversi Media</b>: -ca -cv
/cmd tautan -ca mp3 -cv mp4 (konversi semua audio ke mp3 dan semua video ke mp4)
/cmd tautan -ca mp3 (konversi semua audio ke mp3)
/cmd tautan -cv mp4 (konversi semua video ke mp4)
/cmd tautan -ca mp3 + flac ogg (konversi hanya audio flac dan ogg ke mp3)
/cmd tautan -cv mkv - webm flv (konversi semua video ke mp4 kecuali webm dan flv)"""

force_start = """<b>Mulai Paksa</b>: -f -fd -fu
/cmd tautan -f (paksa unduh dan unggah)
/cmd tautan -fd (paksa unduh saja)
/cmd tautan -fu (paksa unggah langsung setelah unduhan selesai)"""

gdrive = """<b>Gdrive</b>: tautan
Jika DEFAULT_UPLOAD adalah `rc`, maka Anda dapat menggunakan up: `gd` untuk mengunggah menggunakan alat gdrive ke GDRIVE_ID.
/cmd tautanGdrive atau gdl atau gdriveId -up gdl atau gdriveId atau gd
/cmd tp:tautanGdrive atau tp:gdriveId -up tp:gdriveId atau gdl atau gd (untuk menggunakan token.pickle jika akun layanan diaktifkan)
/cmd sa:tautanGdrive atau sa:gdriveId -p sa:gdriveId atau gdl atau gd (untuk menggunakan akun layanan jika akun layanan dinonaktifkan)
/cmd mtp:tautanGdrive atau mtp:gdriveId -up mtp:gdriveId atau gdl atau gd (jika Anda telah menambahkan upload gdriveId dari usetting) (untuk menggunakan token.pickle pengguna yang diunggah oleh usetting)"""

rclone_cl = """<b>Rclone</b>: path
Jika DEFAULT_UPLOAD adalah `gd`, maka Anda dapat menggunakan up: `rc` untuk mengunggah ke RCLONE_PATH.
/cmd rcl/rclone_path -up rcl/rclone_path/rc -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue
/cmd rcl atau rclonePath -up rclonePath atau rc atau rcl
/cmd mrcc:rclonePath -up rcl atau rc (jika Anda telah menambahkan rclone path dari usetting) (untuk menggunakan konfigurasi pengguna)"""

name_sub = """<b>Penggantian Nama</b>: -ns
/cmd tautan -ns tea : coffee : s|ACC :  : s|mP4
Ini akan mempengaruhi semua file. Format: kataYangDiganti : kataPengganti : sensitifKasus
1. tea akan diganti dengan coffee, sensitif terhadap huruf besar/kecil karena saya menambahkan `s` di akhir opsi.
2. ACC akan dihapus karena saya tidak menambahkan apa-apa di bagian pengganti, sensitif terhadap huruf besar/kecil karena saya menambahkan `s` di akhir opsi.
3. mP4 akan dihapus karena saya tidak menambahkan pengganti sama sekali.
"""

mixed_leech = """Leech Campuran: -ml
/cmd tautan -ml (leech dari sesi pengguna dan bot sesuai ukuran)"""

YT_HELP_DICT = {
    "main": yt,
    "New-Name": f"{new_name}\nNote: Don't add file extension",
    "Zip": zip_arg,
    "Quality": qual,
    "Options": yt_opt,
    "Multi-Link": multi_link,
    "Same-Directory": same_dir,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "Name-Substitute": name_sub,
    "Mixed-Leech": mixed_leech,
}

MIRROR_HELP_DICT = {
    "main": mirror,
    "New-Name": new_name,
    "DL-Auth": "<b>Direct link authorization</b>: -au -ap\n\n/cmd link -au username -ap password",
    "Headers": "<b>Direct link custom headers</b>: -h\n\n/cmd link -h key: value key1: value1",
    "Extract/Zip": extract_zip,
    "Torrent-Files": "<b>Bittorrent File Selection</b>: -s\n\n/cmd link -s or by replying to file/link",
    "Torrent-Seed": seed,
    "Multi-Link": multi_link,
    "Same-Directory": same_dir,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Join": join,
    "Rclone-DL": rlone_dl,
    "Tg-Links": tg_links,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "User-Download": user_download,
    "Name-Substitute": name_sub,
    "Mixed-Leech": mixed_leech,
}

CLONE_HELP_DICT = {
    "main": clone,
    "Multi-Link": multi_link,
    "Bulk": bulk,
    "Gdrive": gdrive,
    "Rclone": rclone_cl,
}

RSS_HELP_MESSAGE = """
Gunakan format ini untuk menambahkan URL feed:
Judul1 tautan (wajib)
Judul2 tautan -c cmd -inf xx -exf xx
Judul3 tautan -c cmd -d rasio:waktu -z password

-c perintah -up mrcc:remote:path/subdir -rcf --buffer-size:8M|key|key:value
-inf Untuk filter kata yang disertakan.
-exf Untuk filter kata yang dikecualikan.
-stv true atau false (filter sensitif)

Contoh: Judul https://www.rss-url.com -inf 1080 atau 720 atau 144p|mkv atau mp4|hevc -exf flv atau web|xxx
Filter ini akan memparsing tautan yang judulnya mengandung `(1080 atau 720 atau 144p) dan (mkv atau mp4) dan hevc` dan tidak mengandung (flv atau web) dan xxx. Kamu bisa menambahkan apa saja yang kamu mau.

Contoh lain: -inf 1080 atau 720p|.web. atau .webrip.|hvec atau x264. Ini akan memparsing judul yang mengandung (1080 atau 720p) dan (.web. atau .webrip.) dan (hvec atau x264). Saya menambahkan spasi sebelum dan sesudah 1080 untuk menghindari pencocokan yang salah. Jika ada angka `10805695` di judul, itu akan mencocokkan 1080 jika ditambahkan 1080 tanpa spasi setelahnya.

Catatan Filter:
1. | artinya dan.
2. Tambahkan `or` antara kunci yang mirip, kamu bisa menambahkannya antara kualitas atau antara ekstensi, jadi jangan menambahkan filter seperti ini f: 1080|mp4 atau 720|web karena ini akan memparsing 1080 dan (mp4 atau 720) dan web ... bukan (1080 dan mp4) atau (720 dan web).
3. Kamu bisa menambahkan `or` dan `|` sebanyak yang kamu mau.
4. Perhatikan judul jika ada karakter khusus statis setelah atau sebelum kualitas atau ekstensi atau apapun, dan gunakan karakter tersebut dalam filter untuk menghindari pencocokan yang salah.
Timeout: 60 detik.
"""

PASSWORD_ERROR_MESSAGE = """
<b>This link requires a password!</b>
- Masukkan <b>::</b> setelah tautan dan tulis kata sandinya setelah tanda tersebut.

<b>Contoh:</b> tautan::kata sandiku
"""

