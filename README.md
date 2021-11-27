# du2

VYSVĚTLENÍ FUNKČNOSTI PROGRAMU

NAČTENÍ DAT A ZÁKLADNÍ OPERACE
První částí programu je načtení vstupního souboru s daty ve formátu CSV. Následně je definovaný reader "dataInput", ale také 2 writery, které slouží pro pozdější zápis a tvorbu nových CSV souborů.

DEFINICE POMOCNÝCH PROMĚNNÝCH
V této části jsou definovány pomocné proměnné před průběhem následného FOR cyklu. Jedná se například o proměnnou rowNumber, která slouží pro určení čísla řádku v n-té iteraci FOR cyklu.

CYKLUS ČTOUCÍ ŘÁDKY VSTUPU
V první části jsou určeny a následně zapsány do proměnné řádky, které se propíšou do souborů. Následuje zápis a úprava (přetypování na int či float) určitých hodnot v řádku. Dále se zde vyskytují vyjímky, ve kterých je především dosaženo výpočtu součtu hodnot pro týdenní, roční průměry a výpisu pátého sloupce, kdy hodnoty musí být shopna přetypovat na float hodnotu. V případě, že se nebude jednat o desetinné číslo, nebude přičtena k součtu. Tuto část si můžeme představit, že k celkovému součtu se přičte nulová hodnota a s řádkem se v následujících částích nadále operuje.

ZÁPIS DO SOUBORU S ROČNÍMI HODNOTAMI
Pokud je načten první řádek s jiným rokem, tak je spočítán průměr a následně zapsán do CSV souboru s ročním průměrem. Tomu předchází výpočet průměru ze součtu hodnot a počtu dní. 

ZÁPIS DO SOUBORU SE SEDMIDENNÍMI HODNOTAMI
Pokud je načten poslední den sedmidenního okna, tak je spočítán průměr a zapsán do CSV souboru se sedmidenním průměrem. 

VÝPOČET MAXIMA A MINIMA
Minimum a maximum souboru je provedeno ve FOR cyklu pomocí podmínky, která se provede v případě, že hodnota průměru je největší či nejmenší oproti minulým v předchozích řádcích. Následně se řádek zapíše do proměnné, ze kterého je po skončení celého cyklu vytvořen formátovaný řetězec a následně vytiskut do konzole. 

VÝPIS NEKORETNÍCH DAT
Pokud hodnota pátého sloupce je nula či menší, vytiskne se řádek do konzole.

PŘIDÁNÍ POSLEDNÍHO ŘÁDKU S ROČNÍM PRŮMĚREM
Provede se dodatečný výpočet posledního roku z hodnot zbylých proměnných z FOR cyklu. Zápis posledního řádku je syntaxně a funkčně shodný jako při zápisu ve FOR cyklu.

PŘÍDÁNÍ POSLEDNÍHO ŘÁDKU SE SEDMIDENNÍM PRŮMĚREM
Jedná se o obdobný postup zápisu posledního řádku jako v předchozím zmíněném. Na závěr bych dodal, že obě části dodatečného zápisu jsou provedeny při splnění podmínky (calculateYear == theYear) a (rowNumber % 7 != 6).