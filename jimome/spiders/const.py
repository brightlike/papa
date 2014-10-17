# -*- coding: utf-8 -*-

AGE = {
    '不限': '0',
    '18岁': '1',
    '19岁': '2',
    '20岁': '3',
    '21岁': '4',
    '22岁': '5',
    '23岁': '6',
    '24岁': '7',
    '25岁': '8',
    '26岁': '9',
    '29岁': '10',
    '28岁': '11',
    '29岁': '12',
    '30岁': '13',
    '31岁': '14',
    '32岁': '15',
    '33岁': '16',
    '34岁': '17',
    '35岁': '18',
    '36岁': '19',
    '37岁': '20',
    '38岁': '21',
    '39岁': '22',
    '40岁': '23',
    '41岁': '24',
    '42岁': '25',
    '43岁': '26',
    '44岁': '27',
    '45岁': '28',
    '46岁': '29',
    '47岁': '30',
    '48岁': '31',
    '49岁': '32',
    '50岁': '33'
}

HEIGHT = {
    '保密': '0',
    '150cm': '1',
    '151cm': '2',
    '152cm': '3',
    '153cm': '4',
    '154cm': '5',
    '155cm': '6',
    '156cm': '7',
    '157cm': '8',
    '158cm': '9',
    '159cm': '10',
    '160cm': '11',
    '161cm': '12',
    '162cm': '13',
    '163cm': '14',
    '164cm': '15',
    '165cm': '16',
    '166cm': '17',
    '167cm': '18',
    '168cm': '19',
    '169cm': '20',
    '170cm': '21',
    '171cm': '22',
    '172cm': '23',
    '173cm': '24',
    '174cm': '25',
    '175cm': '26',
    '176cm': '27',
    '177cm': '28',
    '178cm': '29',
    '179cm': '30',
    '180cm': '31',
    '181cm': '32',
    '182cm': '33',
    '183cm': '34',
    '184cm': '35',
    '185cm': '36',
    '186cm': '37',
    '187cm': '38',
    '188cm': '39',
    '189cm': '40',
    '170cm': '41',
    '191cm': '42',
    '192cm': '43',
    '193cm': '44',
    '194cm': '45',
    '195cm': '46',
    '196cm': '47',
    '197cm': '48',
    '198cm': '49',
    '199cm': '50',
    '200cm': '51'
}

SALARY = {
    '小于2000元': '0',
    '2000-5000元': '1',
    '5000-10000元': '2',
    '10000-20000元': '3',
    '20000元以上': '4'
}   

HAS_HOUSE = {
    '保密': '0',
    '已购房': '1',
    '与父母同住': '2',
    '租房': '3',
    '其他': '4'
}

FLAGS = {
    '做运动': ['1', '0'],
    '烹饪': ['1', '1'],
    '读书': ['1', '2'],
    '看电影': ['1', '3'],
    '上网': ['1', '4'],
    '听音乐': ['1', '5'],
    '养小动物': ['1', '6'],
    '摄影': ['1', '7'],
    '旅游': ['1', '8'],
    '幽默': ['2', '0'],
    '理智': ['2', '1'],
    '小资': ['2', '2'],
    '温柔': ['2', '3'],
    '有爱心': ['2', '4'],
    '可爱': ['2', '5'],
    '直爽': ['2', '6'],
    '顾家': ['2', '7'],
    '孝顺': ['2', '8']
}

PROVINCE = {
    '北京': '0',
    '天津': '1',
    '河北': '2',
    '山西': '3',
    '内蒙古': '4',
    '辽宁': '5',
    '吉林': '6',
    '黑龙江': '7',
    '上海': '8',
    '江苏': '9',
    '浙江': '10',
    '安徽': '11',
    '福建': '12',
    '江西': '13',
    '山东': '14',
    '河南': '15',
    '湖北': '16',
    '湖南': '17',
    '广东': '18',
    '广西': '19',
    '海南': '20',
    '重庆': '21',
    '四川': '22',
    '贵州': '23',
    '云南': '24',
    '西藏': '25',
    '陕西': '26',
    '甘肃': '27',
    '青海': '28',
    '宁夏': '29',
    '新疆': '30',
    '香港': '31',
    '澳门': '32',
    '台湾': '33'
}

