"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 26 Februari 2022
    Waktu: 06:58:07 WIB
    Magnitudo: 5.1
    Kedalaman: 18 km
    Lokasi: LS=4.92 BT=101.72
    Pusat Gempa: Pusat gempa berada di laut 77 km arah BaratLaut Enggano
    Dirasakan (Skala MMI): II-III Bengkulu
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '26 Februari 2022'
    hasil['waktu'] = '06:58:07 WIB'
    hasil['magnitudo'] = 5.1
    hasil['kedalaman'] = '18 km'
    hasil['lokasi'] = {'ls': 4.92, 'bt': 101.72}
    hasil['pusat'] = 'gempa berada di laut 77 km arah BaratLaut Enggano'
    hasil['dirasakan'] = 'II-III Bengkulu'

    return hasil


def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
