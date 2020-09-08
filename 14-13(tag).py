# ex14_13.py
import zipfile

zipdir = input("請輸入欲解壓縮的目錄 : ")
unzipdir = input("請輸入存放解壓縮的目錄 : ")
fileUnZip = zipfile.ZipFile(zipdir)
fileUnZip.extractall(unzipdir)
fileUnZip.close()