CITY = {
    '北京': '0',
    '天津': '0',
    '石家庄': '0',
    '唐山': '1',
    '秦皇岛': '2',
    '邯郸': '3',
    '邢台': '4',
    '保定': '5',
    '张家口': '6',
    '承德': '7',
    '沧州': '8',
    '廊坊': '9',
    '衡水': '10',
    '太原': '0',
    '大同': '1',
    '阳泉': '2',
    '长治': '3',
    '晋城': '4',
    '朔州': '5',
    '晋中': '6',
    '运城': '7',
    '忻州': '8',
    '临汾': '9',
    '吕梁': '10',
    '呼和浩特': '0',
    '包头': '1',
    '乌海': '2',
    '赤峰': '3',
    '通辽': '4',
    '鄂尔多斯': '5',
    '呼伦贝尔': '6',
    '巴彦淖尔': '7',
    '乌兰察布': '8',
    '兴安盟': '9',
    '锡林郭勒盟': '10',
    '阿拉善盟': '11',
    '沈阳': '0',
    '大连': '1',
    '鞍山': '2',
    '抚顺': '3',
    '本溪': '4',
    '丹东': '5',
    '锦州': '6',
    '营口': '7',
    '阜新': '8',
    '辽阳': '9',
    '盘锦': '10',
    '铁岭': '11',
    '朝阳': '12',
    '葫芦岛': '13',
    '长春': '0',
    '吉林': '1',
    '四平': '2',
    '辽源': '3',
    '通化': '4',
    '白山': '5',
    '松原': '6',
    '白城': '7',
    '延边': '8',
    '哈尔滨': '0',
    '齐齐哈尔': '1',
    '鸡西': '2',
    '鹤岗': '3',
    '双鸭山': '4',
    '大庆': '5',
    '伊春': '6',
    '佳木斯': '7',
    '七台河': '8',
    '牡丹江': '9',
    '黑河': '10',
    '绥化': '11',
    '大兴安岭': '12',
    '上海': '0',
    '南京': '0',
    '无锡': '1',
    '徐州': '2',
    '常州': '3',
    '苏州': '4',
    '南通': '5',
    '连云港': '6',
    '淮安': '7',
    '盐城': '8',
    '扬州': '9',
    '镇江': '10',
    '泰州': '11',
    '宿迁': '12',
    '杭州': '0',
    '宁波': '1',
    '温州': '2',
    '嘉兴': '3',
    '湖州': '4',
    '绍兴': '5',
    '金华': '6',
    '衢州': '7',
    '舟山': '8',
    '台州': '9',
    '丽水': '10',
    '合肥': '0',
    '芜湖': '1',
    '蚌埠': '2',
    '淮南': '3',
    '马鞍山': '4',
    '淮北': '5',
    '铜陵': '6',
    '安庆': '7',
    '黄山': '8',
    '滁州': '9',
    '阜阳': '10',
    '宿州': '11',
    '巢湖': '12',
    '六安': '13',
    '亳州': '14',
    '池州': '15',
    '宣城': '16',
    '福州': '0',
    '厦门': '1',
    '莆田': '2',
    '三明': '3',
    '泉州': '4',
    '漳州': '5',
    '南平': '6',
    '龙岩': '7',
    '宁德': '8',
    '南昌': '0',
    '景德镇': '1',
    '萍乡': '2',
    '九江': '3',
    '新余': '4',
    '鹰潭': '5',
    '赣州': '6',
    '吉安': '7',
    '宜春': '8',
    '抚州': '9',
    '上饶': '10',
    '济南': '0',
    '青岛': '1',
    '淄博': '2',
    '枣庄': '3',
    '东营': '4',
    '烟台': '5',
    '潍坊': '6',
    '济宁': '7',
    '泰安': '8',
    '威海': '9',
    '日照': '10',
    '莱芜': '11',
    '临沂': '12',
    '德州': '13',
    '聊城': '14',
    '滨州': '15',
    '荷泽': '16',
    '郑州': '0',
    '开封': '1',
    '洛阳': '2',
    '平顶山': '3',
    '安阳': '4',
    '鹤壁': '5',
    '新乡': '6',
    '焦作': '7',
    '濮阳': '8',
    '许昌': '9',
    '漯河': '10',
    '三门峡': '11',
    '南阳': '12',
    '商丘': '13',
    '信阳': '14',
    '周口': '15',
    '驻马店': '16',
    '武汉': '0',
    '黄石': '1',
    '十堰': '2',
    '宜昌': '3',
    '襄樊': '4',
    '鄂州': '5',
    '荆门': '6',
    '孝感': '7',
    '荆州': '8',
    '黄冈': '9',
    '咸宁': '10',
    '随州': '11',
    '恩施': '12',
    '神农架': '13',
    '长沙': '0',
    '株洲': '1',
    '湘潭': '2',
    '衡阳': '3',
    '邵阳': '4',
    '岳阳': '5',
    '常德': '6',
    '张家界': '7',
    '益阳': '8',
    '郴州': '9',
    '永州': '10',
    '怀化': '11',
    '娄底': '12',
    '湘西': '13',
    '广州': '0',
    '韶关': '1',
    '深圳': '2',
    '珠海': '3',
    '汕头': '4',
    '佛山': '5',
    '江门': '6',
    '湛江': '7',
    '茂名': '8',
    '肇庆': '9',
    '惠州': '10',
    '梅州': '11',
    '汕尾': '12',
    '河源': '13',
    '阳江': '14',
    '清远': '15',
    '东莞': '16',
    '中山': '17',
    '潮州': '18',
    '揭阳': '19',
    '云浮': '20',
    '南宁': '0',
    '柳州': '1',
    '桂林': '2',
    '梧州': '3',
    '北海': '4',
    '防城港': '5',
    '钦州': '6',
    '贵港': '7',
    '玉林': '8',
    '百色': '9',
    '贺州': '10',
    '河池': '11',
    '来宾': '12',
    '崇左': '13',
    '海口': '0',
    '三亚': '1',
    '重庆': '0',
    '成都': '0',
    '自贡': '1',
    '攀枝花': '2',
    '泸州': '3',
    '德阳': '4',
    '绵阳': '5',
    '广元': '6',
    '遂宁': '7',
    '内江': '8',
    '乐山': '9',
    '南充': '10',
    '眉山': '11',
    '宜宾': '12',
    '广安': '13',
    '达州': '14',
    '雅安': '15',
    '巴中': '16',
    '资阳': '17',
    '阿坝': '18',
    '甘孜': '19',
    '凉山': '20',
    '贵阳': '0',
    '六盘水': '1',
    '遵义': '2',
    '安顺': '3',
    '铜仁': '4',
    '黔西南': '5',
    '毕节': '6',
    '黔东南': '7',
    '黔南': '8',
    '昆明': '0',
    '曲靖': '1',
    '玉溪': '2',
    '保山': '3',
    '昭通': '4',
    '丽江': '5',
    '思茅': '6',
    '临沧': '7',
    '楚雄': '8',
    '红河': '9',
    '文山': '10',
    '西双版纳': '11',
    '大理': '12',
    '德宏': '13',
    '怒江': '14',
    '迪庆': '15',
    '拉萨': '0',
    '昌都': '1',
    '山南': '2',
    '日喀则': '3',
    '那曲': '4',
    '阿里': '5',
    '林芝': '6',
    '西安': '0',
    '铜川': '1',
    '宝鸡': '2',
    '咸阳': '3',
    '渭南': '4',
    '延安': '5',
    '汉中': '6',
    '榆林': '7',
    '安康': '8',
    '商洛': '9',
    '兰州': '0',
    '嘉峪关': '1',
    '金昌': '2',
    '白银': '3',
    '天水': '4',
    '武威': '5',
    '张掖': '6',
    '平凉': '7',
    '酒泉': '8',
    '庆阳': '9',
    '定西': '10',
    '陇南': '11',
    '临夏': '12',
    '甘南': '13',
    '西宁': '0',
    '海东': '1',
    '海北': '2',
    '黄南': '3',
    '海南': '4',
    '果洛': '5',
    '玉树': '6',
    '海西': '7',
    '银川': '0',
    '石嘴山': '1',
    '吴忠': '2',
    '固原': '3',
    '中卫': '4',
    '乌鲁木齐': '0',
    '克拉玛依': '1',
    '吐鲁番': '2',
    '哈密': '3',
    '昌吉': '4',
    '博尔塔拉': '5',
    '巴音郭楞': '6',
    '阿克苏': '7',
    '克孜勒苏': '8',
    '喀什': '9',
    '和田': '10',
    '伊犁': '11',
    '塔城': '12',
    '阿勒泰': '13',
    '石河子': '14',
    '阿拉尔': '15',
    '图木舒克': '16',
    '五家渠': '17',
    '香港': '0',
    '澳门': '0',
    '台湾': '0'
}

