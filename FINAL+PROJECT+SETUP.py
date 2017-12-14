
# coding: utf-8

# In[12]:


#Imports regex
import re


#Sets up files
def filesetup(text, filename):
    
    #REGEX FOOTNOTE/CITATION REMOVER
    #Removes footnotes/citations
    
    #Finds all footnotes/citations
    matches = re.findall(r"\[[0-9a-zA-Z]*\]", text)
    
    #Replaces all found footnotes/citations with empty strings (removes them)
    for i in matches:
        text = re.sub("\[" + i + "*\]", '', text)
    
    #FORMATTER/FILE CREATION
    #Formats raw data into usable form and makes it a file
    
    #Uses regex to convert newlines to spaces
    data = re.sub('\n', ' ', text)
    data = data.lower()
    
    #Splits data on period and following space and limits datalist to 50 lines
    datalist = data.split('. ')
    datalist = datalist[:50]
    if filename == "en" or filename == "bl" or filename == "an":
        datalist = ['0\t' + line + '.' for line in datalist]
    if filename == "de" or filename == "blinkenlights":
        datalist = ['1\t' + line + '.' for line in datalist]
    if filename == "af":
        datalist = ['2\t' + line + '.' for line in datalist]
    if filename == "nl":
        datalist = ['3\t' + line + '.' for line in datalist]
    #Creates a text of lines from datalist, joined with a newline
    datalines = "\n".join(datalist)
    
    #Creates the datafile
    datafile = open(filename + ".txt", "w", encoding='utf8')
    
    #Writes datalines to file and closes file
    datafile.write(datalines)
    datafile.close()
    


# In[33]:


#SETUP OF ACTUAL FILES

filesetup("""On October 15, 1966, the Historic Preservation Act created the National Register of Historic Places and the corresponding State Historic Preservation Offices (SHPO).[2] Initially, the National Register consisted of the National Historic Landmarks designated before the Register's creation, as well as any other historic sites in the National Park system.[3] Approval of the act, which was amended in 1980 and 1992, represented the first time the United States had a broad-based historic preservation policy.[2][4] The 1966 act required those agencies to work in conjunction with the SHPO and an independent federal agency, the Advisory Council on Historic Preservation (ACHP), to confront adverse effects of federal activities on historic preservation.[5]
To administer the newly created National Register of Historic Places, the National Park Service of the U.S. Department of the Interior, with director George B. Hartzog Jr., established an administrative division named the Office of Archeology and Historic Preservation (OAHP).[5][6] Hartzog charged OAHP with creating the National Register program mandated by the 1966 law. Ernest Connally was the Office's first director. Within OAHP new divisions were created to deal with the National Register.[7] The division administered several existing programs, including the Historic Sites Survey and the Historic American Buildings Survey, as well as the new National Register and Historic Preservation Fund.[5]
The first official Keeper of the Register was William J. Murtagh, an architectural historian.[3] During the Register's earliest years in the late 1960s and early 1970s, organization was lax and SHPOs were small, understaffed, and underfunded.[6] However, funds were still being supplied for the Historic Preservation Fund to provide matching grants-in-aid to listed property owners, first for house museums and institutional buildings, but later for commercial structures as well.[5]
A few years later in 1979, the NPS history programs affiliated with both the U.S. National Parks system and the National Register were categorized formally into two "Assistant Directorates." Established were the Assistant Directorate for Archeology and Historic Preservation and the Assistant Directorate for Park Historic Preservation.[7] From 1978 until 1981, the main agency for the National Register was the Heritage Conservation and Recreation Service (HCRS) of the United States Department of the Interior.[8]
In February 1983, the two assistant directorates were merged to promote efficiency and recognize the interdependency of their programs. Jerry L. Rogers was selected to direct this newly merged associate directorate. He was described as a skilled administrator, who was sensitive to the need for the NPS to work with SHPOs, academia, and local governments.[7]
Although not described in detail in the 1966 act, SHPOs eventually became integral to the process of listing properties on the National Register. The 1980 amendments of the 1966 law further defined the responsibilities of SHPOs concerning the National Register.[8] Several 1992 amendments of the NHPA added a category to the National Register, known as Traditional Cultural Properties: those properties associated with Native American or Hawaiian groups.[4]
The National Register of Historic Places has grown considerably from its legislative origins in 1966. In 1986, citizens and groups nominated 3,623 separate properties, sites, and districts for inclusion on the National Register, a total of 75,000 separate properties.[8] Of the more than one million properties on the National Register, 80,000 are listed individually. Others are listed as contributing members within historic districts.[5][9]
Properties are not protected in any strict sense by the Federal listing. States and local zoning bodies may or may not choose to protect listed historic places. Indirect protection is possible, by state and local regulations on development of National Register properties, and by tax incentives.[10]
Until 1976, federal tax incentives were virtually non-existent for buildings on the National Register. Before 1976 the federal tax code favored new construction rather than the reuse of existing, sometimes historical, structures.[5] In 1976, the tax code was altered to provide tax incentives that promote preservation of income-producing historic properties. The National Park Service was given the responsibility to ensure that only rehabilitations that preserved the historic character of a building would qualify for federal tax incentives. A qualifying rehabilitation is one that the NPS deems consistent with the Secretary of the Interior's Standards for Rehabilitation.[11] Properties and sites listed in the Register, as well as those located in and contributing to the period of significance of National Register Historic Districts, became eligible for the federal tax benefits.[5]
Owners of income-producing properties listed individually in the National Register of Historic Places or of properties that are contributing resources within a National Register Historic District may be eligible for a 20% investment tax credit for the rehabilitation of the historic structure. The rehabilitation may be of a commercial, industrial, or residential property, for rentals.[12] The tax incentives program is operated by the Federal Historic Preservation Tax Incentives program, which is managed jointly by the National Park Service, individual State Historic Preservation Offices, and the Internal Revenue Service.[13] Aside from the 20% tax credit, the tax incentive program offers a 10% tax credit for rehabilitation to owners of non-historic, non-residential buildings constructed before 1936.[14]
Some property owners may qualify for grants as well, for instance the Save America's Treasures grants, which apply specifically to properties entered in the Register with national significance or designated as National Historic Landmarks.[15] The Save America's Treasures office has closed. The United States Congress did not renew the funding for the program for fiscal years 2011 and 2012, and does not plan to re-establish funding.[16]
The NHPA did not distinguish between properties listed in the National Register of Historic Places and those designated as National Historic Landmarks concerning qualification for tax incentives or grants. This was deliberate, as the authors of the act had learned from experience that distinguishing between categories of significance for such incentives caused the lowest category to become expendable.[3] Essentially, this made the Landmarks a kind of

Old Slater Mill, a historic district in Pawtucket, Rhode Island, was the first property listed in the National Register on November 13, 1966.[17]

The Loren Andrus Octagon House in Washington, Michigan has been on the NRHP since September 3, 1971.

Chichester Friends Meetinghouse near Boothwyn, in Upper Chichester Township, Delaware County, Pennsylvania, built in 1688 and then rebuilt in 1769 after a fire, was one of the earliest areas settled by Quakers in Pennsylvania – added to the National Register of Historic Places in 1973.[17]

Log Cabin within Green Valley Historic District, built ca. 1795 and is located in parts of East Marlborough Township and Newlin Township, Pennsylvania – added to the National Register of Historic Places in 1985.[17]

From 1802 to 1921 outside Wilmington, Eleutherian Mills was a gunpowder mill site used for the manufacture of explosives by the Du Pont family business – declared a National Historic Landmark in 1966.[18]

Built in 1800 by Samuel McIntire in Salem, the Stephen Phillips House is operated as a historic house museum by Historic New England and open for public tours.

Hamilton Hall, Salem – added to the National Register of Historic Places in 1972& built in 1805, also by McIntire
"honor roll" of the most significant properties of the National Register of Historic Places.[3]""", "en")



