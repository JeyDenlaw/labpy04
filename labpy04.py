data = []

while True:
  nama = input("Nama: ")
  nim = int(input("NIM: "))
  nilai_tugas = int(input("Nilai Tugas: "))
  nilai_uts = int(input("Nilai UTS: "))
  nilai_uas = int(input("Nilai UAS: "))

  nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
  data.append([nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir])

  tambah_data = input("Tambah data (y/t)? ")
  if tambah_data == 't':
    break

print("\nDaftar Data:")
print("--------------------------------------------------")
print("| No | Nama     | NIM    | Tugas  | UTS  | UAS  | Akhir   |")
print("--------------------------------------------------")
for i, d in enumerate(data):
  print(f"| {i+1} | {d[0]:<8} | {d[1]:<6} | {d[2]:<6} | {d[3]:<4} | {d[4]:<4} | {d[5]:<7.2f} |")
print("--------------------------------------------------")