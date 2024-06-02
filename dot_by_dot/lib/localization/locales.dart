import 'package:flutter_localization/flutter_localization.dart';

const List<MapLocale> LOCALES = [
  MapLocale("en", LocaleData.EN),
  MapLocale("sr", LocaleData.SR),
  MapLocale("mk", LocaleData.MK),
];

mixin LocaleData {
  static const String walking_1 = 'walking_1';
  static const String walking_2 = 'walking_2';
  static const String cycling_1 = 'cycling_1';
  static const String main_title = 'main_title';
  static const String main_more = 'main_more';
  static const String sidebar_home = 'sidebar_home';
  static const String sidebar_language = 'sidebar_language';
  static const String home_title = 'home_title';
  static const String home_vucje_about = 'home_vucje_about';
  static const String home_vucje_about_title = 'home_vucje_about_title';
  static const String home_vucje_about_extended = 'home_vucje_about_extended';
  static const String home_show_more = 'home_show_more';
  static const String home_show_less = 'home_show_less';
  static const String home_walking_1 = 'home_walking_1';
  static const String home_walking_2 = 'home_walking_2';
  static const String home_cycling_1 = 'home_cycling_1';
  static const String button_close = 'button_close';
  static const String home_vucje_eu_text_1 = 'home_vucje_eu_text_1';
  static const String home_vucje_eu_text_2 = 'home_vucje_eu_text_2';
  static const String tour_info_screen_description_1 =
      'tour_info_screen_description_1';
  static const String tour_info_screen_description_2 =
      'tour_info_screen_description_2';
  static const String tour_info_screen_description_3 =
      'tour_info_screen_description_3';
  static const String tour_info_screen_description_4 =
      'tour_info_screen_description_4';
  static const String tour_info_screen_tab_1 = 'tour_info_screen_tab_1';
  static const String tour_info_screen_tab_2 = 'tour_info_screen_tab_2';
  static const String tour_info_screen_tab_3 = 'tour_info_screen_tab_3';
  static const String tour_info_screen_start_tour =
      'tour_info_screen_start_tour';
  static const String body = 'body';

  static const Map<String, dynamic> EN = {
    walking_1:
        'walking_1.en', //! u main.dart routes: ima string koji se šalje na API pomoću koga se definiše jezik stringova
    walking_2:
        'walking_2.en', //! u main.dart routes: ima string koji se šalje na API pomoću koga se definiše jezik stringova
    cycling_1:
        'cycling_1.en', //! u main.dart routes: ima string koji se šalje na API pomoću koga se definiše jezik stringova
    main_title: 'Travel guide',
    main_more: 'More',
    sidebar_home: 'Home',
    sidebar_language: 'Language: ',
    home_title: 'Home',
    home_vucje_about:
        "Vučje is a town settlement in the Leskovac district with about 2,865 inhabitants according to the 2011 census. Until 1965, it was the seat of the municipality of Vučje, which consisted of many settlements. It is located about 17 km southwest of Leskovac and is the geographical center of the Porečje area, through which the river Vučjanka flows. It has a health center, police station, football club FC Vučje, primary and secondary schools. The population is predominantly Serbian.",
    home_vucje_about_title: 'More about Vučje',
    home_vucje_about_extended:
        '''Vučje is an urban settlement in the town of Leskovac in the Jablanički district. According to the 2011 census, there were 2,865 inhabitants.

Until 1965, this settlement was the seat of the municipality of Vučje, which consisted of settlements: Barje, Beli Potok, Brza, Bukova Glava, Bunuša (from which today's independent settlements of Bunuški Čifluk, Gornja Bunuša and Donja Bunuša arose), Crcavac, Čukljenik, Drvodelja, Gagince, Gorina, Gornja Jajina, Igrište, Kaludjerce, Kukulovce, Melovo, Miroševce, Nakrivanj, Oruglica, Palikuća, Presečina, Radonjica (then officially called Radonjice), Ravni Del, Slavujevce, Strojkovce, Šainovac, Todorovce, Veliko Trnjane, Vina, Vučje and Žabljane. After the abolition of the municipality, the entire area of the former municipality became part of the Leskovac municipality.

Geography
It is located approximately 17 km southwest of the town of Leskovac and is the geographical center of the Porečje area. The river Vučjanka flows through Vučje, after which the place got its name. On the river Vučjanka, a few kilometers above Vučje, there is a hydroelectric power plant from 1903 that is still working. Near Vučje was the medieval Zelen-grad. Not far from Vučje are the remains of Skobaljić town.

Vučje has a health center, police station, football club FC Vučje, etc. It has primary school "Bora Stanković" and secondary school "Svetozar Krstić Toza". This place is also the cultural center of the region, where young people from the surrounding villages come to have fun and socialize.

Demographics
There are 2,649 adults living in the Vučje settlement, and the average age of the population is 41.3 years (40.2 for men and 42.3 for women). There are 1049 households in the settlement, and the average number of members per household is 3.11.

This settlement is largely inhabited by Serbs (according to the 2002 census).''',
    home_show_more: 'Show more',
    home_show_less: 'Show less',
    home_walking_1: 'Walking tour',
    home_walking_2: 'Walking cardio tour',
    home_cycling_1: 'Cycling tour',
    button_close: 'Close',
    home_vucje_eu_text_1: 'This application is funded by the European Union',
    home_vucje_eu_text_2:
        'This application is funded by the European Union. The content is the sole responsibility of the Secondary School "Svetozar Krstić - Toza" from Vučje, SOU "Mitko Pendžukliski" from Kratov and Association "Limitless" from Belgrade, and does not necessarily reflect the views of the European Union',
    tour_info_screen_description_1: 'Route length: %a',
    tour_info_screen_description_2: 'Duration: %a',
    tour_info_screen_description_3: 'Height difference: %a m',
    tour_info_screen_description_4: 'Weight: %a',
    tour_info_screen_tab_1: 'List of localities',
    tour_info_screen_tab_2: 'Before you go',
    tour_info_screen_tab_3: 'Places to rest',
    tour_info_screen_start_tour: 'START TOUR',
    body: 'Some random text.',
  };

  static const Map<String, dynamic> SR = {
    walking_1:
        'walking_1.sr', //! u main.dart routes: ima string koji se salje na API pomoću koga se definiše jezik stringova
    walking_2:
        'walking_2.sr', //! u main.dart routes: ima string koji se salje na API pomoću koga se definiše jezik stringova
    cycling_1:
        'cycling_1.sr', //! u main.dart routes: ima string koji se salje na API pomoću koga se definiše jezik stringova
    main_title: 'Turistički vodič',
    main_more: 'Opširnije',
    sidebar_home: 'Pocetna',
    sidebar_language: 'Jezik: ',
    home_title: 'Početna',
    home_vucje_about:
        "Vučje je gradsko naselje u okrugu Leskovca sa oko 2.865 stanovnika prema popisu iz 2011. Do 1965. bilo je sedište opštine Vučje koju su činila mnoga naseljena mesta. Nalazi se oko 17 km jugozapadno od Leskovca i geografski je centar područja Porečje, kroz koje protiče reka Vučjanka. Ima dom zdravlja, policijsku stanicu, fudbalski klub FK Vučje, osnovnu i srednju školu. Stanovništvo je pretežno srpsko.",
    home_vucje_about_title: 'Opširnije o mestu Vučje',
    home_vucje_about_extended:
        '''Vučje je gradsko naseljeno mesto grada Leskovca u Jablaničkom okrugu. Prema popisu iz 2011. bilo je 2.865 stanovnika.

Do 1965. godine je ovo naselje bilo sedište opštine Vučje, koju su činila naseljena mesta: Barje, Beli Potok, Brza, Bukova Glava, Bunuša (od koje su nastala današnja samostalna naseljena mesta Bunuški Čifluk, Gornja Bunuša i Donja Bunuša), Crcavac, Čukljenik, Drvodelja, Gagince, Gorina, Gornja Jajina, Igrište, Kaluđerce, Kukulovce, Melovo, Miroševce, Nakrivanj, Oruglica, Palikuća, Presečina, Radonjica (tada pod zvaničnim nazivom Radonjice), Ravni Del, Slavujevce, Strojkovce, Šainovac, Todorovce, Veliko Trnjane, Vina, Vučje i Žabljane. Posle ukidanja opštine područje bivše opštine je u celini ušlo u sastav opštine Leskovac.

Geografija
Nalazi se približno 17 km jugozapadno od grada Leskovca i geografski je centar područja Porečje. Kroz Vučje protiče reka Vučjanka po kojoj je mesto dobilo ime. Na reci Vučjanki, nekoliko kilometara iznad Vučja, nalazi se hidrocentrala iz 1903. godine koja još uvek radi. U blizini Vučja nalazio se srednjovekovni Zelen-grad. Nedaleko od Vučja nalaze se i ostaci Skobaljić grada.

Vučje ima dom zdravlja, policijsku stanicu, fudbalski klub FK Vučje itd. Ima osnovnu školu „Bora Stanković“ i srednju školu „Svetozar Krstić Toza“. Ovo mesto je i kulturno središte kraja, a u njega dolaze mladi iz okolnih sela da se zabavljaju i druže.

Demografija
U naselju Vučje živi 2649 punoletnih stanovnika, a prosečna starost stanovništva iznosi 41,3 godina (40,2 kod muškaraca i 42,3 kod žena). U naselju ima 1049 domaćinstava, a prosečan broj članova po domaćinstvu je 3,11.

Ovo naselje je velikim delom naseljeno Srbima (prema popisu iz 2002. godine).''',
    home_show_more: 'Prikaži više',
    home_show_less: 'Prikaži manje',
    home_walking_1: 'Pešačka tura',
    home_walking_2: 'Pešačka kardio tura',
    home_cycling_1: 'Biciklistička tura',
    button_close: 'Zatvori',
    home_vucje_eu_text_1: 'Ovu aplikaciju finansira Evropska unija',
    home_vucje_eu_text_2:
        'Ova aplikacija je finansirana od strane Evropske unije. Sadržaj je isključiva odgovornost Srednje škole „Svetozar Krstić – Toza“ iz Vučja, SOU „Mitko Pendžukliski“ iz Kratova i Udruženja "Limitless" iz Beograda, i ne odražava nužno stavove Evropske unije',
    tour_info_screen_description_1: 'Dužina rute: %a',
    tour_info_screen_description_2: 'Trajanje: %a',
    tour_info_screen_description_3: 'Visinka razlika: %a m',
    tour_info_screen_description_4: 'Težina: %a',
    tour_info_screen_tab_1: 'Lista lokacija',
    tour_info_screen_tab_2: 'Pre nego što krenete',
    tour_info_screen_tab_3: 'Mesta za predah',
    tour_info_screen_start_tour: 'POKRENI TURU',
    body: 'Neki nasumični tekst.',
  };
  static const Map<String, dynamic> MK = {
    walking_1:
        'walking_1.mk', //! u main.dart routes: ima string koji se salje na API pomoću koga se definiše jezik stringova
    walking_2:
        'walking_2.mk', //! u main.dart routes: ima string koji se salje na API pomoću koga se definiše jezik stringova
    cycling_1:
        'cycling_1.mk', //! u main.dart routes: ima string koji se salje na API pomoću koga se definiše jezik stringova
    main_title: 'Турски водич',
    main_more: 'Opširnije',
    sidebar_home: 'Поопширно',
    sidebar_language: 'Јазик: ',
    home_title: 'Почетна',
    home_vucje_about:
        "Vučje je gradsko naselje u okrugu Leskovca sa oko 2.865 stanovnika prema popisu iz 2011. Do 1965. bilo je sedište opštine Vučje koju su činila mnoga naseljena mesta. Nalazi se oko 17 km jugozapadno od Leskovca i geografski je centar područja Porečje, kroz koje protiče reka Vučjanka. Ima dom zdravlja, policijsku stanicu, fudbalski klub FK Vučje, osnovnu i srednju školu. Stanovništvo je pretežno srpsko.",
    home_vucje_about_title: 'Opširnije o mestu Vučje',
    home_vucje_about_extended:
        '''Vučje je gradsko naseljeno mesto grada Leskovca u Jablaničkom okrugu. Prema popisu iz 2011. bilo je 2.865 stanovnika.

Do 1965. godine je ovo naselje bilo sedište opštine Vučje, koju su činila naseljena mesta: Barje, Beli Potok, Brza, Bukova Glava, Bunuša (od koje su nastala današnja samostalna naseljena mesta Bunuški Čifluk, Gornja Bunuša i Donja Bunuša), Crcavac, Čukljenik, Drvodelja, Gagince, Gorina, Gornja Jajina, Igrište, Kaluđerce, Kukulovce, Melovo, Miroševce, Nakrivanj, Oruglica, Palikuća, Presečina, Radonjica (tada pod zvaničnim nazivom Radonjice), Ravni Del, Slavujevce, Strojkovce, Šainovac, Todorovce, Veliko Trnjane, Vina, Vučje i Žabljane. Posle ukidanja opštine područje bivše opštine je u celini ušlo u sastav opštine Leskovac.

Geografija
Nalazi se približno 17 km jugozapadno od grada Leskovca i geografski je centar područja Porečje. Kroz Vučje protiče reka Vučjanka po kojoj je mesto dobilo ime. Na reci Vučjanki, nekoliko kilometara iznad Vučja, nalazi se hidrocentrala iz 1903. godine koja još uvek radi. U blizini Vučja nalazio se srednjovekovni Zelen-grad. Nedaleko od Vučja nalaze se i ostaci Skobaljić grada.

Vučje ima dom zdravlja, policijsku stanicu, fudbalski klub FK Vučje itd. Ima osnovnu školu „Bora Stanković“ i srednju školu „Svetozar Krstić Toza“. Ovo mesto je i kulturno središte kraja, a u njega dolaze mladi iz okolnih sela da se zabavljaju i druže.

Demografija
U naselju Vučje živi 2649 punoletnih stanovnika, a prosečna starost stanovništva iznosi 41,3 godina (40,2 kod muškaraca i 42,3 kod žena). U naselju ima 1049 domaćinstava, a prosečan broj članova po domaćinstvu je 3,11.

Ovo naselje je velikim delom naseljeno Srbima (prema popisu iz 2002. godine).''',
    home_show_more: 'Покажи повеќе',
    home_show_less: 'Прикажи помалку',
    home_walking_1: 'Pešačka tura',
    home_walking_2: 'Pešačka kardio tura',
    home_cycling_1: 'Biciklistička tura',
    button_close: 'Затвори',
    home_vucje_eu_text_1: 'Оваа апликација ја финансира Европската унија',
    home_vucje_eu_text_2:
        'Оваа апликација е финансирана од страна на Европската унија. Содржината е исклучива одговорност на Средното училиште „Светозар Крстиќ – Тоза“ од Вучја, СОУ „Митко Пенџуклиски“ од Кратово и Здружението "Limitless" од Белград, и не нуди задолжително гледишта на Европската унија.',
    tour_info_screen_description_1: 'Должина на рутата: %a',
    tour_info_screen_description_2: 'Трајање: %a',
    tour_info_screen_description_3: 'Висинска разлика: %a m',
    tour_info_screen_description_4: 'Тежина: %a',
    tour_info_screen_tab_1: 'Листа локации',
    tour_info_screen_tab_2: 'Пред да почнете',
    tour_info_screen_tab_3: 'Места за одмор',
    tour_info_screen_start_tour: 'ЗАПОЧНИ ОБИКОЛКА',
    body: 'Neki nasumični tekst.',
  };
}
