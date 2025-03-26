print('>>>>>>>>>> Welcome to Hisyam Toy Store <<<<<<<<<<')
print('Hello, Terima kasih sudah mengunjungi Hisyam Toy Store!')
print('Sedang mencari mainan apa, sobat..?')
print('=== Mobil, Pesawat, Perahu, Motor, Tank, Dll__')

barang = input('Masukkan mainan yang dicari: ')
print(f'Wahh, pilihanmu sungguh menarik untuk dibeli: {barang}!')
print('+____+')

while True:
    pilih = input(
        'Saya bisa membantu pilihkan apa saja jenis dan model yang ada di toko Hisyam Toy Store. '
        'BTW, apakah Anda mau saya bantu memberikan rekomendasi (iya/tidak): '
    ).lower()

    if pilih == 'iya':
        print('#### Waittttt!!!!! ####')
        print('Okay, barang yang bestseller di sini adalah mobil dan motor Hotwheels.')
        keren = input('Apakah kamu setuju dengan rekomendasi dari kami? (iya/tidak): ').lower()

        if keren == 'iya':
            print('Terima kasih telah setuju dengan rekomendasi kami!')
        else:
            print('Baik, lain waktu kami akan memberikan yang terbaik untuk kamu.')
        
        mood = input('Silahkan ketik "exit" jika ingin keluar dari beranda (exit - To Hisyam Toy Store): ').lower()
        if mood == 'exit':
            print("Terima kasih sudah mengunjungi Hisyam Toy Store!")
            break
        else:
            print("Baik, silahkan lanjutkan pencarian mainan Anda.")

    elif pilih == 'tidak':
        print('<<<------------------>>>')
        print("Baik, silahkan lanjutkan pencarian mainan Anda.")
        break

    else:
        print('<<<======================>>>')
        print('Maaf, saya tidak tahu barang apa yang anda butuhkan untuk saat ini.')
        pilih = input('Jadi, apakah kamu mau saya berikan pilihan yang terbaik? (iya/tidak): ').lower()

        if pilih == 'tidak':
            print("Baik, silahkan eksplorasi mainan yang anda inginkan. Terima kasih sudah berkunjung di Hisyam Toy Store!!!")
            break
