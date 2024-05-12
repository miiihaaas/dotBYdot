# -*- coding: utf-8 -*-
import time
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #! ovo je dodato da bi moglo da komunicira sa flutter app
@app.route('/api/data', methods=['GET'])
def get_data():
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()
    data = {
        "message": f"Hello from Flask API! Trenutno je {current_time.strftime('%H:%M:%S')} časova.",
        "data": [
            {"name": "Viktor", "surname": "Milivojević", "date_of_birth": datetime(2010, 12, 18)},
            {"name": "Damjan", "surname": "Milivojević", "date_of_birth": datetime(2014, 12, 18)},
            {"name": "Andrija", "surname": "Milivojević", "date_of_birth": datetime(2008, 11, 22)}
        ]
    }
    return jsonify(data)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/tours/<string:tourType>', methods=['GET'])
def api_tours(tourType):
    tour_type = tourType
    tours = {
        "walking": {
            "name": "Panoramska pešačka tura",
            "type": "Pešačka",
            "duration": 2.5,
            "elevationGain": 150.5,
            "startingLocation": "Šetalište kraj reke",
            "difficultyLevel": "Laka",
            "numberOfLocations": 5,
            "locations": [
                #! mesta za testiranje
                {
                    "name": "BGKKS",
                    "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Treće mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                    "short_description": "Treće mesto sa koje smo započeli testiranje",
                    "latlng": [44.817574, 20.535312],
                    "distance_radius": 22.5
                },
                {
                    "name": "BGNPF",
                    "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Četvrto mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                    "short_description": "Četvrto mesto sa koje smo započeli testiranje",
                    "latlng": [44.816916, 20.460592],
                    "distance_radius": 10.5
                },
                {
                    "name": "GMMČK",
                    "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Drugo mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                    "short_description": "Drugo mesto sa koje smo započeli testiranje",
                    "latlng": [44.034661, 20.433998],
                    "distance_radius": 10.5
                },
                {
                    "name": "GMHCP",
                    "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Prvo mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                    "short_description": "Prvo mesto sa koje smo započeli testiranje",
                    "latlng": [44.023905, 20.456093],
                    "distance_radius": 10.5
                },
                #! Vučje
                {
                    "name": "Fontana",
                    "description": 'Fontana "Ribar i hobotnica" je umetničko delo vajara Slavka Miletića iz 1939. godine. Fontana je postavljena kako bi ukrasila tadašnji kompleks tekstilne industrije, prema nacrtu arhitekte Samojlova. Sa leve strane se nalazio fabrički pogon za proizvodnju tekstila.',
                    "short_description": 'Fontana "RIBAR I HOBOTNICA" je umetničko delo vajara Slavka Miletića iz 1939. godine, postavljena kako bi ukrasila tadašnji kompleks tekstilne industrije.',
                    "latlng": [42.868972, 21.910444],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Hostel srednje škole Svetozar Krstić - Toza',
                    "description": 'Hostel koji vidite je isturen objekat Srednje škole "Svetozar Krstić - Toza" iz Vučja. Nekada je to bio restoran u kojem su učenici imali samo praksu. Danas je to prvi učenički hostel koji posluje u okviru školskog preduzeća čiji je osnivač škola. Renoviranje školskog hostela pomogao je Grad Leskovac, dok je sredstva za kompletno opremanje hostela dala Evropska unija preko IPA II Programa prekogranične saradnje Srbije i Severne Makedonije. U Kratovu, Severnoj Makedoniji se takođe nalazi učenički hostel u okviru bratske škole "Mitko Penđuklijski".',
                    "short_description": 'Hostel srednje škole Svetozar Krstić - Toza je isturen objekat škole iz Vučja, nekadašnji restoran sada prvi učenički hostel, renoviran uz pomoć Grada Leskovca i sredstava Evropske unije.',
                    "latlng": [42.867278, 21.911111],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Vila Teokarević',
                    "description": 'Delo arhitekte Grigorija Ivanovića Samojlova, vila porodice Teokarević podignuta je 1935. godine i u početku je korišćena za prijem istaknutih klijenata, da bi kasnije bila dom Lazara Teokarevića.',
                    "short_description": 'Vila Teokarević je delo arhitekte Grigorija Ivanovića Samojlova, izgrađena 1935. godine, korišćena za prijem klijenata, kasnije dom Lazara Teokarevića.',
                    "latlng": [42.866989, 21.910972],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Park Nikole Tesle',
                    "description": 'Park Nikole Tesle posvećen je srpskom naučniku koji je 1903. godine u Vučju pomogao pokretanje hidroelektrane koja i danas proizvodi struju.',
                    "short_description": 'Park Nikole Tesle je posvećen srpskom naučniku koji je 1903. godine pomogao pokretanje hidroelektrane u Vučju, koja i danas funkcioniše.',
                    "latlng": [42.866833, 21.911139],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Spomen česma',
                    "description": 'Palim borcima Vučja i okoline u Narodnooslobodilačkom ratu 1941-1945. Kolektiv fabrike vunenih tkanina Vučje, Srez Leskovac. 18. avgust 1951. Vučje je dalo mnogo života u odbrani slobode od nacističkog okupatora. U znak sećanja podignuta je spomen česma srpskim junacima.',
                    "short_description": 'Spomen česma podignuta je u znak sećanja palim borcima Vučja i okoline u Narodnooslobodilačkom ratu, 18. avgusta 1951. godine, kao omaž srpskim junacima koji su dali živote u odbrani slobode od nacista.',
                    "latlng": [42.866472, 21.911417],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Nikola Skobaljić - (fotografisanje)',
                    "description": 'Ovde se možete fotografisati pored portreta srednjovekovnog viteza Nikole Skobaljića, vladara ovih krajeva u 15. veku. O srpskom vojvodi Nikoli Skobaljiću postoji legenda prema kojoj nije rođen, nije ni stradao kao drugi, obični ljudi. Rodila ga je devojka iz sela Vina, koja ga je začela jedući živu ribu skobalja. Nastradao je zbog izdaje svoje kume, ali ga Turci uhvatili živog nisu već je na svom konju odleteo. Podigao je grad na visu iznad Vučja i taj grad nosi njegovo ime, Skobaljić grad. Ispod grada se nalazi njegov kladenac. U dolini reke Vučjanke sazidao je crkvu na čijim je ruševinama 30-tih godina 20. veka podignuta nova crkva posvećena Sv. Jovanu. Daljim obilaskom lokacija možete saznati nešto više o Skobaljić gradu i o našem junaku Nikoli.',
                    "short_description": 'Ovde možete fotografisati portret srednjovekovnog viteza Nikole Skobaljića, vladara ovih krajeva u 15. veku. Legenda kaže da nije rođen, već je začet dok je njegova majka jela živu ribu skobalja. Bio je poznat po hrabrosti i izdaji svoje kume. Podigao je grad koji nosi njegovo ime i sagradio crkvu posvećenu Sv. Jovanu.',
                    "latlng": [42.866139, 21.911472],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Vodenice',
                    "description": 'Vučjanka kao izuzetno brza reka pogodovala je nastajanju velikog broja vodenica, procenjuje se da je nekada na toku reke Vučjanke bilo preko 20 vodenica. Danas je u radu ostalo svega 4 vodenice. Vodenice pretežno se koriste za mlevenje kukuruza čime se dobija kukuruzno brašno za ishranu ljudi i životinja.',
                    "short_description": 'Reka Vučjanka nekada je imala preko 20 vodenica, ali danas su aktivne samo 4. Vodenice se koriste za mlevenje kukuruza i proizvodnju kukuruznog brašna za ishranu ljudi i životinja.',
                    "latlng": [42.856887, 21.912933],
                    "distance_radius": 10.5
                },
                
                {
                    "name": 'Crkva Sv. Jovana Krstitelja',
                    "description": 'Crkva je posvećena rođenju svetog Jovana Krstitelja, predstavlja pravi dragulj pravoslavnih bogomolja na ovim prostorima. Podignuta je na temeljima crkve koju je u 15. veku podigao vitez, vojvoda Nikola Skobaljić. Crkva sv. Jovana Krstitelja je zadužbina porodice Teokarević, industrijalaca iz Leskovca. Crkva je podizana u periodu od 1932. do 1936. godine. Crkvu je projektovao arhitekta Gligorije Ivanović Samojlov, kao i većinu objekata porodice Teokarević. Crkva je izgrađena kamenom koji se nalazi u podnožju planine Kukavica čiji se obronci nalaze oko vas. Crkva je građena u Moravskom stilu sa pridodatim zvonicima koji su karakteristični za crkve i manastire iz doba Nemanjića. Postoji zapis koji svedoči da je prilikom izgradnje crkve pronađen veliki broj skeleta koji su pripadali srpskim vojnicima iz perioda srednjeg veka. Skeleti koji su tada pronađeni začudili su pronalazače, skeleti su bili izrazito veliki čak i za današnje prilike. Svi posmrtni ostaci srpskih vojnika su pothranjeni u grobnici unutar crkvene porte i pored njih su posađeni borovi koji i danas postoje.',
                    "short_description": 'Crkva Sv. Jovana Krstitelja je posvećena rođenju ovog svetitelja i predstavlja dragocenost među pravoslavnim bogomoljama. Podignuta je na temeljima srednjovekovne crkve, a izgrađena je u periodu od 1932. do 1936. godine u Moravskom stilu. Za vreme izgradnje pronađeni su skeleti srpskih vojnika iz srednjeg veka, a njihovi ostaci sahranjeni su unutar crkve.',
                    "latlng": [42.855833, 21.915278],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Vidikovac (fotografisanje)',
                    "description": 'Sada je vreme za fotografisanje 🙂 - vodite računa, nemojte se previše približavati ivici.',
                    "short_description": 'Sada je pravo vreme za fotografisanje na vidikovcu - samo pazite da ne idete previše blizu ivice!',
                    "latlng": [42.8542888, 21.9160698],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Izletište Vučjanka',
                    "description": 'Ovde se možete odmoriti, a ako ste ovde u periodu od 20. jula do 10. septembra možete poneti kupaći kostim i rashladiti se u bazenu brane na reci Vučjanki.',
                    "short_description": 'Izletište Vučjanka je idealno mesto za odmor, a tokom letnjih meseci možete uživati u bazenu na reci Vučjanki.',
                    "latlng": [42.8535, 21.91625],
                    "distance_radius": 10.5
                },
                {
                    "name": 'Hidroelektrana Vučje',
                    "description": 'Hidroelektrana je počela sa radom 1903. godine, dodatnom izgradnjom i unapređenjem dobija današnji izgled 1930. godine. Za pokretanje i izgradnju hidroelektrane zadužen je fizičar Đorđe Stanojević, koji je bio profesor i rektor Beogradskog univerziteta. Hidroelektrana Vučje podignuta je novcem 168 akcionara "Leskovačkog električnog društva", i po svojoj priči otvorena na Dan oslobođenja Leskovca od turske okupacije, čime je mala varošica na jugu Srbije Vučje i Leskovac sa svojim fabrikama (onog vremena) dobilo struju. Oprema, u koju spada i prvi dalekovod u Kraljevini Srbiji - od Vučja do Leskovca (16 km) - kupljena je za 152.700 dinara u zlatu od nemačke firme "Simens-Halske", a gradnja je poverena Josifu Granžanu, poreklom iz Velikog Bečkereka. Hidroelektrana zahteva vodu iz reke kanalom dugim oko kilometar (980 m), delimično uklesanim u visoke nepristupačne stene. Na ovoj hidroelektrani je tokom Drugog svetskog rata izvršena diverzija. Hidroelektrana danas proizvodi od 5.2 do 6.5 miliona kilovata godišnje.',
                    "short_description": 'Hidroelektrana Vučje je počela sa radom 1903. godine i danas proizvodi između 5.2 i 6.5 miliona kilovata godišnje. Izgrađena je uz pomoć 168 akcionara "Leskovačkog električnog društva" i bila je važan izvor struje za Vučje i Leskovac, otvarajući put za industrijski razvoj ovih mesta.',
                    "latlng": [42.8525706, 21.9160508],
                    "distance_radius": 10.5
                },
                
                {
                    "name": 'Vodopad reke Vučjanke',
                    "description": 'Vodopad reke Vučjanke je delo prelepe prirode ovog kraja. Reči su ovde suvišne, uživajte u prizoru.',
                    "short_description": 'Vodopad reke Vučjanke predstavlja prelepi prirodni fenomen ovog kraja. Uživajte u njegovom pogledu.',
                    "latlng": [42.8513617, 21.9172287],
                    "distance_radius": 10.5
                },
                #! Kratovo
                {
                    "name": "Видиковец",
                    "description": "Видиковецот е ново туристичко место во Кратово. Од него се отвора прекрасен панорамски поглед кон Кратово. Се гледа централното градско подрачје на Кратово со најзначајните културни споменици на градот како што се: кулите, мостовите, турскиот затвор, еврејската куќа, црквата Св. Јован Крстител, старите борови итн. Ова претставува место за уживање, релаксација и фотографирање.",
                    "short_description": "Видиковецот во Кратово нуди прекрасен поглед на градот и неговите историски споменици, претставувајќи идеално место за релаксација и уживање во природата.",
                    "latlng": [42.077047, 22.179709],
                    "distance_radius": 10.5
                },
                {
                    "name": "Рудно окно",
                    "description": '''Целата историја на Кратово се поврзува со рударството, што се докажува со повеќе од 40 рудни окна и складишта за преработена руда – згура. Уште од пред римскиот период Кратово се споменува како богат рударски центар. Во време на Римскиот период Кратово бил рударско средиште во Североисточниот дел, а се експлоатирало олово, цинк, злато, сребро бакар и други руди. Од рудните производи се изработувале и монети. Така, подоцна од Византискиот период пронајдени се монети, меѓу кои и златни на византиските императори Анастасие (491-519г), Јустин I (518 – 527), Јустинијан (527 – 565). Во подоцнежниот период со Кратово управувале повеќе заслужни феудалци коишто управувале со рудниците во Целата Кратовска област. Најголем процут има доживеано во XIV век и тоа поради рудните богатства и тоа злато и оттука градот напредува. Деспот Јован Оливер (1336 – 1355) – важна историска личност од средновековието. Освен што ги искористувал рудниците имал свој дворец тука и е ктитор на Лесновскиот манастир. Еден од попознатите е Јован Оливер (1336 – 1355) – очув на цар Душан - како деспот интензивно ги користел кратовските рудни богатства, преку старите но и отворајќи нови рудни окна. Се обезбедувале големи приход. За ова помогнале и познатите германски рудари Саси кои биле доселени тука со цел поголем развој на рударството. Покрај рудните окна имало и Топилница за руда и Леарница (ковачница) за пари. Развиена била и трговијата, а со неа раководеле Дубровчаните.''',
                    "short_description": '''Кратово, средиште на рударството векови назад, прославено по своите рудници и богатства, од кои се изработувале и монети, со важни историски личности како деспот Јован Оливер.''',
                    "latlng": [42.077990, 22.179178],
                    "distance_radius": 20.5
                },
                {
                    "name": "Ковач",
                    "description": "Познато е дека Општина Кратово, освен по богата историја е град познат и по занаетчиството. Еден од занаетите кој што бил многу развиен во минатото, а не се среќава веќе често денес е всушност ковачкиот занает. Во центарот на градот се наоѓа една од последните работилници во кој ковачот Мише се уште ги обработува металите за да направи алат кој се користи во кратовското секојдневие. Занаетот го наследил од својот татко и се уште работи во неговата работилница.",
                    "short_description": 'Кратово, освен по богатата историја, се истакнува и по ковачкиот занает, што се прекува во последната работилница во центарот на градот, каде што ковачот Мише ги обработува металите како наследство од својот татко.',
                    "latlng": [42.077990, 22.179230],
                    "distance_radius": 20.5
                },
                {
                    "name": "Спомен костурница во чест на паднатите борци на НОБ",
                    "description": "Спомен костурница на НОБ во Кратово е место каде се чуваат останките на храбрите борци кои се бореле за слободата на Македонија за време на Втората светска војна, а потекнувале од Кратовско. На посебни мермерни плочи изгравирани се нивните имиња, како и годините на раѓање и смрт. Тоа е важен споменик и место на почит кон нивната жртва и храброст. Луѓето го посетуваат за да се потсетат на бурната и тешка македонска историја и на тие кои се бореле за нашата слобода. Главните посети се прават на 25 април (првото ослободување на Кратово) и 6 Септември (конечното ослободување на Кратово).",
                    "short_description": 'Спомен костурницата на НОБ во Кратово е место на почит кон храбрите борци од Кратовско од Втората светска војна.',
                    "latlng": [42.077109, 22.179230],
                    "distance_radius": 100.5
                },
                # ... add more locations
            ],
            "preTourInformation": [
                "Udobni sportski cipi i odeća po vremenu.",
                "Poneti vodu za piće.",
            ],
            "restStops": [
                {
                    "name": "Kafić kod fontane",
                    "description": "Kafić sa prelepim pogledom",
                    "latlng": [40.12345, 20.12345]
                },
            ],
        },
        "cycling": {
            "name": "Izazovna biciklistička tura",
            "type": "Biciklistička",
            "duration": 4.0,
            "elevationGain": 500.0,
            "startingLocation": "Biciklistička staza kod mosta",
            "difficultyLevel": "Srednja",
            "numberOfLocations": 3,
            "locations": [
                {
                    "name": "Spomenik na brdu",
                    "description": "Spomenik posvećen herojima.",
                    "short_description": 'Spomenik posvećen herojima.',
                    "latlng": [40.12345, 20.12345],
                    "distance_radius": 10.5
                },
                # ... add more locations
            ],
            "preTourInformation": [
                "Spravljena bicikl i oprema.",
                "Udobna odeća i kaciga.",
                "Dovoljno vode i energijskih napitaka.",
            ],
            "restStops": [
                {
                    "name": "Planinski restoran",
                    "description": "Restoran sa domaćom hranom",
                },
            ],
        },
    }
    
    # time.sleep(5)
    # print(f'debug iz api/tours/ : {tours[tour_type]["locations"][3]["latlng"]=}')
    # print(f'debug iz api/tours/ : {type(tours[tour_type]["locations"][3]["latlng"][0])=}')
    return jsonify(tours[tour_type])

if __name__ == '__main__':
    app.run(debug=True)
