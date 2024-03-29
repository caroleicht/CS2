import matplotlib.pyplot as plt             # import graphing software
import seaborn                              # import graphing software

def cleanse_file(file):
### function takes file, reads it, makes all letters lowercase and removes endline characters ('\n')
### input: file - opened shakespear file
### output: list - list of lines in file, all lowercase and no ('\n')

    file = file.readlines()                 # list, reads file, list of strings
    for line in file:                       # goes through each line of file
        line = line.lower()                 # str, all lowercase letters

    list = []                               # list, empty list
    for x in file:                          # goes through each line in file
        list.append(x.replace('\n', ''))    # list, takes out '\n'

    return list                             # returns list

def make_dict(file):
### function makes dictionary from file thats gone through cleanse_file() function
### input: file - list thats gone through cleanse_file() function
### output: d - dictionary made from file

    d = dict()                              # dict, empty dictionary

    for line in file:                       # goes through each line in file
        line = line.split(' ')              # list, list of words in line
        for word in line:                   # goes through each word in line
            if word not in d:               # bool, if word isnt in dictionary
                d[word] = 1                 # int, 1, value for dictionary
            else:                           # bool, if word is in dictionary
                d[word] = d[word] + 1       # int, ex: 2, value for dictionary

    return d                                # return d, dictionary

