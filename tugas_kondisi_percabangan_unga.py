def tentukan_predikat(skor):
    if skor >= 90 and skor <= 100:
        return "A", "Dengan Pujian"
    elif skor >= 80:
        return "B", "Sangat Memuaskan"
    elif skor >= 70:
        return "C", "Memuaskan"
    elif skor >= 60:
        return "D", "Tidak Memuaskan"
    elif skor >= 0:
        return "E", "Tidak LULUS"
    else:
        return None, None

try:
    skor = float(input("Masukkan skor (0-100): "))
    
    if 0 <= skor <= 100:
        huruf, predikat = tentukan_predikat(skor)
        print(f"Nilai Huruf: {huruf}")
        print(f"Predikat: {predikat}")
    else:
        print("Skor harus antara 0 sampai 100!")

except ValueError:
    print("Input tidak valid! Harap masukkan angka.")
