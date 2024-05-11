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
