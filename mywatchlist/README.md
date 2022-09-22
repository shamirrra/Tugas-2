__Nama: Shamira Alifanindya Prasetya__

__NPM: 2106636376__

__Kelas: PBP-A__

## PBP TUGAS 3 ##
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Deskripsi Tugas
Mengimplementasikan konsep data delivery serta beberapa hal yang dipelajari selama tutorial lab 2.

## Jawaban
__Jelaskan perbedaan antara JSON, XML, dan HTML!__

JSON:
* Format text yang dituis dalam JavaScript
* Menyimpan data dalam format map, berpasangan key dengan value
* Data yang dapat dimasukkan hanya berupa string, angka, array Boolean, dan objek bertipe primitif
* Menggunakan memori yang kecil sehingga proses transfer data relatif cepat
* Tidak bisa memproses atau melakukan perhitungan data

XML:
* XML adalah bahasa markup (tidak memiliki logic/fungsionalitas seperti bahasa pemrograman)
* Menyimpan data sebagai tree structure (memiliki tag untuk mendefinisikan elemen)
* Data yang dapat dimasukkan beragam, termasuk tipe data yang kompleks seperti bagan, charts, dan data non-primitif lainnya
* XML berukuran besar dan membutuhkan memori yang besar sehingga proses transfer data relatif lebih lambat
* Yang di-highlight adalah bagaimana format tampilan dari data

HTML:
* HTML adalah bahasa markup (tidak memiliki logic/fungsionalitas seperti bahasa pemrograman)
* Yang di-highlight adalah struktur dan konteks dari data
* Tujuan utama HTML adalah untuk penyajian data



__Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?__

Seiring berkembangnya teknologi, data yang dikirimkan semakin beragam bentuk dan formatnya. Data delivery yang dilakukan dapat membuat penyajian datanya menjadi dinamis.



__Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!__
* Pertama, membuat aplikasi baru bernama mywatchlist dengan menjalankan perintah 'python manage.py startapp mywatchlist' pada CMD. Lalu, menambahkan aplikasi tersebut ke dalam INSTALLED_APPS pada settings.py di folder project_django.

* Selanjutnya, di dalam models.py pada folder aplikasi mywatchlist dibuat models dengan atribut: watched, title, rating, release_date, dan review. Lalu, melakukan migrate pada CMD.

* Setelah itu, membuat folder baru bernama fixture dan menambahkan file baru berformat json dengan nama 'initial_mywatchlist_data.json'. Lalu, menambahkan 10 data baru pada file json tersebut dan langsung melakukan load data di CMD.

* Pada views.py di aplikasi mywatchlist, membuat fungsi-fungsi untuk menampilkan data dalam format HTML, XML, dan JSON. Selanjutnya membuat folder baru bernama templates untuk menambahkan file HTML. Lalu, menambahkan routing menuju page HTML, XML, dan JSON pada views.py di aplikasi mywatchlist. Pada urls.py di folder project_django juga ditambahkan path menuju urls milik mywatchlist.


## Postman
Postman HTML
![](https://raw.githubusercontent.com/shamirrra/Tugas-2/main/asset/postman%20html.png)

Postman XML
![](https://raw.githubusercontent.com/shamirrra/Tugas-2/main/asset/postman%20xml.png)

Postman JSON
![](https://raw.githubusercontent.com/shamirrra/Tugas-2/main/asset/postman%20json.png)

## Link Aplikasi Heroku
Lihat HTML di [link ini.](https://pbp-tugas-2-shamira.herokuapp.com/mywatchlist/html)

Lihat XML di [link ini.](https://pbp-tugas-2-shamira.herokuapp.com/mywatchlist/xml)

Lihat JSON di [link ini.](https://pbp-tugas-2-shamira.herokuapp.com/mywatchlist/json)
