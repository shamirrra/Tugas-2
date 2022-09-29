__Nama: Shamira Alifanindya Prasetya__

__NPM: 2106636376__

__Kelas: PBP-A__

## PBP TUGAS 4 ##
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Deskripsi Tugas
Mengimplementasikan elemen form , konsep autentikasi, dan beberapa hal yang dipelajari selama tutorial lab 3.

## Jawaban
__Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?__

Kegunaan syntax {% csrf_token %} pada elemen form adalah sebagai tindakan pengamanan web karena dapat menghindarkan web serta user dari serangan Cross-Site Request Forgery (CSRF). Jika tidak terdapat syntax {% csrf_token %} pada elemen form, request dari user tidak diizinkan untuk diproses dan akan terbaca sebagai threat CSRF oleh program.



__Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual__

Ya, bisa dengan menjadikan form sebagai object melalui input fields pada file HTML. Lalu, menggunakan method POST untuk melakukan triggering input yang dimasukkan user.



__Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.__

Ketika user melakukan submisi form lalu menekan button submit, save, atau sebagainya, browser akan melakukan generate HTTP request, method, dan arguments ke destinasi URL sesuai pada HTML page form-nya. Server akan menerima request tersebut lalu akan memproses data dengan memanggil fungsi pada views.py yang dipilih, kemudian akan melakukan redirect ke path yang telah ditentukan. Server akan men-generate HTML page dari path yang dipilih lalu browser akan menampilkan layout dan UI dari HTML page tersebut kepada user.



__Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!__
* Pertama, membuat aplikasi baru bernama todolist dengan menjalankan perintah 'python manage.py startapp todolist' pada CMD. Lalu, menambahkan aplikasi tersebut ke dalam INSTALLED_APPS pada settings.py di folder project_django.

* Selanjutnya, di dalam models.py pada folder aplikasi todolist dibuat models dengan fields: user, date, title, description, dan is_finished. Lalu, melakukan migrate pada CMD.

* Setelah itu, pada views.py membuat fungsi-fungsi yang dibutuhkan, diantaranya fungsi untuk register, login, logout, show_todolist, create_task, task_status, dan delete_task. Selanjutnya, membuat folder baru bernama templates pada aplikasi todolist untuk menampung HTML pages yang akan ditampilkan.

* Lalu, pada urls.py di folder todolist juga menambahkan variabel app_name, yang berisi nama aplikasi, dan variabel urlpatterns, yang berisi path untuk routing. Pada urls.py di folder project_django juga ditambahkan path menuju urls dan routings pada todolist.

* Terakhir, melakukan deployment ke Heroku dan membuat dua contoh user dengan masing-masing tiga task to do.



## Link Aplikasi Heroku
Akses To Do List di [link ini.](https://pbp-tugas-2-shamira.herokuapp.com/todolist)