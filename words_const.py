words_women = ['kobieta', 'ona', 'jej', 'dziewczyna', 'kobiecy', 'baba', 'dama'] 
words_man = ['mężczyzna', 'on', 'jego', 'męski', 'chłopiec', 'facet']

words_obywatel = ['obywatel', 'obywatelka', 'towarzysz', 'towarzyszka']

words_jews = [ 'żyd', 'żydówka', 'izraelita']

words_imigrants = ['imigrant', 'przesiedleniec', 'wysiedleniec', 'wysiedlony', 'przybysz']

words_others = ['Rosja', 'Rosjanin', 'Ruscy', 'Ukraina', 'Ukrainiec', 'Niemcy', 'Niemiec', 'Szwab', 'szkop', 'Arab', 'rosyjski', 'ukraiński', 'szwabski', 'niemiecki', 'arabski']

words_positive = ['inteligentny', 'mądry', 'uczciwy', 'pracowity', 'taktowny', 'rozmowny','niezawodny', 'skromny', 'zaradny', 'wytrwały', 'wybaczający', 'asertywny', 'towarzyski', 'metodyczny', 'idealistyczny', 'oszczędny', 'pomysłowy', 'marzycielski', 'doceniający', 'wszechstronny', 'refleksyjny','szczery', 'uczynny', 'ostrożny', 'dyskretny', 'przedsiębiorczy', 'opanowany', 'optymistyczny', 'pokojowy', 'rozważny', 'ufny', 'krzepki', 'tolerancyjny', 'realistyczny', 'racjonalny', 'dowcipny', 'wesoły', 'odważny', 'potulny', 'powściągliwy', 'zrelaksowany', 'przebiegły', 'sumienny', 'godny', 'zdrowy', 'czuły', 'energiczny', 'twardy', 'ostrożny', 'wymagający', 'zadowolony', 'entuzjastyczny', 'ambitny', 'czujny', 'dojrzały', 'czarujący', 'surowy', 'emocjonalny', 'łagodny', 'artystyczny', 'pospieszny', 'sympatyczny', 'cywilizowany', 'lojalny', 'umiarkowany', 'pomocny', 'delikatny', 'hojny', 'rzetelny', 'precyzyjny', 'spokojny', 'atrakcyjny', 'postępowy', 'stabilny', 'wrażliwy', 'inicjatywny', 'dokładny', 'logiczny', 'inteligentny', 'ciekawy', 'cichy', 'szybki', 'przyjazny', 'skuteczny', 'przyjemny', 'zorganizowany', 'rozsądny', 'zdolny',
 'aktywny', 'cierpliwy', 'praktyczny', 'poważny', 'wyrozumiały', 'odpowiedzialny', 'prosty', 'oryginalny', 'silny', 'zdecydowany', 'naturalny', 'miły']
 
word_neative = ['nieufny', 'kłótliwy', 'urażony', 'sarkastyczny', 'kapryśny', 'mściwy', 'wyrachowany', 'podstępny', 'impulsywny', 'nietolerancyjny', 'autokratyczny', 'zarozumiały', 'uległy', 'pesymistyczny', 'zrezygnowany', 'samolubny', 'niedojrzały', 'leniwy','infantylny',
 'przebiegły', 'cyniczny', 'nieodpowiedzialny', 'arogancki', 'chciwy', 'wstrętny', 'drażliwy', 'niepoważny', 'tchórzliwy', 'buntowniczy', 'nastrojowy', 'nieprzyjazny', 'nieporządny', 'chaotyczny', 'złośliwy', 'przesądny', 'hałaśliwy', 'nieracjonalny', 'nieżyczliwy', 'uprzedzony', 'lekkomyślny', 'uparty', 'sentymentalny', 'narzekający', 'niewzruszony', 'niestabilny', 'lękliwy', 'ponury', 'nieostrożny', 'niespokojny', 'spięty', 'podejrzliwy', 'niezadowolony', 'agresywny', 'bojaźliwy', 'niecierpliwy', 'niegrzeczny', 'sprytny', 'płytki', 'szorstki', 'okrutny', 'tępy', 'obojętny', 'głupi', 'wrogi', 'zagubiony', 'głośny', 'skomplikowany', 'chłodny', 'słaby', 'nerwowy', 'powolny', 'surowy', 'zimny']
 
words_competence = ['kompetentny', 'zaradny', 'dociekliwy', 'roztropny', 'pomysłowy', 'bystry', 'zdolny', 'refleksyjny', 'wnikliwy', 'intuicyjny',
 'rozsądny', 'analityczny', 'kreatywny', 'rozważny', 'mądry', 'genialny', 'logiczny', 'inteligentny', 'trafny', 'geniusz', 'leniwy']

words_appearance = ['ładny', 'atrakcyjny', 'pociągający', 'zmysłowy', 'zarumieniony', 'wspaniały', 'szczupły', 'łysy', 'atletyczny', 'modny', 'gruby', 'brzydki', 'muskularny', 'smukły', 'przystojny', 'zdrowy', 'słaby', 'chudy', 'ładny', 'piękny']

words_foreign = ['obcy', 'przebiegły', 'dziwaczny', 'barbarzyński', 'przerażający', 'podstępny', 'zwodniczy', 'chciwy', 'nienawistny', 'pogardliwy',
 'brutalny', 'potworny', 'wyrachowany', 'okrutny', 'nietolerancyjny', 'agresywny']

words_entities = {
    'obywatel': words_obywatel,
    'women': words_women,
    'man': words_man,
    'bothsexes': words_women + words_man,
    'jews': words_jews,
    'imigrants': words_imigrants,
    'others': words_others
}

words_descriptions = {
    'positive': words_positive,
    'negative' : word_neative,
    'competence': words_competence,
    'appearance': words_appearance,
    'foreign': words_foreign
}