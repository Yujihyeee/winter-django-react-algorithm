import pandas as pd
from icecream import ic
from admin.common.models import Reader, Printer, ValueObject


class CrimeCctvModelOld():
    vo = ValueObject()
    printer = Printer()
    reader = Reader()

    def __init__(self):
        '''
        Raw Data - bring features
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.vo.context = 'admin/crime/data/'
        self.crime_columns = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']  # Nominal
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']  # Nominal
        self.crime_rate_columns = ['살인 검거율', '강도 검거율', '강간 검거율', '절도 검거율', '폭력 검거율']  # Ratio

    def create_crime_model(self):
        vo = self.vo
        reader = self.reader
        vo.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(vo)
        print(f'file_name: {crime_file_name}')
        crime = reader.csv(crime_file_name)
        self.printer.dframe(crime)
        return crime

    def create_police_position(self) -> object:
        crime = self.create_crime_model()
        reader = self.reader
        station_names = []
        [station_names.append('서울' + str(name[:-1] + '경찰서')) for name in crime['관서명']]
        station_addrs = []
        station_lats = []
        station_lngs = []
        gmaps = reader.gmaps()
        '''for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_addrs.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_lats.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
            print(f'name : {temp[0].get("formatted_address")}')'''
        gu_names = []
        for name in station_addrs:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        print('======================================================')
        print(f"샘플 중 혜화서 정보: {crime[crime['관서명'] == '혜화서']}")
        print(f"샘플 중 금천서 정보: {crime[crime['관서명'] == '금천서']}")
        #  crime.to_csv(self.vo.context + 'new_data/police_positions.csv')

    def create_cctv_model(self) -> object:
        vo = self.vo
        reader = self.reader
        vo.fname = 'CCTV_in_Seoul'
        cctv_file_name = reader.new_file(vo)
        cctv = reader.csv(cctv_file_name)
        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace=True)
        self.printer.dframe(cctv)
        cctv.to_csv(vo.context + 'new_data/new_cctv.csv')
        return cctv

    def create_population_model(self) -> object:
        vo = self.vo
        reader = self.reader
        vo.fname = 'population_in_Seoul'
        pop_file_name = reader.new_file(vo)
        pop = reader.xls(pop_file_name, 2, 'b,d,g,j,n')
        pop.columns = ['구별', '인구수', '한국인', '외국인', '고령자']
        pop.drop([26], inplace=True)
        self.printer.dframe(pop)
        # pop.to_csv(vo.context + 'new_data/new_population.csv')
        return pop

    def merge_cctv_pop(self):
        cctv = self.create_cctv_model()
        pop = self.create_population_model()
        cctv_pop = pd.merge(cctv, pop)
        '''
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계,
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        '''
        ic(cctv_pop.corr())
        '''
                      소계     2013년도 이전   2014년   2015년     2016년    인구수     한국인     외국인     고령자
        소계           1.000000   0.862756  0.450062  0.624402  0.593398  0.306342  0.304287 -0.023786  0.255196
        2013년도 이전   0.862756   1.000000  0.121888  0.257748  0.355482  0.168177  0.163142  0.048973  0.105379
        2014년         0.450062   0.121888  1.000000  0.312842  0.415387  0.027040  0.025005  0.027325  0.010233
        2015년         0.624402   0.257748  0.312842  1.000000  0.513767  0.368912  0.363796  0.013301  0.372789
        2016년         0.593398   0.355482  0.415387  0.513767  1.000000  0.144959  0.145966 -0.042688  0.065784
        인구수         [0.306342]   0.168177  0.027040  0.368912  0.144959  1.000000  0.998061 -0.153371  0.932667
        한국인         [0.304287]   0.163142  0.025005  0.363796  0.145966  0.998061  1.000000 -0.214576  0.931636
        외국인        [-0.023786]   0.048973  0.027325  0.013301 -0.042688 -0.153371 -0.214576  1.000000 -0.155381
        고령자         [0.255196]   0.105379  0.010233  0.372789  0.065784  0.932667  0.931636 -0.155381  1.000000
        '''
        self.printer.dframe(cctv_pop)
        #  cctv_pop.to_csv(f'{self.vo.context}new_data/cctv_pop.csv')

    def merge_cctv_position(self):
        pass
