__Nama: Shamira Alifanindya Prasetya__

__NPM: 2106636376__

__Kelas: PBP-A__

## PBP TUGAS 6 ##
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Deskripsi Tugas
Mengimplementasikan AJAX pada aplikasi To Do List Tugas 4 dan 5.

## Jawaban
__Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.__
* _Asynchronous programming_ pada sebuah website memungkinkan user untuk tetap berinteraksi selagi server memproses data dan/atau _request_ dari user tersebut. Banyak proses yang dapat tetap berjalan tanpa harus menunggu salah satunya selesai.

* _Synchronous programming_ pada sebuah website mengharuskan user untuk menunggu server memproses data atau _request_ dari user tersebut agar bisa berinteraksi lagi dengan website. _Synchronous programming_ bersifat click, wait, dan refresh sehingga hanya satu proses yang dapat dieksekusi pada satu waktu.


__Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.__

_Event-Driven Programming_ merupakan paradigma pemrograman yang ditentukan dengan event. Event yang terjadi merupakan output dari tindakan yang dilakukan oleh user. Konsep _event-driven_ juga dapat dilihat sebagai interaksi antar objek yang mengirimkan pesan. Ketika user berinteraksi dengan halaman website lalu misalnya melakukan click pada tombol, event ini akan diterima sebagai suatu pesan. Pesan tersebut akan diteruskan ke kode JavaScript yang disebut event handler. Event handler akan memproses pesan tersebut dan memberikan respons berupa perubahan atau tampilan baru pada halaman website.

Penerapan paradigma _event-driven programming_ pada tugas ini adalah ketika user menekan tombol save pada halaman create task. Event tersebut dilakukan handle dengan AJAX untuk meneruskan data task baru ke server. Selanjutnya, pada halaman todolist akan muncul task baru yang telah dilakukan _update_ oleh AJAX.


__Jelaskan penerapan asynchronous programming pada AJAX.__

Setelah user memasukkan data baru, AJAX akan mengambil data tersebut lalu mengirimkannya dalam bentuk XML, JSON, ataupun teks kepada server. Lalu, AJAX akan memperbarui halaman website dengan data baru dari user. Proses ini terjadi di belakang layar atau secara asinkronus sehingga user tidak perlu melakukan _reload_ keseluruhan halaman website untuk melihat _update_ data.


__Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!__

1. Membuat function baru di views.py untuk me-_return_ data task baru dalam format JSON.
2. Menambahkan event handler berupa atribut on click.
3. ...


## Link Aplikasi Heroku
Akses To Do List pada tautan [ini.](https://pbp-tugas-2-shamira.herokuapp.com/todolist)