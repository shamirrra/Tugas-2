__Nama : Shamira Alifanindya Prasetya
NPM  : 2106636376
Kelas: PBP-A__

## PBP TUGAS 2 ##
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Deskripsi Tugas
Mengimplementasikan konsep Model-View-Template pada Django serta beberapa hal yang sudah dipelajari selama tutorial lab 1.

## Jawaban
__Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.__
![](https://github.com/shamirrra/Tugas-2/blob/main/asset/Bagan%20Tugas%202%20Shamira.png)

__Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?__

Virtual environment adalah ruang virtual yang mengisolasi _project_ yang sedang dijalankan dari _dependencies_ utama. Virtual environment digunakan agar pada _project_ yang sedang dikembangkan tidak terjadi perbedaan dan perubahan versi _library_ atau _package_ meski telah melakukan update _library version_ pada _project_ lainnya. Setiap _project_ memiliki kebutuhannya masing-masing, virtual environment memungkinkan kita mengembangkan _project_ dengan _library version_ dan _dependencies_ yang berbeda-beda sesuai dengan kebutuhan _project_ tersebut. Virtual environment sangat berperan ketika melakukan pengembangan _project_ bersama tim. Setiap orang dapat memiliki versi Python dan sistem operasi yang berbeda-beda. Virtual environment memastikan _project_ dapat dikembangkan dengan versi _library_ dan _dependencies_ yang sama. Pengembangan web dengan Django tanpa virtual environment tetap dapat dilakukan, tetapi tidak akan efektif jika berada di dalam tim. Dengan kata lain, lebih cocok untuk _individual developer_, tetapi tetap harus memperhatikan kebutuhan _project_.

__Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.__
* Pertama, membuat function show_catalog pada views.py di folder katalog. Function ini mengambil data catalog items dari models. Function ini mengambil parameter request dan me-_return_ render(request, ‘katalog.html’, context) untuk nantinya akan di-render dan ditampilkan pada HTML.

* Selanjutnya, membuat _routing_ sebagai pemetaan function show_catalog pada views.py ke katalog.html agar data-data tersebut dapat ditampilkan pada browser. Pada urls.py di folder katalog, saya membuat variabel app_name berisi string katalog, lalu membuat variabel url_patterns berupa list yang berisi path dengan route ‘ ‘ dan memanggil function show_catalog (pada views.py di folder katalog). Setelah itu, saya melakukan konfigurasi pada folder project_django. Pada file settings.py, saya menambahkan ‘katalog’ pada variabel INSTALLED_APPS. Lalu, pada file urls.py, saya menambahkan path katalog dengan menuliskan path('katalog/', include('katalog.urls')) pada variabel url_patterns.

* Lalu, saya melakukan mapping dari data yang telah di-_render_ pada views.py agar dapat ditampilkan pada halaman HTML. Pada file katalog.html, saya menambahkan sintaks {{ name }} dan {{ student_id }}. Selanjutnya, saya memanggil data-data atribut spesifik dari objek Class CatalogItem.

* Terakhir, saya melakukan _deployment_ pada Heroku. Setelah log in akun, saya membuat aplikasi baru melalui _create new app_. Saya menggunakan nama aplikasi “pbp-tugas-2-shamira” untuk tugas ini. Setelah itu, saya menambahkan _key_ dan _value_ pada Config Vars. Dua _key_ serta _value_ baru tersebut adalah _key_ HEROKU_APP_NAME dengan _value_ nama aplikasi dan _key_ SECRET_KEY dengan _value_ berupa _secrets_. Lalu, saya membuat file dpl.yml serta menambahkan _directory_ menuju file tersebut pada Github. File dpl.yml berisi instruksi untuk mengeksekusi _deployment_ oleh _runner_ di GitHub Actions. Setelah itu, saya menghubungkan _repository_ pada Github dan melakukan _deploy_ dengan Deploy Branch.

## Link Aplikasi Heroku
Akses melalui ![link ini](https://pbp-tugas-2-shamira.herokuapp.com/katalog/)