filesetup("""Eine frühe dokumentierte Form eines organisierten wissenschaftsähnlichen Lehrbetriebs findet sich im antiken Griechenland mit der Platonischen Akademie, die (mit Unterbrechungen) bis in die Spätantike Bestand hatte. Wissenschaft der Neuzeit findet traditionell an Universitäten statt, inzwischen auch an anderen Hochschulen, die auf diese Idee zurückgehen. Daneben sind Wissen schaffende Personen (Wissenschaftler) auch an Akademien, Ämtern, privat finanzierten Forschungsinstituten, bei Beratungsfirmen und in der Wirtschaft tätig. In Deutschland ist eine bedeutende öffentliche „Förderorganisation“ die Deutsche Forschungsgemeinschaft, die projektbezogene Forschung an Universitäten und außeruniversitären Einrichtungen fördert. Daneben existieren „Forschungsträgerorganisationen“ wie etwa die Fraunhofer-Gesellschaft, die Helmholtz-Gemeinschaft Deutscher Forschungszentren, die Max-Planck-Gesellschaft und die Leibniz-Gemeinschaft, die – von Bund und Ländern finanziert – eigene Forschungsinstitute betreiben. In Österreich entsprechen der DFG der Fonds zur Förderung der wissenschaftlichen Forschung (FWF) sowie die Österreichische Forschungsförderungsgesellschaft (FFG), in der Schweiz und Frankreich die nationalen Forschungsfonds. Andere Fonds werden z. B. von Großindustrien oder dem Europäischen Patentamt dotiert.
Neben den wissenschaftlichen Veröffentlichungen erfolgt der Austausch mit anderen Forschern durch Fachkonferenzen, bei Kongressen der internationalen Dachverbände und scientific Unions (z. B. IUGG, COSPAR, IUPsyS, ISWA, SSRN) oder der UNO-Organisation. Auch Einladungen zu Seminaren, Institutsbesuchen, Arbeitsgruppen oder Gastprofessuren spielen eine Rolle. Von großer Bedeutung sind auch Auslandsaufenthalte und internationale Forschungsprojekte.
Für die interdisziplinäre Forschung wurden in den letzten Jahrzehnten eine Reihe von Instituten geschaffen, in denen industrielle und universitäre Forschung zusammenwirken (Wissenschaftstransfer). Zum Teil verfügen Unternehmen aber auch über eigene Forschungseinrichtungen, in denen Grundlagenforschung betrieben wird.
Die eigentliche Teilnahme am Wissenschaftsbetrieb ist grundsätzlich nicht an Voraussetzungen oder Bedingungen geknüpft: Die wissenschaftliche Betätigung außerhalb des akademischen oder industriellen Wissenschaftsbetriebs steht jedermann offen und ist auch gesetzlich von der Forschungsfreiheit abgedeckt. Universitäten bieten außerdem die voraussetzungslose Teilnahme am Lehrbetrieb als Gasthörer an. Wesentliche wissenschaftliche Leistungen außerhalb eines beruflichen Rahmens sind jedoch die absolute Ausnahme geblieben. Die staatlich bezahlte berufliche Tätigkeit als Wissenschaftler ist meist an die Voraussetzung des Abschlusses eines Studiums gebunden, für das wiederum die Hochschulreife notwendig ist. Leitende öffentlich finanzierte Positionen in der Forschung und die Beantragung von öffentlichen Forschungsgeldern erfordern die Promotion, die Professur die Habilitation. In den USA findet sich statt der Habilitation das Tenure-Track-System, das 2002 in Form der Juniorprofessur auch in Deutschland eingeführt werden sollte, wobei allerdings kritisiert wird, dass ein regelrechter Tenure Track, bei dem den Nachwuchswissenschaftlern für den Fall entsprechender Leistungen eine Dauerstelle garantiert wird, in Deutschland nach wie vor eine Ausnahme darstellt.
Dementsprechend stellt die Wissenschaft durchaus einen gewissen Konjunkturen unterliegenden Arbeitsmarkt dar, bei dem insbesondere der Nachwuchs angesichts der geringen Zahl an Dauerstellen ein hohes Risiko eingeht. Besonders die gestiegene Beteiligung von Frauen an Promotion und Habilitation sowie die mit den neueren hochschulpolitischen Entwicklungen einhergehende Fokussierung und somit Beschneidung der thematischen Breite von Lehre und Forschung führt auf diesem zu einem erhöhten Konkurrenzdruck.[8]
Für die Wissenschaftspolitik an Bedeutung gewonnen hat die Wissenschaftsforschung, die wissenschaftliche Praxis mit empirischen Methoden zu untersuchen und zu beschreiben versucht. Dabei kommen unter anderem Methoden der Scientometrie zum Einsatz. Die Ergebnisse der Wissenschaftsforschung haben im Rahmen der Evaluation Einfluss auf Entscheidungen.
Gesellschaftliche Fragen innerhalb des Wissenschaftsbetriebs sowie die gesellschaftlichen Zusammenhänge und Beziehungen zwischen Wissenschaft, Politik und übriger Gesellschaft untersucht die Wissenssoziologie.
Der Buddhismus nimmt die im indischen Raum vorherrschende Glaubensvorstellung der Wiedergeburt auf und sieht somit sein schlussendliches Ziel nicht im Erreichen einer göttlichen Welt oder eines Paradieses, in welches das Individuum nach dem Tod eintreten könnte. Der Grund dafür ist, dass jegliche bedingte Daseinsform, so genussvoll sie auch sein mag, als letzten Endes vergänglich betrachtet wird und somit keine absolute Erfüllung schenken kann. Vielmehr wird eine Loslösung aus dem Kreislauf des bedingten Entstehens (pratityasamutpada) von Geburt und Tod angestrebt. Diese Befreiung ist das Nirvāna, das als Ende allen Leids beschrieben wird.
Die direkte Ursache der Wiedergeburt im Daseinskreislauf (Saṃsāra) ist ein von Begierde, von Durst getriebener Geist. Die Grundlage für das Entstehen von Begierde ist Unwissenheit: das Nicht-Wissen um die tatsächliche Beschaffenheit der Welt, bzw. der Gegebenheiten (Pali: dhammas). Solange diese „Befleckungen“ den Geist konditionieren, erfolgt daraus eine letztlich von Leid, bzw. der Unmöglichkeit, letztendliche Erfüllung zu finden (Pali: dukkha), gekennzeichnete Wiedergeburt. Zum Unterschied zu anderen im indischen Subkontinent verbreiteten Vorstellungen, verzichtet der Buddhismus allerdings auf metaphysische Spekulationen bezüglich einer wie auch immer gearteten Seele oder einer dem Menschen (bzw. den Lebewesen im Allgemeinen) innewohnenden nicht-materiellen Substanz, die von Wiedergeburt zu Wiedergeburt fortdauern würde, um schließlich Erlösung zu erlangen. In den frühen Schriften des Pali-Kanon vermeidet der Buddha das Formulieren derartiger Philosophien mit der Begründung, sie würden seine Zuhörer bloß in ein Netz von Gedankenkonstrukten verwickeln, was für die Befreiung nicht zuträglich sei. Weder das Anhaften an die Idee eines Selbst, noch das geistige Greifen nach der Vorstellung eines Nicht-Selbst könne dem Menschen den ersehnten Frieden schenken. Es gilt, sich von Gedankenkonstrukten über die Beschaffenheit der Welt zu lösen, um die Dinge so zu sehen, wie sie sind: vergänglich (anicca), nicht das Selbst (anatta) und letztlich nicht erfüllend (bzw. leidhaft – dukkha). Was das „Selbst“ nicht ist, erläutert der Buddha aber unermüdlich, um falsche Vorstellungen diesbezüglich aufzulösen, nämlich alle empirisch erfassbaren Gegebenheiten und Phänomene, inklusive der die menschliche Erfahrung konstituierenden Aggregate (Sanskrit: skandha, Pali: khandha).
Das für den Buddhismus charakteristische Modell des Nicht-Selbst (Sanskrit: anatman; Pali: anatta) in Verbindung mit der Wiedergeburt wird in einem bekannten Lehrgespräch zwischen dem Mönch Nagasena und dem hellenistischen König Menandros anschaulich dargestellt (siehe Milindapañha). Auf die Frage hin, ob ein Wiedergeborener derselbe oder ein anderer sei als der Verstorbene, heißt es: „Weder derselbe noch ein anderer.“ Vielmehr, so Nagasena, verhält es sich bei der Wiedergeburt wie mit dem Licht einer Öllampe, das eine Nacht lang brennt. Man könne weder behaupten, die Flamme am Morgen sei identisch mit der des Vorabends, noch sie wäre eine völlig andere. Es ließe sich lediglich feststellen, dass die am Morgen abhängig von der des Vorabends sei. Das heißt, bedingt durch diese Flamme (bzw. diesen Menschen) kommt die nächste zum Erscheinen (bzw. die Wiedergeburt). Ein Bewusstseins-Moment bedingt den nächsten, ohne dass es in diesem Prozess eine unwandelbare, fortdauernde Substanz geben müsste. Und dies gilt auch für die Wiedergeburt: der letzte Bewusstseins-Moment eines Lebens bedingt den ersten Moment des nächsten.
Im Allgemeinen kennen alle buddhistischen Traditionen die drei-schichtige Welt, die in sechs Daseinsbereiche untergliedert wird, in denen Wesen geboren werden. Die erste dieser drei Schichten wird vor allem durch Begierde gekennzeichnet (kāmadhātu) und beinhaltet die Welten der Höllenwesen, der hungrigen Geister (preta), der Tiere, der Menschen, der Asura-Wesen und einen Teil der Götterwelten. Eine Wiedergeburt in diesen Welten ist bedingt durch einen von Begierde, Zorn und Verblendung konditionierten Geisteszustand. Die zweite Schicht „beherbergt“ Götterwesen, deren Dasein zwar keine Verlangen auftreten lässt, die aber durch eine manifeste Form gekennzeichnet sind (rūpadhātu). In der dritten Schicht, dem Formlosen (arūpadhātu), befinden sich Götterwesen, deren Dasein besonders subtil und somit nicht durch manifeste Formen gekennzeichnet ist. Eine Geburt in die letzten zwei „Schichten“ ist bedingt durch einen Geist, der durch stabile Konzentration und bestimmte Formen der Meditation zwar frei von grobem Verlangen ist, die endgültige Befreiung allerdings nicht erlangen konnte. Da diese Zustände bedingt und somit vergänglich sind, sind sie aus buddhistischer Sicht letztlich nicht erstrebenswert.
Der Mahāyāna-Buddhismus kennt eine Vielzahl an Buddha Gestalten oder Formen, denen jeweils bestimmte Bereiche (siehe Reines Land) zugeordnet sind. Unter ihnen ist besonders der „Bereich der Freude“ von Buddha Amitabha erwähnenswert, da auch gewöhnliche, nicht-erleuchtete Wesen dorthin gelangen können. Voraussetzung dafür ist ein unerschütterlicher Glaube und die geistige Ausrichtung auf diesen Buddha im Augenblick des Todes. Aber auch dieser Bereich ist kein Endziel an sich, wird jedoch sehr wohl als perfektes Umfeld für das schnelle Erlangen der Erleuchtung angesehen. Manche Schulen des Buddhismus richten ihre religiösen Praktiken ausschließlich auf Buddha Amitabha und sein Reines Land aus.""", "de")