def romeo_cleanse(dict):
### function takes specific words out of dictionary
### input: dict - dictionary made from romeo & juliet file in make_dict() function
### output: dict - dictionary after words have been removed

    del dict['']
    del dict['two']
    del dict['with']
    del dict['an']
    del dict['three']
    del dict['both']
    del dict['chor']
    del dict['alike']
    del dict['fair']
    del dict['where']
    del dict['lay']
    del dict['from']
    del dict['scene']
    del dict['break']
    del dict['new']
    del dict['makes']
    del dict['hands']
    del dict['these']
    del dict['pair']
    del dict['take']
    del dict['their']
    del dict['be']
    del dict['bring']
    del dict['lie-']
    del dict['figure']
    del dict['known']
    del dict['whiles']
    del dict['statue']
    del dict['demand']
    del dict['jointure']
    del dict['brace']
    del dict['winking']
    del dict['scourge']
    del dict['montage']
    del dict['therewithal']
    del dict['pothecary']
    del dict['writes']
    del dict["friar's"]
    del dict['did']
    del dict['alo']
    del dict['departed']
    del dict['brought']
    del dict['severest']
    del dict['rigour']
    del dict["sacrific'd"]
    del dict['miscarried']
    del dict['privy']
    del dict['entreated']
    del dict['wakes']
    del dict['awaking']
    del dict['conveniently']
    del dict['closely']
    del dict['waking']
    del dict['prefixed']
    del dict["return'd"]
    del dict['yesternight']
    del dict['accident']
    del dict['cease']
    del dict['dramatis']
    del dict['personae']
    del dict['chorus']
    del dict['escalus']
    del dict['verona']
    del dict['count']
    del dict['paris']
    del dict['young']
    del dict['kinsman']
    del dict['montague']
    del dict['heads']
    del dict['houses']
    del dict['variance']
    del dict['each']
    del dict['other']
    del dict['capulet']
    del dict['old']
    del dict['man']
    del dict['family']
    del dict['son']
    del dict['tybalt']
    del dict['nephew']
    del dict['lady']
    del dict['mercutio']
    del dict['benvolio']
    del dict['friar']
    del dict['franciscan']
    del dict['abram']
    del dict['pages']
    del dict['guards']
    del dict['watchmen']
    del dict['attendants']
    del dict['scene--verona']
    del dict['households']
    del dict['dignity']
    del dict['grudge']
    del dict['unclean']
    del dict['loins']
    del dict['foes']
    del dict["star-cross'd"]
    del dict["misadventur'd"]
    del dict['overthrows']
    del dict['passage']
    del dict["death-mark'd"]
    del dict['my']
    del dict['that']
    del dict['is']
    del dict['you']
    del dict['thou']
    del dict['me']
    del dict['not']
    del dict['this']
    del dict['it']
    del dict['for']
    del dict['but']
    del dict['thy']
    del dict['what']
    del dict['rom']
    del dict['as']
    del dict['her']
    del dict['will']
    del dict['o']
    del dict['so']
    del dict['nurse']
    del dict['thee']
    del dict['his']
    del dict['have']
    del dict['he']
    del dict['jul']
    del dict['she']
    del dict['shall']
    del dict['by']
    del dict['no']
    del dict['him']
    del dict['come']
    del dict['all']
    del dict['do']
    del dict['then']
    del dict['if']
    del dict['good']
    del dict['enter']
    del dict['here']
    del dict['now']
    del dict['go']
    del dict['on']
    del dict["i'll"]
    del dict['or']
    del dict['night']
    del dict['more']
    del dict['there']
    del dict['hath']
    del dict['ben']
    del dict['which']
    del dict['mer']
    del dict['one']
    del dict['how']
    del dict['am']
    del dict['well']
    del dict['they']
    del dict['too']
    del dict['some']
    del dict['would']
    del dict['sir']
    del dict['up']
    del dict['cap']
    del dict['say']
    del dict['when']
    del dict['out']
    del dict['was']
    del dict['should']
    del dict['than']
    del dict['yet']
    del dict['may']
    del dict['give']
    del dict['doth']
    del dict['such']
    del dict['tell']
    del dict['day']
    del dict['let']
    del dict['upon']
    del dict['them']
    del dict["'tis"]
    del dict['like']
    del dict['make']
    del dict['can']
    del dict['must']
    del dict['why']
    del dict['much']
    del dict['see']
    del dict['were']
    del dict['know']
    del dict['sweet']
    del dict['gone']
    del dict['who']
    del dict['time']
    del dict['look']
    del dict['us']
    del dict['mine']
    del dict['back']
    del dict['wilt']
    del dict['hast']
    del dict['light']
    del dict['speak']
    del dict['house']
    del dict['eyes']
    del dict['hence']
    del dict['stay']
    del dict['word']
    del dict['dear']
    del dict['exeunt']
    del dict['again']
    del dict['comes']
    del dict['stand']
    del dict['hand']
    del dict['very']
    del dict['true']
    del dict['being']
    del dict['ay']
    del dict['find']
    del dict['name']
    del dict['par']
    del dict['bed']
    del dict['call']
    del dict['part']
    del dict['away']
    del dict['therefore']
    del dict['i']
    del dict['face']
    del dict['bid']
    del dict['till']
    del dict['hear']
    del dict['cannot']
    del dict['think']
    del dict['men']
    del dict['nor']
    del dict['before']
    del dict['ere']
    del dict['made']
    del dict['nay']
    del dict['been']
    del dict['samp']
    del dict['watch']
    del dict['had']
    del dict['exit']
    del dict['county']
    del dict["romeo's"]
    del dict['down']
    del dict['help']
    del dict['eye']
    del dict['never']
    del dict['serv']
    del dict['ah']
    del dict['cell']
    del dict['poor']
    del dict['own']
    del dict['early']
    del dict['tyb']
    del dict['could']
    del dict['lips']
    del dict['most']
    del dict['hour']
    del dict['rest']
    del dict['hold']
    del dict['long']
    del dict['keep']
    del dict['put']
    del dict['any']
    del dict['friend']
    del dict['news']
    del dict['to-morrow']
    del dict['to-night']
    del dict['none']
    del dict['world']
    del dict['child']
    del dict['said']
    del dict['dost']
    del dict['sun']
    del dict['those']
    del dict['myself']
    del dict['greg']
    del dict['whose']
    del dict['mus']
    del dict['thursday']
    del dict['haste']
    del dict['breath']
    del dict['joy']
    del dict['use']
    del dict['boy']
    del dict['gentleman']
    del dict['fall']
    del dict['same']
    del dict['get']
    del dict['a']
    del dict['thine']
    del dict['still']
    del dict['many']
    del dict['nothing']
    del dict['head']
    del dict['lives']
    del dict['mantua']
    del dict['daughter']
    del dict['peter']
    del dict['letter']
    del dict['send']
    del dict['little']
    del dict['woe']
    del dict['soul']
    del dict['within']
    del dict['leave']
    del dict['else']
    del dict['without']
    del dict['cousin']
    del dict['soon']
    del dict['came']
    del dict['ho']
    del dict['run']
    del dict['forth']
    del dict['shame']
    del dict['sin']
    del dict['hither']
    del dict['late']
    del dict['thing']
    del dict['best']
    del dict["capulet's"]
    del dict['wit']
    del dict['ill']
    del dict["she's"]
    del dict['sleep']
    del dict['gentle']
    del dict['happy']
    del dict['about']
    del dict['hate']
    del dict['talk']
    del dict['bear']
    del dict['turn']
    del dict['ever']
    del dict['place']
    del dict['full']
    del dict['alack']
    del dict['pale']
    del dict['another']
    del dict['every']
    del dict['warrant']
    del dict['since']
    del dict['ye']
    del dict['though']
    del dict['even']
    del dict['years']
    del dict["o'er"]
    del dict["he's"]
    del dict["love's"]
    del dict['beauty']
    del dict['shalt']
    del dict['better']
    del dict['law']
    del dict['show']
    del dict['quarrel']
    del dict['draw']
    del dict['gentlemen']
    del dict['pet']
    del dict['church']
    del dict['tongue']
    del dict['pardon']
    del dict['answer']
    del dict['says']
    del dict['madam']
    del dict['married']
    del dict['husband']
    del dict['wife']
    del dict['romeo']
    del dict['mother']
    del dict['father']
    del dict['farewell']
    del dict['marriage']
    del dict['juliet']

    return dict                   # return dict, dictionary with words removed

