#把要處理的資料夾放到 file_dir參數中
#執行>python renameCreateTxt.py
#會把資料夾中所有.avi檔案名稱複製
#產生前面加上2碼流水號的相對應txt檔
#再把.avi檔名改為「2碼流水號.avi」

import os,shutil

def main():
    file_dir = 'X:\\Vedio\\SonyAX40'
    i = 1
    for file_name in os.listdir(file_dir):
        if(os.path.splitext(file_name)[1] == '.avi'):
            os.chdir(file_dir)
            newfilename = str(i).zfill(2)+'.avi'
            f=open(str(i).zfill(2)+str(os.path.basename(file_name))[0:-4]+'.txt','w')
            f.write('\n')
            f.close()
            os.rename(file_name, newfilename)
            i = i + 1

if __name__=='__main__':
    main()