filesetup("""De Aarde (soms de wereld of Terra genoemd) is vanaf de Zon gerekend de derde planeet van ons zonnestelsel. Hierin behoort ze tot de naar haar genoemde "aardse planeten", waarvan ze zowel qua massa als qua volume de grootste is. Op de Aarde komt leven voor: ze is de woonplaats van miljoenen soorten organismen.[1] Of ze daarin alleen staat is onduidelijk, maar in de rest van het heelal zijn tot nog toe nergens sporen van leven, nu of in het verleden, gevonden. Radiometrische dateringen hebben uitgewezen dat de Aarde 4,57 miljard jaar geleden is ontstaan[2] en het leven maximaal 1 miljard jaar daarna.[3] Sinds het ontstaan van leven op Aarde heeft de biosfeer (het leven) de aardatmosfeer zuurstofrijk gemaakt, zodat aerobe organismen er kunnen overleven, en de ozonlaag kon ontstaan. Die beschermt het aardoppervlak tegen schadelijke ultravioletstraling, zodat leven op het land mogelijk is.[4]
Het aardoppervlak is voor 71% bedekt met water in de vorm van zeeën en oceanen, de rest bestaat uit continenten en eilanden. Water is noodzakelijk voor het overleven van alle bekende levensvormen.
De lithosfeer, de buitenste laag van de vaste Aarde, is verdeeld in een aantal rigide platen of schollen, die op een geologische tijdschaal (over miljoenen jaren) langzaam over het aardoppervlak bewegen. Deze beweging veroorzaakt de vorming van gebergten en vulkanisme. Onder de lithosfeer bevindt zich de langzaam convecterende aardmantel. De stroming in de mantel veroorzaakt de bewegingen van de platen en vulkanisme aan het aardoppervlak. Onder de mantel bevinden zich een vloeibare buitenkern (waarin het aardmagnetisch veld wordt opgewekt) en een vaste binnenkern. Dit magnetisch veld beschermt het leven tegen de zonnewind en kosmische straling.
De Aarde draait om de Zon in dezelfde tijd dat ze 366,26 maal om haar eigen as draait. Deze tijdsduur wordt een siderisch jaar genoemd. Omdat de rotatie van de Aarde om haar as en de baan van de Aarde om de Zon dezelfde richting volgen (vanaf de noordpool gezien tegen de wijzers van de klok in) is de lengte van het jaar in zonnedagen gemeten precies één dag korter, namelijk 365,26 dagen.
De aardas staat in een hoek van 23,439281° met een lijn die loodrecht staat op het vlak waarin de aardbaan ligt, wat de seizoenen veroorzaakt. De Aarde heeft één natuurlijke satelliet, de Maan, die vlak na de vorming van de Aarde moet zijn ontstaan. De zwaartekracht van de Maan veroorzaakt getijden in de oceanen, stabiliseert de hellingshoek van de aardas en doet de rotatiesnelheid van de planeet langzaam afnemen.
De Nationale Bank van België werd opgericht in 1850. Ze was aanvankelijk gevestigd in een gehuurd herenhuis aan de Warmoesberg. Later kocht men een gebouw op de hoek van de Nieuwe Koningsstraat en de Abrikozenstraat. Daarnaast opende de bank ook (24) afdelingen in belangrijke steden in heel België.
Toen de hoofdzetel te klein werd, kocht de Nationale Bank enkele gebouwen aan de Brusselse de Berlaimontstraat en de aanpalende Wildewoudstraat. Die werden gesloopt en onder leiding van Hendrik Beyaert en Wynand Janssens werd een nieuw kantoor gebouwd dat opgeleverd werd in 1865. In 1971 werd een eerste keer uitgebreid. Omstreeks 1900 kreeg het Beyaertgebouw een nieuwe vleugel.
Eind jaren 1930 maakte Georges Janssen als gouverneur nieuwe bouwplannen en architect Marcel Van Goethem realiseerde een volledig nieuw gebouw.
De oude gebouwen van de Bank Union du Credit aan de Brusselse Warmoesberg, ontworpen in 1872 door Désiré De Keyser, werden in 1979 aangekocht. Het gebouw werd in 1984 beschermd en na restauratie in 2010 werd de wetenschappelijke bibliotheek van de NBB erin ondergebracht tot 2016. Vanaf 2018 zou deze site, enkele straten van het hoofdgebouw verwijderd ingezet worden als permanente tentoonstellingsruimte en museum van de Nationale Bank.

Biljet Amerikaanse dollar
Het komt vrij vaak voor dat monetaire autoriteiten een bepaalde bandbreedte rondom een referentiekoers nastreven. Die bandbreedte kan variëren van 15 procent tot minder dan 1 procent. Een nauwe koppeling werd (vóór de invoering van de euro) door De Nederlandsche Bank nagestreefd tussen de gulden en de D-Mark. Een aantal in 2004 tot de Europese Unie toegetreden lidstaten hanteert een dergelijke koppeling tussen hun valuta en de euro.
Grote schommelingen in wisselkoersen worden in het algemeen nadelig gevonden, omdat ze de internationale handel bemoeilijken (en volgens sommige lezingen uitnodigen tot speculatie). Bij internationale handelstransacties zullen de daarbij betrokken partijen zich moeten afvragen of ze het risico van valutastijgingen of -dalingen moeten afdekken met termijncontracten. Dit kan extra kosten met zich meebrengen.
Monetaire autoriteiten zullen ernaar streven om, ook als er geen formele koppeling of bandbreedte wordt gehanteerd, fluctuaties beheersbaar te houden, maar door de omvang van de internationale valutamarkten is dit vaak nauwelijks haalbaar. Een centrale bank kan (soms in samenwerking met andere centrale banken) een ongewenste stijging of daling van de koers van een valuta trachten af te remmen door op de markt die valuta te verkopen of te kopen (dit staat bekend als interventie) maar hiermee zijn dusdanig grote bedragen gemoeid dat het effect vaak zeer gering is. Het "verbaal sturen" van markten lijkt vaak meer vruchten af te werpen.
De indruk bestaat dat er sprake is van een spanning tussen de economische en de psychologische aspecten van een valutakoers: een "sterke valuta" is uit psychologisch (en politiek) oogpunt nastrevenswaardig, maar een exporteur zal het onwenselijk vinden als zijn producten als gevolg van een hoge valutakoers voor buitenlandse afnemers te duur zijn. (Hierbij wordt aangetekend dat het vermoedelijk onmogelijk is om een objectief "correcte" valutakoers vast te stellen. Of een koers hoog of laag is, lijkt vaak ten dele door emoties bepaald te worden. Zie tevens het artikel wisselkoers
Het Graafschap Vlaanderen (Frans: Comté de Flandre of Comté de Flandres) is een historisch gebied dat aanvankelijk deel uitmaakte van West-Francië en vanaf 1464 van de (zuidelijke) Nederlanden. Het graafschap bestond van 862 tot 1795.
Vlaanderen behoorde door het Verdrag van Verdun (843) als enig gewest van de latere Nederlanden tot West-Francië. Al vanaf het einde van de negende eeuw voer het graafschap een onafhankelijke koers tegenover zijn leenheer, de Franse koning. Dit resulteerde in verschillende conflicten. Naast Kroon-Vlaanderen was er echter ook Rijks-Vlaanderen, deel rond Aalst en Zeeland, deel van het Heilige Roomse Rijk in leen van de Duitse keizer. Ten noorden van de Alpen was het graafschap Vlaanderen eeuwenlang een van de meest economisch- en cultureel ontwikkelde gebieden van Europa. Een hoog percentage van de inwoners leefde reeds in steden. Lange tijd konden Brugge en Gent zich qua omvang met Londen en Parijs meten.
Het graafschap Vlaanderen was een tweetalig graafschap.[1][2] Het zuiden rond Rijsel was Romaans (Frans-Vlaanderen), het noorden en de kuststreek sprak Oud-Nederlands.
In de 15e eeuw werd gestart met de eenmaking van de Nederlanden. Vanaf het einde van de veertiende eeuw maakte Vlaanderen deel uit van het Bourgondische Rijk, dat na de dood van Maria van Bourgondië in 1482 aan de Habsburgers toeviel. Na een oorlog tussen Frankrijk en Duitsland onder Keizer Karel V kwam Kroon-Vlaanderen formeel los van Franse kroon (Vrede van Madrid in 1525). De Pragmatieke Sanctie in 1549 vervolmaakte het eenmakingsproces van de (zuidelijke) Nederlanden.
Als gevolg van de Tachtigjarige Oorlog trad een eerst langzaam, maar steeds dieper verval in. Niet alleen was er grote schade aangericht, maar ook emigreerde een groot deel van de protestantse elite naar Holland en Zeeland. Vervolgens kreeg Vlaanderen ook zwaar te lijden onder de Devolutieoorlog en de Spaanse Successieoorlog. Hierdoor ging veel Vlaams gebied definitief verloren aan Frankrijk. Aan het einde van deze periode was er niets meer over van de vooraanstaande positie die Vlaanderen gedurende eeuwen in Europa had gespeeld.
Het graafschap Vlaanderen is het enige deel van het middeleeuwse Frankrijk dat vandaag geen deel meer uitmaakt van het hedendaagse Frankrijk (met uitzondering van Frans-Vlaanderen). Kleinere delen van het oude Vlaanderen maken nu deel uit van het Waals Gewest en de Nederlandse provincie Zeeland. Het overige deel van het graafschap vormt nu ongeveer 40% van het hedendaagse Vlaams Gewest.""", "nl")



