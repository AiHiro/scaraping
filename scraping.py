from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# ファイル出力用ライブらり
import csv

import settings

def main():
    # define
    max_Row_Num = int(settings.s_max_Row_Num)
    chrome_driver_url = settings.s_Chrome_Driver_Url
    get_url = settings.s_Get_Url
    begin_job_title_xpath = settings.s_Begin_Job_Title_Xpath
    end_job_title_xpath = settings.s_End_Job_Title_Xpath
    table_class_name = 'cw-table.worker_list'
    table_of_apply_xpath = settings.s_Table_Of_Apply_Xpath
    title_of_job_xpath = settings.s_Title_Of_Job_Xpath
    
    driver = webdriver.Chrome(chrome_driver_url)
    driver.get(get_url)
    
    csvfile = open('scrapeResult.csv','w',newline='')
    writer = csv.writer(csvfile, lineterminator='\n')
    # １件ずつ読み込む
    for job_Row_Num in range(max_Row_Num):
        #仕事のタイトルをクリックする
        driver.find_element_by_xpath(begin_job_title_xpath + str(job_Row_Num+1) + end_job_title_xpath).click()
        driver.switch_to.window(driver.window_handles[job_Row_Num+1])
        
        #スクレイピング
        job_title = driver.find_element_by_xpath(title_of_job_xpath).text
        
        try:
            driver.find_element_by_xpath(table_of_apply_xpath).click()
            sleep(1)
            table = driver.find_element_by_class_name(table_class_name)
            trs = table.find_elements(By.TAG_NAME, 'tr')
            #Tableのheaderを取得
            list_header_line = []
            try:
                ths = table.find_elements(By.TAG_NAME,'th')
            except NoSuchElementException as nsExcep:
                print('NoSuchElementException occured')
                print(nsExcep)
                pass
            else:
                # ヘッダの値を取得
                for i in range(0, len(ths)):
                    list_header_line.append(ths[i].text)

            #Table のbodyを取得
            list_table = []
            for i in range(1, len(trs)):
                tds = trs[i].find_elements(By.TAG_NAME, 'td')
                line = ""
                list_line = []
                list_line.append(job_title)
                for j in range(0, len(tds)):
                    list_line.append(tds[j].text)
                list_table.append(list_line)

            for list_line in list_table:
                writer.writerow(list_line)  

        except NoSuchElementException as nsExcep:
            print('NoSuchElementException occured')
            print(nsExcep)
            pass

        # 最後の取得仕事の場合はファイルをクローズする
        if job_Row_Num == max_Row_Num -1:
            csvfile.close()

        # heightは１仕事あたり２１０の枠で囲われていたため、２１０で指定
        # 画面をスクロールする
        driver.switch_to.window(driver.window_handles[0])
        scrollWindowY(driver,job_Row_Num+1)
        sleep(1)

# 画面Y方向に指定位置Y分スクロールする
def scrollWindowY(driver,work_Row_Num):
    driver.execute_script("window.scrollTo(0," + str(210*work_Row_Num) + ");")

if __name__ == '__main__':
    main()