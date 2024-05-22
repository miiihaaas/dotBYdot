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
                    "distance_radius": 30.5
                },
                {
                    "name": 'Hostel of the Svetozar Krstić secondary school - Toza',
                    "description": 'The hostel you see is an outpost of the Secondary School "Svetozar Krstić - Toza" from Vučje. It used to be a restaurant where students only had practice. Today, it is the first student hostel that operates within the school enterprise founded by the school. The renovation of the school hostel was helped by the City of Leskovac, while funds for the complete equipment of the hostel were provided by the European Union through the IPA II Cross-Border Cooperation Program of Serbia and North Macedonia. In Kratovo, North Macedonia, there is also a student hostel within the brother school "Mitko Penđuklijski".',
                    "short_description": 'The hostel of the secondary school Svetozar Krstić - Toza is an outpost of the school from Vučje, a former restaurant, now the first student hostel, renovated with the help of the City of Leskovac and funds from the European Union.',
                    "latlng": [42.867278, 21.911111],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Villa Teokarević',
                    "description": 'The work of the architect Grigori Ivanović Samojlov, the villa of the Teokarević family was built in 1935 and was initially used to receive prominent clients, and later became the home of Lazar Teokarević.',
                    "short_description": 'Villa Teokarević is the work of architect Grigori Ivanović Samojlov, built in 1935, used for receiving clients, later the home of Lazar Teokarević.',
                    "latlng": [42.866989, 21.910972],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Nikola Tesla Park',
                    "description": 'The Nikola Tesla Park is dedicated to the Serbian scientist who in 1903 helped start a hydroelectric plant in Vucje that still produces electricity today.',
                    "short_description": 'The Nikola Tesla Park is dedicated to the Serbian scientist who in 1903 helped start the hydroelectric power plant in Vucje, which is still functioning today.',
                    "latlng": [42.866833, 21.911139],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Memorial fountain',
                    "description": 'To the fallen fighters of Vucje and its surroundings in the National Liberation War 1941-1945. Collective of woolen fabric factory Vučje, Srez Leskovac. August 18, 1951. Vučje gave many lives in defense of freedom from the Nazi occupier. A memorial fountain to Serbian heroes was erected as a sign of memory.',
                    "short_description": 'The memorial fountain was built in memory of the fallen fighters of Vucje and its surroundings in the National Liberation War on August 18, 1951, as a tribute to the Serbian heroes who gave their lives in defense of freedom from the Nazis.',
                    "latlng": [42.866472, 21.911417],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Nikola Skobaljić - (photography)',
                    "description": 'Here you can take a photo next to the portrait of the medieval knight Nikola Skobaljić, the ruler of these regions in the 15th century. There is a legend about the Serbian duke Nikola Skobaljić, according to which he was not born, nor did he suffer like other, ordinary people. He was born to a girl from the village of Vina, who conceived him by eating a live scaby fish. He died because of the betrayal of his godmother, but the Turks did not capture him alive, but he flew away on his horse. He built a town on a hill above Vučje and that town bears his name, Skobaljić town. His well is located below the city. In the valley of the river Vučjanka, he built a church on the ruins of which a new church dedicated to St. was built in the 1930s. to Jovan. By further visiting the locations, you can find out more about the town of Skobaljić and about our hero Nikola.',
                    "short_description": 'Here you can photograph the portrait of the medieval knight Nikola Skobaljić, the ruler of these regions in the 15th century. Legend has it that he was not born, but conceived while his mother was eating a live sable fish. He was known for his bravery and betrayal of his godmother. He built the city that bears his name and built a church dedicated to St. to Jovan.',
                    "latlng": [42.866139, 21.911472],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Water mills',
                    "description": 'Vučjanka, as an extremely fast river, favored the creation of a large number of watermills, it is estimated that once there were more than 20 watermills along the Vučjanka river. Today, only 4 mills remain in operation. Mills are mainly used for grinding corn, which produces corn flour for human and animal consumption.',
                    "short_description": 'The Vučjanka River used to have over 20 watermills, but today only 4 are active. The watermills are used for grinding corn and producing corn flour for human and animal consumption.',
                    "latlng": [42.856887, 21.912933],
                    "distance_radius": 30.5
                },
                
                {
                    "name": 'Church of St. John the Baptist',
                    "description": "The church is dedicated to the birth of St. John the Baptist, it is a true gem of Orthodox places of worship in this area. It was built on the foundations of a church built in the 15th century by the knight Duke Nikola Skobaljić. Church of St. John the Baptist is the endowment of the Teokarević family, industrialists from Leskovac. The church was built in the period from 1932 to 1936. The church was designed by the architect Gligorije Ivanović Samojlov, as well as most of the buildings of the Teokarević family. The church was built with stone located at the foot of Kukavica mountain, whose slopes are around you. The church was built in the Moravian style with added bell towers, which are characteristic of churches and monasteries from the Nemanjić era. There is a record that testifies that during the construction of the church, a large number of skeletons belonging to Serbian soldiers from the Middle Ages were found. The skeletons that were found then amazed the finders, the skeletons were extremely large even for today's conditions. All the remains of Serbian soldiers were buried in a tomb inside the church gate and pine trees were planted next to them, which still exist today.",
                    "short_description": 'Church of St. John the Baptist is dedicated to the birth of this saint and is a treasure among Orthodox churches. It was built on the foundations of a medieval church, and was built between 1932 and 1936 in the Moravian style. During construction, skeletons of Serbian soldiers from the Middle Ages were found, and their remains were buried inside the church.',
                    "latlng": [42.855833, 21.915278],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Viewpoint (photograph)',
                    "description": "Now it's time to take a photo 🙂 - be careful not to get too close to the edge.",
                    "short_description": 'Now is a great time to take photos at the lookout - just be careful not to go too close to the edge!',
                    "latlng": [42.8542888, 21.9160698],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Excursion Vučjanka',
                    "description": 'You can rest here, and if you are here between July 20 and September 10, you can bring your bathing suit and cool off in the pool of the dam on the Vucjanka River.',
                    "short_description": 'The Vučjanka picnic area is an ideal place for a vacation, and during the summer months you can enjoy the swimming pool on the Vučjanka river.',
                    "latlng": [42.8535, 21.91625],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Vučje Hydropower Plant',
                    "description": 'The hydroelectric power plant began operating in 1903, with additional construction and improvements to give it its current appearance in 1930. Physicist Đorđe Stanojević, who was a professor and rector of Belgrade University, was responsible for starting and building the hydroelectric power plant. The Vučje hydroelectric power plant was built with the money of 168 shareholders of "Leskovac Electric Company", and according to its story, it was opened on the day of the liberation of Leskovac from the Turkish occupation, thus the small town in the south of Serbia Vučje and Leskovac with its factories (at that time) got electricity. The equipment, which includes the first transmission line in the Kingdom of Serbia - from Vučje to Leskovac (16 km) - was purchased for 152,700 dinars in gold from the German company "Siemens-Halske", and the construction was entrusted to Josif Granžan, originally from Veliki Bečkerek. The hydroelectric plant takes water from the river through a channel about a kilometer (980 m) long, partially carved into the high inaccessible rocks. This hydroelectric power plant was diverted during the Second World War. Today, the hydroelectric power plant produces from 5.2 to 6.5 million kilowatts per year.',
                    "short_description": 'The Vučje hydroelectric power plant began operating in 1903 and today produces between 5.2 and 6.5 million kilowatts per year. It was built with the help of 168 shareholders of "Leskovac Electric Company" and was an important source of electricity for Vučje and Leskovac, paving the way for the industrial development of these places.',
                    "latlng": [42.8525706, 21.9160508],
                    "distance_radius": 30.5
                },
                
                {
                    "name": 'Vučjanka river waterfall',
                    "description": 'The waterfall of the river Vučjanka is a work of the beautiful nature of this region. Words are redundant here, enjoy the scene.',
                    "short_description": 'The waterfall of the river Vučjanka is a beautiful natural phenomenon of this region. Enjoy his view.',
                    "latlng": [42.8513617, 21.9172287],
                    "distance_radius": 30.5
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
                    "latlng": [40.12345, 20.12345]
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
                    "distance_radius": 30.5
                },
                {
                    "name": 'Hostel srednje škole Svetozar Krstić - Toza',
                    "description": 'Hostel koji vidite je isturen objekat Srednje škole "Svetozar Krstić - Toza" iz Vučja. Nekada je to bio restoran u kojem su učenici imali samo praksu. Danas je to prvi učenički hostel koji posluje u okviru školskog preduzeća čiji je osnivač škola. Renoviranje školskog hostela pomogao je Grad Leskovac, dok je sredstva za kompletno opremanje hostela dala Evropska unija preko IPA II Programa prekogranične saradnje Srbije i Severne Makedonije. U Kratovu, Severnoj Makedoniji se takođe nalazi učenički hostel u okviru bratske škole "Mitko Penđuklijski".',
                    "short_description": 'Hostel srednje škole Svetozar Krstić - Toza je isturen objekat škole iz Vučja, nekadašnji restoran sada prvi učenički hostel, renoviran uz pomoć Grada Leskovca i sredstava Evropske unije.',
                    "latlng": [42.867278, 21.911111],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Vila Teokarević',
                    "description": 'Delo arhitekte Grigorija Ivanovića Samojlova, vila porodice Teokarević podignuta je 1935. godine i u početku je korišćena za prijem istaknutih klijenata, da bi kasnije bila dom Lazara Teokarevića.',
                    "short_description": 'Vila Teokarević je delo arhitekte Grigorija Ivanovića Samojlova, izgrađena 1935. godine, korišćena za prijem klijenata, kasnije dom Lazara Teokarevića.',
                    "latlng": [42.866989, 21.910972],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Park Nikole Tesle',
                    "description": 'Park Nikole Tesle posvećen je srpskom naučniku koji je 1903. godine u Vučju pomogao pokretanje hidroelektrane koja i danas proizvodi struju.',
                    "short_description": 'Park Nikole Tesle je posvećen srpskom naučniku koji je 1903. godine pomogao pokretanje hidroelektrane u Vučju, koja i danas funkcioniše.',
                    "latlng": [42.866833, 21.911139],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Spomen česma',
                    "description": 'Palim borcima Vučja i okoline u Narodnooslobodilačkom ratu 1941-1945. Kolektiv fabrike vunenih tkanina Vučje, Srez Leskovac. 18. avgust 1951. Vučje je dalo mnogo života u odbrani slobode od nacističkog okupatora. U znak sećanja podignuta je spomen česma srpskim junacima.',
                    "short_description": 'Spomen česma podignuta je u znak sećanja palim borcima Vučja i okoline u Narodnooslobodilačkom ratu, 18. avgusta 1951. godine, kao omaž srpskim junacima koji su dali živote u odbrani slobode od nacista.',
                    "latlng": [42.866472, 21.911417],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Nikola Skobaljić - (fotografisanje)',
                    "description": 'Ovde se možete fotografisati pored portreta srednjovekovnog viteza Nikole Skobaljića, vladara ovih krajeva u 15. veku. O srpskom vojvodi Nikoli Skobaljiću postoji legenda prema kojoj nije rođen, nije ni stradao kao drugi, obični ljudi. Rodila ga je devojka iz sela Vina, koja ga je začela jedući živu ribu skobalja. Nastradao je zbog izdaje svoje kume, ali ga Turci uhvatili živog nisu već je na svom konju odleteo. Podigao je grad na visu iznad Vučja i taj grad nosi njegovo ime, Skobaljić grad. Ispod grada se nalazi njegov kladenac. U dolini reke Vučjanke sazidao je crkvu na čijim je ruševinama 30-tih godina 20. veka podignuta nova crkva posvećena Sv. Jovanu. Daljim obilaskom lokacija možete saznati nešto više o Skobaljić gradu i o našem junaku Nikoli.',
                    "short_description": 'Ovde možete fotografisati portret srednjovekovnog viteza Nikole Skobaljića, vladara ovih krajeva u 15. veku. Legenda kaže da nije rođen, već je začet dok je njegova majka jela živu ribu skobalja. Bio je poznat po hrabrosti i izdaji svoje kume. Podigao je grad koji nosi njegovo ime i sagradio crkvu posvećenu Sv. Jovanu.',
                    "latlng": [42.866139, 21.911472],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Vodenice',
                    "description": 'Vučjanka kao izuzetno brza reka pogodovala je nastajanju velikog broja vodenica, procenjuje se da je nekada na toku reke Vučjanke bilo preko 20 vodenica. Danas je u radu ostalo svega 4 vodenice. Vodenice pretežno se koriste za mlevenje kukuruza čime se dobija kukuruzno brašno za ishranu ljudi i životinja.',
                    "short_description": 'Reka Vučjanka nekada je imala preko 20 vodenica, ali danas su aktivne samo 4. Vodenice se koriste za mlevenje kukuruza i proizvodnju kukuruznog brašna za ishranu ljudi i životinja.',
                    "latlng": [42.856887, 21.912933],
                    "distance_radius": 30.5
                },
                
                {
                    "name": 'Crkva Sv. Jovana Krstitelja',
                    "description": 'Crkva je posvećena rođenju svetog Jovana Krstitelja, predstavlja pravi dragulj pravoslavnih bogomolja na ovim prostorima. Podignuta je na temeljima crkve koju je u 15. veku podigao vitez, vojvoda Nikola Skobaljić. Crkva sv. Jovana Krstitelja je zadužbina porodice Teokarević, industrijalaca iz Leskovca. Crkva je podizana u periodu od 1932. do 1936. godine. Crkvu je projektovao arhitekta Gligorije Ivanović Samojlov, kao i većinu objekata porodice Teokarević. Crkva je izgrađena kamenom koji se nalazi u podnožju planine Kukavica čiji se obronci nalaze oko vas. Crkva je građena u Moravskom stilu sa pridodatim zvonicima koji su karakteristični za crkve i manastire iz doba Nemanjića. Postoji zapis koji svedoči da je prilikom izgradnje crkve pronađen veliki broj skeleta koji su pripadali srpskim vojnicima iz perioda srednjeg veka. Skeleti koji su tada pronađeni začudili su pronalazače, skeleti su bili izrazito veliki čak i za današnje prilike. Svi posmrtni ostaci srpskih vojnika su pothranjeni u grobnici unutar crkvene porte i pored njih su posađeni borovi koji i danas postoje.',
                    "short_description": 'Crkva Sv. Jovana Krstitelja je posvećena rođenju ovog svetitelja i predstavlja dragocenost među pravoslavnim bogomoljama. Podignuta je na temeljima srednjovekovne crkve, a izgrađena je u periodu od 1932. do 1936. godine u Moravskom stilu. Za vreme izgradnje pronađeni su skeleti srpskih vojnika iz srednjeg veka, a njihovi ostaci sahranjeni su unutar crkve.',
                    "latlng": [42.855833, 21.915278],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Vidikovac (fotografisanje)',
                    "description": 'Sada je vreme za fotografisanje 🙂 - vodite računa, nemojte se previše približavati ivici.',
                    "short_description": 'Sada je pravo vreme za fotografisanje na vidikovcu - samo pazite da ne idete previše blizu ivice!',
                    "latlng": [42.8542888, 21.9160698],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Izletište Vučjanka',
                    "description": 'Ovde se možete odmoriti, a ako ste ovde u periodu od 20. jula do 10. septembra možete poneti kupaći kostim i rashladiti se u bazenu brane na reci Vučjanki.',
                    "short_description": 'Izletište Vučjanka je idealno mesto za odmor, a tokom letnjih meseci možete uživati u bazenu na reci Vučjanki.',
                    "latlng": [42.8535, 21.91625],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Hidroelektrana Vučje',
                    "description": 'Hidroelektrana je počela sa radom 1903. godine, dodatnom izgradnjom i unapređenjem dobija današnji izgled 1930. godine. Za pokretanje i izgradnju hidroelektrane zadužen je fizičar Đorđe Stanojević, koji je bio profesor i rektor Beogradskog univerziteta. Hidroelektrana Vučje podignuta je novcem 168 akcionara "Leskovačkog električnog društva", i po svojoj priči otvorena na Dan oslobođenja Leskovca od turske okupacije, čime je mala varošica na jugu Srbije Vučje i Leskovac sa svojim fabrikama (onog vremena) dobilo struju. Oprema, u koju spada i prvi dalekovod u Kraljevini Srbiji - od Vučja do Leskovca (16 km) - kupljena je za 152.700 dinara u zlatu od nemačke firme "Simens-Halske", a gradnja je poverena Josifu Granžanu, poreklom iz Velikog Bečkereka. Hidroelektrana zahteva vodu iz reke kanalom dugim oko kilometar (980 m), delimično uklesanim u visoke nepristupačne stene. Na ovoj hidroelektrani je tokom Drugog svetskog rata izvršena diverzija. Hidroelektrana danas proizvodi od 5.2 do 6.5 miliona kilovata godišnje.',
                    "short_description": 'Hidroelektrana Vučje je počela sa radom 1903. godine i danas proizvodi između 5.2 i 6.5 miliona kilovata godišnje. Izgrađena je uz pomoć 168 akcionara "Leskovačkog električnog društva" i bila je važan izvor struje za Vučje i Leskovac, otvarajući put za industrijski razvoj ovih mesta.',
                    "latlng": [42.8525706, 21.9160508],
                    "distance_radius": 30.5
                },
                
                {
                    "name": 'Vodopad reke Vučjanke',
                    "description": 'Vodopad reke Vučjanke je delo prelepe prirode ovog kraja. Reči su ovde suvišne, uživajte u prizoru.',
                    "short_description": 'Vodopad reke Vučjanke predstavlja prelepi prirodni fenomen ovog kraja. Uživajte u njegovom pogledu.',
                    "latlng": [42.8513617, 21.9172287],
                    "distance_radius": 30.5
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
                    "latlng": [40.12345, 20.12345]
                },
            ],
        },
    }
    
    
    # walking_2 = {
    #     "en": {
    #         "name": "Walking cardio tour",
    #         "type": "Walking",
    #         "routeLenght": "5.06 km",
    #         "duration": "1h 25min",
    #         "elevationGain": 272.0,
    #         "difficultyLevel": "Heavy",
    #         "numberOfLocations": 12,
    #         "locations": [
    #             {}
    #         ]
    #     },
    #     "sr": {
    #         "name": "Pešačka kardio tura",
    #         "type": "Pešačka",
    #         "routeLenght": "5.06 km",
    #         "duration": "1h 25min",
    #         "elevationGain": 272.0,
    #         "difficultyLevel": "Teška",
    #         "numberOfLocations": 12,
    #         "locations": [
    #             {}
    #         ]
    #     },
    # }
    
    
    if tour_type == 'walking_1':
        tour = walking_1[language]
    # elif tour_type == 'walking_2':
    #     tour = walking_2 #! kada se ubaci druga tura aktivirati ostale if blokove
    
    return jsonify(tour)
    
    
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
                # {
                #     "name": "BGKKS",
                #     "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Treće mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                #     "short_description": "Treće mesto sa koje smo započeli testiranje",
                #     "latlng": [44.817574, 20.535312],
                #     "distance_radius": 22.5
                # },
                # {
                #     "name": "BGNPF",
                #     "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Četvrto mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                #     "short_description": "Četvrto mesto sa koje smo započeli testiranje",
                #     "latlng": [44.816916, 20.460592],
                #     "distance_radius": 10.5
                # },
                # {
                #     "name": "GMMČK",
                #     "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Drugo mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                #     "short_description": "Drugo mesto sa koje smo započeli testiranje",
                #     "latlng": [44.034661, 20.433998],
                #     "distance_radius": 10.5
                # },
                # {
                #     "name": "GMHCP",
                #     "description": "Ovo mesto služi za testiranje rada aplikacije i lokacije. Prvo mesto za koje sa kojeg smo započeli testiranja ovog tipa",
                #     "short_description": "Prvo mesto sa koje smo započeli testiranje",
                #     "latlng": [44.023905, 20.456093],
                #     "distance_radius": 10.5
                # },
                #! Vučje
                {
                    "name": "Fontana",
                    "description": 'Fontana "Ribar i hobotnica" je umetničko delo vajara Slavka Miletića iz 1939. godine. Fontana je postavljena kako bi ukrasila tadašnji kompleks tekstilne industrije, prema nacrtu arhitekte Samojlova. Sa leve strane se nalazio fabrički pogon za proizvodnju tekstila.',
                    "short_description": 'Fontana "RIBAR I HOBOTNICA" je umetničko delo vajara Slavka Miletića iz 1939. godine, postavljena kako bi ukrasila tadašnji kompleks tekstilne industrije.',
                    "latlng": [42.868972, 21.910444],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Hostel srednje škole Svetozar Krstić - Toza',
                    "description": 'Hostel koji vidite je isturen objekat Srednje škole "Svetozar Krstić - Toza" iz Vučja. Nekada je to bio restoran u kojem su učenici imali samo praksu. Danas je to prvi učenički hostel koji posluje u okviru školskog preduzeća čiji je osnivač škola. Renoviranje školskog hostela pomogao je Grad Leskovac, dok je sredstva za kompletno opremanje hostela dala Evropska unija preko IPA II Programa prekogranične saradnje Srbije i Severne Makedonije. U Kratovu, Severnoj Makedoniji se takođe nalazi učenički hostel u okviru bratske škole "Mitko Penđuklijski".',
                    "short_description": 'Hostel srednje škole Svetozar Krstić - Toza je isturen objekat škole iz Vučja, nekadašnji restoran sada prvi učenički hostel, renoviran uz pomoć Grada Leskovca i sredstava Evropske unije.',
                    "latlng": [42.867278, 21.911111],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Vila Teokarević',
                    "description": 'Delo arhitekte Grigorija Ivanovića Samojlova, vila porodice Teokarević podignuta je 1935. godine i u početku je korišćena za prijem istaknutih klijenata, da bi kasnije bila dom Lazara Teokarevića.',
                    "short_description": 'Vila Teokarević je delo arhitekte Grigorija Ivanovića Samojlova, izgrađena 1935. godine, korišćena za prijem klijenata, kasnije dom Lazara Teokarevića.',
                    "latlng": [42.866989, 21.910972],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Park Nikole Tesle',
                    "description": 'Park Nikole Tesle posvećen je srpskom naučniku koji je 1903. godine u Vučju pomogao pokretanje hidroelektrane koja i danas proizvodi struju.',
                    "short_description": 'Park Nikole Tesle je posvećen srpskom naučniku koji je 1903. godine pomogao pokretanje hidroelektrane u Vučju, koja i danas funkcioniše.',
                    "latlng": [42.866833, 21.911139],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Spomen česma',
                    "description": 'Palim borcima Vučja i okoline u Narodnooslobodilačkom ratu 1941-1945. Kolektiv fabrike vunenih tkanina Vučje, Srez Leskovac. 18. avgust 1951. Vučje je dalo mnogo života u odbrani slobode od nacističkog okupatora. U znak sećanja podignuta je spomen česma srpskim junacima.',
                    "short_description": 'Spomen česma podignuta je u znak sećanja palim borcima Vučja i okoline u Narodnooslobodilačkom ratu, 18. avgusta 1951. godine, kao omaž srpskim junacima koji su dali živote u odbrani slobode od nacista.',
                    "latlng": [42.866472, 21.911417],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Nikola Skobaljić - (fotografisanje)',
                    "description": 'Ovde se možete fotografisati pored portreta srednjovekovnog viteza Nikole Skobaljića, vladara ovih krajeva u 15. veku. O srpskom vojvodi Nikoli Skobaljiću postoji legenda prema kojoj nije rođen, nije ni stradao kao drugi, obični ljudi. Rodila ga je devojka iz sela Vina, koja ga je začela jedući živu ribu skobalja. Nastradao je zbog izdaje svoje kume, ali ga Turci uhvatili živog nisu već je na svom konju odleteo. Podigao je grad na visu iznad Vučja i taj grad nosi njegovo ime, Skobaljić grad. Ispod grada se nalazi njegov kladenac. U dolini reke Vučjanke sazidao je crkvu na čijim je ruševinama 30-tih godina 20. veka podignuta nova crkva posvećena Sv. Jovanu. Daljim obilaskom lokacija možete saznati nešto više o Skobaljić gradu i o našem junaku Nikoli.',
                    "short_description": 'Ovde možete fotografisati portret srednjovekovnog viteza Nikole Skobaljića, vladara ovih krajeva u 15. veku. Legenda kaže da nije rođen, već je začet dok je njegova majka jela živu ribu skobalja. Bio je poznat po hrabrosti i izdaji svoje kume. Podigao je grad koji nosi njegovo ime i sagradio crkvu posvećenu Sv. Jovanu.',
                    "latlng": [42.866139, 21.911472],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Vodenice',
                    "description": 'Vučjanka kao izuzetno brza reka pogodovala je nastajanju velikog broja vodenica, procenjuje se da je nekada na toku reke Vučjanke bilo preko 20 vodenica. Danas je u radu ostalo svega 4 vodenice. Vodenice pretežno se koriste za mlevenje kukuruza čime se dobija kukuruzno brašno za ishranu ljudi i životinja.',
                    "short_description": 'Reka Vučjanka nekada je imala preko 20 vodenica, ali danas su aktivne samo 4. Vodenice se koriste za mlevenje kukuruza i proizvodnju kukuruznog brašna za ishranu ljudi i životinja.',
                    "latlng": [42.856887, 21.912933],
                    "distance_radius": 30.5
                },
                
                {
                    "name": 'Crkva Sv. Jovana Krstitelja',
                    "description": 'Crkva je posvećena rođenju svetog Jovana Krstitelja, predstavlja pravi dragulj pravoslavnih bogomolja na ovim prostorima. Podignuta je na temeljima crkve koju je u 15. veku podigao vitez, vojvoda Nikola Skobaljić. Crkva sv. Jovana Krstitelja je zadužbina porodice Teokarević, industrijalaca iz Leskovca. Crkva je podizana u periodu od 1932. do 1936. godine. Crkvu je projektovao arhitekta Gligorije Ivanović Samojlov, kao i većinu objekata porodice Teokarević. Crkva je izgrađena kamenom koji se nalazi u podnožju planine Kukavica čiji se obronci nalaze oko vas. Crkva je građena u Moravskom stilu sa pridodatim zvonicima koji su karakteristični za crkve i manastire iz doba Nemanjića. Postoji zapis koji svedoči da je prilikom izgradnje crkve pronađen veliki broj skeleta koji su pripadali srpskim vojnicima iz perioda srednjeg veka. Skeleti koji su tada pronađeni začudili su pronalazače, skeleti su bili izrazito veliki čak i za današnje prilike. Svi posmrtni ostaci srpskih vojnika su pothranjeni u grobnici unutar crkvene porte i pored njih su posađeni borovi koji i danas postoje.',
                    "short_description": 'Crkva Sv. Jovana Krstitelja je posvećena rođenju ovog svetitelja i predstavlja dragocenost među pravoslavnim bogomoljama. Podignuta je na temeljima srednjovekovne crkve, a izgrađena je u periodu od 1932. do 1936. godine u Moravskom stilu. Za vreme izgradnje pronađeni su skeleti srpskih vojnika iz srednjeg veka, a njihovi ostaci sahranjeni su unutar crkve.',
                    "latlng": [42.855833, 21.915278],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Vidikovac (fotografisanje)',
                    "description": 'Sada je vreme za fotografisanje 🙂 - vodite računa, nemojte se previše približavati ivici.',
                    "short_description": 'Sada je pravo vreme za fotografisanje na vidikovcu - samo pazite da ne idete previše blizu ivice!',
                    "latlng": [42.8542888, 21.9160698],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Izletište Vučjanka',
                    "description": 'Ovde se možete odmoriti, a ako ste ovde u periodu od 20. jula do 10. septembra možete poneti kupaći kostim i rashladiti se u bazenu brane na reci Vučjanki.',
                    "short_description": 'Izletište Vučjanka je idealno mesto za odmor, a tokom letnjih meseci možete uživati u bazenu na reci Vučjanki.',
                    "latlng": [42.8535, 21.91625],
                    "distance_radius": 30.5
                },
                {
                    "name": 'Hidroelektrana Vučje',
                    "description": 'Hidroelektrana je počela sa radom 1903. godine, dodatnom izgradnjom i unapređenjem dobija današnji izgled 1930. godine. Za pokretanje i izgradnju hidroelektrane zadužen je fizičar Đorđe Stanojević, koji je bio profesor i rektor Beogradskog univerziteta. Hidroelektrana Vučje podignuta je novcem 168 akcionara "Leskovačkog električnog društva", i po svojoj priči otvorena na Dan oslobođenja Leskovca od turske okupacije, čime je mala varošica na jugu Srbije Vučje i Leskovac sa svojim fabrikama (onog vremena) dobilo struju. Oprema, u koju spada i prvi dalekovod u Kraljevini Srbiji - od Vučja do Leskovca (16 km) - kupljena je za 152.700 dinara u zlatu od nemačke firme "Simens-Halske", a gradnja je poverena Josifu Granžanu, poreklom iz Velikog Bečkereka. Hidroelektrana zahteva vodu iz reke kanalom dugim oko kilometar (980 m), delimično uklesanim u visoke nepristupačne stene. Na ovoj hidroelektrani je tokom Drugog svetskog rata izvršena diverzija. Hidroelektrana danas proizvodi od 5.2 do 6.5 miliona kilovata godišnje.',
                    "short_description": 'Hidroelektrana Vučje je počela sa radom 1903. godine i danas proizvodi između 5.2 i 6.5 miliona kilovata godišnje. Izgrađena je uz pomoć 168 akcionara "Leskovačkog električnog društva" i bila je važan izvor struje za Vučje i Leskovac, otvarajući put za industrijski razvoj ovih mesta.',
                    "latlng": [42.8525706, 21.9160508],
                    "distance_radius": 30.5
                },
                
                {
                    "name": 'Vodopad reke Vučjanke',
                    "description": 'Vodopad reke Vučjanke je delo prelepe prirode ovog kraja. Reči su ovde suvišne, uživajte u prizoru.',
                    "short_description": 'Vodopad reke Vučjanke predstavlja prelepi prirodni fenomen ovog kraja. Uživajte u njegovom pogledu.',
                    "latlng": [42.8513617, 21.9172287],
                    "distance_radius": 30.5
                },
                #! Kratovo
                # {
                #     "name": "Видиковец",
                #     "description": "Видиковецот е ново туристичко место во Кратово. Од него се отвора прекрасен панорамски поглед кон Кратово. Се гледа централното градско подрачје на Кратово со најзначајните културни споменици на градот како што се: кулите, мостовите, турскиот затвор, еврејската куќа, црквата Св. Јован Крстител, старите борови итн. Ова претставува место за уживање, релаксација и фотографирање.",
                #     "short_description": "Видиковецот во Кратово нуди прекрасен поглед на градот и неговите историски споменици, претставувајќи идеално место за релаксација и уживање во природата.",
                #     "latlng": [42.077047, 22.179709],
                #     "distance_radius": 10.5
                # },
                # {
                #     "name": "Рудно окно",
                #     "description": '''Целата историја на Кратово се поврзува со рударството, што се докажува со повеќе од 40 рудни окна и складишта за преработена руда – згура. Уште од пред римскиот период Кратово се споменува како богат рударски центар. Во време на Римскиот период Кратово бил рударско средиште во Североисточниот дел, а се експлоатирало олово, цинк, злато, сребро бакар и други руди. Од рудните производи се изработувале и монети. Така, подоцна од Византискиот период пронајдени се монети, меѓу кои и златни на византиските императори Анастасие (491-519г), Јустин I (518 – 527), Јустинијан (527 – 565). Во подоцнежниот период со Кратово управувале повеќе заслужни феудалци коишто управувале со рудниците во Целата Кратовска област. Најголем процут има доживеано во XIV век и тоа поради рудните богатства и тоа злато и оттука градот напредува. Деспот Јован Оливер (1336 – 1355) – важна историска личност од средновековието. Освен што ги искористувал рудниците имал свој дворец тука и е ктитор на Лесновскиот манастир. Еден од попознатите е Јован Оливер (1336 – 1355) – очув на цар Душан - како деспот интензивно ги користел кратовските рудни богатства, преку старите но и отворајќи нови рудни окна. Се обезбедувале големи приход. За ова помогнале и познатите германски рудари Саси кои биле доселени тука со цел поголем развој на рударството. Покрај рудните окна имало и Топилница за руда и Леарница (ковачница) за пари. Развиена била и трговијата, а со неа раководеле Дубровчаните.''',
                #     "short_description": '''Кратово, средиште на рударството векови назад, прославено по своите рудници и богатства, од кои се изработувале и монети, со важни историски личности како деспот Јован Оливер.''',
                #     "latlng": [42.077990, 22.179178],
                #     "distance_radius": 20.5
                # },
                # {
                #     "name": "Ковач",
                #     "description": "Познато е дека Општина Кратово, освен по богата историја е град познат и по занаетчиството. Еден од занаетите кој што бил многу развиен во минатото, а не се среќава веќе често денес е всушност ковачкиот занает. Во центарот на градот се наоѓа една од последните работилници во кој ковачот Мише се уште ги обработува металите за да направи алат кој се користи во кратовското секојдневие. Занаетот го наследил од својот татко и се уште работи во неговата работилница.",
                #     "short_description": 'Кратово, освен по богатата историја, се истакнува и по ковачкиот занает, што се прекува во последната работилница во центарот на градот, каде што ковачот Мише ги обработува металите како наследство од својот татко.',
                #     "latlng": [42.077990, 22.179230],
                #     "distance_radius": 20.5
                # },
                # {
                #     "name": "Спомен костурница во чест на паднатите борци на НОБ",
                #     "description": "Спомен костурница на НОБ во Кратово е место каде се чуваат останките на храбрите борци кои се бореле за слободата на Македонија за време на Втората светска војна, а потекнувале од Кратовско. На посебни мермерни плочи изгравирани се нивните имиња, како и годините на раѓање и смрт. Тоа е важен споменик и место на почит кон нивната жртва и храброст. Луѓето го посетуваат за да се потсетат на бурната и тешка македонска историја и на тие кои се бореле за нашата слобода. Главните посети се прават на 25 април (првото ослободување на Кратово) и 6 Септември (конечното ослободување на Кратово).",
                #     "short_description": 'Спомен костурницата на НОБ во Кратово е место на почит кон храбрите борци од Кратовско од Втората светска војна.',
                #     "latlng": [42.077109, 22.179230],
                #     "distance_radius": 100.5
                # },
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