def macbeth_cleanse(dict):
### function takes specific words out of dictionary
### input: dict - dictionary made from macbeth file in make_dict() function
### output: dict - dictionary after words have been removed

    del dict['']
    del dict['two']
    del dict['with']
    del dict['an']
    del dict['three']
    del dict['both']
    del dict['alike']
    del dict['where']
    del dict['lay']
    del dict['from']
    del dict['new']
    del dict['makes']
    del dict['hands']
    del dict['these']
    del dict['take']
    del dict['their']
    del dict['be']
    del dict['bring']
    del dict['known']
    del dict['whiles']
    del dict['demand']
    del dict['writes']
    del dict['did']
    del dict['brought']
    del dict['wakes']
    del dict["return'd"]
    del dict['cease']
    del dict['young']
    del dict['kinsman']
    del dict['heads']
    del dict['houses']
    del dict['each']
    del dict['other']
    del dict['old']
    del dict['man']
    del dict['son']
    del dict['lady']
    del dict['attendants']
    del dict['dignity']
    del dict['foes']
    del dict['passage']
    del dict['my']
    del dict['that']
    del dict['is']
    del dict['you']
    del dict['thou']
    del dict['me']
    del dict['not']
    del dict['this']
    del dict['it']
    del dict['for']
    del dict['but']
    del dict['thy']
    del dict['what']
    del dict['as']
    del dict['her']
    del dict['will']
    del dict['o']
    del dict['so']
    del dict['thee']
    del dict['his']
    del dict['he']
    del dict['she']
    del dict['shall']
    del dict['by']
    del dict['no']
    del dict['him']
    del dict['come']
    del dict['all']
    del dict['do']
    del dict['then']
    del dict['if']
    del dict['good']
    del dict['enter']
    del dict['here']
    del dict['now']
    del dict['go']
    del dict['on']
    del dict['or']
    del dict['night']
    del dict['more']
    del dict['there']
    del dict['hath']
    del dict['which']
    del dict['one']
    del dict['how']
    del dict['am']
    del dict['well']
    del dict['they']
    del dict['too']
    del dict['some']
    del dict['would']
    del dict['sir']
    del dict['cap']
    del dict['say']
    del dict['when']
    del dict['out']
    del dict['was']
    del dict['should']
    del dict['than']
    del dict['yet']
    del dict['may']
    del dict['doth']
    del dict['such']
    del dict['tell']
    del dict['day']
    del dict['let']
    del dict['them']
    del dict["'tis"]
    del dict['like']
    del dict['make']
    del dict['can']
    del dict['must']
    del dict['why']
    del dict['much']
    del dict['see']
    del dict['were']
    del dict['know']
    del dict['sweet']
    del dict['gone']
    del dict['who']
    del dict['time']
    del dict['mine']
    del dict['back']
    del dict['wilt']
    del dict['hast']
    del dict['light']
    del dict['speak']
    del dict['house']
    del dict['eyes']
    del dict['hence']
    del dict['stay']
    del dict['word']
    del dict['exeunt']
    del dict['comes']
    del dict['stand']
    del dict['hand']
    del dict['very']
    del dict['true']
    del dict['being']
    del dict['name']
    del dict['bed']
    del dict['call']
    del dict['part']
    del dict['away']
    del dict['therefore']
    del dict['i']
    del dict['face']
    del dict['bid']
    del dict['till']
    del dict['cannot']
    del dict['men']
    del dict['nor']
    del dict['before']
    del dict['ere']
    del dict['made']
    del dict['nay']
    del dict['been']
    del dict['watch']
    del dict['had']
    del dict['exit']
    del dict['down']
    del dict['eye']
    del dict['could']
    del dict['lips']
    del dict['most']
    del dict['rest']
    del dict['hold']
    del dict['long']
    del dict['put']
    del dict['any']
    del dict['friend']
    del dict['none']
    del dict['world']
    del dict['said']
    del dict['dost']
    del dict['sun']
    del dict['those']
    del dict['whose']
    del dict['haste']
    del dict['breath']
    del dict['boy']
    del dict['gentleman']
    del dict['fall']
    del dict['same']
    del dict['get']
    del dict['a']
    del dict['thine']
    del dict['still']
    del dict['many']
    del dict['nothing']
    del dict['head']
    del dict['letter']
    del dict['send']
    del dict['little']
    del dict['woe']
    del dict['within']
    del dict['else']
    del dict['without']
    del dict['cousin']
    del dict['came']
    del dict['run']
    del dict['forth']
    del dict['shame']
    del dict['hither']
    del dict['late']
    del dict['thing']
    del dict['best']
    del dict['wit']
    del dict['ill']
    del dict['sleep']
    del dict['gentle']
    del dict['happy']
    del dict['about']
    del dict['hate']
    del dict['place']
    del dict['full']
    del dict['alack']
    del dict['pale']
    del dict['another']
    del dict['warrant']
    del dict['since']
    del dict['ye']
    del dict['though']
    del dict["he's"]
    del dict['shalt']
    del dict['better']
    del dict['show']
    del dict['draw']
    del dict['gentlemen']
    del dict['tongue']
    del dict['pardon']
    del dict['answer']
    del dict['and']
    del dict['macb']
    del dict['haue']
    del dict['the']
    del dict['to']
    del dict['macbeth']
    del dict['macd']
    del dict['vpon']
    del dict['vs']
    del dict['at']
    del dict['rosse']
    del dict['doe']
    del dict['ile']
    del dict['feare']
    del dict['banquo']
    del dict['wife']
    del dict['selfe']
    del dict['great']
    del dict['speake']
    del dict['lenox']
    del dict["th'"]
    del dict['vp']
    del dict['thane']
    del dict['mal']
    del dict['banq']
    del dict['sleepe']
    del dict['things']
    del dict['looke']
    del dict['heere']
    del dict['scena']
    del dict['la']
    del dict['cawdor']
    del dict['againe']
    del dict['doct']
    del dict['loue']
    del dict['giue']
    del dict['done']
    del dict['macduffe']
    del dict['heare']
    del dict['in']
    del dict['owne']
    del dict["ha's"]
    del dict['way']
    del dict['&']
    del dict['our']
    del dict["do's"]
    del dict['poore']
    del dict['knock']
    del dict['shew']
    del dict['strange']
    del dict['malc']
    del dict['downe']
    del dict["i'th'"]
    del dict['goe']
    del dict['worthy']
    del dict['deed']
    del dict["there's"]
    del dict['thought']
    del dict['against']
    del dict['ayre']
    del dict['sey']
    del dict['father']
    del dict['dare']
    del dict['borne']
    del dict['malcolme']
    del dict['neuer']
    del dict['euer']
    del dict['euery']
    del dict['thus']
    del dict["o'th'"]
    del dict['haile']
    del dict["what's"]
    del dict['first']
    del dict['keepe']
    del dict['we']
    del dict['thinke']
    del dict['onely']
    del dict['into']
    del dict['scotland']
    del dict['leaue']
    del dict['gent']
    del dict['wood']
    del dict['seruant']
    del dict['morrow']
    del dict['welcome']
    del dict['words']
    del dict['mac']
    del dict['are']
    del dict['grace']
    del dict['beare']
    del dict['houre']
    del dict['seyward']
    del dict['flye']
    del dict['double']
    del dict['euen']
    del dict['whom']
    del dict['finde']
    del dict['once']
    del dict['fleans']
    del dict['duncan']
    del dict['thoughts']
    del dict['woman']
    del dict['beene']
    del dict['sight']
    del dict["that's"]
    del dict['false']
    del dict['further']
    del dict['macduff']
    del dict['f']
    del dict['lye']
    del dict['minde']
    del dict['last']
    del dict['ten']
    del dict['businesse']
    del dict['report']
    del dict['thunder']
    del dict['dunsinane']
    del dict['doctor']
    del dict['sonne']
    del dict['england']


    return dict                         # return dict, dictionary with words removed