filesetup("""Filosofiese vrae is oorweeg deur mense van baie tye, volkere en kulture. Die term "filosofie" in 'n Europese of Amerikaanse akademiese konteks verwys oor die algemeen na die tradisies van die westerse beskawing en word gevolglik "westerse filosofie" genoem. In die weste word die term "oosterse filosofie" meestal gebruik as omvattende term om te verwys na die filosofiese tradisies van Asië en die ooste.
Filosofiese tradisies uit spesifieke tye en geloofsrigtings word gereeld apart gesien, byvoorbeeld (antieke) Griekse en Hellenistiese Filosofie, Christelike filosofie, Hindoe-filosofie, ensovoorts.
Suid-Afrikaanse filosofie uit westerse tradisies word meestal gesien as deel van westerse filosofie. Die bestaan van iets soos Afrikafilosofie (of ander filosofiese tradisies) as onderskeibare tradisie word soms bespreek, maar is gewoonlik afwesig of sleg verteenwoordig in meeste akademiese besprekings oor filosofie.
Daar is verskeie hoofstrome in Westerse filosofie. Van die mees bekende hoofstrome is:
Analitiese filosofie word gekarakteriseer deur bewyse en argumente, aandag aan detail, en 'n presiese benadering tot die analise van die taal van filosofiese vrae om onduidelikheid uit die weg te ruim. Hierdie benadering domineer Engels-Amerikaanse filosofie. Dit het begin met Gottlob Frege, Bertrand Russell, G. E. Moore en Ludwig Wittgenstein met die draai van die 20ste eeu.
Kontinentale filosofie is 'n versamelnaam vir verskeie uiteenlopende denkrigtings, hoofsaaklik uit kontinentale Europa. Dit is gevolglik moeilik om die tradisie as sodanig te beskryf. Dit kan gekontrasteer word met die tradisie van analitiese filosofie in sommige opsigte. Waar analitiese filosowe byvoorbeeld spesifieke probleme analiseer, fokus kontinentale filosowe soms meer op die werk van sleuteldenkers en die verwantskap tussen verskillendes se werk.
Die metodes van analitiese filosofie word soms beskou as nader verwant aan dié van die wiskunde (veral wat formele argumentasie betref), terwyl kontinentale filosofie weer dikwels metodes uit die letterkunde gebruik.
Eksistensialisme word gekenmerk as 'n filosofiese beweging waar die individu homself bemoei met filosofiese vrae soos "wat is die sin van die lewe?", "wie is ek?", "wat maak ek in hierdie wêreld en hoe kan ek sin vind in realiteit?". Soren Kierkegaard word meestal beskou as die vader van eksistensialisme, maar dit is egter noodsaaklik om te besef dat daar twee vertakkinge van eksistensialisme is: Christelike eksistensialisme en Ateistiese eksistensialisme. Kierkegaard is die groot sentrale denker van die Christelike eksistensialisme en Jean-Paul Sartre word weer as die sleutelfiguur van die ateistiese eksistensialisme beskou. Hoewel Friedrich Nietzsche ook beskryf word as 'n eksistensialis kom hy eintlik meer in die beweging van nihilisme voor, hoewel hy tog 'n impak op eksistensialisme gemaak het.
Dekonstruksionisme is 'n beweging waarvan Jacques Derrida hoofsaaklik die sleutelfiguur was. Derrida se sentrale idee was dat die hele wêreld in werklikheid 'n "teks" is. Dekonstruksionisme gaan baie sterk gepaard met die beweging van Poststrukturalisme.
Negatiewe Dialektiek is begin deur Theodor W. Adorno. Hoewel Adorno gesidder het wanneer hy die woord "teorie" hoor, het hy tog erken dat 'n mens nie sonder teorie te werk kan gaan in enige vakwetenskap nie. Daarom word sy negatiewe dialektiek tog as teorie beskou. Die negatiewe dialektiek funksioneer basies as 'n teorie wat twee kontrasterende konsepte teenoor mekaar opweeg en dit in negatiewe dialektiek teenoor mekaar laat staan. Met behulp van hierdie negatiewe dialektiese verhouding, kan 'n sentrale idee of begrip gedekonstrueer word om sodoende by die kern van iets uit te kom of om die leemtes van 'n begrip of konsep aan te toon.
Vroeërjare was sekere waardevolle items geruil vir ander waardevolle items. 'n Geskikte voorbeeld is die van 'n visserman wat vis vir koring verruil by 'n koringboer. Indien die koringboer nie vis wou hê nie, maar velle, was die proses moeiliker. Eers moet die visserman velle vir sy vis ruil en dan kon hy met die koringboer verder onderhandel. In die onderhandeling moes hy dan bepaal hoeveel velle die koringboer vir 'n gerf koring wil hê. Die aantal velle was die prys vir 'n gerf koring.
Die probleem soos die visserman ondervind het met die koringboer was algemeen. Dit het die behoefte laat ontstaan na 'n item wat vir alles geruil kan word. Sommige van die waarde-items was meer in aanvraag as ander en was as 'n ruilmiddel gebruik. Dit het egter nie die probleem opgelos nie.
Die volgende fase van ontwikkeling was om van "waardelose" items te gebruik as ruilmiddel. Dit was baie belangrik dat hierdie items skaars moes wees en 'n relatiewe lang lewensduur sou hê. Ruilmiddels wat gebruik was, was skulpe, klippe, boombas, walvistande, hondetande en vere. Sulke ruilmiddels is veral op die eilande van die Stille Oseaan gebruik. Daar word berig dat fei-klippe tot omstreeks 1965 as ruilmiddel op die eiland Yap in die Stille Oseaan gebruik is.
Ander ruilmiddels soos vee is ook gebruik. Op party plekke in Afrika word beeste vandag nog gebruik as ruilmiddel. Die Latynse woord vir geld, pecunia, kom van die woord pecus wat 'vee' beteken. In Engels word die woord 'pecuniary' gebruik as van geldsake gepraat word. Dit kom van dieselfde woord af. Dit wys dat mense lank gelede in Europa vee as ruilmiddel gebruik het. "Geld" het die simbool vir waarde geword.
Om hierdie simboliese waarde van geld in konteks te plaas: Wanneer 'n visserman een vis gevang het en hy kon dit verruil vir een skulp, verteenwoordig die skulp die moeite wat die visserman gedoen het om die seehulpbron te ontgin deur een vis te vang sodat 'n mens dit kan eet. Wanneer hy daardie skulp neem en 'n gerf koring wou koop, moes die boer besluit of die skulp wat hy gaan ontvang verteenwoordigend was van die moeite wat hy gedoen het om die gerf te ontgin uit die landbouhulpbron. Indien hy nie so gevoel het nie, kon hy meer gevra het. Sy behoefte aan skulpe om vleis te koop sou ook sy besluit beïnvloed het. Daarom lê die waarde van "geld" tussen die moeite om te ontgin en die behoefte van die mens.""", "af")


