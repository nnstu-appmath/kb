from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd
import matplotlib.pyplot as plt

# Инициализация объекта GoogleAuth
gauth = GoogleAuth()

# Файл client_secrets.json проверен
# и он автоматически обрабатывает аутентификацию
gauth.LocalWebserverAuth()

# Экземпляр GoogleDrive создается с использованием
# экземпляра аутентификации Google Auth.
drive = GoogleDrive(gauth)

# Инициализировать экземпляр GoogleDriveFile с идентификатором файла
file_obj = drive.CreateFile({'id': '10jbRmL81NLdKo4l03Xah3XLS1t99Qs8pYZU7IBShHBA'})
file_obj.GetContentFile('Alumni_data.xlsx',
                        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

excel_file = 'Alumni_data.xlsx'

# Часть кода выше отвечает за связь между Google таблицей и Python
#-----------------------------------------------------------------------------------------------------
# Ниже код, где вводятся некоторые ограничения на данные таблицы, и визуализация данных
# В действительности, с таблицей нужно работать через Pandas, следовательно, методы визуализации будут другими
# Поэтому следует рассматривать код ниже как черновик, который не стоит использовать для продолжения проекта

movies = pd.read_excel(excel_file)
movies_sheet1 = pd.read_excel(excel_file, 0, index_col=0)
movies_sheet1.head()

ms=[]
age = movies['Возраст (полных лет)']
for i in age:
    if isinstance(i, int):
        ms.append(i)

clow=0
cmid=0
cheg=0
cold=0
for i in ms:
    if 18 <= i < 25:
        clow+=1
    elif 25<=i<35:
        cmid+=1
    elif 35<=i<45:
        cheg+=1
    elif 45<=i:
        cold+=1

gender=list(movies['Пол'])
mcount=0
wcount=0

for i in gender:
    if i == 'Мужской':
        mcount+=1
    elif i== 'Женский':
        wcount+=1

fwork=list(movies['В какой сфере была Ваша первая работа?'])
w1=0
w2=0
w3=0
w4=0
w5=0
w6=0

for i in fwork:
    if i == 'Продажи, закупки.':
        w1+=1
    elif i== 'Производственные и рабочие специальности.':
        w2+=1
    elif i== 'Строительная отрасль и архитектура.':
        w3+=1
    elif i== 'Научная и образовательная.':
        w4+=1
    elif i== 'Рынок недвижимости.':
        w5+=1
    elif i== 'Делопроизводство, секретариат.':
        w6+=1

plt.figure()

plt.subplot()
plt.title('Age')
plt.xlabel('возраст')
plt.ylabel('кол-во')
age_fin= [clow,cmid,cheg,cold]
x_age=['18-25','25-35','35-45','45+']
plt.bar(x_age, age_fin,)


plt.subplot()
fig=plt.figure(figsize=(6,4))
ax=fig.add_subplot()
plt.title('Gender')
gen_fin=[mcount,wcount]
labels=['Муж','Жен']
ax.pie(gen_fin,labels=labels)

ax.grid()

plt.subplot()
fig1=plt.figure(figsize=(6,4))
ax1=fig1.add_subplot()
plt.title('Work')
fwork_fin=[w1,w2,w3,w4,w5,w6]
labels1=['Продажи, закупки.', 'Производственные и рабочие специальности.', 'Строительная отрасль и архитектура.',
        'Научная и образовательная.', 'Рынок недвижимости.', 'Делопроизводство, секретариат.']
ax1.pie(fwork_fin,labels=labels1)

ax1.grid()

plt.show()