def get_data(dict, int):
### function takes numbers or words and puts them in separate list
### inputs: dict - dictionary with words as keys and number values; 
###         int - int either -1 or 0, dictates where function takes words or numbers
### output: l 
    l = list()                          # list, empty list
    for line in dict:                   # goes through each line in dict              
        num = line[int]                 # str/int, either word key or number value
        l.append(num)                   #list, add either key or value
    return l                            # list

def main():
### main function
### inputs: NONE
### outouts: ' '
    
    romeo = open('romeo&juliet')        # io.TextIOWrapper
    romeo = cleanse_file(romeo)         # list, list of strings from file

    romeo_dict = make_dict(romeo)                                                       # dict, words as keys, ints as values
    romeo_dict = romeo_cleanse(romeo_dict)                                              # dict, certain words removed                       
    romeo_dict = sorted(romeo_dict.items(), key=lambda x: x[1])                         # dict, sorted by number
    romeo_dict = romeo_dict[-30:]                                                       # dict, last 30 key:values

    romeo_data = get_data(romeo_dict, -1)                                               # list, just int values
    romeo_keys = get_data(romeo_dict, 0)                                                # list, just word keys

    color = seaborn.color_palette('pastel')                                             # assigns colors for graph
    plt.pie(romeo_data, labels = romeo_keys, colors = color, autopct = '%.0f%%')        # creates pie chart
    plt.show()                                                                          # shows pie chart

    macbeth = open('macbeth')                                                           # io.TextIOWrapper
    macbeth = cleanse_file(macbeth)                                                     # list, list of strings from file

    macbeth_dict = make_dict(macbeth)                                                   # dict, words as keys, ints as values   
    macbeth_dict = macbeth_cleanse(macbeth_dict)                                        # dict, certain words removed
    macbeth_dict = sorted(macbeth_dict.items(), key=lambda x: x[1])                     # dict, sorted by number
    macbeth_dict = macbeth_dict[-30:]                                                   # dict, last 30 key:values

    macbeth_data = get_data(macbeth_dict, -1)                                           # list, just int values
    macbeth_keys = get_data(macbeth_dict, 0)                                            # list, list of strings from file

    color = seaborn.color_palette('pastel')                                             # assigns colors for graph
    plt.pie(macbeth_data, labels = macbeth_keys, colors = color, autopct = '%.0f%%')    # creates pie chart
    plt.show()                                                                          # shows pie chart

    return ' '                                                                          # returns ' '

print(main())                                                                           # runs main
