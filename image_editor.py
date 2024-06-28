from PIL import Image, ImageEnhance, ImageFilter
import os

# Giriş ve çıkış dizinlerini belirle
path = "./imgs"
pathOut = "./editedimgs"

# Çıkış dizininin varlığını tespit eder,'exits_ok' ile hata yoksa devam etmesini sağlar.
os.makedirs(pathOut, exist_ok=True)

# Giriş dizinindeki dosyaları işleme
for filename in os.listdir(path):
        # Tam dosya yolunu oluştur
        file_path = os.path.join(path, filename)
        print(f"İşlenen dosya: {file_path}")

        # Resim dosyasını aç
        img = Image.open(file_path)

        # Keskinleştirme filtresi uygula
        edit = img.filter(ImageFilter.SHARPEN)
        factor = 2
        enchancer = ImageEnhance.Color(edit)
        edit = enchancer.enhance(factor)

        # Çıkış dosya yolunu oluştur
        clean_name = os.path.splitext(filename)[0]
        output_file_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")

        # Düzenlenen resmi kaydet
        edit.save(output_file_path)
        print(f"Düzenlenen dosya kaydedildi: {output_file_path}")

    
