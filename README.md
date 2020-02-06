# Biblioteczka

Projekt zautomatyzowanego systemu wyboru drewanianych klocków z regału.

Urządzenie zbudowano z wykorzystaniem elementów z drukarki 3D (stelaż, silniki krokowe).

Za pomocą chwytaka pobierane są trzy dowolnie rozmieszczone drewniane klocki na półkach regału i składowane do jednego wybranego okna w dolnym rzędzie tego regału. Dla tych trzech klocków wybierane jest takie okno w dolnym rzędzie regału, do którego trasa od tych obiektów jest najkrótsza.

Lista funkcji:

1. Sterowanie urządzeniem za pomocą graficznego interfejsu użytkownika:
    a) Wybór miejsc na graficznej klawiaturze, na którcyh umieszczone zostały klocki.
    b) Wprowadzenie przycisku START uruchamiającego urządzenie.
    c) Wyświetlanie informacji o wybranych pozycjach.

2. Pobieranie i odkładanie klocków za pomocą chwytaka zamontowanego wózku z napędu DVD-ROM.

3. Wprowadzenie algorytmu Dijkstry, dzięki któremu można odnaleźć najkrótszą ścieżkę od punktu startowego do celu.

4. Rozpoznawanie, czy dany obiekt znajduje się we właściwej kolumnie. Na klockach znajdują się kody QR, które rozpoznawane są przez kamerkę internetową umieszczoną nad chwytakiem.
