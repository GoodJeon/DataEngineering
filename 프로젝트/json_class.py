# -*- coding:utf-8 -*-
import requests
import json
import pandas as pd


class Traffic():
    SiDo = {'서울특별시': ['11',
                      {'강남구': '680', '강동구': '740', '강북구': '305', '강서구': '500', '관악구': '620', '광진구': '215', '구로구': '530',
                       '금천구': '545', '노원구': '350', '도봉구': '320', '동대문구': '230', '동작구': '590', '마포구': '440',
                       '서대문구': '410', '서초구': '650', '성동구': '200', '성북구': '290', '송파구': '710', '양천구': '470',
                       '영등포구': '560',
                       '용산구': '170', '은평구': '380', '종로구': '110', '중구': '140', '중랑구': '260'}],
            '부산광역시': ['26',
                      {'강서구': '440', '금정구': '410', '기장군': '710', '남구': '290', '동구': '170', '동래구': '260', '부산진구': '230',
                       '북구': '320', '사상구': '530', '사하구': '380', '서구': '140', '수영구': '500', '연제구': '470', '영도구': '200',
                       '중구': '110', '해운대구': '350'}],
            '대구광역시': ['27',
                      {'남구': '200', '달서구': '290', '달성군': '710', '동구': '140', '북구': '230', '서구': '170', '수성구': '260',
                       '중구': '110'}],
            '인천광역시': ['28',
                      {'강화군': '710', '계양구': '245', '남구': '170', '남동구': '200', '동구': '140', '부평구': '237', '서구': '260',
                       '연수구': '185', '옹진군': '720', '중구': '110'}],
            '광주광역시': ['29', {'광산구': '200', '남구': '155', '동구': '110', '북구': '170', '서구': '140'}],
            '대전광역시': ['30', {'대덕구': '230', '동구': '110', '서구': '170', '유성구': '200', '중구': '140'}],
            '울산광역시': ['31', {'남구': '140', '동구': '170', '북구': '200', '울주군': '710', '중구': '110'}],
            '세종특별자치시': ['36', {'세종특별자치시': '100'}],
            '경기도': ['41',
                    {'가평군': '820',
                     '고양시': '280', '고양시덕양구': '281', '고양시일산구': '283', '고양시일산동구': '285', '고양시일산서구': '287',
                     '과천시': '290', '광명시': '610', '광주시': '610', '구리시': '310', '군포시': '410',
                     '김포시': '570', '남양주시': '360', '동두천시': '250',
                     '부천시': '190', '부천시소사구': '197', '부천시오정구': '199', '부천시원미구': '195',
                     '성남시': '130', '성남시분당구': '135', '성남시수정구': '131', '성남시중원구': '133',
                     '수원시': '110', '수원시권선구': '113', '수원시영통구': '117', '수원시장안구': '111', '수원시팔달구': '115',
                     '시흥시': '390',
                     '안산시': '270', '안산시단원구': '273', '안산시상록구': '271',
                     '안성시': '550',
                     '안양시': '170', '안양시동안구': '173', '안양시만안구': '171',
                     '양주시': '630', '양평군': '830', '여주군': '730', '여주시': '670',
                     '연천군': '800', '오산시': '370',
                     '용인시': '460', '용인시기흥구': '463', '용인시수지구': '465', '용인시처인구': '461',
                     '의왕시': '430', '의정부시': '150', '이천시': '500',
                     '파주시': '480', '평택시': '220', '포천군': '810', '포천시': '650', '하남시': '450', '화성시': '590'}],
            '강원도': ['42',
                    {'강릉시': '150', '고성군': '820', '동해시': '170', '삼척시': '230', '속초시': '210', '양구군': '800', '양양군': '830',
                     '영월군': '750', '원주시': '130', '인제군': '810', '정선군': '770', '철원군': '780', '춘천시': '110', '태백시': '190',
                     '평창군': '760', '홍천군': '720', '화천군': '790', '횡성군': '730'}],
            '충청북도': ['43',
                     {'괴산군': '760', '단양군': '800', '보은군': '720', '영동군': '740', '옥천군': '730', '음성군': '770', '제천시': '150',
                      '증평군': '745', '진천군': '750', '청원군': '710',
                      '청주시': '110', '청주시상당구': '111', '청주시서원구': '112', '청주시청원구': '114', '청주시흥덕구': '113',
                      '충주시': '130'}],
            '충청남도': ['44',
                     {'계룡시': '250', '공주시': '150', '금산군': '710', '논산시': '230', '당진군': '830', '당진시': '270', '보령시': '180',
                      '부여군': '760', '서산시': '210', '서천군': '770', '아산시': '200', '연기군': '730', '예산군': '810',
                      '천안시': '130', '천안시동남구': '131', '천안시서북구': '133',
                      '청양군': '790', '태안군': '825', '홍성군': '800'}],
            '전라북도': ['45',
                     {'고창군': '790', '군산시': '130', '김제시': '210', '남원시': '190', '무주군': '730', '부안군': '800', '순창군': '770',
                      '완주군': '710', '익산시': '140', '임실군': '750', '장수군': '740',
                      '전주시': '110', '전주시덕진구': '113', '전주시완산구': '111',
                      '정읍시': '180',
                      '진안군': '720'}],
            '전라남도': ['46',
                     {'강진군': '810', '고흥군': '720', '곡성군': '720', '광양시': '230', '구례군': '730', '나주시': '170', '담양군': '710',
                      '목포시': '110', '무안군': '840', '보성군': '780', '순천시': '150', '신안군': '910', '여수시': '130', '영광군': '870',
                      '영암군': '830', '완도군': '890', '장성군': '880', '장흥군': '800', '진도군': '900',
                      '함평군': '860', '해남군': '820', '화순군': '790'}],
            '경상북도': ['47',
                     {'경산시': '290', '경주시': '130', '고령군': '830', '구미시': '190', '군위군': '720', '김천시': '150', '문경시': '280',
                      '봉화군': '920', '상주시': '250', '성주군': '840', '안동시': '170', '영덕군': '770', '영양군': '760', '영주시': '210',
                      '영천시': '230', '예천군': '900', '울릉군': '940', '울진군': '930', '의성군': '730', '청도군': '820', '청송군': '750',
                      '칠곡군': '850',
                      '포항시': '110', '포항시남구': '111', '포항시북구': '113'}],
            '경상남도': ['48',
                     {'거제시': '310', '거창군': '880', '고성군': '820', '김해시': '250', '남해군': '840', '마산시': '160', '밀양시': '270',
                      '사천시': '240', '산청군': '860', '양산시': '330', '의령군': '720', '진주시': '170', '진해시': '190', '창녕군': '740',
                      '창원시': '120', '창원시마산합포구': '125', '창원시마산회원구': '127', '창원시성산구': '123', '창원시의창구': '121',
                      '창원시진해구': '129',
                      '통영시': '220', '하동군': '850', '함안군': '730', '함양군': '870', '합천군': '890'}],
            '제주특별자치도': ['50', {'서귀포시': '130', '제주시': '110'}]}
    Year = ['2017', '2018', '2019', '2020',]
    def __init__(self,url,file_name):
        self.url = url
        self.file_name = file_name

    def Make_Json(self):
        url = self.url
        Year = Traffic.Year
        SiDo = Traffic.SiDo
        service_key = 'SaSnehC34rO3z%2Ff%2Fjavc%2FfzjQCJwxfuTfLP5JNBfIOGmvKQtXfuAX8tm2GGi1%2FY2lX3Gbx07wScwmZsCdeLpyQ%3D%3D'

        new_tmp = {}
        year_dict = {}
        for year in Year:
            print(year)
            lst_sido = []
            for sido in SiDo.keys():
                print(sido)
                lst_gu = []

                for gugun in SiDo[sido][1].keys():
                    # print(gugun)
                    # url = f'http://apis.data.go.kr/B552061/frequentzoneTmzon/getRestFrequentzoneTmzon?serviceKey={service_key}&searchYearCd={year}&siDo={SiDo[sido][0]}&guGun={SiDo[sido][1][gugun]}&type=json&numOfRows=9999&pageNo=1'
                    # url = f'http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg?serviceKey={service_key}&searchYearCd={year}&siDo={SiDo[sido][0]}&guGun={SiDo[sido][1][gugun]}&type=json&numOfRows=9999&pageNo=1'
                    urls = url.format(service_key,year,SiDo[sido][0],SiDo[sido][1][gugun])
                    # print(url)

                    resp = requests.get(urls)
                    # json
                    json_data = resp.json()
                    # print(json_data)
                    if json_data['resultMsg'] == 'NODATA_ERROR':  # 비어있는 구는 치우고 싶은데 어디로???
                        continue  # 컨티뉴?
                    '''
                    5 : 지점명  spot_nm
                    6 : 발생건수  occrrnc_cnt
                    7 : 사상자수  caslt_cnt
                    8 : 사망자수  dth_dnv_cnt
                    9 : 중상자수  se_dnv_cnt
                    10 : 경상자수  sl_dnv_cnt
                    12 : 폴리곤  geom_json
                    13 : 경도   lo_crd
                    14 : 위도   la_crd

                    '''
                    # print(json['items']['item'])
                    data = json_data['items']['item']
                    # print(data)
                    lst = []
                    total_occrrnc_cnt, total_caslt_cnt, total_dth_dnv_cnt, total_se_dnv_cnt, total_sl_dnv_cnt = 0, 0, 0, 0, 0

                    for item in data:
                        # print(item)
                        tmp = {}
                        for key in item.keys():
                            # print(key)
                            if key == 'spot_nm':
                                tmp['상세주소'] = item[key]
                            elif key == 'occrrnc_cnt':
                                tmp['발생건수'] = item[key]
                                total_occrrnc_cnt += item[key]
                            elif key == 'caslt_cnt':
                                tmp['사상자수'] = item[key]
                                total_caslt_cnt += item[key]
                            elif key == 'dth_dnv_cnt':
                                tmp['사망자수'] = item[key]
                                total_dth_dnv_cnt += item[key]
                            elif key == 'se_dnv_cnt':
                                tmp['중상자수'] = item[key]
                                total_se_dnv_cnt = +item[key]
                            elif key == 'sl_dnv_cnt':
                                tmp['경상자수'] = item[key]
                                total_sl_dnv_cnt = +item[key]
                            elif key == 'geom_json':
                                    tmp['폴리곤'] = item[key]
                            elif key == 'lo_crd':
                                tmp['경도'] = item[key]
                            elif key == 'la_crd':
                                tmp['위도'] = item[key]

                        lst.append(tmp)   ## 두번 담김

                    # 데이터 없으면 에러 발생
                    # try:
                    #     new_tmp['총합발생건수'] = total_occrrnc_cnt
                    #     new_tmp['총합사상자수'] = total_caslt_cnt
                    #     new_tmp['총합사망자수'] = total_dth_dnv_cnt
                    #     new_tmp['총합중상자수'] = total_se_dnv_cnt
                    #     new_tmp['총합경상자수'] = total_sl_dnv_cnt
                    #     lst.append(new_tmp)    ## 두번 담김
                    # except NameError as e:
                    #     # print('데이터가 없음')
                    #     pass

                    # print(lst)
                    gu = {gugun: lst}
                    # print(gu)
                    # sido_dict = {sido: gu}
                    # print(sido_dict)
                    lst_gu.append(gu)
                    # print(lst_gu)
                # print(lst_gu)

                sido_dict = {sido: lst_gu}   # 구까지는 쉽게 찾을수 있게 해야함, 원본 == lst_gu
                lst_sido.append(sido_dict)
            # print(lst_sido)


            year_dict[year] = lst_sido

            # year_lst.append(year_dict)

        # print(year_lst)
        print(year_dict)

        res_json = json.dumps(year_dict, ensure_ascii=False)
        with open(f'{self.file_name}.json', 'w', encoding='utf-8') as f:
            f.write(res_json)

    def find_index(self,want_sido, want_gugun):
        # print(SiDo.keys())
        cnt = -1
        for s in Traffic.SiDo.keys():
            cnt += 1
            if s == want_sido:
                # print(cnt)
                cnt_s = cnt
        cnt = -1
        # print(SiDo[want_sido][1].keys())
        gugun_key = Traffic.SiDo[want_sido][1].keys()
        for g in gugun_key:
            cnt += 1
            if g == want_gugun:
                # print(cnt)
                cnt_g = cnt
        return cnt_s, cnt_g



    # json형태(년도가 key)의 데이터를 넣어주면 csv파일로 바꿔준다.
    def json_to_csv(self):
        with open(f'{self.file_name}.json', 'r', encoding='utf-8') as j:
            x= json.loads(j.read())  #  UnboundLocalError: local variable 'json' referenced before assignment
        data = []
        df = pd.DataFrame()
        for year_add in x.keys():  # year_add
            json_x = x[year_add]
            for year_data in range(len(json_x)):  # year_data
                for sido_add in json_x[year_data]:      # # sido_add
                    for sido_data in range(len(json_x[year_data][sido_add])):  # sido_data
                        for gugun_add in json_x[year_data][sido_add][sido_data]:  # gugun_add
                            for details_data in range(len(json_x[year_data][sido_add][sido_data][gugun_add])):  # details_data
                                data.append(list(json_x[year_data][sido_add][sido_data][gugun_add][details_data].values()))
                                columns = json_x[year_data][sido_add][sido_data][gugun_add][details_data].keys()
            year_df = pd.DataFrame(data, columns=columns)
            year_df['발생년도'] = year_add
            df = pd.concat([df, year_df], ignore_index=True)

        # 입력받은 파라미터가 파일 이름에 쓰인다.
        # 예) json형태의 변수 child를 넣어주면 'child_accident.csv'로 저장된다.

        df.to_csv(f'{self.file_name}_accident.csv')
        return df

# 아래가 자치구 위에가 연휴
# url = 'http://apis.data.go.kr/B552061/frequentzoneTmzon/getRestFrequentzoneTmzon?serviceKey={0}&searchYearCd={1}&siDo={2}&guGun={3}&type=json&numOfRows=9999&pageNo=1'
url = 'http://apis.data.go.kr/B552061/frequentzoneLg/getRestFrequentzoneLg?serviceKey={0}&searchYearCd={1}&siDo={2}&guGun={3}&type=json&numOfRows=9999&pageNo=1'
# 보행자 무단횡단
# url = 'http://apis.data.go.kr/B552061/jaywalking/getRestJaywalking?serviceKey={0}&searchYearCd={1}&siDo={2}&guGun={3}&type=json&numOfRows=9999&pageNo=1'

# t = Traffic(url,'namename')
# t.Make_Json()

t1 = Traffic(url,'namename4')
t1.Make_Json()
t1.json_to_csv()
# print(t.find_index('충청남도','서천군'))
