#Kastali
=======

##Nú búum við allir saman til leik þar sem við hönnum hver eitt herbergi í kastalanum okkar

Það sem þið þurfið að gera er að búa til ykkar eigið herbergi í kastalanum. Kastalinn lítur svona út:

-------------
|11|12|13|14|
-------------
|21|22|23|24|
-------------
|31|32|33|34|
-------------
|41|42|43|44|
-------------
|51|in|út|54|
----     ----

Herbergin eru sem hér segir:
Eiður:			11
Guðmundur:		12
Ágúst:			13
Aron:			14
Hlynur Ægir:	21
Hlynur Almar:	22
Gabríel:		23
Stefán Ingi:	24
Breki:			31
Davíð:			32
Stefán Már:		33
Hinrik:			34
Gunnar:			41
Elmar:			42
Halldór:		43
Sigurþór:		44
Sigurpáll:		51
Alexander		54

##Reglurnar eru:

- skrárnar sem túlka herbergin eiga að vera inni í pythonHus möppunni
- Þið þurfið bara að búa til eina skrá inni í þeirri möppu sem á að heita roomxx.py þar sem xx er númerið á herberginu ykkar
- Hver svona skrá í python verkefni kallast module
- Hver skrá á að importa room module-ið (from . import room)
- Sá kóði sem þið skrifið fyrir neðan importið (utan allra falla og klasa) keyrist bara í fyrsta skipti sem leikmaðurinn kemur inn í herbergið
- Til þess að láta kóða keyrast í hvert skipti sem notandinn kemur inn í herbergið setjið þið hann í sérstakt fall sem heitir go (þið búið til fallið með því að skrifa 'def go():')
- Skoðið room.py module-ið. Þið getið nýtt ykkur það sem þar er með því að eintaka klasann
- þið verðið að nota go aðferðina í þeim klasa því að það er eina leiðin til þess að láta notandann fara út úr herberginu ykkar (Þetta var reyndar óheppilegt hjá mér að láta báðar aðferðirnar heita go...)
- Notið items breytuna til þess að láta notandann finna hluti
- Talið við aðra nemendur sem eru meða aðlyggjandi herbergi svo að sagan verið ekki kjánaleg
- Látið eitthvað undarlegt gerast eins og turtle eða tkinter fara af stað. Þið gætuð meiraðsegja látið poppa upp vefsíðu með django. Verið frumlegir!
- gangi ykkur vel!

##Mat á verkefninu:

* Þið þurfið að nota a.m.k. eitt utanaðkomandi library s.s. pygame, django etc...
* þið þurfið að búa til module sem virkar
* Þið þurfið að hafa a.m.k. einn hlut sem notandinn getur fundið inni í herberginu og nota a.m.k. einn hlut frá öðrum nemanda (úr öðru herbergi).
* Þið þurfið að skrifa eitthvað inn í info breytuna og hafa það þannig að notandinn geti sem oftast (helst alltaf) prentað hana út.
* Þegar þið eintakið room.grunnur þrufið þið að setja inn herbergisnúmerið ykkar eins og gert er í room52.py
* pull-ið verkefnið og forkið það
	* búið til auka module til þess að geta prufað ykkar module
	* Þegar allt virkar ættuð þið að geta merge-að og committað

Gangi ykkur vel!