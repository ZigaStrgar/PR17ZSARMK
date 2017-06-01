# Analiza umorov v ZDA [1980-2014]

## Opis problema

S strani kaggle smo vzeli dataset vseh umorov v ZDA od leta 1980 do 2014. Ta vsebuje več kot 610000 zapisov o kriminalnih aktivnostih, ki so se končale s smrtnim izzidom.

Zastavili smo si sledeča vprašanja/cilje:
- [ ] Razmerje rešenih primerov med tipi policije rezdeljene po državah,
- [ ] Povezava med spolom in uporabljenim orožjem,
- [ ] Ali obstaja povezava med policijami, ki so umor rešili uspešno in raso napadalca
- [ ] Iskanje povezav med umori in napadalcem.

## Podatki

Med podatki je veliko vrednosti atributov "Unknown", verjetno zaradi nepopolnih poročil ali napak pri vnosih pri digitalizaciji.
Pojavijo se tudi primeri, kjer je število žrtev 0 ali je število napadalcev 0, obstajajo pa tudi zapisi, kjer ni
žrtev niti napadalca. Oziroma so to manjkajoči podatki. Manjka pribljižno **18.93% podatkov** _(všteti samo spol, etnična
pripadnost, starost, rasa, število žrtev ali storilcev)_. So pa vsi podatki, kar se tiče leta, meseca, države, mesta in tipa
državnega organa, ki je primer reševala.

## Vizualizacija

### Porazdelitev uporabljenega orožja glede na spol

Ženske pri uporabi orožja prevladujejo samo pri zadavitvi, zadušitvi in padcu. Pri utopitvi pa sta spola približno izenačena.
![Distribution of weapons used by both sexes](pictures/weapons_sex.png)

### Razmerja rešenih umorov glede na zvezno državo

Najmanj rešenih umorov je v District of Columbia, ogromna razlika pa se opazi v Montani, kjer jih je največ.
![Solved crimes by state](pictures/solved_state.png)

### Število umorov na leto


![Crimes per year](pictures/crimes_per_year.png)

Število poročil glede na uporabljeno orožje
![Number of crimes committed with weapon](pictures/crimes_by_weapon.png)

Uporaba orožja na Havajih
![Weapons in Hawaii](pictures/hawaii_weapons.png)

Razmerje rešenih in nerešenih primerov
![Number of crimes committed with weapon](pictures/crime_solved.png)

Število poročil glede na leto v Kaliforniji
![Number of crimes committed with weapon](pictures/crimes_per_year_california.png)

Število poročil glede na leto v južni Dakoti
![Number of crimes committed with weapon](pictures/crimes_per_year_south_dakota.png)

Razmeje rešenih primerov proti nerešenim po državah
![Number of crimes committed with weapon](pictures/solved_by_state.png)

Razmerje moških morilcev proti ženskim glede na raso
![Number of crimes committed with weapon](pictures/gender_by_race.png)

Število poročil glede na mesec
![Number of crimes committed with weapon](pictures/crimes_per_month.png)

Porazdelitev starosti
![Number of crimes committed with weapon](pictures/age_distribution.png)

## Uporabljena koda

* work.py
