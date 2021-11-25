# du2

VYSVĚTLENÍ FUNKČNOSTI PROGRAMU

1. Příprava vstupu a výstupů
    1. První část načte csv soubor a zapíše do READERu
    2. Poté jsou definovány zápisové soubory writeWeek a writeYear
    3. Poté začíná FOR cyklus čtoucí všechny řádky postupně

2. Zápis týdenních průměrů 
    1. Existence podmínky, kdy se vybere řádek s pondělím (zbytek čísla řádku dělitelné sedmi) a celý řádek se přiřadí do nové proměnné
    2. Výpočet součtu hodnot v týdnu obalený výjimkou nesprávnosti hodnoty (float) a délkou řetězce v řádku
    3. Následně existence podmínky, kdy se vybere řádek s nedělí (zbytek čísla řádku dělitelné sedmi)
        1. Výpočet průměru ze součtu (součet / 7)
        2. Formátování hodnoty
        3. Zápis hodnot do proměnné vzniklé v rámci první podmínky
        4. Zápis do výstupního souboru a smazání hodnot průměru před novým opakováním cyklu
    4. Po skončení FOR cyklu dopsání posledního řádku
        1. Výpočet zbylého počtu řádku a zápis do souboru
        2. Vše obaleno v podmínce, že se poslední řádek nesmí rovnat 6 (neděle)

3. Zápis ročních průměru
    1. Existence podmínky, kdy se vybere první den roku (zbytek čísla řádku dělitelné sedmi) a celý řádek se přiřadí do nové proměnné
    2. Výpočet součtu hodnot v roce obalený stejnou výjimkou nesprávnosti hodnoty (float) a délkou řetězce v řádku jako v týdenním případě
    3. Následně existence podmínky, kdy se vybere řádek s prvním dnem v novém roce 
        1. Výpočet průměru ze součtu (součet/počet dní v roce)
        2. Formátování hodnoty
        3. Zápis hodnot do proměnné vzniklé v rámci první podmínky
        4. Zápis do výstupního souboru a smazání hodnot průměru, ale také dní v roce, před novým opakováním cyklu
        5. Součástí je také počet dní v posledním roce, který se prozatím nevypsal
    4. Po skončení FOR cyklu dopsání posledního řádku, což je obdobné jako v případě výpisu týdne



Bonusový úkol

1. Maximum a minimum
    1. inicializace pomocných proměnných
    2. zápis floatu průtoku v daném řádku (zapsáno ve vyjímce)
    3. podmínka, že pokud bude hodnotaprůtoku větší (menší) než u doposud největší hodnoty zapíše se do proměné
    4. po skončení cyklu výpis řádku s nejmenší a největší hodnotou