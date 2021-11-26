# du2

VYSVĚTLENÍ FUNKČNOSTI PROGRAMU

NAČTENÍ DAT A ZÁKLADNÍ OPERACE
První částí programu je načtení vstupního souboru s daty ve formátu .csv. Následně je definový reader "dataInput", ale také 2 writery, které slouží pro pozdější zápis a tvorbu nových .csv souborů.

DEFINICE POMOCNÝCH PROMĚNNÝCH
V této části jsou definovány pomocné proměnné před průběhem následného FOR cyklu. Jedná se například o proměnnou rowNumber, která slouží pro určení čísla řádku v n-té iteraci FOR cyklu.

CYKLUS ČTOUCÍ ŘÁDKY VSTUPU
V první části jsou určeny a následně zapsány do proměnné řádky, které budou následně uvedeny ve výstupních souborech. Následuje zápis a úprava (přetypování na int či float) určitých hodnot v řádku a jejich zápis do proměnných. Dále se zde vyskytují vyjímky, ve kterých je především dosaženo výpočtu součtu hodnot pro týdenní, roční průměry a výpisu pátého řádku, kdy hodnoty musí být shopna přetypovat na float hodnotu. V případě, že se nebude jednat o desetinné číslo, nebude přičtena k součtu. Tuto část si můžeme představit, že k celkovému součtu se přičte nulová hodnota a s řádkem se v následujících částích nadále operuje.

ZÁPIS DO SOUBORU S ROČNÍMI HODNOTAMI
Tato část kódu je zaobalena do podmínky, kdy kód v ní se provede v případě, že současný rok se nerovná vypisovanému roku. Následně se provede výpočet průměru ze součtu hodnot a počtu dní. Vytvořený formátovaný text se zapíše pomocí writeru do nově vzniklého souboru s ročními hodnotami.

ZÁPIS DO SOUBORU SE SEDMIDENNÍMI HODNOTAMI
Tato část kódu je zaobalená do podmínky, kdy kód v ní se provede v případě, že zbytek podělení čísla řádku 7 se rovná 6. Nezbytnou součástí je zápis řádku do nového .csv souboru se sedmidenními hodnotami a ostatní náležitosti popsány v přechozí části.

PŘIDÁNÍ POSLEDNÍHO ŘÁDKU S ROČNÍM PRŮMĚREM
Provede se dodatečný výpočet posledního roku z hodnot zbylých proměnných z FOR cyklu. Zápis posledního řádku je syntaxně a funkčně shodný jako při zápisu ve FOR cyklu.

PŘÍDÁNÍ POSLEDNÍHO ŘÁDKU SE SEDMIDENNÍM PRŮMĚREM
Jedná se o obdobný postup zápisu posledního řádku jako v předchozím zmíněném. Na závěr bych dodal, že obě části dodatečného zápisu jsou provedeny při splnění podmínky (calculateYear == theYear) a (rowNumber % 7 != 6).

BONUS
VÝPOČET MAXIMA A MINIMA
Minimum a maximum souboru je provedeno ve FOR cyklu pomocí podmínky, která se provede v případě, že hodnota průměru je největší či nejmenší oproti minulým v předchozích řádcích. Následně se řádek zapíše do proměnné, ze kterého je po skončení celého cyklu vytvořen formátovaný řetězec a následně vytiskut do konzole. 