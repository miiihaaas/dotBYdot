# -*- coding: utf-8 -*-
import time
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #! ovo je dodato da bi moglo da komunicira sa flutter app


@app.route('/api/tours/<string:tourType>', methods=['GET'])
def api_tours(tourType):
    tour_type, language = tourType.split('.')
    server_route = f'https://popis.online/dotBYdot' #! izmeni url u listama pictures: []
    
    walking_1 = {
        "en": {
            "name": "Walking tour",
            "type": "Walking tour",
            "routeLenght": "5.1 km",
            "duration": "1h 20min",
            "elevationGain": 238.0,
            "difficultyLevel": "Medium",
            "numberOfLocations": 12,
            "locations": [
                #! Vučje
                {
                    "name": "Fountain",
                    "description": 'The "Fisherman and Octopus" fountain is a work of art by sculptor Slavko Miletić from 1939. The fountain was installed to decorate the former textile industry complex, according to the design of the architect Samoilov. On the left side was a factory for the production of textiles.',
                    "short_description": 'The fountain "FISHERMAN AND OCTOPUS" is a work of art by sculptor Slavko Miletić from 1939, placed to decorate the textile industry complex at the time.',
                    "latlng": [42.868972, 21.910444],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/1.jpg']
                },
                {
                    "name": 'Hostel of the Svetozar Krstić secondary school - Toza',
                    "description": 'The hostel you see is an outpost of the Secondary School "Svetozar Krstić - Toza" from Vučje. It used to be a restaurant where students only had practice. Today, it is the first student hostel that operates within the school enterprise founded by the school. The renovation of the school hostel was helped by the City of Leskovac, while funds for the complete equipment of the hostel were provided by the European Union through the IPA II Cross-Border Cooperation Program of Serbia and North Macedonia. In Kratovo, North Macedonia, there is also a student hostel within the brother school "Mitko Penđuklijski".',
                    "short_description": 'The hostel of the secondary school Svetozar Krstić - Toza is an outpost of the school from Vučje, a former restaurant, now the first student hostel, renovated with the help of the City of Leskovac and funds from the European Union.',
                    "latlng": [42.867278, 21.911111],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/2.jpg']
                },
                {
                    "name": 'Villa Teokarević',
                    "description": 'The work of the architect Grigori Ivanović Samojlov, the villa of the Teokarević family was built in 1935 and was initially used to receive prominent clients, and later became the home of Lazar Teokarević.',
                    "short_description": 'Villa Teokarević is the work of architect Grigori Ivanović Samojlov, built in 1935, used for receiving clients, later the home of Lazar Teokarević.',
                    "latlng": [42.866989, 21.910972],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/3.png']
                },
                {
                    "name": 'Nikola Tesla Park',
                    "description": 'The Nikola Tesla Park is dedicated to the Serbian scientist who in 1903 helped start a hydroelectric plant in Vucje that still produces electricity today.',
                    "short_description": 'The Nikola Tesla Park is dedicated to the Serbian scientist who in 1903 helped start the hydroelectric power plant in Vucje, which is still functioning today.',
                    "latlng": [42.866833, 21.911139],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/4.jpg']
                },
                {
                    "name": 'Memorial fountain',
                    "description": 'To the fallen fighters of Vucje and its surroundings in the National Liberation War 1941-1945. Collective of woolen fabric factory Vučje, Srez Leskovac. August 18, 1951. Vučje gave many lives in defense of freedom from the Nazi occupier. A memorial fountain to Serbian heroes was erected as a sign of memory.',
                    "short_description": 'The memorial fountain was built in memory of the fallen fighters of Vucje and its surroundings in the National Liberation War on August 18, 1951, as a tribute to the Serbian heroes who gave their lives in defense of freedom from the Nazis.',
                    "latlng": [42.866472, 21.911417],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/5.jpg']
                },
                {
                    "name": 'Nikola Skobaljić - (photography)',
                    "description": 'Here you can take a photo next to the portrait of the medieval knight Nikola Skobaljić, the ruler of these regions in the 15th century. There is a legend about the Serbian duke Nikola Skobaljić, according to which he was not born, nor did he suffer like other, ordinary people. He was born to a girl from the village of Vina, who conceived him by eating a live scaby fish. He died because of the betrayal of his godmother, but the Turks did not capture him alive, but he flew away on his horse. He built a town on a hill above Vučje and that town bears his name, Skobaljić town. His well is located below the city. In the valley of the river Vučjanka, he built a church on the ruins of which a new church dedicated to St. was built in the 1930s. to Jovan. By further visiting the locations, you can find out more about the town of Skobaljić and about our hero Nikola.',
                    "short_description": 'Here you can photograph the portrait of the medieval knight Nikola Skobaljić, the ruler of these regions in the 15th century. Legend has it that he was not born, but conceived while his mother was eating a live sable fish. He was known for his bravery and betrayal of his godmother. He built the city that bears his name and built a church dedicated to St. to Jovan.',
                    "latlng": [42.866139, 21.911472],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/6.jpg']
                },
                {
                    "name": 'Water mills',
                    "description": 'Vučjanka, as an extremely fast river, favored the creation of a large number of watermills, it is estimated that once there were more than 20 watermills along the Vučjanka river. Today, only 4 mills remain in operation. Mills are mainly used for grinding corn, which produces corn flour for human and animal consumption.',
                    "short_description": 'The Vučjanka River used to have over 20 watermills, but today only 4 are active. The watermills are used for grinding corn and producing corn flour for human and animal consumption.',
                    "latlng": [42.856887, 21.912933],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/7.jpg']
                },
                
                {
                    "name": 'Church of St. John the Baptist',
                    "description": "The church is dedicated to the birth of St. John the Baptist, it is a true gem of Orthodox places of worship in this area. It was built on the foundations of a church built in the 15th century by the knight Duke Nikola Skobaljić. Church of St. John the Baptist is the endowment of the Teokarević family, industrialists from Leskovac. The church was built in the period from 1932 to 1936. The church was designed by the architect Gligorije Ivanović Samojlov, as well as most of the buildings of the Teokarević family. The church was built with stone located at the foot of Kukavica mountain, whose slopes are around you. The church was built in the Moravian style with added bell towers, which are characteristic of churches and monasteries from the Nemanjić era. There is a record that testifies that during the construction of the church, a large number of skeletons belonging to Serbian soldiers from the Middle Ages were found. The skeletons that were found then amazed the finders, the skeletons were extremely large even for today's conditions. All the remains of Serbian soldiers were buried in a tomb inside the church gate and pine trees were planted next to them, which still exist today.",
                    "short_description": 'Church of St. John the Baptist is dedicated to the birth of this saint and is a treasure among Orthodox churches. It was built on the foundations of a medieval church, and was built between 1932 and 1936 in the Moravian style. During construction, skeletons of Serbian soldiers from the Middle Ages were found, and their remains were buried inside the church.',
                    "latlng": [42.855833, 21.915278],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/8.jpg']
                },
                {
                    "name": 'Viewpoint (photograph)',
                    "description": "Now it's time to take a photo 🙂 - be careful not to get too close to the edge.",
                    "short_description": 'Now is a great time to take photos at the lookout - just be careful not to go too close to the edge!',
                    "latlng": [42.8542888, 21.9160698],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/9.jpg']
                },
                {
                    "name": 'Excursion Vučjanka',
                    "description": 'You can rest here, and if you are here between July 20 and September 10, you can bring your bathing suit and cool off in the pool of the dam on the Vucjanka River.',
                    "short_description": 'The Vučjanka picnic area is an ideal place for a vacation, and during the summer months you can enjoy the swimming pool on the Vučjanka river.',
                    "latlng": [42.8535, 21.91625],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/10.png']
                },
                {
                    "name": 'Vučje Hydropower Plant',
                    "description": 'The hydroelectric power plant began operating in 1903, with additional construction and improvements to give it its current appearance in 1930. Physicist Đorđe Stanojević, who was a professor and rector of Belgrade University, was responsible for starting and building the hydroelectric power plant. The Vučje hydroelectric power plant was built with the money of 168 shareholders of "Leskovac Electric Company", and according to its story, it was opened on the day of the liberation of Leskovac from the Turkish occupation, thus the small town in the south of Serbia Vučje and Leskovac with its factories (at that time) got electricity. The equipment, which includes the first transmission line in the Kingdom of Serbia - from Vučje to Leskovac (16 km) - was purchased for 152,700 dinars in gold from the German company "Siemens-Halske", and the construction was entrusted to Josif Granžan, originally from Veliki Bečkerek. The hydroelectric plant takes water from the river through a channel about a kilometer (980 m) long, partially carved into the high inaccessible rocks. This hydroelectric power plant was diverted during the Second World War. Today, the hydroelectric power plant produces from 5.2 to 6.5 million kilowatts per year.',
                    "short_description": 'The Vučje hydroelectric power plant began operating in 1903 and today produces between 5.2 and 6.5 million kilowatts per year. It was built with the help of 168 shareholders of "Leskovac Electric Company" and was an important source of electricity for Vučje and Leskovac, paving the way for the industrial development of these places.',
                    "latlng": [42.8525706, 21.9160508],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/11.png']
                },
                
                {
                    "name": 'Vučjanka river waterfall',
                    "description": 'The waterfall of the river Vučjanka is a work of the beautiful nature of this region. Words are redundant here, enjoy the scene.',
                    "short_description": 'The waterfall of the river Vučjanka is a beautiful natural phenomenon of this region. Enjoy his view.',
                    "latlng": [42.8513617, 21.9172287],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/12.jpg']
                },
                #! testne lokacije
                {
                    "name": "GMMČK",
                    "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Drugo mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                    "short_description": "Drugo mesto sa koje smo započeli testiranje",
                    "latlng": [44.034661, 20.433998],
                    "distance_radius": 40.5,
                    "pictures": [f'{server_route}/static/pictures/12.jpg']
                },
                {
                    "name": "GMHCP",
                    "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Prvo mesto za koje sa kojeg smo započeli testiranja ovog tipa. Na srpskomk jeziku namerno ima puno teksta kako bi se testirao slajder u popup prozoru. Ovo je jako bitno da bi na lošijim telefonom sa manjom rezolucijom bili u mogućnosti da vidimo ceo tekst pomoću skorlovanja gore-dole. Do sad nimo imali tu opciju i korisnici su se žalili na to, u verziji 0.5 smo napravili izmenu koja će da otkoni ovaj problem i učini naše korisnike srećnije jer im se njihovi predlozi usvajaju i tako dobijamo bolju i praktičniju aplikaciju. Inače ovo je mesto sa kojeg se pravi ova aplikacija. Ponestaje mi inspiracije šta da pišem pa ću zato nastaviti da pišem nevezano i nepovezano. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun. Vuk čupa grane, zimi meda juri vrane. letnje gume travu kose, paunovi zvono nose. ima zime nema srama, sve do tvrđave rama. dasni klik je iznad levog zakonitog pravi meloun.",
                    "short_description": "Prvo mesto sa koje smo započeli testiranje",
                    "latlng": [44.023905, 20.456093],
                    "distance_radius": 40.5,
                    "pictures": [f'{server_route}/static/pictures/12.jpg', f'{server_route}/static/pictures/11.png']
                },
            ],
            "preTourInformation": [
                "Comfortable sports shoes, clothes according to weather conditions",
                "Bring drinking water.",
            ],
            "restStops": [
                {
                    "name": "Kafić kod fontane",
                    "description": "Kafić sa prelepim pogledom",
                    "latlng": [42.8511627, 21.9179207]
                },
            ],
        },
        "sr": {
            "name": "Pešačka tura",
            "type": "Pešačka tura",
            "routeLenght": "5.1 km",
            "duration": "1h 20min",
            "elevationGain": 238.0,
            "difficultyLevel": "Srednja",
            "numberOfLocations": 12,
            "locations": [
                #! Vučje
                {
                    "name": "Fontana",
                    "description": 'Fontana "Ribar i hobotnica" je umetničko delo vajara Slavka Miletića iz 1939. godine. Fontana je postavljena kako bi ukrasila tadašnji kompleks tekstilne industrije, prema nacrtu arhitekte Samojlova. Sa leve strane se nalazio fabrički pogon za proizvodnju tekstila.',
                    "short_description": 'Fontana "RIBAR I HOBOTNICA" je umetničko delo vajara Slavka Miletića iz 1939. godine, postavljena kako bi ukrasila tadašnji kompleks tekstilne industrije.',
                    "latlng": [42.868972, 21.910444],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/1.jpg']
                },
                {
                    "name": 'Hostel srednje škole Svetozar Krstić - Toza',
                    "description": 'Hostel koji vidite je isturen objekat Srednje škole "Svetozar Krstić - Toza" iz Vučja. Nekada je to bio restoran u kojem su učenici imali samo praksu. Danas je to prvi učenički hostel koji posluje u okviru školskog preduzeća čiji je osnivač škola. Renoviranje školskog hostela pomogao je Grad Leskovac, dok je sredstva za kompletno opremanje hostela dala Evropska unija preko IPA II Programa prekogranične saradnje Srbije i Severne Makedonije. U Kratovu, Severnoj Makedoniji se takođe nalazi učenički hostel u okviru bratske škole "Mitko Penđuklijski".',
                    "short_description": 'Hostel srednje škole Svetozar Krstić - Toza je isturen objekat škole iz Vučja, nekadašnji restoran sada prvi učenički hostel, renoviran uz pomoć Grada Leskovca i sredstava Evropske unije.',
                    "latlng": [42.867278, 21.911111],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/2.jpg']
                },
                {
                    "name": 'Vila Teokarević',
                    "description": 'Delo arhitekte Grigorija Ivanovića Samojlova, vila porodice Teokarević podignuta je 1935. godine i u početku je korišćena za prijem istaknutih klijenata, da bi kasnije bila dom Lazara Teokarevića.',
                    "short_description": 'Vila Teokarević je delo arhitekte Grigorija Ivanovića Samojlova, izgrađena 1935. godine, korišćena za prijem klijenata, kasnije dom Lazara Teokarevića.',
                    "latlng": [42.866989, 21.910972],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/3.png']
                },
                {
                    "name": 'Park Nikole Tesle',
                    "description": 'Park Nikole Tesle posvećen je srpskom naučniku koji je 1903. godine u Vučju pomogao pokretanje hidroelektrane koja i danas proizvodi struju.',
                    "short_description": 'Park Nikole Tesle je posvećen srpskom naučniku koji je 1903. godine pomogao pokretanje hidroelektrane u Vučju, koja i danas funkcioniše.',
                    "latlng": [42.866833, 21.911139],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/4.jpg']
                },
                {
                    "name": 'Spomen česma',
                    "description": 'Palim borcima Vučja i okoline u Narodnooslobodilačkom ratu 1941-1945. Kolektiv fabrike vunenih tkanina Vučje, Srez Leskovac. 18. avgust 1951. Vučje je dalo mnogo života u odbrani slobode od nacističkog okupatora. U znak sećanja podignuta je spomen česma srpskim junacima.',
                    "short_description": 'Spomen česma podignuta je u znak sećanja palim borcima Vučja i okoline u Narodnooslobodilačkom ratu, 18. avgusta 1951. godine, kao omaž srpskim junacima koji su dali živote u odbrani slobode od nacista.',
                    "latlng": [42.866472, 21.911417],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/5.jpg']
                },
                {
                    "name": 'Nikola Skobaljić - (fotografisanje)',
                    "description": 'Ovde se možete fotografisati pored portreta srednjovekovnog viteza Nikole Skobaljića, vladara ovih krajeva u 15. veku. O srpskom vojvodi Nikoli Skobaljiću postoji legenda prema kojoj nije rođen, nije ni stradao kao drugi, obični ljudi. Rodila ga je devojka iz sela Vina, koja ga je začela jedući živu ribu skobalja. Nastradao je zbog izdaje svoje kume, ali ga Turci uhvatili živog nisu već je na svom konju odleteo. Podigao je grad na visu iznad Vučja i taj grad nosi njegovo ime, Skobaljić grad. Ispod grada se nalazi njegov kladenac. U dolini reke Vučjanke sazidao je crkvu na čijim je ruševinama 30-tih godina 20. veka podignuta nova crkva posvećena Sv. Jovanu. Daljim obilaskom lokacija možete saznati nešto više o Skobaljić gradu i o našem junaku Nikoli.',
                    "short_description": 'Ovde možete fotografisati portret srednjovekovnog viteza Nikole Skobaljića, vladara ovih krajeva u 15. veku. Legenda kaže da nije rođen, već je začet dok je njegova majka jela živu ribu skobalja. Bio je poznat po hrabrosti i izdaji svoje kume. Podigao je grad koji nosi njegovo ime i sagradio crkvu posvećenu Sv. Jovanu.',
                    "latlng": [42.866139, 21.911472],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/6.jpg']
                },
                {
                    "name": 'Vodenice',
                    "description": 'Vučjanka kao izuzetno brza reka pogodovala je nastajanju velikog broja vodenica, procenjuje se da je nekada na toku reke Vučjanke bilo preko 20 vodenica. Danas je u radu ostalo svega 4 vodenice. Vodenice pretežno se koriste za mlevenje kukuruza čime se dobija kukuruzno brašno za ishranu ljudi i životinja.',
                    "short_description": 'Reka Vučjanka nekada je imala preko 20 vodenica, ali danas su aktivne samo 4. Vodenice se koriste za mlevenje kukuruza i proizvodnju kukuruznog brašna za ishranu ljudi i životinja.',
                    "latlng": [42.856887, 21.912933],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/7.jpg']
                },
                
                {
                    "name": 'Crkva Sv. Jovana Krstitelja',
                    "description": 'Crkva je posvećena rođenju svetog Jovana Krstitelja, predstavlja pravi dragulj pravoslavnih bogomolja na ovim prostorima. Podignuta je na temeljima crkve koju je u 15. veku podigao vitez, vojvoda Nikola Skobaljić. Crkva sv. Jovana Krstitelja je zadužbina porodice Teokarević, industrijalaca iz Leskovca. Crkva je podizana u periodu od 1932. do 1936. godine. Crkvu je projektovao arhitekta Gligorije Ivanović Samojlov, kao i većinu objekata porodice Teokarević. Crkva je izgrađena kamenom koji se nalazi u podnožju planine Kukavica čiji se obronci nalaze oko vas. Crkva je građena u Moravskom stilu sa pridodatim zvonicima koji su karakteristični za crkve i manastire iz doba Nemanjića. Postoji zapis koji svedoči da je prilikom izgradnje crkve pronađen veliki broj skeleta koji su pripadali srpskim vojnicima iz perioda srednjeg veka. Skeleti koji su tada pronađeni začudili su pronalazače, skeleti su bili izrazito veliki čak i za današnje prilike. Svi posmrtni ostaci srpskih vojnika su pothranjeni u grobnici unutar crkvene porte i pored njih su posađeni borovi koji i danas postoje.',
                    "short_description": 'Crkva Sv. Jovana Krstitelja je posvećena rođenju ovog svetitelja i predstavlja dragocenost među pravoslavnim bogomoljama. Podignuta je na temeljima srednjovekovne crkve, a izgrađena je u periodu od 1932. do 1936. godine u Moravskom stilu. Za vreme izgradnje pronađeni su skeleti srpskih vojnika iz srednjeg veka, a njihovi ostaci sahranjeni su unutar crkve.',
                    "latlng": [42.855833, 21.915278],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/8.jpg']
                },
                {
                    "name": 'Vidikovac (fotografisanje)',
                    "description": 'Sada je vreme za fotografisanje 🙂 - vodite računa, nemojte se previše približavati ivici.',
                    "short_description": 'Sada je pravo vreme za fotografisanje na vidikovcu - samo pazite da ne idete previše blizu ivice!',
                    "latlng": [42.8542888, 21.9160698],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/9.jpg']
                },
                {
                    "name": 'Izletište Vučjanka',
                    "description": 'Ovde se možete odmoriti, a ako ste ovde u periodu od 20. jula do 10. septembra možete poneti kupaći kostim i rashladiti se u bazenu brane na reci Vučjanki.',
                    "short_description": 'Izletište Vučjanka je idealno mesto za odmor, a tokom letnjih meseci možete uživati u bazenu na reci Vučjanki.',
                    "latlng": [42.8535, 21.91625],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/10.png']
                },
                {
                    "name": 'Hidroelektrana Vučje',
                    "description": 'Hidroelektrana je počela sa radom 1903. godine, dodatnom izgradnjom i unapređenjem dobija današnji izgled 1930. godine. Za pokretanje i izgradnju hidroelektrane zadužen je fizičar Đorđe Stanojević, koji je bio profesor i rektor Beogradskog univerziteta. Hidroelektrana Vučje podignuta je novcem 168 akcionara "Leskovačkog električnog društva", i po svojoj priči otvorena na Dan oslobođenja Leskovca od turske okupacije, čime je mala varošica na jugu Srbije Vučje i Leskovac sa svojim fabrikama (onog vremena) dobilo struju. Oprema, u koju spada i prvi dalekovod u Kraljevini Srbiji - od Vučja do Leskovca (16 km) - kupljena je za 152.700 dinara u zlatu od nemačke firme "Simens-Halske", a gradnja je poverena Josifu Granžanu, poreklom iz Velikog Bečkereka. Hidroelektrana zahteva vodu iz reke kanalom dugim oko kilometar (980 m), delimično uklesanim u visoke nepristupačne stene. Na ovoj hidroelektrani je tokom Drugog svetskog rata izvršena diverzija. Hidroelektrana danas proizvodi od 5.2 do 6.5 miliona kilovata godišnje.',
                    "short_description": 'Hidroelektrana Vučje je počela sa radom 1903. godine i danas proizvodi između 5.2 i 6.5 miliona kilovata godišnje. Izgrađena je uz pomoć 168 akcionara "Leskovačkog električnog društva" i bila je važan izvor struje za Vučje i Leskovac, otvarajući put za industrijski razvoj ovih mesta.',
                    "latlng": [42.8525706, 21.9160508],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/11.png']
                },
                
                {
                    "name": 'Vodopad reke Vučjanke',
                    "description": 'Vodopad reke Vučjanke je delo prelepe prirode ovog kraja. Reči su ovde suvišne, uživajte u prizoru.',
                    "short_description": 'Vodopad reke Vučjanke predstavlja prelepi prirodni fenomen ovog kraja. Uživajte u njegovom pogledu.',
                    "latlng": [42.8513617, 21.9172287],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/12.jpg']
                },
                #! testne lokacije
                {
                    "name": "GMMČK",
                    "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Drugo mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                    "short_description": "Drugo mesto sa koje smo započeli testiranje",
                    "latlng": [44.034661, 20.433998],
                    "distance_radius": 40.5,
                    "pictures": [f'{server_route}/static/pictures/12.jpg']
                },
                {
                    "name": "GMHCP",
                    "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Prvo mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                    "short_description": "Prvo mesto sa koje smo započeli testiranje",
                    "latlng": [44.023905, 20.456093],
                    "distance_radius": 40.5,
                    "pictures": [f'{server_route}/static/pictures/12.jpg', f'{server_route}/static/pictures/11.png']
                },
            ],

            "preTourInformation": [
                "Udobne sportska obuća, odeća prema vremenskim uslovima",
                "Poneti vodu za piće.",
            ],
            "restStops": [
                {
                    "name": "Kafić kod fontane",
                    "description": "Kafić sa prelepim pogledom",
                    "latlng": [42.8511627, 21.9179207]
                },
            ],
        },
    }
    
    
    walking_2 = {
        "en": {
            "name": "Walking cardio tour",
            "type": "Walking",
            "routeLenght": "5.06 km",
            "duration": "1h 25min",
            "elevationGain": 272.0,
            "difficultyLevel": "Heavy",
            "numberOfLocations": 12,
            "locations": [
                #! Vučje
                {
                    "name": 'Starting point',
                    "description": 'Carefully observe the starting position extending from the left side of the road. The path is also marked with a mountain marking you can see on the tree, a red circle with a white color in the center. These markings will help you during the route as confirmation that you are on the right track. Also, if for some reason you are unable to use your phone or other smart device, follow these markings to return to the populated area. This hiking route is extremely physically demanding and dangerous in some parts, and is not recommended for beginners and those who, due to health and other problems, cannot overcome steep forest terrains. For the most part, the route goes through forests and forest areas. Stick to the middle of the path, if you encounter animals, among which there may be snakes, do not panic. Either go back or pass slowly by them without looking away. For this route, be sure to bring water and something sweet, also make sure you have appropriate clothing and footwear. Good luck! Enjoy!',
                    "short_description": 'Carefully observe the starting position on the left side of the road. The path is marked with mountain markings. Follow these markings to return to the populated area. The route is physically demanding and dangerous, and is not recommended for beginners. Bring water and something sweet. Good luck! Enjoy!',
                    "latlng": [42.853471, 21.916613],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/13.jpg'],
                },
                {
                    "name": 'Viewpoint - view of the Hydroelectric Power Plant',
                    "description": 'Bravo, you have conquered the first peak and this is your first victory on this trail :) Rest a bit, drink some water, and then slowly approach the edge, towards the rocks, to receive your reward. The reward is a beautiful view from the elevation, take a safe photo and continue further.',
                    "short_description": 'Bravo, you have conquered the first peak on this trail :) Rest, drink some water, and approach the edge of the rocks for a beautiful view. Enjoy taking photos!',
                    "latlng": [42.851781, 21.917327],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/14.png'],
                },
                {
                    "name": 'Viewpoint',
                    "description": 'Another viewpoint, time for a bit more rest. The continuation of the route will partly go along an asphalt road, be careful not to get hit by a car or get into trouble with cows you might encounter :)',
                    "short_description": 'Another viewpoint for a rest. The route continues along an asphalt road, watch out for cars and cows :)',
                    "latlng": [42.850720, 21.918126],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/15.jpg'],
                },
                {
                    "name": 'Sokolica Rock',
                    "description": 'Tanana the famous Sokolica rock, below you is the canyon of the Vučjanka river. If you are lucky and the day is clear, the view extends all the way to Niš. Be careful, the area is not secured, enjoy the view from a safe distance from the edge. Across the way, you can see a path with handrails that you can explore another time or after visiting this route. Ask the locals how best to reach that path and enjoy the view of the canyon from another angle. Rest and enjoy the fresh air and the sound of the canyon.',
                    "short_description": 'Sokolica Rock with the canyon of the Vučjanka river. The view extends to Niš on clear days. Enjoy from a safe distance from the edge. Across the way is a path with handrails you can explore later. Ask the locals about the path. Rest and enjoy the fresh air and the sound of the canyon.',
                    "latlng": [42.847656, 21.914257],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/16.jpg'],
                },
                {
                    "name": 'Wooden Bridge',
                    "description": 'No need to panic :) feel free to cross the wooden bridge and enjoy it, wagons and other much heavier vehicles pass over the bridge :) Pay attention while moving so you don\'t miss the next point, the turn will be on your left side.',
                    "short_description": 'Feel free to cross the wooden bridge. Wagons and heavier vehicles pass over it. Be careful not to miss the next point, the turn is on the left side.',
                    "latlng": [42.846207, 21.914482],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/17.jpg'],
                },
                {
                    "name": 'Guardian Rock',
                    "description": 'The Guardian Rock is painted with the works of our famous Vučjanac Bratislav Bata Anđelković, who enriched the cultural heritage of Vučje with his works and contributed to awakening the spirit of the past. On the rock, there are depictions of Serbian saints and clergy on both sides.',
                    "short_description": 'The Guardian Rock with depictions of Serbian saints and clergy, painted by Bratislav Bata Anđelković. It enriched the cultural heritage of Vučje.',
                    "latlng": [42.849925, 21.913351],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/18.jpg'],
                },
                {
                    "name": 'Viewpoint Rock',
                    "description": 'Another viewpoint and an opportunity for rest and photography.',
                    "short_description": 'Another viewpoint for rest and photography.',
                    "latlng": [42.850322, 21.912492],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/19.png'],
                },
                {
                    "name": 'Skobaljić Fortress',
                    "description": 'Skobaljić Fortress is a medieval fortress. It belonged to Duke Nikola Skobaljić. Today, only the remains of the city exist. In 1986, it was declared a cultural monument of the Republic of Serbia. Tradition ties this location to Duke Nikola Skobaljić, a great hero who fought against the Ottoman Turks and was never defeated. He built the city on a hill above Vučje, and the city bears his name. Below the city is his spring. In the valley of the Vučjanka river, he built a church on whose ruins a new church dedicated to Saint John was erected in the 1930s. The site is multi-layered: the oldest traces of the use of this area date back to the Eneolithic — the Copper Age. Also, fragments of pottery found during excavations testify that this fortification, due to its strategically important position and position suitable for defense, was used during several phases of the Bronze Age. The oldest stone fortification dates from pre-Roman times, and the fortification built of stone and bricks with mortar from the early Byzantine period. According to archaeological findings, the fortress was used in the Roman period, and later in the period from the 10th to the 13th century. The youngest fortification, the remains of whose ramparts and towers are still visible, dates from the 15th century. The city consisted of the Upper, Lower City, and a suburb that stretched on the eastern side. It covered an area of about 2 hectares. The most powerful preserved ramparts are located in the west, and a defensive trench is located in the north. The Upper City is square-shaped with about 400 square meters of area and has a powerful cultural layer preserved in it. Two towers are placed diagonally. A smaller tower is located next to the gate leading to the Lower City, and a larger — Donjon Tower is located in the northwest part and its walls are preserved up to the height of the ground floor. Excavations were carried out in the Upper City along the inner side of the southern rampart. In this area, fragments of pottery from the 3rd-1st centuries BC were found in the layer of the destroyed wall built of stone bound with mud. The layer is dated to a republican denarius from 100 BC. These are the remains of a pre-Roman fortification. The younger phase of the fortification dates from the early Byzantine period from the 6th century. Parts of the rampart built of stone and mortar are preserved. This rampart is damaged. The Lower City with the suburb of 1400 square meters extends east of the Upper City and follows the configuration of the terrain. Research was carried out in the northern, lowest part, at the place where it is assumed that there was a gate, which unfortunately was not discovered. On the eastern side, remains of a tower built in a mixed technique of brick and stone were discovered and belongs to the early Byzantine period. Based on the pottery, layers from the 10th-11th and 12th-13th centuries can also be identified, indicating that the fortification had a certain role in events in the 11th century, as well as later during the time of Duke Desa, Stefan Nemanja, and his successors.',
                    "short_description": 'Skobaljić Fortress is a medieval fortress that belonged to Duke Nikola Skobaljić. Today, the remains of the city are declared a cultural monument of the Republic of Serbia. Tradition ties this location to Duke Nikola Skobaljić, a great hero who fought against the Ottoman Turks. The city consisted of the Upper, Lower City, and a suburb.',
                    "latlng": [42.850106, 21.911732],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/20.jpg'],
                },
                {
                    "name": 'Crossroad',
                    "description": 'Passing point of the route - enjoy nature.',
                    "short_description": 'Passing point of the route - enjoy nature.',
                    "latlng": [42.851414, 21.9132466],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/21.jpg'],
                },
                {
                    "name": 'View of Vučje',
                    "description": 'Phenomenal view of Vučje, rest and immortalize the scene before you.',
                    "short_description": 'Phenomenal view of Vučje, rest and immortalize the scene.',
                    "latlng": [42.8514885, 21.9125155],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/22.png'],
                },
                {
                    "name": 'Crossroad',
                    "description": 'Passing point of the route - enjoy nature.',
                    "short_description": 'Passing point of the route - enjoy nature.',
                    "latlng": [42.8516527, 21.9083007],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/23.png'],
                },
                {
                    "name": 'Forest rock',
                    "description": 'The last rock and the view offered during this route. Thank you for choosing this route, we hope you leave Vučje with beautiful photos and even better impressions.',
                    "short_description": 'The last rock and the view offered during this route. Thank you for choosing this route.',
                    "latlng": [42.8525745, 21.9104787],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/24.png'],
                },
                {
                    "name": 'Church of St. John the Baptist',
                    "description": "The church is dedicated to the birth of St. John the Baptist, representing a true jewel of Orthodox shrines in this area. It was built on the foundations of a church erected in the 15th century by the knight, Duke Nikola Skobaljić. The Church of St. John the Baptist is the endowment of the Teokarević family, industrialists from Leskovac. The church was built between 1932 and 1936. The church was designed by architect Grigorije Ivanovich Samojlov, who also designed most of the Teokarević family's buildings. The church is made of stone found at the base of Mount Kukavica, whose slopes surround you. The church was built in the Moravian style with an added bell tower characteristic of churches and monasteries from the Nemanjić era. There is a record that during the construction of the church, a large number of skeletons belonging to Serbian soldiers from the medieval period were found. The skeletons found then surprised the finders, as they were exceptionally large even by today's standards. All the remains of the Serbian soldiers are interred in a tomb within the church yard, and pine trees were planted beside them, which still exist today.",
                    "short_description": 'The church is dedicated to the birth of St. John the Baptist, representing a true jewel of Orthodox shrines in this area. It was built on the foundations of a church erected in the 15th century by the knight, Duke Nikola Skobaljić.',
                    "latlng": [42.855732, 21.914078],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/8,25.jpg'],
                },


            ],
            "preTourInformation": [
                "Udobne sportska obuća, odeća prema vremenskim uslovima",
                "Poneti vodu za piće.",
            ],
            "restStops": [
                {
                    "name": "Kafić kod fontane",
                    "description": "Kafić sa prelepim pogledom",
                    "latlng": [42.8511627, 21.9179207]
                },
            ],
        },
        "sr": {
            "name": "Pešačka kardio tura",
            "type": "Pešačka",
            "routeLenght": "5.06 km",
            "duration": "1h 25min",
            "elevationGain": 272.0,
            "difficultyLevel": "Teška",
            "numberOfLocations": 12,
            "locations": [
                #! Vučje
                {
                    "name": 'Početna tačka',
                    "description": 'Pažljivo pogledajte početnu poziciju koja se pruža sa leve strane puta. Staza je takođe obeležena planinskom markacijom koju možete videti na drvetu, crveni krug u čijem je središtu bela boja. Te oznake će vam tokom rute pomoći kao potvrda da ste na pravom putu. Takođe, ako iz nekog slučaja ostanete bez mogućnosti da koristite telefon ili drugi pametni uređaj držite se tih markacija kako bi se vratili u naseljeni deo. Ova pešačka ruta je u pojedinim delovima izuzetno fizički zahtevna i opasna, te se ne preporučuje početnicima i onima koji iz zdravstvenih i drugih problema ne mogu da savladaju strme šumske terene. Većim delom ruta prolazi šumom i šumskim predelima. Držite se sredine staze, ako naiđete na životinje, među kojima mogu biti i zmije, nemojte paničiti. Ili se vratite ili prođite polako pored njih ne sklanjajući pogled. U obilazak ove rute obavezno ponesite vodu i nešto slatko, takođe vodite računa da imate adekvatnu garderobu i obuću. Srećno! Uživajte!',
                    "short_description": 'Pažljivo pogledajte početnu poziciju sa leve strane puta. Staza je obeležena planinskom markacijom. Držite se tih markacija kako bi se vratili u naseljeni deo. Ruta je fizički zahtevna i opasna, te se ne preporučuje početnicima. U obilazak ponesite vodu i nešto slatko. Srećno! Uživajte!',
                    "latlng": [42.853471, 21.916613],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/13.jpg'],
                },
                {
                    "name": 'Vidikovac - pogled na Hidroelektranu',
                    "description": 'Bravo, uspeli ste da osvojite prvi vrh i to je u vašem pohodu na ovu stazu prva pobeda :) Malo odmorite, popite vodu, pa se onda sasvim lagano približite ivici, u pravcu stena, kako bi dobili nagradu. Nagrada je predivan pogled koji se pruža sa uzvišenja, uhvatite koju fotografiju bezbedno i nastavite dalje.',
                    "short_description": 'Bravo, osvojili ste prvi vrh na ovoj stazi :) Odmorite se, popite vodu, i približite se ivici stena za predivan pogled. Uživajte u fotografisanju!',
                    "latlng": [42.851781, 21.917327],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/14.png'],
                },
                {
                    "name": 'Vidikovac',
                    "description": 'Još jedan vidikovac, vreme je za još malo predaha, nastavak puta će jednim delom ići asfaltiranim putem, obratite pažnju da vas ne udari automobil ili da se ne zamerate kravama na koje je moguće naići :)',
                    "short_description": 'Još jedan vidikovac za predah. Nastavak puta ide asfaltiranim putem, pazite na automobile i krave :)',
                    "latlng": [42.850720, 21.918126],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/15.jpg'],
                },
                {
                    "name": 'Stena Sokolica',
                    "description": 'Tanana čuvena stena Sokolica, ispod vas se nalazi kanjon reke Vučjanke. Ako imate sreće i dan je vedar pogled seže sve do Niša. Vodite računa prostor nije obezbeđen, uživajte u pogledu sa bezbedne udaljenosti od ivice. Preko puta se nazire staza ograđena rukohvatima koju možete istražiti nekom drugom prilikom ili nakon obilaska ove rute. Raspitajte se kod meštana kako najbolje da stignete do te staze i uživate u prizoru kanjona iz drugog ugla. Odmorite i uživajte u čistom vazduhu i zvuku kanjona.',
                    "short_description": 'Stena Sokolica sa kanjonom reke Vučjanke. Pogled seže do Niša u vedrim danima. Uživajte sa bezbedne udaljenosti od ivice. Preko puta je staza ograđena rukohvatima koju možete istražiti kasnije. Raspitajte se kod meštana o stazi. Odmorite i uživajte u čistom vazduhu i zvuku kanjona.',
                    "latlng": [42.847656, 21.914257],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/16.jpg'],
                },
                {
                    "name": 'Drveni most',
                    "description": 'Nema mesta panici :) slobodno pređite preko drvenog mosta i uživajte, preko mosta prolaze zaprežna kola i druga mnogo teža vozila :) Obratite pažnju tokom kretanja da ne prođete sledeću tačku, skretanje će biti sa vaše leve strane.',
                    "short_description": 'Slobodno pređite preko drvenog mosta. Preko njega prolaze zaprežna kola i teža vozila. Pazite da ne prođete sledeću tačku, skretanje je sa leve strane.',
                    "latlng": [42.846207, 21.914482],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/17.jpg'],
                },
                {
                    "name": 'Stena Čuvar',
                    "description": 'Stena čuvar je oslikana delima našeg čuvenog Vučijanca Bratislava Bate Anđelkovića koji je svojim delima obogatio kulturno nasleđe Vučja i doprineo buđenju duha prošlosti. Na steni su sa dve strane prikazi srpskih svetaca i sveštenstva.',
                    "short_description": 'Stena čuvar sa prikazima srpskih svetaca i sveštenstva, oslikana delima Bratislava Bate Anđelkovića. Obogatila je kulturno nasleđe Vučja.',
                    "latlng": [42.849925, 21.913351],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/18.jpg'],
                },
                {
                    "name": 'Vidikovac u mestena',
                    "description": 'Još jedan vidikovac i prilika za predah i fotografisanje.',
                    "short_description": 'Još jedan vidikovac za predah i fotografisanje.',
                    "latlng": [42.850322, 21.912492],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/19.png'],
                },
                {
                    "name": 'Skobaljić grad',
                    "description": 'Skobaljić grad je srednjovekovna tvrđava. Pripadao je vojvodi Nikoli Skobaljiću. Danas postoje samo ostaci grada. Godine 1986. godine proglašen je za kulturno dobro Republike Srbije. Tradicija vezuje ovaj lokalitet za vojvodu Nikolu Skobaljića, velikog junaka koji je ratovao sa Turcima Osmanlijama i nikada nije bio poražen. On je izgradio grad na visu iznad Vučja i taj grad nosi njegovo ime. Ispod grada se nalazi njegov kladenac. U dolini reke Vučjanke sazidao je crkvu na čijim je ruševinama 30-ih godina 20. veka podignuta nova crkva posvećena Svetom Jovanu. Lokacija je višeslojna: najstariji tragovi korišćenja ovog prostora potiču iz eneolita — bakarnog doba. Takođe, fragmenti keramike pronađeni tokom iskopavanja svedoče da je ovo utvrđenje zbog strateški važnog položaja i položaja pogodnog za odbranu korišćeno i tokom više faza bronzanog doba. Najstarije kameno utvrđenje potiče iz predrimskog doba, a utvrđenje zidano od kamena i opeka sa malterom iz ranovizantijskog doba. Prema arheološkim nalazima, tvrđava je korišćena i u rimskom, a kasnije i u periodu od X do XIII veka. Najmlađe utvrđenje, čiji se ostaci zidova bedema i kula još uvek vide potiče iz 15. veka. Grad se sastojao od Gornjeg, Donjeg grada i podgrađa koje se prostiralo na istočnoj strani. Zahvatao je površinu od oko 2 hektara. Najmoćniji sačuvani bedemi se nalaze na zapadu, a na severu se nalazi odbrambeni rov. Gornji Grad je kvadratnog oblika sa oko 400 kvadrata površine i u njemu je sačuvan moćan kulturni sloj. Dve kule su dijagonalno postavljene. Manja kula se nalazi pored kapije koja vodi u Donji grad, a veća — Donžon kula se nalazi u severozapadnom delu i njeni zidovi su očuvani do visine prizemlja. U Gornjem Gradu su iskopavanja vršena uz unutrašnju stranu južnog bedema. Na ovom prostoru pronađeni su fragmenti grnčarije iz perioda III-1. veka p.n.e. u sloju rušenja zida građenog od kamena povezanog blatom. Sloj je datovan republikanskim denarom iz 100. p.n.e. To su ostaci tvrđave iz predrimskog vremena. Mlađa faza utvrđenja potiče iz ranovizantijskog vremena iz 6. veka. Sačuvani su delovi bedema građeni od kamena i maltera. Ovaj bedem je oštećen. Donji Grad sa podgrađem veličine 1400 kvadrata se prostire istočno od Gornjeg Grada i prati konfiguraciju terena. Istraživanja su vršena na severnom, najnižem delu, na mestu gde se pretpostavlja da je bila kapija, koja nažalost nije otkrivena. Na istočnoj strani otkriveni su ostaci kule koja je zidana u mešovitoj tehnici od opeke i kamena i pripada ranovizantijskom vremenu. Na osnovu grnčarije može se identifikovati i sloj iz X-XI i XII-XIII veka koji govori da je utvrđenje imalo određenu ulogu u događajima u XI veku, kao i docnije u vreme župana Dese, Stefana Nemanje i njegovih naslednika.',
                    "short_description": 'Skobaljić grad je srednjovekovna tvrđava koja je pripadala vojvodi Nikoli Skobaljiću. Danas su ostaci grada proglašeni za kulturno dobro Republike Srbije. Tradicija vezuje ovaj lokalitet za vojvodu Nikolu Skobaljića, velikog junaka koji je ratovao sa Turcima Osmanlijama. Grad se sastojao od Gornjeg, Donjeg grada i podgrađa.',
                    "latlng": [42.850106, 21.911732],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/20.jpg'],
                },
                {
                    "name": 'Raskršće',
                    "description": 'Prolazna tačka rute - uživajte u prirodi.',
                    "short_description": 'Prolazna tačka rute - uživajte u prirodi.',
                    "latlng": [42.851414, 21.9132466],
                    "distance_radius": 50.0,
                    "pictures": [f'{server_route}/static/pictures/21.jpg'],
                },
                {
                    "name": 'Pogled na Vučje',
                    "description": 'Fenomenalan pogled na Vučje, odmorite i ovekovečite prizor koji je pred vama.',
                    "short_description": 'Fenomenalan pogled na Vučje, odmorite i ovekovečite prizor.',
                    "latlng": [42.8514885, 21.9125155],
                    "distance_radius": 50.0,
                    "pictures": [f'{server_route}/static/pictures/22.png'],
                },
                {
                    "name": 'Raskršće',
                    "description": 'Prolazna tačka rute - uživajte u prirodi.',
                    "short_description": 'Prolazna tačka rute - uživajte u prirodi.',
                    "latlng": [42.8516527, 21.9083007],
                    "distance_radius": 50.0,
                    "pictures": [f'{server_route}/static/pictures/23.png'],
                },
                {
                    "name": 'Šumska stena',
                    "description": 'Poslednja stena i pogled koji vam se pruža tokom ove rute. Hvala što ste odabrali ovu rutu, nadamo se da sa lepim fotografijama i još lepšim utiscima napuštate Vučje.',
                    "short_description": 'Poslednja stena i pogled koji vam se pruža tokom ove rute. Hvala što ste odabrali ovu rutu.',
                    "latlng": [42.8525745, 21.9104787],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/24.png'],
                },
                {
                    "name": 'Crkva Sv. Jovana Krstitelja',
                    "description": 'Crkva je posvećena rođenju svetog Jovana krstitelja, predstavlja pravi dragulj pravoslavnih bogomolja na ovim prostorima. Podignuta je na temeljima crkve koju je u 15. veku podigao vitez, vojvoda Nikola Skobaljić. Crkva sv. Jovana krstitelja je zadužbina porodice Teokarević, industrijalaca iz Leskovca. Crkva je podizana u periodu od 1932. do 1936. godine. Crkvu je projektovao arhitekta Grigorije Ivanovich Samojlov, kao i većinu objekata porodice Teokarević. Crkva je izgrađena kamenom koji se nalazi u podnožju planine Kukavica čiji se obronci nalaze oko vas. Crkva je građena u Moravskom stilu sa pridodatim zvonikom koji je karakterističan za srkve i manastire iz doba Nemanjića. Postoji zapis koji svedoči da je prilikom izgradnje crkve pronađen veliki broj skeleta koji su pripadali srpskim vojnicima iz perioda srednjeg veka. Skeleti koji su tada pronađeni začudili su pronalazače, skeleti su bili izrazoto veliki čak i za današnje prilike. Svi posmrtni ostaci srpskih vojnika su pohranjeni u grobnici unutar crkvene porte i pored njih su posađeni borovi koji i danas postoje.',
                    "short_description": 'Crkva je posvećena rođenju svetog Jovana krstitelja, predstavlja pravi dragulj pravoslavnih bogomolja na ovim prostorima. Podignuta je na temeljima crkve koju je u 15. veku podigao vitez, vojvoda Nikola Skobaljić.',
                    "latlng": [42.855732, 21.914078],
                    "distance_radius": 25.8,
                    "pictures": [f'{server_route}/static/pictures/8,25.jpg'],
                },
            ],
            "preTourInformation": [
                "Udobne sportska obuća, odeća prema vremenskim uslovima",
                "Poneti vodu za piće.",
            ],
            "restStops": [
                {
                    "name": "Kafić kod fontane",
                    "description": "Kafić sa prelepim pogledom",
                    "latlng": [42.8511627, 21.9179207]
                },
            ],
        },
    }
    
    cycling_1 = {
        "en": {
            "name": "Cycling tour",
            "type": "Cycling",
            "routeLenght": "17.3 km",
            "duration": "1h 20min",
            "elevationGain": 126.0,
            "difficultyLevel": "Medium",
            "numberOfLocations": 12,
            "locations": [
                {
                    "name": 'Hostel of the Secondary School Svetozar Krstić - Toza',
                    "description": 'The hostel you see is an extension of the Secondary School "Svetozar Krstić - Toza" from Vučje. It used to be a restaurant where students only had practice. Today, it is the first student hostel operating within a school enterprise founded by the school. The renovation of the school hostel was supported by the City of Leskovac, while the European Union provided funds for the complete equipping of the hostel through the IPA II Cross-Border Cooperation Program between Serbia and North Macedonia. In Kratovo, North Macedonia, there is also a student hostel within the brother school "Mitko Pendžukliski".',
                    "short_description": 'The hostel you see is an extension of the Secondary School "Svetozar Krstić - Toza" from Vučje. It used to be a restaurant where students only had practice. Today, it is the first student hostel operating within a school enterprise founded by the school.',
                    "latlng": [42.867278, 21.911111],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/2.jpg'],
                },
                {
                    "name": 'Factory "Porečje"',
                    "description": 'PREMIUM RAKIJA PRODUCER - The "Porečje" kombinat, founded in 1960, has been known from the start for its high-quality products. The "Porečje" distillery bases its procurement and selection of all fruit types primarily from the territory of Porečje, where rakija production is also located. The "Porečje" distillery continues the well-trodden path of producing premium rakijas with the desire to share its experience in producing the highest quality rakijas with enthusiasts of fine spirits both in Serbia and around the world. Trivunova rakija, as a famous brand, originated in the south of Serbia, at the foot of the Kukavica mountain, with the unique Vučjanka river canyon, which has created the rich plain - POREČJE. This fertile land produces the highest quality fruit that transforms into premium rakijas. Capacity of 5000 liters per day.',
                    "short_description": 'PREMIUM RAKIJA PRODUCER - The "Porečje" kombinat, founded in 1960, has been known from the start for its high-quality products. The "Porečje" distillery bases its procurement and selection of all fruit types primarily from the territory of Porečje, where rakija production is also located.',
                    "latlng": [42.87475, 21.907694],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/27.png'],
                },
                {
                    "name": 'Church of St. George the Great Martyr',
                    "description": 'The Church of St. George the Great Martyr in Beli Potok near Leskovac is a temple of the Serbian Orthodox Church. The church was built in 2015 with the help of funds from Slobodan Stojanović from Beli Potok. Construction lasted for two years, and the church was consecrated on May 6, 2014.',
                    "short_description": 'The Church of St. George the Great Martyr in Beli Potok near Leskovac is a temple of the Serbian Orthodox Church.',
                    "latlng": [42.885805, 21.914167],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/28.jpg'],
                },

            ],
            "preTourInformation": [
                "Udobne sportska obuća, odeća prema vremenskim uslovima",
                "Poneti vodu za piće.",
            ],
            "restStops": [
                {
                    "name": "Kafić kod fontane",
                    "description": "Kafić sa prelepim pogledom",
                    "latlng": [42.8511627, 21.9179207]
                },
            ],
        },
        "sr": {
            "name": "Bicikilistička tura",
            "type": "Biciklistička",
            "routeLenght": "17.3 km",
            "duration": "1h 20min",
            "elevationGain": 126.0,
            "difficultyLevel": "Srednja",
            "numberOfLocations": 12,
            "locations": [
                {
                    "name": 'Hostel srednje škole Svetozar Krstić - Toza',
                    "description": 'Hostel koji vidite je istureni objekat Srednje škole „Svetozar Krstić - Toza“ iz Vučja. Nekada je to bio restoran u kojem su učenici imali samo praksu. Danas je to prvi učenički hostel koji posluje u okviru školskog preduzeća čiji je osnivač škola. Renoviranje školskog hostela pomogao je Grad Leskovac, dok je sredstva za kompletno opremanje hostela dala Evropska unija preko IPA II Programa prekogranične saradnje Srbije i Severne Makedonije. U Kratovu, Severnoj Makedoniji se takođe nalazi učenički hostel u okviru bratske škole „Mitko Pendžukliski“.',
                    "short_description": 'Hostel koji vidite je istureni objekat Srednje škole „Svetozar Krstić - Toza“ iz Vučja. Nekada je to bio restoran u kojem su učenici imali samo praksu. Danas je to prvi učenički hostel koji posluje u okviru školskog preduzeća čiji je osnivač škola.',
                    "latlng": [42.867278, 21.911111],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/2.jpg'],
                },
                {
                    "name": 'Fabrika „Porečje“',
                    "description": 'VRHUNSKI PROIZVOĐAČ RAKIJA - Kombinat "Porečje" osnovan 1960. godine od samog početka postao je poznat po proizvodima vrhunskog kvaliteta. Destilerija "Porečje" bazira nabavku i odabir svih voćnih vrsta prvenstveno sa teritorije Porečja, gde se i nalazi proizvodnja rakija. Destilerija „Porečje“ nastavlja utabanim putem proizvodnje vrhunskih rakija sa željom da svoje iskustvo u proizvodnji najkvalitetnijih rakija koje treba da upoznaju poštovaoci dobre kapljice kako u Srbiji tako i u čitavom svetu. Trivunova rakija, kao čuveni brend, nastala je na jugu Srbije, u podnožju planine Kukavice, sa jedinstvenim kanjonom reke Vučjanke koja je iznedrila bogatu ravnicu - POREČJE. Ta blagodna zemlja rađa najkvalitetnije voće koje se pretvaraju u vrhunske rakije. Kapaciteti 5000 litara dnevno.',
                    "short_description": 'VRHUNSKI PROIZVOĐAČ RAKIJA - Kombinat "Porečje" osnovan 1960. godine od samog početka postao je poznat po proizvodima vrhunskog kvaliteta. Destilerija "Porečje" bazira nabavku i odabir svih voćnih vrsta prvenstveno sa teritorije Porečja, gde se i nalazi proizvodnja rakija.',
                    "latlng": [42.87475, 21.907694],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/27.png'],
                },
                {
                    "name": 'Hram Svetog Velikomučenika Georgija',
                    "description": 'Crkva Svetog velikomučenika Georgija u Belom Potoku kod Leskovca je hram Srpske pravoslavne crkve. Crkva je 2015. godine sagrađena uz pomoć sredstava Slobodana Stojanovića iz Belog Potoka. Gradnja je trajala dve godine, a crkva je osvećena 6. maja 2014. godine.',
                    "short_description": 'Crkva Svetog velikomučenika Georgija u Belom Potoku kod Leskovca je hram Srpske pravoslavne crkve.',
                    "latlng": [42.885805, 21.914167],
                    "distance_radius": 50.5,
                    "pictures": [f'{server_route}/static/pictures/28.jpg'],
                },


            ],
            "preTourInformation": [
                "Udobne sportska obuća, odeća prema vremenskim uslovima",
                "Poneti vodu za piće.",
            ],
            "restStops": [
                {
                    "name": "Kafić kod fontane",
                    "description": "Kafić sa prelepim pogledom",
                    "latlng": [42.8511627, 21.9179207]
                },
            ],
        },
    }
    
    
    if tour_type == 'walking_1':
        tour = walking_1[language]
    elif tour_type == 'walking_2':
        tour = walking_2[language]
    elif tour_type == 'cycling_1':
        tour = cycling_1[language] #! kada se ubaci druga tura aktivirati ostale if blokove
    
    return jsonify(tour)


@app.route('/api/picture', methods=['GET'])
def api_picture():
    return app.send_static_file('pictures/3.1.jpg')
    
