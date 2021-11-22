# du1

VYSVĚTLENÍ FUNKČNOSTI PROGRAMU

1. Funkce
    V programu se vyskytují 4 funkce, přičemž 2 z nich jso určeny pro vykreslení křížku a kolečka.
    Další 2 slouží pro načítání souřadnic pro jednotlivé křížky a kolečka uživatelem.
    účelem funkcí je zjednodušit kód a zkrátit jej na minimální délku, jelikož jsou jednotlivé funkce použity v samotném kódu několikrát.
    
    1. Vykreslení křížku (hashtag_function)
        Pro vykreslení křížku byl použit FOR cyklus, kdy počátek každé části je určen v jeho středu.
        Poté jsou vykresleny jednotlivé "výběžky středu".
        Funkci jsou předány 2 parametry (souřadnice X a Y).

    2. Vykreslení kolečka(circle_function)
        Pro výpočet je nezbytné se přesunot do horizontálního středu buňky, kdy počátek vykreslení kružnice započne v dolní části buňky.
        stejně jako v případě křížku se do středu buňky dostaneme pomocí funkce "setpos" z knihovny turtle.
        Funkci jsou předány 2 parametry (souřadnice X a Y).

    3. Určení požadované buňky pro zákres(coordinates_hor; coordinates_ver)
        Pro tento účel slouží 2 funkce, přičemž 1. z nich určuje vertikální souřadnici a 2. určuje horizontální souřadnici.
        Funkce načte hodnotu zadanou uživatelem.
        Funkce obsahují především while cyklus, který nedovolí uživateli pokračovat, pokud nezadá hodnoty buňky v platném rozsahu, který je především v rozsahu 0 - velikost (X Y) hracího pole (viz. dále).
        Pokud nezadá uživatel platné hodnoty, definované podmínky mu mohou napovědět.
        Pomocí returnu se navrátí hodnota.
    
2. Samotná část kódu
    1.  Vykreslení hracího pole
        Při spuštění programu bude uživatel dotázán na velikost hracího pole.
        Program se nedříve táže na horizontální osu a poté osu vertikální.
        Pokud uživatel zadá neplatné hodnoty, tedy hodnoty 1 (piškvorky nelze hrát v jednom řádku či sloupci) a menší, program neproběhne.
        Jelikož se může jednat o poměrně náročně časovou problematiku, je rychlost výkresu nastavena na největší (speed(0)).
        Samotný výkres probíhá pomocí 3 FOR cyklů, které jsou do sebe vnořené.
        První z vykreslí celkový počet buňek v řádku.
        Druhý vykreslí celkový počet řádků seřazeny pod sebou.
        Třetí slouží pro přesun k první buňce v horizontálním směru. Tato část vždy předchází výkresu nového řádku.

    2. Mezivýpočty
        V této části je proveden výpočet celkového množství buňek vynásobením velikosti stran hracího pole.
        Následně se provede dělení celkového počtu buňek, kdy se následně zjistí jeho zbytek. Ten určuje sudý či lichý počet tahů (viz. dále).
   
    3. Samotná hra
        Ve hře začíná vždy hráč 1, který hraje pomocí křížku.
        Sudý počet her je proveden pomocí bodu 3.1.
        Lichý počet her je proveden pomocí bodů 3.1. a 3.2.
       
        1. Sudý počet her
            Tato část je provedena pomocí For cyklu a můžeme ji dělit na dvě části.
            Část 1 je určena pro načítání křížku do zvolené buňky.
            Hráč Zvolí souřadnici X a Y, kdy jejich platnost se ověří bodem 1.3 (tedy načtou se 2 definované funkce pro určení buňky na horizontální a vertikální ose).
            Po správném načtení pokračuje hra výkresem křížku.
            Druhá část je funkčně totožná jako část 1, avšak na konci části skriptu je vykresleno kolečko, nikoliv křížek.

        2. Lichý počet her
            Jak již bylo sepsáno, nejdříve se provede část 1, kdy je odehráno maximální sudé množství tahů.
            Následně, pokud je tedy počet tahů lichý (popis v části 2.), provede se 1 tah hráče X, který je blíže definovaný v části 3.1.
        
    Pokud hra proběhne správně, hráči o tom budou náležitě obeznámeni a kliknutím na hrací plochu ukončí hru.
    Důležité je poznamenat, že program je navržen pouze pro zadávání celých čísel uživatelem