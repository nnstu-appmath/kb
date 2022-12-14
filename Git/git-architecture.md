![avatar](https://miro.medium.com/max/1200/1*PqEPOjr7MGG1bYwYYlN5sw.png)

## Git:
•    хранит историю изменений в коде  
•    способствует разработке в команде

В git клиенты полностью копируют репозиторий. Каждая копия репозитория является полным бэкапом всех данных. То есть, если один из серверов, через который разработчики обменивались данными, умрёт, любой клиентский репозиторий может быть скопирован на другой сервер для продолжения работы. 

![](https://git-scm.com/book/en/v2/images/distributed.png)

## Хранение данных в Git
Большинство других систем хранят информацию в виде списка изменений в файлах. 

Вместо этого, подход Git к хранению данных больше похож на набор снимков миниатюрной файловой системы. Каждый раз, когда вы делаете коммит, то есть сохраняете состояние своего проекта в Git, система запоминает, как выглядит каждый файл в этот момент, и сохраняет ссылку на этот снимок. Для увеличения эффективности, если файлы не были изменены, Git не запоминает эти файлы вновь, а только создаёт ссылку на предыдущую версию идентичного файла, который уже сохранён. Итак, Git представляет свои данные как поток снимков.  

![](https://git-scm.com/book/en/v2/images/snapshots.png)  


## Обязательно ли подключение к сети для выполнения операций git?  
Для работы большинства операций в Git достаточно локальных файлов и ресурсов — в основном, системе не нужна никакая информация с других компьютеров в сети, что ускоряет и упрощает работу.

Если вы в самолёте или в поезде и хотите немного поработать, вы сможете создавать коммиты без каких-либо проблем (в вашу локальную копию) и, когда будет возможность подключиться к сети, все изменения можно будет синхронизировать.

## У Git есть три основных состояния, в которых могут находиться ваши файлы: изменён (modified), индексирован (staged) и зафиксирован (committed):  

•    К изменённым относятся файлы, которые поменялись, но ещё не были зафиксированы.<br>
•    Индексированный — это изменённый файл в его текущей версии, отмеченный для включения в следующий коммит.<br>
•    Зафиксированный значит, что файл уже сохранён в вашей локальной базе.<br>

## В Git есть три основные секции проекта: рабочая копия (working tree), область индексирования (staging area) и каталог Git (Git directory).  

![](https://git-scm.com/book/en/v2/images/areas.png)

Рабочая копия является снимком одной версии проекта. Эти файлы извлекаются из сжатой базы данных в каталоге Git и помещаются на диск, для того чтобы их можно было использовать или редактировать.
Область индексирования (индекс) — это файл, в котором содержится информация о том, что попадёт в следующий коммит. 
Каталог Git — это то место, где Git хранит метаданные и базу объектов вашего проекта. Это та часть, которая копируется при клонировании репозитория с другого компьютера.  
## Базовый подход в работе с Git выглядит так:  
1.    Изменить файлы вашей рабочей копии.  
2.    Выборочно добавить в индекс только те изменения, которые должны попасть в следующий коммит, добавляя тем самым снимки только этих изменений в индекс.  
3.    Когда вы делаете коммит, используются файлы из индекса как есть, и этот снимок сохраняется в ваш каталог Git.  

## Ветка – это последовательность коммитов  
С точки зрения внутренней реализации – это ссылка на последний коммит в этой ветке

![](https://static.tildacdn.com/tild3232-3639-4135-a639-316239376265/1_3.png)


Как правило, ветка main (или master) – является основной, в ней находится рабочий продукт, стабильная версия кода.  
Ветка develop (или dev) нужна для разработки, она менее стабильна, но именно здесь идёт работа над выпуском новых версий продукта.   
В рамках проекта, ветка может быть прикреплена за конкретным разработчиком. Но чаще на каждую задачу создаётся ветка и, когда задача готова, она мёржится с основной веткой dev.

## Merge конфликты

![](https://fuzeservers.ru/wp-content/uploads/8/0/9/8097bbd36b7b9c48d4ba68e63492581d.png)

Конфликты возникают при мердже веток если в этих ветках одна и та же строка кода была изменена по-разному. Git не может сам решить какое из изменений нужно применить и он предлагает вручную решить эту ситуацию. Это замедляет работу с кодом в проекте. 

Избежать этого можно разными методами:
- распределять задачи так, чтобы связанные задачи не выполнялись одновременно различными программистами.
- вносить минимум изменений в код при решении задач. Чем меньше строчек вы поменяли, тем меньше вероятность что вы измените ту же самую строку что и другой программист в другой задаче.

## Разница между git fetch и git pull
Для синхронизации текущей ветки с репозиторием используются команды: git fetch и git pull.

git fetch — забирает изменения удаленной ветки из репозитория, основной ветки; той, которая была использована при клонировании репозитория. Изменения обновят удаленную ветку, после чего надо будет провести слияние с локальной веткой командой git merge.

Команда git pull сразу забирает изменения и проводит слияние с активной веткой. Забирает из репозитория, для которого были созданы удаленные ветки по умолчанию.

При использовании fetch, git собирает все коммиты из целевой ветки, которых нет в текущей ветке, и сохраняет их в локальном репозитории. Однако он не сливает их в текущую ветку. Чтобы слить коммиты в основную ветвь, нужно использовать merge.

Таким образом (грубо говоря) git pull — это шоткод для последовательности двух команд: git fetch (получение изменений с сервера) и git merge (сливание в локальную копию).