WEIGHT = {
    '保密': '0',
    '80斤': '1',
    '81斤': '2',
    '82斤': '3',
    '83斤': '4',
    '84斤': '5',
    '85斤': '6',
    '86斤': '7',
    '87斤': '8',
    '88斤': '9',
    '89斤': '10',
    '90斤': '11',
    '91斤': '12',
    '92斤': '13',
    '93斤': '14',
    '94斤': '15',
    '95斤': '16',
    '96斤': '17',
    '97斤': '18',
    '98斤': '19',
    '99斤': '20',
    '100斤': '21',
    '101斤': '22',
    '102斤': '23',
    '103斤': '24',
    '104斤': '25',
    '105斤': '26',
    '106斤': '27',
    '107斤': '28',
    '108斤': '29',
    '109斤': '30',
    '110斤': '31',
    '111斤': '32',
    '112斤': '33',
    '113斤': '34',
    '114斤': '35',
    '115斤': '36',
    '116斤': '37',
    '117斤': '38',
    '118斤': '39',
    '119斤': '40',
    '120斤': '41',
    '121斤': '42',
    '122斤': '43',
    '123斤': '44',
    '124斤': '45',
    '125斤': '46',
    '126斤': '47',
    '127斤': '48',
    '128斤': '49',
    '129斤': '50',
    '130斤': '51',
    '131斤': '52',
    '132斤': '53',
    '133斤': '54',
    '134斤': '55',
    '135斤': '56',
    '136斤': '57',
    '137斤': '58',
    '138斤': '59',
    '139斤': '60',
    '140斤': '61',
    '141斤': '62',
    '142斤': '63',
    '143斤': '64',
    '144斤': '65',
    '145斤': '66',
    '146斤': '67',
    '147斤': '68',
    '148斤': '69',
    '149斤': '70',
    '150斤': '71',
    '151斤': '72',
    '152斤': '73',
    '153斤': '74',
    '154斤': '75',
    '155斤': '76',
    '156斤': '77',
    '157斤': '78',
    '158斤': '79',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
}










