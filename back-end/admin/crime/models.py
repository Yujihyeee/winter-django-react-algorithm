from datetime import datetime
import folium
import pandas as pd
import numpy as np
from sklearn import preprocessing
from admin.common.models import Reader, ValueObject
import csv


class CrimeCctvModel():
    def __init__(self):
        pass
    '''
    Raw Data - bring features
    살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
    '''
    # noinspection PyMethodMayBeStatic
    def process(self):
        print(f'========= start process {datetime.now()} ========')
        vo = ValueObject()
        reader = Reader()
        vo.context = 'admin/crime/data/'
        crime_columns = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']  # Nominal
        arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']  # Nominal
        arrest_rate_columns = ['살인 검거율', '강도 검거율', '강간 검거율', '절도 검거율', '폭력 검거율']  # Ratio
        print('[1] create crime DF')
        vo.fname = 'crime_in_Seoul'
        crime_df = reader.csv(reader.new_file(vo))
        print('[2] crime_df 에 경찰서위치 추가 ')
        # self.crime_police(crime_df, reader, vo)
        vo.fname = 'new_data/police_positions'
        crime_df = reader.csv(reader.new_file(vo))
        print('[3] create CCTV DF')
        vo.fname = 'CCTV_in_Seoul'
        cctv_df = reader.csv(reader.new_file(vo))
        cctv_df.rename(columns={cctv_df.columns[0]: '구별'}, inplace=True)
        print('[4] create POP DF')
        vo.fname = 'population_in_Seoul'
        pop_df = reader.xls(reader.new_file(vo), 2, 'b,d,g,j,n')
        pop_df.columns = ['구별', '인구수', '한국인', '외국인', '고령자']
        pop_df.drop([26], inplace=True)
        print('[5] create CCTV_POP_MERGE DF')
        cctv_pop_df = pd.merge(cctv_df, pop_df)
        cctv_pop_corr = cctv_pop_df.corr()
        print(cctv_pop_corr)
        '''
        CCTV와 상관계수: 한국인 0.3, 외국인 0, 고령자 0.2
        '''
        crime_df = crime_df.groupby('구별').sum()
        crime_df['총 범죄 수'] = crime_df.loc[:, crime_df.columns.str.contains(' 발생$', case=False, regex=True)].sum(axis=1)
        crime_df['총 검거 수'] = crime_df.loc[:, crime_df.columns.str.contains(' 검거$', case=False, regex=True)].sum(axis=1)
        crime_df['총 검거율'] = crime_df['총 검거 수'] / crime_df['총 범죄 수'] * 100
        cctv_crime_df = pd.merge(cctv_df.loc[:, ['구별', '소계']], crime_df.loc[:, '총 범죄 수':'총 검거율'], on='구별')
        cctv_crime_df.rename(columns={"소계": "CCTV 총합"}, inplace=True)
        print(cctv_crime_df.corr())
        '''
        CCTV와 상관계수: 범죄수 .047, 검거수 0.52
        '''
        print('[6] create Police DF')
        police_df = pd.pivot_table(crime_df, index='구별', aggfunc=np.sum)
        print(police_df)
        print(f'Police_position DF columns: {police_df.columns}')
        '''
        ['살인 발생','살인 검거','강도 발생','강도 검거','강간 발생','강간 검거',
        '절도 발생','절도 검거','폭력 발생','폭력 검거', '총범죄수', '총검거수', '총검거율']'''
        '''police_df['살인검거율'] = (police_df['살인 검거'].astype(int) / police_df['살인 발생'].astype(int)) * 100
        police_df['강도검거율'] = (police_df['강도 검거'].astype(int) / police_df['강도 발생'].astype(int)) * 100
        police_df['강간검거율'] = (police_df['강간 검거'].astype(int) / police_df['강간 발생'].astype(int)) * 100
        police_df['절도검거율'] = (police_df['절도 검거'].astype(int) / police_df['절도 발생'].astype(int)) * 100
        police_df['폭력검거율'] = (police_df['폭력 검거'].astype(int) / police_df['폭력 발생'].astype(int)) * 100'''
        for i, j in enumerate(crime_columns):
            police_df[arrest_rate_columns[i]] = \
                (police_df[arrest_columns[i]].astype(int) / police_df[j].astype(int)) * 100

        police_df.drop(columns={'살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'}, axis=1, inplace=True)
        for i in arrest_rate_columns:
            police_df.loc[police_df[i] > 100, 1] = 100
        vals = ['살인', '강도', '강간', '절도', '폭력']
        keys = [f'{i} 발생' for i in vals]
        columns = dict(zip(keys, vals))
        police_df.rename(columns=columns, inplace=True)
        x = police_df[arrest_rate_columns].values
        # from sklearn import preprocessing 추가
        min_max_scalar = preprocessing.MinMaxScaler()
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        # 정규화 normalization
        # 1. 빅데이터를 처리하면서 데이터의 범위(도메인)을 일치시킨다
        # 2. 분포(스케일)을 유사하게 만든다
        print('[7] police_norm_df Creation')
        police_norm_df = pd.DataFrame(x_scaled, columns=crime_columns, index=police_df.index)
        police_norm_df[arrest_rate_columns] = police_df[arrest_rate_columns]
        police_norm_df['범죄'] = np.sum(police_norm_df[crime_columns], axis=1)
        police_norm_df['검거'] = np.sum(police_norm_df[arrest_rate_columns], axis=1)
        police_norm_df.to_csv(vo.context + 'new_data/police_norm.csv', sep=',', encoding='UTF-8')
        print('[8] Seoul Map Creation')
        vo.fname = 'geo_simple'
        crime_df = reader.json(reader.new_file(vo))

        url = (
            "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
        )
        state_geo = f"{url}/us-states.json"
        state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
        state_data = pd.read_csv(state_unemployment)

        m = folium.Map(location=[37, 126], zoom_start=8)

        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=state_data,
            columns=["State", "Unemployment"],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name="Unemployment Rate (%)",
        ).add_to(m)

        folium.LayerControl().add_to(m)

        m.save(vo.context + 'folium.html')

    def crime_police(self, crime_df, reader, vo):
        station_names = []
        [station_names.append('서울' + str(name[:-1] + '경찰서')) for name in crime_df['관서명']]
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
        gu_names = []
        for name in station_addrs:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime_df['구별'] = gu_names
        print(crime_df[crime_df['관서명'] == '혜화서'])
        crime_df.to_csv(vo.context + 'new_data/crime_police.csv')
        dt = dict(zip(station_lats, station_lngs))
        print(dt)

        with open(vo.context + 'test.csv', 'w', encoding='UTF-8') as f:
            w = csv.writer(f)
            w.writerow(dt.keys())
            w.writerow(dt.values())
