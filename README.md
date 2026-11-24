# Showroom Management System

Aplikasi berbasis terminal untuk mengelola data mobil, pelanggan, dan transaksi penjualan showroom. Program dibuat dengan Python dan menyimpan data dalam file JSON.

## Fitur

- **Manajemen mobil:** tambah, tampilkan, ubah, dan hapus data mobil.
- **Manajemen pelanggan:** tambah, tampilkan, ubah, dan hapus data pelanggan.
- **Pencarian dan pengurutan mobil.**
- **Transaksi penjualan** dengan diskon dan tiga status:
  - `Pending`: transaksi tercatat dan menunggu pembayaran. Mobil tidak ditawarkan untuk transaksi baru selama statusnya pending.
  - `Berhasil`: pembayaran dikonfirmasi dan mobil ditandai terjual.
  - `Dibatalkan`: transaksi pending dibatalkan dan mobil kembali tersedia.
- **Riwayat transaksi** dan **laporan statistik** showroom.
- ID baru melanjutkan nomor terbesar yang sudah digunakan. Contoh: jika ID yang ada `M001` dan `M003`, ID berikutnya `M004`.

Transaksi berstatus `Berhasil` tidak dapat dibatalkan. Fitur pembatalan hanya menampilkan transaksi yang masih `Pending`.

## Persyaratan

- Python 3
- Tidak memerlukan instalasi paket tambahan; program menggunakan modul bawaan Python.

## Menjalankan Program

Buka terminal pada folder proyek, lalu jalankan:

```bash
python3 showroom.py
```

Pilih menu dengan memasukkan nomor yang ditampilkan. Pada menu transaksi, tabel mobil tersedia akan muncul sebelum program meminta konfirmasi `Y/N`.

## Alur Pembelian

1. Pilih **Transaksi Penjualan**.
2. Pilih `Y` untuk melanjutkan setelah melihat daftar mobil yang tersedia.
3. Masukkan ID mobil dan ID pelanggan.
4. Masukkan diskon (0–100%) dan konfirmasi transaksi.
5. Transaksi tersimpan dengan status `Pending`.
6. Pilih **Konfirmasi Pembayaran Pending** untuk mengubah transaksi menjadi `Berhasil`, atau pilih **Pembatalan Transaksi** untuk mengubahnya menjadi `Dibatalkan`.

## Penyimpanan Data

Data disimpan dalam `showroom_data.json` di folder kerja saat program dijalankan. File ini berisi koleksi `mobil`, `pelanggan`, dan `transaksi`. Perubahan disimpan saat operasi selesai.
