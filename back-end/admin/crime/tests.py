import csv

if __name__ == '__main__':
    crime_titles = ['살인', '강도', '강간', '절도', '폭력']
    crime_values = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']
    dt = dict(zip(crime_titles, crime_values))
    print(dt)

    with open('./data/test.csv', 'w', encoding='UTF-8') as f:
        w = csv.writer(f)
        w.writerow(dt.keys())
        w.writerow(dt.values())
