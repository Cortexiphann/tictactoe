# Taş Kağıt Makas Oyunu

Bu Python programı, iki oyuncu arasında taş kağıt makas oyununu simüle eder.

## Nasıl Çalışır?

1. Oyun tahtası, 1'den 9'a kadar olan pozisyonları içeren bir sözlük olarak oluşturulur.
2. `display_board()` fonksiyonu, oyun tahtasını ekrana yazdırır.
3. `check_winner()` fonksiyonu, kazananı kontrol eder.
4. `check_tie()` fonksiyonu, oyunun berabere bitip bitmediğini kontrol eder.
5. `play_game()` fonksiyonu, oyunun ana döngüsünü yürütür.
6. Oyuncular sırayla hamle yapar ve tahtaya işaretlerini yerleştirirler.
7. Her hamleden sonra kazanan veya beraberlik durumu kontrol edilir.
8. Oyun sonlandığında, sonuç ekrana yazdırılır.

## Kullanım

Program çalıştırıldığında, sırayla taş, kağıt veya makas seçen iki oyuncuya hamle yapmaları istenir. Hamleler tahtada işaretlenir ve sonuç ekrana yazdırılır.
