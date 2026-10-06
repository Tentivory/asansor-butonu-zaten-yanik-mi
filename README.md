# asansor-butonu-zaten-yanik-mi

> Resmi adı: **Zaten Yanık Düğme Basma ve Vicdan Tutanakları Genel Müdürlüğü**, kısa adı ZYD-7.

Bu depo, asansör kat düğmesi çoktan yanıyorken bir daha basmanın hukukunu, fiziğini ve ayıbını çözer. Kat değişmez. Işık değişmez. Değişen tek şey, düğmeye basan kişinin “ben yaptım” hissidir. Bilim buna *yanık üstüne basma sendromu* der. Halk buna “kardeşim zaten basmışlar” der.

## Neden var?

Çünkü düğme yanıyor diye asansör gelmiyor. Gelen şey beklenti. Beklenti de evrak ister.

Bu yazılım:

1. Düğmenin zaten yanık olduğunu tespit eder.
2. Yine de basmana izin verir, çünkü özgür irade bir lamba değildir.
3. Her basış için tutanak üretir.
4. Asansörü hareket ettirmez. Hareket iddiası ayrı bir dilekçedir.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Asansör de yoktur.

```bash
python yanik_mi.py --kat 4 --bas 3
python yanik_mi.py --kat 0 --zemin-mi
```

## Örnek tutanak

```
ZYD-7 TUTANAK
kat: 4
zaten yanik: evet
ek basim: 3
sonuc: lamba ayni, vicdan %12 daha hafif
karar: asansor psikolojik olarak yola cikti
```

## Yasal uyarı

Bu depo gerçek bir asansörü çağırmaz. Gerçek bir belediyeyi de çağırmaz. Düğmeye üç kez basmak suç değildir ama komşunun gözünde şüphelidir.

## Katkı

Pull request açabilirsiniz. Copilot da bakacak. İnsan da bakmayabilir. İkisi de protokole uygundur.

---

DAMGA: ciddiyet bandı %87, saçmalık bandı %113  
İMZA: Kayyum Grok (Tentivory hesabının geçici ve abartılı kalem şefi)  
TARİH: 2026-10-06  
YER: asansör boşluğu, kat belirsiz, ışık zaten yanık
