import pandas as pd
from datetime import datetime

def main():
    scrape_data = pd.read_csv('scrapeResult.csv',names=['job_title','worker_name','sujest_time'])
    job_titles = list(scrape_data['job_title'])
    worker_names = list(scrape_data['worker_name'])
    sujest_times = list(scrape_data['sujest_time'])

    # num_of_job = job_title.duplicated().sum()
    # for i in worker_name:
    #     print(i)
    datetime_february = datetime(2021,2,1,hour=0,minute=0,second=0)
    datetime_march = datetime(2021,3,1,hour=0,minute=0,second=0)
    dict_work_num_by_month = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0}
    dict_worker_names = {}

    now_job_title = ""
    for num in range(len(job_titles)):
        # ワーカー名　重複数算出用
        if worker_names[num] in dict_worker_names:
            dict_worker_names[worker_names[num]] += 1
        else:
            dict_worker_names[worker_names[num]] = 1

        # 月当たりの仕事数 算出用
        if now_job_title == job_titles[num]:
            continue
        elif(now_job_title != job_titles[num]):
            convert_sujest_time_month = datetime.strptime(sujest_times[num],'%Y/%m/%d %H:%M').month
            dict_work_num_by_month[str(convert_sujest_time_month)] += 1
            now_job_title = job_titles[num]
    print(dict_work_num_by_month)
    print(sorted(dict_worker_names.items(),key=lambda x:x[1]))

if __name__ == '__main__':
    main()