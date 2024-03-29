# Немного теории
### Что такое GitHub?
GitHub — это самый популярный сервис для публичного хранения репозиториев. Репозитории опенсорсных проектов в GitHub видны всем — можно делать копии основной ветки (это называется форкнуть, сделать форк; от англ. __fork__ — вилка, ответвление), чтобы что-то изменить и после предложить свои изменения автору проекта.

### Что такое Git? 
Git — это система контроля версий, которая позволяет нескольким разработчикам одновременно работать над одним продуктом.
### Зачем нужен Git?
В Git хранятся все версии проекта — как бы по вертикали. Они называются коммитами (от англ. __commit__ — совершать, фиксировать). Такая система позволяет вернуться к любой сохранённой версии при необходимости, например, если новый коммит не работает.

А ещё Git позволяет работать над одним кодом десяткам и даже тысячам людей — как бы по горизонтали. В таком случае каждый разработчик получает свою версию кода, вносит в неё изменения и отправляет обратно. Коммиты разных программистов объединяются — мёржатся (от англ. __merge__ — сливать, соединять). У каждого коммита есть уникальный номер, он называется хешем, и комментарий, который описывает суть изменений. А все коммиты в одном проекте складываются в единую структуру — бранч (от англ. __branch__ — отделение, ветка). 

Ветвь — это параллельная версия вашего репозитория (проекта). По умолчанию в вашем репозитории есть одна главная ветвь с именем main (англ. __main__ — основной, главный). Вы можете создавать дополнительные ветви от ветки main в своём репозитории, что позволяет одновременно разрабатывать разные версии проекта. В дополнительных ветвях вы можете вносить изменения, не влияя на main версию, то есть обеспечивая её безопасность.

Важное преимущество Git-проектов состоит ещё и в том, что код хранится и на сервере, и локально, то есть на компьютерах разработчиков. Это значит, что код нельзя случайно (или специально) удалить — всегда найдётся версия, из которой можно восстановить сразу всё.
### Одновременная работа над одним и тем же
Например, один разработчик ищет баг в коде и чуть переписывает несколько строк, а другой берёт и удаляет весь кусок кода целиком. В таком случае во время коммита последнего разработчика возникнет конфликт версий: Git остановит мёрж и предложит программистам самим разобраться, что делать с конфликтным куском кода.

