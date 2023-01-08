# Mayin-Tarlasi-Py
Mayın tarlası oyununu aşağıdaki oyun kurallarını dikkate alarak Python programlama dilinde yazınız.
Oyun Kuralları:
-	Oyun alam (en az I OxIO) mxm boyutlarından oluşan bir kare matristir. Boyut isteğe göre değiştirilebilecektir.
-	Yerleştirilecek mayın sayısı oyun alanı büyüklüğünün %30'u olarak hesaplanacaktır. (Örneğin I Ox10 bir oyun alanmda 30 adet mayın bulunmalıdır.)
-	Mayınlar oyun alanına; oyun alanının dışına çıkmayacak ve üst üste konumlarda olmayacak şekillerde rastgele yerleşir.
-	Mayınlar oyun alanına yerleştirildikten sonra kullanıcıya oyun alanı 2 mod ile gösterilebilecektir (Her iki modun sunulması zorunludur).
1- Gizli mod: Kullanıcı mayınların nerde olduğunu bilmeyecektir.
2- Açık mod: Mayınların yerleri oyun alanında görünecektir.
-	Oyun alanında açılmayan kareler (hücreler) ? ile gösterilecektir. Yapılan seçim boş ise, ilgili alanın etrafını çevreleyen 8 (oyun alanının kenarında ise 5, köşesinde ise 3) karelik alanda kaç adet mayın bulunduğunun bilgisi
  gösterilecektir. Çevre alanlarda mayın bulunmaması halinde 0 ile gösterilecektir. Seçim yapılan alanda bir mayın bulunursa oyun alanındaki tüm mayınlar X ile gösterilecek ve oyun sona erecektir.
-	Yapılan her seçim içın oyun alanının görünümü güncellenecektir (Her atıştan sonra konsol temizlenebilir ve oyun alanının yeni hali ekrana yazdırılabilir).
-	Daha önce seçim yapılmış bir konum seçilirse kullanıcıya başka bir konum seçmesi için bilgi verilecektir,
-	Oyun iki şekilde sona erecektır. Kullanıcı mayın bulunan bir alanı işaretlerse "Maalesef kaybettiniz” mesajı verilerek oyun sonlandırılır, Oyun alanındaki mayın bulunmayan her bir karenin bulunması halinde de oyun biter ve kullanıcıya "Oyunu kazandınız” mesajı gösterilir. Her İki durumda kullanıcının puanı hesaplamr ve "Puanınız: 12” şeklinde mesaj verilir. Oyun puanı oyun sona erene kadar yapılan toplam hamle sayısı ile hesaplanır. Böylece oyunda mayına basmadan tamamlayan bir kişi oyun alan büyüklüğünün %70'i kadar puan almış olur.
-	Oyun bittikten sonra kullamcıya yeni oyun oynamak İçin veya çıkmak İçin tercih sunulur.