# In[4]:


def splitter(file):
    contents = [line for line in open(file + '.txt', encoding='utf8')]
    trainfile = open(file + '_train.txt', 'w', encoding='utf8')
    testfile = open(file + '_test.txt', 'w', encoding='utf8')
    trainfile.write('\n'.join(contents[:44]))
    testfile.write('\n'.join(contents[45:]))
    trainfile.close()
    testfile.close()
    
splitter("en")

splitter("de")

splitter("af")

splitter("nl")



# In[8]:


filesetup("""ALLES TURISTEN UND NONTEKNISCHEN LOOKENPEEPERS!
DAS KOMPUTERMASCHINE IST NICHT FÜR DER GEFINGERPOKEN UND MITTENGRABEN! ODERWISE IST EASY TO SCHNAPPEN DER SPRINGENWERK, BLOWENFUSEN UND POPPENCORKEN MIT SPITZENSPARKEN.
IST NICHT FÜR GEWERKEN BEI DUMMKOPFEN. DER RUBBERNECKEN SIGHTSEEREN KEEPEN DAS COTTONPICKEN HÄNDER IN DAS POCKETS MUSS.
ZO RELAXEN UND WATSCHEN DER BLINKENLICHTEN.""", "blinkenlights")

splitter("blinkenlights")


