__Nama: Shamira Alifanindya Prasetya__

__NPM: 2106636376__

__Kelas: PBP-A__

## PBP TUGAS 4 ##
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Deskripsi Tugas
Mengimplementasikan elemen `<form>` , konsep autentikasi, dan beberapa hal yang dipelajari selama tutorial lab 3.

## Jawaban
__Apa kegunaan `{% csrf_token %}` pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?__

Kegunaan syntax `{% csrf_token %}` pada elemen form adalah sebagai tindakan pengamanan web karena dapat menghindarkan web serta user dari serangan Cross-Site Request Forgery (CSRF). Jika tidak terdapat syntax `{% csrf_token %}` pada elemen form, request dari user tidak diizinkan untuk diproses dan akan terbaca sebagai threat CSRF oleh program.
<br>

__Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual__

Ya, bisa dengan menjadikan form sebagai object melalui input fields pada file HTML. Lalu, menggunakan method POST untuk melakukan triggering input yang dimasukkan user.
<br>

__Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.__

Ketika user melakukan submisi form lalu menekan button submit, save, atau sebagainya, browser akan melakukan generate HTTP request, method, dan arguments ke destinasi URL sesuai pada HTML page form-nya. Server akan menerima request tersebut lalu akan memproses data dengan memanggil fungsi pada views.py yang dipilih, kemudian akan melakukan redirect ke path yang telah ditentukan. Server akan men-generate HTML page dari path yang dipilih lalu browser akan menampilkan layout dan UI dari HTML page tersebut kepada user.
<br>

__Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!__
* Pertama, membuat aplikasi baru bernama todolist dengan menjalankan perintah 'python manage.py startapp todolist' pada CMD. Lalu, menambahkan aplikasi tersebut ke dalam INSTALLED_APPS pada settings.py di folder project_django.

* Selanjutnya, di dalam models.py pada folder aplikasi todolist dibuat models dengan fields: user, date, title, description, dan is_finished. Lalu, melakukan migrate pada CMD.

* Setelah itu, pada views.py membuat fungsi-fungsi yang dibutuhkan, diantaranya fungsi untuk register, login, logout, show_todolist, create_task, task_status, dan delete_task. Selanjutnya, membuat folder baru bernama templates pada aplikasi todolist untuk menampung HTML pages yang akan ditampilkan.

* Lalu, pada urls.py di folder todolist juga menambahkan variabel app_name, yang berisi nama aplikasi, dan variabel urlpatterns, yang berisi path untuk routing. Pada urls.py di folder project_django juga ditambahkan path menuju urls dan routings pada todolist.

* Terakhir, melakukan deployment ke Heroku dan membuat dua contoh user dengan masing-masing tiga task to do.
<br>

## PBP TUGAS 5 ##
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Deskripsi Tugas
Mengimplementasikan HTML, CSS, pengaturan _static files_ pada Django, dan beberapa hal yang dipelajari selama tutorial lab 3.

## Jawaban
__Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?__

Pada Inline CSS, kode CSS ditulis langsung pada atribut elemen HTML pada _body section_-nya. Atribut _style_ hanya dapat diimplementasikan pada HTML tag tertentu. _Style_ ini kurang efisien karena setiap HTML tag harus memiliki _style_-nya masing-masing. Oleh karena itu, Inline CSS banyak digunakan dan bermanfaat ketika hanya untuk mengubah satu elemen saja pada tampilan HTML. Selain itu, proses request HTTP tidak terlalu panjang sehingga ketika _user_ tidak perlu terlalu lama melakukan _loading_ pada _website_.

Pada Internal CSS, kode CSS ditulis pada bagian `<head>`. Kita dapat menggunakan Class dan ID untuk mengacu pada kode CSS yang dimaksud. Namun, Class dan ID tersebut hanya akan aktif pada halaman yang ditambahkan sintaks tersebut sehingga Internal CSS kurang cocok untuk diimplementasikan jika menggunakan CSS pada beberapa _file_.

Pada External CSS, perlu dihubungkan dengan file .CSS external dan umumnya diletakkan setelah bagian `<head>`. Diantara ketiga _style_, External CSS adalah _style_ yang paling nyaman digunakan karena file CSS yang sama dapat diimplementasikan ke banyak halaman. Selain itu, struktur dari _file_ HTML menjadi lebih rapih dan kecepatan _loading webpage_-nya relatif lebih cepat. Kekurangan dari External CSS adalah kita tidak bisa melihat keseluruhan tampilan halaman hingga _file_ CSS selesai dipanggil.
<br>

__Jelaskan tag HTML5 yang kamu ketahui.__

1. `<body>`, mendefinisikan body dari halaman HTML.
2. `<head>`, memberikan keterangan tentang isi halaman HTML, seperti title, heading, dan lainnya.
3. `<h1>` hingga `<h6>`, mendefinisikan judul halaman HTML, `<h1>` adalah heading ukuran terbesar.
4. `<p>`, mendefinisikan paragraf pada halaman HTML.
5. `<style>`, mendefinisikan _style_ yang diterapkan pada elemen.
6. `<br>`, mendefinisikan _single line break_ pada halaman HTML.
<br>

__Jelaskan tipe-tipe CSS selector yang kamu ketahui.__

* Element Selector, _selector_ ini menggunakan tag HTML-nya langsung untuk mengubah properti elemennya. Contohnya adalah sebagai berikut.
```
h2 {
    text-align: center;
    font-size: 30px;
    color: red;
}
```

* ID Selector, _selector_ ini menggunakan ID pada tag HTML-nya. Penulisan ID selector diawali dengan tanda pagar (#) dan ID tersebut harus unik. Contohnya adalah sebagai berikut.
```
...
<body>
  <div id="header">
    <h2>To Do List</h2>
  </div>
  ...
</body>
```
Isi dari ID adalah sebagai berikut.
```
#header {
  background-color: #f0f0f0;
  padding: 20px 20px 20px 40px;
}
```

* Class Selector, _selector_ ini menggunakan atribut class pada elemen yang akan diubah tampilannya. Penulisan Class selector diawali dengan tanda titik (.). Elemen HTML dapat diimplementasikan menggunakan lebih dari satu class. Contohnya adalah sebagai berikut.
```
...
<p class="hometown"> I am from New York.</p>
...
```
Class hometown didefinisikan sebagai berikut.
```
p.hometown {
    background: yellow;
}
```
<br>

__Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!__



## Link Aplikasi Heroku
Akses To Do List di [link ini.](https://pbp-tugas-2-shamira.herokuapp.com/todolist)