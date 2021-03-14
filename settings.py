import os
from os.path import join, dirname
from dotenv import load_dotenv

dotnev_path = join(dirname(__file__),'.env')
load_dotenv(dotnev_path)
s_max_Row_Num = os.environ.get("MAX_ROW_NUM")
s_Chrome_Driver_Url = os.environ.get("CHROME_DRIVER_URL")
s_Get_Url = os.environ.get("GET_URL")
s_Begin_Job_Title_Xpath = os.environ.get("BEGIN_JOB_TITLE_XPATH")
s_End_Job_Title_Xpath = os.environ.get("END_JOB_TITLE_XPATH")
s_Table_Of_Apply_Xpath = os.environ.get("TABLE_OF_APPLY_XPATH")
s_Title_Of_Job_Xpath = os.environ.get("TITLE_OF_JOB_XPATH")