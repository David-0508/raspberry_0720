import os.path
from datetime import datetime
import random


def created_log_file(folder:str,file:str)->str:
    current_path=os.path.abspath(__name__) #取得目前檔案路徑
    directory_name=os.path.dirname(current_path) #取得目前資料夾路行
    data_path=os.path.join(directory_name,folder) #目前資料夾路徑加上data目錄
    print(data_path)
    if not os.path.isdir(data_path):
        print(f"沒有{folder}的目錄,需手動建立目錄")
        os.mkdir(data_path)
    else:
        print("資料已建立")
    


    log_path=os.path.join(data_path,file)
    if not os.path.isfile(log_path):
        print(f"沒有{file},建立新檔")
        with open(log_path,mode="w",encoding="utf-8",newline="") as file: #(改成with as寫法)
            file.write("時間,濕度,溫度\n")
    else:
        print("已經有log檔")
    return log_path

def record_info(log_path):
    now=datetime.now()
    now_str=now.strftime("%Y-%m-%d %H:%M:%S")
    humidity=str(random.randint(330,820)/10) #改寫
    celsius=str(random.randint(50,400)/10)  #改寫2
    with open(log_path,mode="a",encoding="utf-8",newline="") as file:
        file.write(now_str +","+humidity+","+celsius+"\n")