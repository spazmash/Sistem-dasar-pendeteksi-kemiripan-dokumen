import re

def preprocess_text(nama_file):
    if(nama_file == ""):
        print("Nama file tidak boleh kosong.")
        return []
    with open(nama_file, 'r', encoding='utf-8') as file:
        teks = file.read()
    teks_bersih = re.sub(r'[^\w\s]', '', teks.lower()) # Menghapus tanda baca & mengubah ke huruf kecil
    kata_kata = teks_bersih.split() # Tokenisasi
    stopwords = set(["yang", "di", "ke", "dari", "itu", "dan", "adalah"]) # Daftar stopwords
    for i in range(len(kata_kata)):
        if kata_kata[i] in stopwords:
            kata_kata[i] = '' # Menghapus stopwords
    return kata_kata

def mu(kata, frekuensi):
    return frekuensi[kata] / max(frekuensi.values())

def pemetaan(kata_kata):
    frekuensi = {}
    for i in range(len(kata_kata)):
        kata = kata_kata[i]
        if kata != '':  # Pastikan kata tidak kosong
            if kata in frekuensi:
                frekuensi[kata] += 1
            else:
                frekuensi[kata] = 1
    kata_unik = set(kata_kata)  # Membuat set kata unik
    keanggotaan_dict = {}           
    for kata in kata_unik:
        if kata != '':  # Pastikan kata tidak kosong
            keanggotaan_dict[kata] = mu(kata, frekuensi)
    return keanggotaan_dict

def intersect(setA, setB):
    setD = {}
    for item in setA.keys():
        if item in setB.keys():
            setD[item] = min(setA[item], setB[item])
    return setD 

def union(setA, setB):
    setC = {}
    for item in setA.keys():
        if item in setB.keys():
            setC[item] = max(setA[item], setB[item])
        else:
            setC[item] = setA[item]
    for item in setB.keys():
        if item not in setA.keys():
            setC[item] = setB[item]
    return setC

def Jaccard_similarity(setA, setB):
    setD = intersect(setA, setB)
    setC = union(setA, setB)
    if len(setC) == 0:
        return 0.0
    sum_D = 0.0;
    sum_C = 0.0;
    for item in setD.keys():
        sum_D += setD[item]
    for item in setC.keys():
        sum_C += setC[item]
    print (f"Jumlah keanggotaan irisan (D): {sum_D}")
    print (f"Jumlah keanggotaan gabungan (C): {sum_C}")
    return sum_D / sum_C



def main():
    nama_file = input("Masukkan nama file A teks (misal: dokumen.txt): ")
    kata_kata = preprocess_text(nama_file)
    setA = pemetaan(kata_kata)
    nama_file = input("Masukkan nama file B teks (misal: dokumen2.txt): ")
    kata_kata = preprocess_text(nama_file)
    setB = pemetaan(kata_kata)

    sim = Jaccard_similarity(setA, setB)
    print(f"Similarity setA dan setB: {sim*100:.2f}%")
    if sim > 0.8:
        print("Teks memiliki kemiripan yang tinggi.")
    elif sim > 0.5:        
        print("Teks memiliki kemiripan yang cukup.")
    else:
        print("Teks memiliki kemiripan yang rendah.")
main()  