
#Drozhzhin Sergey
#Аналог грепа
import os
import sys


def filesindir():
	print('Введите полный адрес директории, которую будем обследовать и нажмите Enter. Например, C:\Program Files\ ')
	filesdir=str(input())
	#Получаем список файлов в переменную files 
	files = os.listdir(filesdir) 
	print('Все файлы')
	print(files)
	print('----------')

	print('фильтрация')
	# #Фильтруем список 
	print('тексты')
	texts = filter(lambda x: x.endswith('.txt'), files) 
	for i in texts:
		# sizetext = os.path.getsize(i)
		print(i)
		# print('Размер файла: ', sizetext)
	print('----------')
	print('питоновские файлы')
	pytons = filter(lambda y: y.endswith('.py'), files)
	for j in pytons:
		print(j) 
	print('----------')
	print('файлы библиотек')
	dlls = filter(lambda z: z.endswith('.dll'), files) 
	for k in dlls:
		print(k) 
	print('----------')	

	print('файлы изображений')
	dlls = filter(lambda z: z.endswith('.dll'), files) 
	for k in dlls:
		print(k) 
	print('----------')	



def razmer(start_path = 'C:\Logs'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def derevo(files):
	tree = os.walk(files) 
	for d in tree:
		print (d)
    	    

def menu():
	print('Меню')
	print('Для того чтобы посмотреть список файлов в директории, нажмите 1')
	print('Для того чтобы посмотреть посмтреть размер  файлов в директории, нажмите 2')
	print('Для того чтобы посмотреть дерево вложенных каталогов, нажмите 4')
	print('Для того чтобы выйти, нажмите 0')

	nomer= int(input())

	if nomer==1:
		filesindir()
		menu()

	if nomer==2:
		print('Введите полный адрес директории, которую будем обследовать и нажмите Enter. Например, C:\Program Files\ ')
		filesdir=str(input())
		print ('Мегабайт: ', razmer(filesdir)/1024/ 1024)
		menu()

	if nomer==0:
		sys.exit()	

	if nomer==4:
		print('Введите полный адрес директории, которую будем обследовать и нажмите Enter. Например, C:\Program Files\ ')
		filesdir=str(input())
		derevo(filesdir)
		menu()	

menu()