Но обычно разработчики не коммитят в основную ветку, чтобы случайно не нарушить работоспособность проекта. Они могут днями и даже годами коммитить в свои ветки, синхронизируя их с основной и проверяя работоспособность решений, и после релизить изменения в основную — её часто называют мастером. Но в западном мире уже говорят main.
# Практика
Полезным будет предварительно пройти [вводный курс от GitHub](https://github.com/skills/introduction-to-github). 

[Шпаргалка по Git](https://training.github.com/downloads/ru/github-git-cheat-sheet/) от GitHub на русском языке.

### Установка Git
Открываем шпаргалку и скачиваем Git на нужную систему, переходя по первым ссылкам. [Руководство к установке](https://git-scm.com/book/ru/v2/Введение-Установка-Git).
### Первоначальная настройка Git
Выполняем все пункты [руководства](https://git-scm.com/book/ru/v2/Введение-Первоначальная-настройка-Git), можно пропустить _выбор редактора_ и _настройку ветки по умолчанию_.
### Создание Git-репозитория
У нас есть 2 варианта: превратить локальный каталог в репозиторий Git или клонировать существующий репозиторий Git.

[Руководство](https://git-scm.com/book/ru/v2/Основы-Git-Создание-Git-репозитория).
#### Создание репозитория в существующем каталоге
Находим в руководстве команду для нашей системы, с её помощью переходим к каталогу, который хотим сделать репозиторием, и инициализируем его через `git init` [если перейти к каталогу не получается, попробуйте заключить путь в кавычки ""]. Эта команда создаёт в текущем каталоге новый подкаталог с именем __.git__, содержащий все необходимые файлы репозитория — структуру Git репозитория. На этом этапе проект ещё не находится под версионным контролем.
#### Клонирование существующего репозитория
Клонирование репозитория осуществляется командой `git clone`. Есть несколько способ клонировать репозиторий, но мы воспользуемся SSH-ключом. Посмотрите [видео](https://www.youtube.com/watch?v=4evR80g--9k&list=PLg5SS_4L6LYstwxTEOU05E0URTHnbtA0l&index=10), в котором SSH-ключ генерируется и добавляется в профиль GitHub. C 2:14 до 3:07 клонируется произвольный репозиторий с GitHub, предварительно нужно перейти в нужный каталог.
### Запись изменений
[Руководство](https://git-scm.com/book/ru/v2/Основы-Git-Запись-изменений-в-репозиторий).
#### Немного теории
Итак, у нас имеется настоящий Git-репозиторий и рабочая копия файлов для некоторого проекта. Нам нужно сделать некоторые изменения и фиксировать «снимки» состояния (англ. __snapshots__ — снимки, фотографии) этих изменений в нашем репозитории каждый раз, когда проект достигает состояния, которое нам хотелось бы сохранить.

Каждый файл в рабочем каталоге может находиться в одном из двух состояний: *под версионным контролем* (__отслеживаемые__) и *нет* (__неотслеживаемые, untracked__). __Отслеживаемые файлы__ — это те файлы, которые были в последнем снимке состояния проекта; они могут быть __неизменёнными__ (__unmodified__), __изменёнными__ (__modified__) или __подготовленными к коммиту__ (__индексированными__, __staged__). Если кратко, то отслеживаемые файлы — это те файлы, о которых знает Git.
<p align="center">
  <img src="https://user-images.githubusercontent.com/125132889/221302594-1200b05e-6370-4f1e-a11e-40a010e8f419.png">
</p>

__Неотслеживаемые файлы__ — это всё остальное, любые файлы в нашем рабочем каталоге, которые не входили в наш последний снимок состояния и не подготовлены к коммиту. Если репозиторий клонировать впервые, все файлы будут отслеживаемыми и неизменёнными, потому что Git только что их извлек, и мы ничего пока не редактировали.

Как только мы отредактируем файл, Git будет рассматривать их как изменённые, так как мы изменили их с момента последнего коммита. Мы индексируем эти изменения, затем фиксируем (__commited__) все проиндексированные изменения и цикл повторяется.
#### Определение состояния файлов
Основной инструмент для определения состояний файлов — это команда `git status`. Если выполнить её сразу после клонирования, выведется что-то вроде этого:
```$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
```
Это означает, что у нас чистый рабочий каталог, другими словами — в нем нет отслеживаемых измененных файлов. Git также не обнаружил неотслеживаемых файлов, в противном случае они бы были перечислены здесь. Наконец, команда сообщает нам, на какой ветке мы находимся, и что она не расходится с веткой на сервере. Пока что это всегда ветка master/main/ветка по умолчанию.

Если мы добавим в проект новый файл, например, `README` и выполним `git status`, то увидим неотслеживаемый файл вот так:
```
$ echo 'My Project' > README
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    README
nothing added to commit but untracked files present (use "git add" to track)
```
Понять, что новый файл `README` не отслеживается, можно по тому, что он находится в секции «__Untracked files__» в выводе команды `status`. Статус Untracked означает, что Git видит файл, которого не было в предыдущем снимке состояния (коммите); Git не станет добавлять его в ваши коммиты, пока вы его явно об этом не попросите. Это предохранит вас от случайного добавления в репозиторий сгенерированных бинарных файлов или каких-либо других, которые мы и не думали добавлять. Попробуем добавить новый файл `README`.
#### Отслеживание новых файлов
Для того чтобы начать отслеживать (добавить под версионный контроль) новый файл, используется команда `git add` и название файла (если мы хотим начать отслеживать все изменения, используется `git add .`). `git add`выбирает файл/ы и перемещает его/их в промежуточную область, помечая его для включения в следующий коммит.
```
$ git add README
```
Если снова выполнить команду `git status`, можно увидеть, что файл `README` теперь отслеживаемый и добавлен в индекс:
```
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    new file:   README
```
Теперь файл проиндексирован, так как он находится в секции «__Changes to be committed__». Если выполнить коммит в этот момент, то версия файла, существовавшая на момент выполнения команды `git add`, будет добавлена в историю снимков состояния. Кому не терпится, введите `git commit -m "New Feature"`, а чтобы изменения отобразились в GitHub — `git push origin main` (вместо main подставьте ветку, которую нужно отправить). Эти действия выполняются на видео с [3:07](https://youtu.be/4evR80g--9k?list=PLg5SS_4L6LYstwxTEOU05E0URTHnbtA0l&t=187). На данный момент "запушить" изменения на GitHub получится только в случае, если вы *клонировали* репозиторий.

#### Индексация изменённых файлов
Попробуйте самостоятельно добавить в репозиторий файл `CONTRIBUTING.md`, проиндексировать его и выполнить коммит.

Попробуем изменить файл `CONTRIBUTING.md`, а после выполнить команду `git status`:
```
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
    new file:   README
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)
    modified:   CONTRIBUTING.md
```
Файл `CONTRIBUTING.md` находится в секции «__Changes not staged for commit__» — это означает, что отслеживаемый файл был изменён в рабочем каталоге, но пока не проиндексирован. Чтобы проиндексировать его, необходимо выполнить команду `git add`. Это многофункциональная команда, она используется для добавления под версионный контроль новых файлов, для индексации изменений, а также для других целей. Можно считать, что эта команда «добавляет *этот* контент в следующий коммит». После индексации выполним `git status`:
```
$ git add CONTRIBUTING.md
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
    new file:   README
    modified:   CONTRIBUTING.md
```
Строки `new file:   README` не будет, если вы из торопливых и уже выполнили коммит ранее.

Теперь оба файла проиндексированы и войдут в следующий коммит. В этот момент вы, предположим, вспомнили одно небольшое изменение, которое хотите сделать в `CONTRIBUTING.md` до коммита. Вы открываете файл, вносите и сохраняете необходимые изменения и вроде бы готовы к коммиту. Но давайте-ка ещё раз выполним `git status`:
```
$ vim CONTRIBUTING.md
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
    new file:   README
    modified:   CONTRIBUTING.md
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)
    modified:   CONTRIBUTING.md
```
Теперь `CONTRIBUTING.md` отображается как проиндексированный и непроиндексированный одновременно. Как такое возможно? Такая ситуация наглядно демонстрирует, что Git индексирует файл в точности в том состоянии, в котором он находился при выполнилнении команды `git add`. Если выполнить коммит сейчас, то файл `CONTRIBUTING.md` не будет содержать последние изменения, то есть текущее состояние файла в рабочем каталоге не учитывается. Если изменить файл после выполнения `git add`, придётся снова выполнить `git add`, чтобы проиндексировать последнюю версию файла:
```
$ git add CONTRIBUTING.md
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
    new file:   README
    modified:   CONTRIBUTING.md
```
#### Коммит изменений
Теперь, когда ваш индекс находится в таком состоянии, как вам и хотелось, вы можете зафиксировать свои изменения. Запомните, всё, что до сих пор не проиндексировано — любые файлы, созданные или изменённые вами, для которых вы не выполнили `git add` после редактирования — не войдут в этот коммит. Они останутся изменёнными файлами на вашем диске. Простейший способ зафиксировать изменения — это набрать `git commit`. Эта команда откроет выбранный вами текстовый редактор.

В редакторе будет отображён следующий текст (это пример окна Vim):
```
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Your branch is up-to-date with 'origin/master'.
#
# Changes to be committed:
#	new file:   README
#	modified:   CONTRIBUTING.md
#
~
~
~
".git/COMMIT_EDITMSG" 9L, 283C
```
Вы можете видеть, что комментарий по умолчанию для коммита содержит закомментированный результат работы команды `git status` и ещё одну пустую строку сверху. Вы можете удалить эти комментарии и набрать своё сообщение или же оставить их для напоминания о том, что вы фиксируете. Когда вы выходите из редактора, Git создаёт для вас коммит с этим сообщением.

Есть и другой способ — вы можете набрать свой комментарий к коммиту в командной строке вместе с командой `commit`, указав его после параметра __-m__, как в следующем примере:
```
$ git commit -m "Story 182: fix benchmarks for speed"
[master 463dc4f] Story 182: fix benchmarks for speed
 2 files changed, 2 insertions(+)
 create mode 100644 README
```
Итак, коммит создан! Вы можете видеть, что коммит вывел вам немного информации о себе: на какую ветку вы выполнили коммит (master), какая контрольная сумма SHA-1 у этого коммита (463dc4f), сколько файлов было изменено, а также статистику по добавленным/удалённым строкам в этом коммите.

Каждый раз, когда вы делаете коммит, вы сохраняете снимок состояния вашего проекта, который позже вы можете восстановить или с которым можно сравнить текущее состояние.
### Заключение
Мы немного познакомились с Git: научились создавать и клонировать репозитории, определять состояние файлов, отслеживать новые файлы и изменения, выполнять коммит и даже "пушить" изменения на GitHub. Безусловно, мы рассмотрели только малую часть того, что представляет собой Git, не затронули многие команды, например, `git log` — позволяет смотреть историю коммитов. С другими полезными командами можно ознакомится в [шпаргалке](https://training.github.com/downloads/ru/github-git-cheat-sheet/), которая приводилась ранее. В дополнительных материалах будет ссылка на учебник по Git на русском языке, а также на более подробный вводный курс. 

__*Желаю удачи в дальнейшем изучении Git!*__
# Дополнительные материалы
[Учебник по Git на русском языке](https://git-scm.com/book/ru/v2)

[Вводный курс по Git](https://smartiqa.ru/courses/git) от [smartiqa.ru](https://smartiqa.ru/about).
