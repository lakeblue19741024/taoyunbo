# coding=gbk
import  os.path
# ���ú���������:�ָ�·��,�ҳ��ļ���.�ҳ��̷�(windowsϵͳ),�ҳ��ļ�����չ��. 
# �����������ʵ������޸��������. 
spath = " D:/html/hello.py" 

#  case 1: 
p,f = os.path.split(spath);
print ( " dir is: " + p)
print ( " file is: " + f)

#  case 2: 
drv,left = os.path.splitdrive(spath);
print ( " driver is: " + drv)
print ( " left is: " + left)
#  case 3: 
f,ext = os.path.splitext(spath);
print ( " f is: " + f)
print ( " ext is: " + ext)
''' 
    ֪ʶ��:    ���������������ض�Ԫ��.
    * case1 �ָ�Ŀ¼���ļ���
    * case2 �ָ��̷����ļ���
    * case3 �ָ��ļ�����չ��
''' 
