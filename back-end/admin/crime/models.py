from admin.common.models import Reader, Printer, DFrameGenerator


class CrimeCctvModel():
    dfg = DFrameGenerator()
    printer = Printer()
    reader = Reader()

    def __init__(self):
        '''
        Raw Data - bring features
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.crime_columns = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']  # Nominal
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']  # Nominal
        self.crime_rate_columns = ['살인 검거율', '강도 검거율', '강간 검거율', '절도 검거율', '폭력 검거율']  # Ratio

    def create_crime_model(self):
        dfg = self.dfg
        reader = self.reader
        printer = self.printer
        dfg.context = 'admin/crime/data/'
        dfg.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(dfg)
        print(f'file_name: {crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        return crime_model

    def create_police_position(self):
        crime = self.create_crime_model()
        reader = self.reader
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울' + str(name[:-1] + '경찰서'))
        station_addrs = []
        station_lats = []
        station_lngs = []
        gmaps = reader.gmaps()
        for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_addrs.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_lats.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
            print(f'name : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_addrs:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        #  구와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] == '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] == '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] == '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] == '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] == '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] == '강남구'
        crime.to_csv(self.dfg.context + 'new_data/police_positions.csv')
