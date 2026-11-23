
import json
import os
from datetime import datetime
import time
import os

# ==========================================
# SHOWROOM MANAGEMENT SYSTEM
# ==========================================

FILE_DATA = "showroom_data.json"

data = {
    "mobil": [],
    "pelanggan": [],
    "transaksi": []
}

# ==========================================
# 1. PENYIMPANAN DATA
# ==========================================

def simpan_data():
    try:
        with open(FILE_DATA, "w") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("Gagal menyimpan data!")


def muat_data():
    global data

    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, "r") as file:
                hasil = json.load(file)

            if not isinstance(hasil, dict):
                raise ValueError("Format data tidak valid")

            for kunci in data:
                if not isinstance(hasil.get(kunci, []), list):
                    raise ValueError("Format koleksi tidak valid")
                data[kunci] = hasil.get(kunci, [])

        except (OSError, json.JSONDecodeError, ValueError):
            print("File data bermasalah. Menggunakan data kosong.")
            data = {
                "mobil": [],
                "pelanggan": [],
                "transaksi": []
            }


# ==========================================
# 2. FUNGSI BANTUAN
# ==========================================

def input_teks(pesan):
    while True:
        nilai = input(pesan).strip()

        if nilai:
            return nilai

        print("Input tidak boleh kosong!")


def input_angka(pesan, minimum=0):
    while True:
        try:
            nilai = int(input(pesan))

            if nilai >= minimum:
                return nilai

            print(f"Nilai minimal adalah {minimum}.")

        except ValueError:
            print("Masukkan angka yang valid!")


def cari_berdasarkan_id(koleksi, id_data):
    for item in koleksi:
        if item["id"] == id_data.upper():
            return item
    return None


def format_rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")


