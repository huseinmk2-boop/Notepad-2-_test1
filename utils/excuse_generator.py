import random

_EXCUSES = {
    "macet": [
        "Macet parah di jalan tol — ada kecelakaan 3 truk sekaligus.",
        "Busnya mogok persis di tengah jembatan, penumpang disuruh jalan kaki.",
        "Ban motor bocor di jalan tol, bengkel terdekat 8 km dari sini.",
        "Ada demo besar-besaran yang blokir jalan utama selama 2 jam.",
        "Jalan alternatif ditutup proyek, GPS sudah angkat tangan.",
        "Genangan banjir setinggi lutut, motor hampir tidak bisa lewat.",
        "Ojek online cancel 5 kali berturut-turut tanpa alasan jelas.",
        "Palang kereta turun 40 menit dan tidak ada tanda mau naik.",
    ],
    "pribadi": [
        "Alarm berbunyi di mimpi saja, bukan di dunia nyata.",
        "Matiin alarm, tidur lagi, bangun 2 jam kemudian.",
        "Kunci rumah jatuh ke dalam selokan — ternyata selokan itu dalam sekali.",
        "Baju yang mau dipakai ternyata belum kering setelah dicuci semalam.",
        "Dompet tertinggal di meja, harus balik ke rumah.",
        "Kucing duduk di atas tas dan menolak keras untuk pindah.",
        "Mati listrik, semua jam digital reset ke 00:00.",
        "HP jatuh ke dalam bak mandi tepat saat alarm bunyi.",
        "Lupa sarapan, hampir pingsan di depan pintu, terpaksa makan dulu.",
    ],
    "absurd": [
        "Google Maps membawa saya ke sungai dan bilang 'tujuan ada di depan'.",
        "Lift turun 10 lantai dulu sebelum naik — katanya itu fitur baru.",
        "Tetangga parkir tepat di depan mobil dan tidak bisa dihubungi sejak kemarin.",
        "Kucing saya menelan kunci motor. Kami masih menunggu perkembangan.",
        "Teman menelepon tepat saat mau keluar dan percakapannya tidak bisa dihentikan.",
        "Beli kopi dulu karena tanpa kopi tidak bisa berpikir — antriannya 45 menit.",
        "Saya salah naik bus dan sudah terlanjur 8 km ke arah yang berlawanan.",
        "Sepatu kanan dan kiri saya ternyata berbeda pasang — harus balik ganti.",
    ],
    "supernatural": [
        "Ada lubang hitam kecil di depan rumah yang menyedot semua waktu saya.",
        "Bulan darah semalam membuat saya tidak bisa tidur sampai subuh.",
        "Jam di rumah saya berjalan mundur sejak kemarin malam.",
        "Notepad saya meminta saya menyelesaikan 3 tantangan sebelum bisa pergi.",
        "Pintu rumah terus berpindah posisi setiap kali saya mendekatinya.",
        "Gravitasi di kamar saya 3x lebih kuat dari biasanya pagi ini.",
        "Ada bisikan misterius yang bilang 'jangan pergi dulu' — saya tidak berani melanggar.",
        "Kalkulator saya mulai berbicara sendiri dan mengajak saya berdebat soal hidup.",
    ],
}

_ALL_EXCUSES = [
    excuse
    for excuses in _EXCUSES.values()
    for excuse in excuses
]


def get_random_excuse() -> str:
    return random.choice(_ALL_EXCUSES)


def get_excuse_by_category(category: str) -> str:
    pool = _EXCUSES.get(category, _ALL_EXCUSES)
    return random.choice(pool)


def get_all_categories() -> list[str]:
    return list(_EXCUSES.keys())