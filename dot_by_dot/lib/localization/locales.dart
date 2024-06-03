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
  static const String home_kratovo_about_extended =
      'home_kratovo_about_extended';
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
    home_kratovo_about_extended:
        '''Kratovo — a city in Northeastern Macedonia, located in the throat of an extinct volcano. It represents one of the oldest cities in Macedonia and the Balkans.
There are several examples of the origin of the name of the city of Kratovo. The name Kratovo comes from the location of the city, which lies on a volcanic base, i.e. a volcanic crater. According to tradition, the city got its name from the words "kirat-ova", after the name of the fortress on the banks of the Kratovska Reka, demolished by the Ottomans. In the Byzantine era, the city was called "Koritos" or "Koriton".''',
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
    home_kratovo_about_extended:
        '''Kratovo — grad u severoistočnoj Makedoniji, smešten u grlu ugašenog vulkana. Predstavlja jedan od najstarijih gradova u Makedoniji i na Balkanu.
Postoji nekoliko primera porekla imena grada Kratova. Naziv Kratovo potiče od lokacije grada koji leži na vulkanskoj podlozi, odnosno vulkanskom krateru. Po predanju, grad je dobio ime po reči "kirat-ova", po imenu tvrđave na obali Kratovske reke, koju su srušile Osmanlije. U vizantijsko doba grad se zvao „Koritos“ ili „Koriton“.''',
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
    sidebar_home: 'Почетна',
    sidebar_language: 'Јазик: ',
    home_title: 'Почетна',
    home_vucje_about: "edit",
    home_vucje_about_title: 'edit',
    home_kratovo_about_extended:
        '''Кратово — град во Североисточна Македонија, сместен во грлото на изгаснат вулкан. Претставува еден од најстарите градови во Македонија и на Балканот.
Постојат повеќе примери за изворот на името на градот Кратово. Името Кратово доаѓа од местоположбата на градот, кој лежи на вулканска подлога, односно вулкански кратер. Според преданието, градот го добил името по зборовите „кират-ова“, по името на тврдината на бреговите на Кратовска Река, урната од Османлиите. Во времето на Византија, градот е наречен „Коритос“ или „Коритон“.''',
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