def buat_id(prefix, koleksi):
    nomor = 1

    while True:
        id_baru = f"{prefix}{nomor:03d}"

        if not cari_berdasarkan_id(koleksi, id_baru):
            return id_baru

        nomor += 1


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def animasi_loading(pesan="Sedang memproses...", durasi=0.02, panjang=20):
    clear_screen()
    print("\n" + "=" * 60)
    print(f"{pesan}")
    print("=" * 60)

    for i in range(101):
        bar = "█" * (i // 5) + "░" * (panjang - i // 5)
        print(f"\r[{bar}] {i}%", end="", flush=True)
        time.sleep(durasi)

    print("\n")


def animasi_berjalan(pesan="Mobil sedang bergerak..."):
    clear_screen()
    print(f"\n{pesan}\n")

    mobil_animasi = [
        "      ___      ___      ___",
        "____/  )____/  )____/  )",
        "(____ _   _   _   _   _  )",
        "     `-(_)--(_)-'  `-(_)--(_)-'",
    ]

    for offset in range(0, 45):
        frame = "\n".join(" " * offset + baris for baris in mobil_animasi)
        print(frame)
        time.sleep(0.05)
        clear_screen()
        print(f"\n{pesan}\n")

    print("\n")


def banner_premium(judul):
    biru = "\033[94m"
    cyan = "\033[96m"
    kuning = "\033[93m"
    putih = "\033[97m"
    reset = "\033[0m"

    print(cyan + "=" * 72 + reset)
    print(kuning + "╔" + "═" * 70 + "╗" + reset)
    print(kuning + "║" + " " * 70 + "║" + reset)
    print(kuning + "║" + f"{judul:^70}" + "║" + reset)
    print(kuning + "║" + " " * 70 + "║" + reset)
    print(kuning + "╚" + "═" * 70 + "╝" + reset)
    print(cyan + "=" * 72 + reset)


def menu_premium(title, daftar_menu):
    clear_screen()
    banner_premium(title)
    print()
    for nomor, label in daftar_menu.items():
        print(f"{nomor}. {label}")
    print()
    print("=" * 72)


# ==========================================
# 3. MANAJEMEN DATA MOBIL (CRUD)
# ==========================================

def animasi_sukses(mobil):
    clear_screen()

    hijau = "\033[92m"
    cyan = "\033[96m"
    kuning = "\033[93m"
    putih = "\033[97m"
    reset = "\033[0m"

    print(cyan + """
    ╔══════════════════════════════════════════════╗
    ║                                              ║
    ║           SHOWROOM MANAGEMENT SYSTEM         ║
    ║                PREMIUM EDITION               ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """ + reset)

    print(kuning + "\n       🚗  PROCESSING NEW VEHICLE DATA\n" + reset)
    animasi_berjalan("Mobil sedang bergerak...")

    print(hijau + "    ╔══════════════════════════════════════╗")
    print("    ║                                      ║")
    print("    ║       ✓ DATA BERHASIL DISIMPAN!      ║")
    print("    ║                                      ║")
    print("    ╚══════════════════════════════════════╝" + reset)

    print(putih + f"""
       ID MOBIL  : {mobil['id']}
       MEREK     : {mobil['merek']}
       MODEL     : {mobil['model']}
       TAHUN     : {mobil['tahun']}
       HARGA     : Rp{mobil['harga']:,}
       STATUS    : {mobil['status']}
    """ + reset)

    print(cyan + "       SHOWROOM SYSTEM | DATA SAVED SUCCESSFULLY" + reset)

    time.sleep(1.5)
  
def tambah_mobil():
    print("\n=== TAMBAH DATA MOBIL ===")

    mobil = {
        "id": buat_id("M", data["mobil"]),
        "merek": input_teks("Merek: ").title(),
        "model": input_teks("Model: ").title(),
        "tahun": input_angka("Tahun produksi: ", 1886),
        "warna": input_teks("Warna: ").title(),
        "transmisi": input_teks("Transmisi: ").title(),
        "bahan_bakar": input_teks("Bahan bakar: ").title(),
        "harga": input_angka("Harga mobil: ", 1),
        "status": "Tersedia"
    }

    data["mobil"].append(mobil)
    animasi_loading("Menyimpan data mobil...")
    simpan_data()
    animasi_sukses(mobil)

def tampilkan_mobil():
    print("\n=== DAFTAR MOBIL SHOWROOM ===")

    if not data["mobil"]:
        print("Belum ada data mobil.")
        return

    print("-" * 100)
    print(f"{'ID':<8} {'MEREK':<15} {'MODEL':<18} "
          f"{'TAHUN':<8} {'HARGA':<20} {'STATUS':<12}")
    print("-" * 100)

    for mobil in data["mobil"]:
        print(
            f"{mobil['id']:<8} "
            f"{mobil['merek']:<15} "
            f"{mobil['model']:<18} "
            f"{mobil['tahun']:<8} "
            f"{format_rupiah(mobil['harga']):<20} "
            f"{mobil['status']:<12}"
        )

    print("-" * 100)


def detail_mobil(mobil):
    print("\n=== DETAIL MOBIL ===")

    for kunci, nilai in mobil.items():
        if kunci == "harga":
            nilai = format_rupiah(nilai)

        print(f"{kunci.replace('_', ' ').title():<15}: {nilai}")


def update_mobil():
    print("\n=== UPDATE DATA MOBIL ===")

    id_mobil = input_teks("Masukkan ID mobil: ").upper()
    mobil = cari_berdasarkan_id(data["mobil"], id_mobil)

    if not mobil:
        print("Mobil tidak ditemukan!")
        return

    detail_mobil(mobil)

    if mobil["status"] == "Terjual":
        print("Mobil terjual tidak dapat diubah melalui menu ini.")
        return

    print("\nMasukkan data baru.")
    print("Tekan ENTER jika ingin mempertahankan data lama.")

    for kunci in ["merek", "model", "warna",
                  "transmisi", "bahan_bakar"]:

        nilai = input(f"{kunci.title()} [{mobil[kunci]}]: ").strip()

        if nilai:
            mobil[kunci] = nilai.title()

    tahun = input(f"Tahun [{mobil['tahun']}]: ").strip()

    if tahun:
        if tahun.isdigit() and 1886 <= int(tahun) <= datetime.now().year + 1:
            mobil["tahun"] = int(tahun)
        else:
            print("Tahun tidak valid, data lama dipertahankan.")

    harga = input(f"Harga [{mobil['harga']}]: ").strip()

    if harga:
        if harga.isdigit() and int(harga) > 0:
            mobil["harga"] = int(harga)
        else:
            print("Harga tidak valid, data lama dipertahankan.")

    animasi_loading("Memperbarui data mobil...")
    simpan_data()
    print("Data mobil berhasil diperbarui!")


def hapus_mobil():
    print("\n=== HAPUS DATA MOBIL ===")

    id_mobil = input_teks("Masukkan ID mobil: ").upper()
    mobil = cari_berdasarkan_id(data["mobil"], id_mobil)

    if not mobil:
        print("Mobil tidak ditemukan!")
        return

    if any(t["id_mobil"] == id_mobil and
           t["status"] == "Berhasil" for t in data["transaksi"]):
        print("Mobil memiliki riwayat transaksi. Tidak dapat dihapus.")
        return

    detail_mobil(mobil)

    konfirmasi = input("Yakin hapus mobil? (Y/N): ").strip().upper()

    if konfirmasi == "Y":
        animasi_loading("Menghapus data mobil...")
        data["mobil"].remove(mobil)
        simpan_data()
        print("Data berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")


# ==========================================
# 4. MANAJEMEN PELANGGAN
# ==========================================

def tambah_pelanggan():
    print("\n=== TAMBAH PELANGGAN ===")

    pelanggan = {
        "id": buat_id("P", data["pelanggan"]),
        "nama": input_teks("Nama pelanggan: ").title(),
        "telepon": input_teks("Nomor telepon: "),
        "alamat": input_teks("Alamat: ").title()
    }

    data["pelanggan"].append(pelanggan)
    animasi_loading("Menyimpan data pelanggan...")
    simpan_data()

    print(f"Pelanggan berhasil ditambahkan! ID: {pelanggan['id']}")


def tampilkan_pelanggan():
    print("\n=== DATA PELANGGAN ===")

    if not data["pelanggan"]:
        print("Belum ada pelanggan.")
        return

    for p in data["pelanggan"]:
        print(
            f"\nID: {p['id']}\n"
            f"Nama: {p['nama']}\n"
            f"Telepon: {p['telepon']}\n"
            f"Alamat: {p['alamat']}"
        )
        print("-" * 35)


def update_pelanggan():
    id_p = input_teks("Masukkan ID pelanggan: ").upper()
    pelanggan = cari_berdasarkan_id(data["pelanggan"], id_p)

    if not pelanggan:
        print("Pelanggan tidak ditemukan!")
        return

    for kunci in ["nama", "telepon", "alamat"]:
        nilai = input(f"{kunci.title()} [{pelanggan[kunci]}]: ").strip()

        if nilai:
            pelanggan[kunci] = (
                nilai.title() if kunci != "telepon" else nilai
            )

    animasi_loading("Memperbarui data pelanggan...")
    simpan_data()
    print("Data pelanggan berhasil diperbarui!")


def hapus_pelanggan():
    id_p = input_teks("Masukkan ID pelanggan: ").upper()
    pelanggan = cari_berdasarkan_id(data["pelanggan"], id_p)

    if not pelanggan:
        print("Pelanggan tidak ditemukan!")
        return

    if any(t["id_pelanggan"] == id_p and
           t["status"] == "Berhasil" for t in data["transaksi"]):
        print("Pelanggan memiliki riwayat transaksi. Tidak dapat dihapus.")
        return

    konfirmasi = input("Hapus pelanggan ini? (Y/N): ").strip().upper()

    if konfirmasi == "Y":
        animasi_loading("Menghapus data pelanggan...")
        data["pelanggan"].remove(pelanggan)
        simpan_data()
        print("Pelanggan berhasil dihapus!")


# ==========================================
# 5. SEARCHING
# ==========================================

def linear_search(koleksi, kata_kunci, atribut):
    hasil = []

    kata_kunci = kata_kunci.strip().lower()

    for item in koleksi:
        nilai = str(item[atribut]).lower()

        if kata_kunci in nilai:
            hasil.append(item)

    return hasil


def binary_search_id(koleksi, id_cari):
    data_urut = sorted(koleksi, key=lambda x: x["id"])
    kiri = 0
    kanan = len(data_urut) - 1

    id_cari = id_cari.upper()

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        id_tengah = data_urut[tengah]["id"]

        if id_tengah == id_cari:
            return data_urut[tengah]

        elif id_tengah < id_cari:
            kiri = tengah + 1

        else:
            kanan = tengah - 1

    return None


def menu_pencarian():
    print("\n=== PENCARIAN MOBIL ===")
    print("1. Berdasarkan ID (Binary Search)")
    print("2. Berdasarkan Merek")
    print("3. Berdasarkan Model")
    print("4. Berdasarkan Tahun")
    print("5. Berdasarkan Status")
    print("6. Berdasarkan Transmisi")

    pilihan = input("Pilih pencarian: ").strip()

    if pilihan == "1":
        kata = input_teks("Masukkan ID: ")
        hasil = binary_search_id(data["mobil"], kata)

        if hasil:
            detail_mobil(hasil)
        else:
            print("Mobil tidak ditemukan!")

        return

    atribut = {
        "2": "merek",
        "3": "model",
        "4": "tahun",
        "5": "status",
        "6": "transmisi"
    }

    if pilihan not in atribut:
        print("Pilihan tidak valid!")
        return

    kata = input_teks("Masukkan kata kunci: ")
    hasil = linear_search(data["mobil"], kata, atribut[pilihan])

    if hasil:
        print(f"\nDitemukan {len(hasil)} mobil:")

        for mobil in hasil:
            detail_mobil(mobil)
    else:
        print("Data tidak ditemukan!")


# ==========================================
# 6. SORTING
# ==========================================

def bubble_sort(koleksi, atribut, ascending=True):
    hasil = koleksi.copy()
    n = len(hasil)

    for i in range(n):
        for j in range(0, n - i - 1):

            a = hasil[j][atribut]
            b = hasil[j + 1][atribut]

            kondisi = a > b if ascending else a < b

            if kondisi:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

    return hasil


def selection_sort(koleksi, atribut, ascending=True):
    hasil = koleksi.copy()
    n = len(hasil)

    for i in range(n):
        indeks = i

        for j in range(i + 1, n):
            a = hasil[j][atribut]
            b = hasil[indeks][atribut]

            if (a < b if ascending else a > b):
                indeks = j

        hasil[i], hasil[indeks] = hasil[indeks], hasil[i]

    return hasil


def insertion_sort(koleksi, atribut, ascending=True):
    hasil = koleksi.copy()

    for i in range(1, len(hasil)):
        kunci = hasil[i]
        j = i - 1

        while j >= 0:
            kondisi = (
                hasil[j][atribut] > kunci[atribut]
                if ascending
                else hasil[j][atribut] < kunci[atribut]
            )

            if kondisi:
                hasil[j + 1] = hasil[j]
                j -= 1
            else:
                break

        hasil[j + 1] = kunci

    return hasil


def menu_sorting():
    print("\n=== PENGURUTAN DATA MOBIL ===")
    print("1. Harga termurah")
    print("2. Harga termahal")
    print("3. Tahun terbaru")
    print("4. Tahun terlama")
    print("5. Merek A-Z")
    print("6. Merek Z-A")

    pilihan = input("Pilih pengurutan: ").strip()

    pengaturan = {
        "1": ("harga", True, bubble_sort),
        "2": ("harga", False, bubble_sort),
        "3": ("tahun", False, selection_sort),
        "4": ("tahun", True, selection_sort),
        "5": ("merek", True, insertion_sort),
        "6": ("merek", False, insertion_sort)
    }

    if pilihan not in pengaturan:
        print("Pilihan tidak valid!")
        return

    atribut, ascending, algoritma = pengaturan[pilihan]
    hasil = algoritma(data["mobil"], atribut, ascending)

    print("\n=== HASIL PENGURUTAN ===")

    for mobil in hasil:
        print(
            f"{mobil['id']} | "
            f"{mobil['merek']} {mobil['model']} | "
            f"{mobil['tahun']} | "
            f"{format_rupiah(mobil['harga'])}"
        )


# ==========================================
# 7. TRANSAKSI PENJUALAN
# ==========================================

def transaksi_penjualan():
    print("\n=== TRANSAKSI PENJUALAN ===")

    tersedia = [
        m for m in data["mobil"]
        if m["status"] == "Tersedia"
    ]

    if not tersedia:
        print("Tidak ada mobil yang tersedia!")
        return

    tampilkan_mobil()

    id_mobil = input_teks("ID mobil yang dibeli: ").upper()
    mobil = cari_berdasarkan_id(tersedia, id_mobil)

    if not mobil:
        print("Mobil tidak tersedia!")
        return

    tampilkan_pelanggan()

    id_p = input_teks("ID pelanggan: ").upper()
    pelanggan = cari_berdasarkan_id(data["pelanggan"], id_p)

    if not pelanggan:
        print("Pelanggan tidak ditemukan!")
        return

    print("\nHarga:", format_rupiah(mobil["harga"]))

    diskon = input_angka("Diskon: ", 0)

    if diskon > mobil["harga"]:
        print("Diskon tidak boleh melebihi harga mobil!")
        return

    total = mobil["harga"] - diskon

    print("Total pembayaran:", format_rupiah(total))

    konfirmasi = input("Konfirmasi transaksi? (Y/N): ").strip().upper()

    if konfirmasi != "Y":
        print("Transaksi dibatalkan.")
        return

    transaksi = {
        "id": buat_id("TR", data["transaksi"]),
        "id_mobil": id_mobil,
        "id_pelanggan": id_p,
        "harga": mobil["harga"],
        "diskon": diskon,
        "total": total,
        "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Berhasil"
    }

    data["transaksi"].append(transaksi)
    mobil["status"] = "Terjual"

    animasi_loading("Memproses transaksi penjualan...")
    simpan_data()

    print("\nTransaksi berhasil!")
    print("ID Transaksi:", transaksi["id"])
    print("Total:", format_rupiah(total))


def riwayat_transaksi():
    print("\n=== RIWAYAT TRANSAKSI ===")

    if not data["transaksi"]:
        print("Belum ada transaksi.")
        return

    for t in data["transaksi"]:
        mobil = cari_berdasarkan_id(data["mobil"], t["id_mobil"])
        pelanggan = cari_berdasarkan_id(
            data["pelanggan"], t["id_pelanggan"]
        )

        nama_mobil = (
            f"{mobil['merek']} {mobil['model']}"
            if mobil else "Data mobil tidak tersedia"
        )

        nama_pelanggan = (
            pelanggan["nama"]
            if pelanggan else "Data pelanggan tidak tersedia"
        )

        print("-" * 45)
        print("ID Transaksi :", t["id"])
        print("Mobil        :", nama_mobil)
        print("Pelanggan    :", nama_pelanggan)
        print("Tanggal      :", t["tanggal"])
        print("Total        :", format_rupiah(t["total"]))
        print("Status       :", t["status"])


def batalkan_transaksi():
    print("\n=== PEMBATALAN TRANSAKSI ===")

    riwayat_transaksi()

    id_tr = input_teks("Masukkan ID transaksi: ").upper()
    transaksi = cari_berdasarkan_id(data["transaksi"], id_tr)

    if not transaksi:
        print("Transaksi tidak ditemukan!")
        return

    if transaksi["status"] != "Berhasil":
        print("Transaksi sudah dibatalkan sebelumnya.")
        return

    konfirmasi = input("Batalkan transaksi? (Y/N): ").strip().upper()

    if konfirmasi == "Y":
        animasi_loading("Membatalkan transaksi...")
        mobil = cari_berdasarkan_id(
            data["mobil"], transaksi["id_mobil"]
        )

        if mobil:
            mobil["status"] = "Tersedia"

        transaksi["status"] = "Dibatalkan"

        simpan_data()
        print("Transaksi berhasil dibatalkan!")


# ==========================================
# 8. LAPORAN DAN STATISTIK
# ==========================================

def laporan_statistik():
    print("\n=== LAPORAN SHOWROOM ===")

    total_mobil = len(data["mobil"])

    tersedia = sum(
        1 for m in data["mobil"]
        if m["status"] == "Tersedia"
    )

    terjual = sum(
        1 for m in data["mobil"]
        if m["status"] == "Terjual"
    )

    transaksi_berhasil = [
        t for t in data["transaksi"]
        if t["status"] == "Berhasil"
    ]

    pendapatan = sum(t["total"] for t in transaksi_berhasil)

    print("Total Mobil       :", total_mobil)
    print("Mobil Tersedia    :", tersedia)
    print("Mobil Terjual     :", terjual)
    print("Total Pelanggan   :", len(data["pelanggan"]))
    print("Total Transaksi   :", len(transaksi_berhasil))
    print("Total Pendapatan  :", format_rupiah(pendapatan))

    if data["mobil"]:
        termahal = max(data["mobil"], key=lambda m: m["harga"])
        termurah = min(data["mobil"], key=lambda m: m["harga"])

        print(
            "Mobil Termahal    :",
            termahal["merek"], termahal["model"]
        )

        print(
            "Mobil Termurah    :",
            termurah["merek"], termurah["model"]
        )

    # Statistik merek menggunakan SET dan DICTIONARY
    statistik_merek = {}

    for m in data["mobil"]:
        merek = m["merek"]
        statistik_merek[merek] = statistik_merek.get(merek, 0) + 1

    if statistik_merek:
        print("\nJumlah Mobil per Merek:")

        for merek, jumlah in statistik_merek.items():
            print(f"- {merek}: {jumlah}")

    # Statistik mobil terlaris
    penjualan = {}

    for t in transaksi_berhasil:
        id_mobil = t["id_mobil"]
        penjualan[id_mobil] = penjualan.get(id_mobil, 0) + 1

    if penjualan:
        terlaris = max(penjualan, key=penjualan.get)
        mobil_laris = cari_berdasarkan_id(data["mobil"], terlaris)

        if mobil_laris:
            print(
                "\nMobil Terlaris:",
                mobil_laris["merek"],
                mobil_laris["model"]
            )


# ==========================================
# 9. MENU MANAJEMEN
# ==========================================

def menu_mobil():
    while True:
        menu_premium("MANAJEMEN DATA MOBIL", {
            "1": "Tambah Mobil",
            "2": "Tampilkan Mobil",
            "3": "Update Mobil",
            "4": "Hapus Mobil",
            "0": "Kembali"
        })

        pilih = input("Pilihan: ").strip()

        if pilih == "1":
            tambah_mobil()
        elif pilih == "2":
            tampilkan_mobil()
        elif pilih == "3":
            update_mobil()
        elif pilih == "4":
            hapus_mobil()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")


def menu_pelanggan():
    while True:
        menu_premium("MANAJEMEN PELANGGAN", {
            "1": "Tambah Pelanggan",
            "2": "Tampilkan Pelanggan",
            "3": "Update Pelanggan",
            "4": "Hapus Pelanggan",
            "0": "Kembali"
        })

        pilih = input("Pilihan: ").strip()

        if pilih == "1":
            tambah_pelanggan()
        elif pilih == "2":
            tampilkan_pelanggan()
        elif pilih == "3":
            update_pelanggan()
        elif pilih == "4":
            hapus_pelanggan()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")


# ==========================================
# 10. PROGRAM UTAMA
# ==========================================

def main():
    muat_data()
    animasi_loading("Memulai showroom system...")

    while True:
        menu_premium("SHOWROOM MANAGEMENT SYSTEM", {
            "1": "Manajemen Data Mobil",
            "2": "Manajemen Data Pelanggan",
            "3": "Transaksi Penjualan",
            "4": "Pencarian Mobil",
            "5": "Pengurutan Data Mobil",
            "6": "Laporan dan Statistik",
            "7": "Riwayat Transaksi",
            "8": "Pembatalan Transaksi",
            "0": "Keluar"
        })

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            menu_mobil()

        elif pilihan == "2":
            menu_pelanggan()

        elif pilihan == "3":
            transaksi_penjualan()

        elif pilihan == "4":
            menu_pencarian()

        elif pilihan == "5":
            menu_sorting()

        elif pilihan == "6":
            laporan_statistik()

        elif pilihan == "7":
            riwayat_transaksi()

        elif pilihan == "8":
            batalkan_transaksi()

        elif pilihan == "0":
            simpan_data()
            clear_screen()
            banner_premium("TERIMA KASIH")
            print("\nProgram selesai. Sampai jumpa kembali!")
            break

        else:
            print("Pilihan tidak valid!")


# MENJALANKAN PROGRAM
if __name__ == "__main__":
    main()