# In[10]:


filesetup("""This room is fullfilled mit special electronische equippment.
Fingergrabbing and pressing the cnoeppkes from the computers is allowed for die experts only!
So all the “lefthanders” stay away and do not disturben the brainstorming von here working intelligencies.
Otherwise you will be out thrown and kicked anderswhere!
Also: please keep still and only watchen astaunished the blinkenlights.""", "bl")

splitter("bl")


# In[15]:


filesetup("""For most of its being, mankind did not know what things are made
of, but could only guess. With the growth of worldken, we began
to learn, and today we have a beholding of stuff and work that
watching bears out, both in the workstead and in daily life.

The underlying kinds of stuff are the *firststuffs*, which link
together in sundry ways to give rise to the rest. Formerly we
knew of ninety-two firststuffs, from waterstuff, the lightest and
barest, to ymirstuff, the heaviest. Now we have made more, such
as aegirstuff and helstuff.

The firststuffs have their being as motes called *unclefts*.
These are mightly small; one seedweight of waterstuff holds a
tale of them like unto two followed by twenty-two naughts. Most
unclefts link together to make what are called *bulkbits*. Thus,
the waterstuff bulkbit bestands of two waterstuff unclefts, the
sourstuff bulkbit of two sourstuff unclefts, and so on. (Some
kinds, such as sunstuff, keep alone; others, such as iron, cling
together in ices when in the fast standing; and there are yet
more yokeways.) When unlike clefts link in a bulkbit, they make
*bindings*. Thus, water is a binding of two waterstuff unclefts
with one sourstuff uncleft, while a bulkbit of one of the
forestuffs making up flesh may have a thousand thousand or more
unclefts of these two firststuffs together with coalstuff and
chokestuff.

At first is was thought that the uncleft was a hard thing that
could be split no further; hence the name. Now we know it is made
up of lesser motes. There is a heavy *kernel* with a forward
bernstonish lading, and around it one or more light motes with
backward ladings. The least uncleft is that of ordinary
waterstuff. Its kernel is a lone forwardladen mote called a
*firstbit*. Outside it is a backwardladen mote called a
*bernstonebit*. The firstbit has a heaviness about 1840-fold that
of the bernstonebit. Early worldken folk thought bernstonebits
swing around the kernel like the earth around the sun, but now we
understand they are more like waves or clouds.

In all other unclefts are found other motes as well, about as
heavy as the firstbit but with no lading, known as *neitherbits*.
We know a kind of waterstuff with one neitherbit in the kernel
along with the firstbit; another kind has two neitherbits. Both
kinds are seldom.

The next greatest firststuff is sunstuff, which has two firstbits
and two bernstonebits. The everyday sort also has two neitherbits
in the kernel. If there are more or less, the uncleft will soon
break asunder. More about this later.

The third firststuff is stonestuff, with three firstbits, three
bernstonebits, and its own share of neitherbits. And so it goes,
on through such everyday stuffs as coalstuff (six firstbits) or
iron (26) to ones more lately found. Ymirstuff (92) was the last
until men began to make some higher still.

It is the bernstonebits that link, and so their tale fastsets how
a firststuff behaves and what kinds of bulkbits it can help make.
The worldken of this behaving, in all its manifold ways, is
called *minglingken*. Minglingers have found that as the
uncleftish tale of the firststuffs (that is, the tale of
firststuffs in their kernels) waxes, after a while they begin to
show ownships not unlike those of others that went before them.
So, for a showdeal, stonestuff (3), glasswortstuff (11),
potashstuff (19), redstuff (37), and bluegraystuff (55) can each
link with only one uncleft of waterstuff, while coalstuff (6),
flintstuff (14), germanstuff (22), tin (50), and lead (82) can
each link with four. This is readily seen when all are set forth
in what is called the *roundaround board of the firststuffs*.

When an uncleft or a bulkbit wins one or more bernstonebits above
its own, it takes on a backward lading. When it loses one or
more, it takes on a forward lading. Such a mote is called a
*farer*, for that the drag between unlike ladings flits it. When
bernstonebits flit by themselves, it may be as a bolt of
lightning, a spark off some faststanding chunk, or the everyday
flow of bernstoneness through wires.

Coming back to the uncleft itself, the heavier it is, the more
neitherbits as well as firstbits in its kernel. Indeed, soon the
tale of neitherbits is the greater. Unclefts with the same tale
of firstbits but unlike tales of neitherbits are called
*samesteads*. Thus, everyday sourstuff has eight neitherbits with
its eight firstbits, but there are also kinds with five, six,
seven, nine, ten, and eleven neitherbits. A samestead is known by
the tale of both kernel motes, so that we have sourstuff-13,
sourstuff-14, and so on, with sourstuff-16 being by far the most
found. Having the same number of bernstonebits, the samesteads of
a firststuff behave almost alike minglingly. They do show some
unlikenesses, outstandingly among the heavier ones, and these can
be worked to sunder samesteads from each other.

Most samesteads of every firststuff are unabiding. Their kernels
break up, each at its own speed. This speed is written as the
*half-life*, which is how long it takes half of any deal of the
samestead thus to shift itself. The doing is known as
*lightrotting*. It may happen fast or slowly, and in any of
sundry ways, offhanging on the makeup of the kernel. A kernel may
spit out two firstbits with two neitherbits, that is, a sunstuff
kernel, thus leaping two steads back in the roundaround board and
four weights back in heaviness. It may give off a bernstonebit
from a neitherbit, which thereby becomes a firstbit and thrusts
the uncleft one stead up in the board while keeping the same
weight. It may give off a *forwardbit*, which is a mote with the
same weight as a bernstonebit but a forward lading, and thereby
spring one stead down in the board while keeping the same weight.
Often, too, a mote is given off with neither lading nor
heaviness, called the *weeneitherbit*. In much lightrotting, a
mote of light with most short wavelength comes out as well.

For although light oftenest behaves as a wave, it can be looked
on as a mote, the *lightbit*. We have already said by the way
that a mote of stuff can behave not only as a chunk, but as a
wave. Down among the unclefts, things do not happen in steady
flowings, but in leaps between bestandings that are forbidden.
The knowledge-hunt of this is called *lump beholding*.

Nor are stuff and work unakin. Rather, they are groundwise the
same, and one can be shifted into the other. The kinship between
them is that work is like unto weight manifolded by the fourside
of the haste of light.

By shooting motes into kernels, worldken folk have shifted
samesteads of one firststuff into samesteads of another. Thus did
they make ymirstuff into aegirstuff and helstuff, and they have
afterward gone beyond these. The heavier firststuffs are all
highly lightrottish and therefore are not found in the
greenworld.

Some of the higher samesteads are *splitly*. That is, when a
neitherbit strikes the kernel of one, as for a showdeal
ymirstuff-235, it bursts into lesser kernels and free
neitherbits; the latter can then split more ymirstuff-235. When
this happens, weight shifts into work. It is not much of the
whole, but nevertheless it is awesome.

With enough strength, lightweight unclefts can be made to
togethermelt. In the sun, through a row of strikings and
lightrottings, four unclefts of waterstuff in this wise become
one of sunstuff. Again some weight is lost as work, and again
this is greatly big when set beside the work gotten from a
minglingish doing such as fire.

Today we wield both kind of uncleftish doings in weapons, and
kernelish splitting gives us heat and bernstoneness. We hope to
do likewise with togethermelting, which would yield an unhemmed
wellspring of work for mankindish goodgain.

Soothly we live in mighty years!""","an")

splitter("an")

