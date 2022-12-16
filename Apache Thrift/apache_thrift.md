![[apache-thrift.png]]

# Apache Thrift. 
**Apache Thrift** — это фреймворк для реализации RPC в сервисах с многоязычной поддержкой. **RPC (удаленный вызов процедур)** подобен вызову функции, только он присутствует удаленно на другом сервере в качестве службы. Служба предоставляет множество таких функций/процедур своему клиенту. И клиенту требуется узнать, какие функции/процедуры предоставляются этой службой и каковы их параметры. 

Здесь на помощь приходит Apache Thrift. У него есть собственный «язык определения интерфейса» (IDL). На этом языке вы определяете, что такое функции и каковы их параметры. А затем используйте компилятор Thrift для создания соответствующего кода для любого языка по вашему выбору. Это означает, что вы можете реализовать функцию в Java, разместить ее на сервере, а затем удаленно вызвать из Python. 

Важная работа фреймворка, такого как Thrift, заключается в следующем: 
1. Обеспечьте независимый от языка, язык определения интерфейса. 
2. Компилятор для компиляции этого IDL для создания клиентского и серверного кода (на одном или разных языках по мере необходимости). 
3. Сгенерированный компилятором клиентский код предоставляет интерфейсы-заглушки для этих функций. Код-заглушка преобразует параметры, переданные функции, в двоичный (сериализованный) формат, который можно передавать по проводам по сети. Этот процесс называется marshalling. Сгенерированный клиентский код никогда не имеет фактической реализации функции, поэтому он называется заглушкой. 
4. На сервере разработчик использует сгенерированный компилятором серверный код, чтобы фактически реализовать эти функции (т.е. написать фактическую функциональность функции). Сгенерированный код на стороне сервера получает двоичное закодированное сообщение от клиента, преобразует его обратно в соответствующие языковые объекты и передает его функции, реализованной разработчиком. Это называется unmarshaling. Например, в Java сгенерированный компилятором серверный код будет интерфейсом, который будет реализовывать разработчик, а также различными другими классами. 
5. Точно так же результат функции преобразуется в двоичный файл и отправляется клиенту.

Для параметров функции IDL определяет собственный набор типов структур данных, таких как List, Map, Struct или Classes, помимо встроенных типов, таких как Int, String, Boolean и т. д. Затем они сопоставляются с соответствующими языковыми реализациями. 

Thrift похож на SOAP и CORBA. Поскольку они оба используются для RPC и предоставляют собственный IDL. CORBA и SOAP обычно также имеют брокера обнаружения служб в качестве промежуточного программного обеспечения для предоставления функций/методов клиенту. Из соображений экономии мы обычно используем Zookeeper для обнаружения сервисов.

REST отличается тем, что не имеет IDL и использует HTTP-методы, такие как GET, PUT и шаблоны URL-адресов, для вызова удаленной функции и передачи параметров. Использование методов HTTP и семантики URL-адресов делает его также независимым от языка. 

Очередь сообщений совершенно другая. Потому что он в основном используется в модели Publish/Subscribe. Принимая во внимание, что RPC - это модель Client/Server. 

В модели Publish/Subscribe несколько "издателей" отправляют/добавляют сериализованное сообщение в очередь. Формат сообщения определяется "издателем" и имеет над ним полный контроль. Их определение семантически связано с очередью, в которой они опубликованы, но строгой проверки их структуры нет. "Подписчик", зная, какое сообщение будет в очереди, подписывается на эти сообщения. "Издатели" не знают, кто является клиентом, а "подписчики" не знают, кто является создателем сообщения. Они знают только, какое сообщение публиковать или потреблять, соответственно, из очереди. Издатель и подписчик несут ответственность за знание правильного сериализатора и десериализатора. Это отличается в Client/Server RPC, поскольку клиент знает (в строгом смысле), что передавать, а сервер определяет это. А также кого пропускать.

# Сравнение Thrift с аналогами

Существуют различные причины, по которым вы можете захотеть использовать Thrift, а не что-то вроде JSON/HTTP.

**Сильная типизация.** JSON отлично подходит, если вы работаете с языками сценариев (Python, Ruby, PHP, JS и т. д.). Однако, если вы создаете значительную часть своего приложения на языке со строгой типизацией, таком как C++ или Java, работа с JSON часто становится головной болью, запутывая то, что вы пытаетесь сделать, а не проясняя его. Thrift позволяет прозрачно работать с сильными, нативными типами, а также предоставляет механизм для создания исключений на уровне приложения по сети.

**Производительность.** Производительность является одним из основных соображений дизайна Thrift. JSON/HTTP гораздо больше ориентированы на удобство чтения кода для человека, что достигается за счет того, что они более интенсивно используют ЦП для работы.

**Эффективность сериализации.** Если вы сериализуете большие объемы данных, двоичный протокол Thrift более эффективен, чем JSON. (Отмечу, что существуют определенно более эффективные механизмы, чем Thrift, и вы также можете сэкономить место, используя сжатие, так что все дело в поиске предпочтительного компромисса между простотой использования и накладными расходами ЦП/пространства.)

**Поддержка версий.** Thrift имеет встроенные механизмы управления версиями данных. Это может быть очень полезно в распределенной среде, где интерфейсы ваших служб могут меняться, но вы не можете атомарно обновить весь свой клиентский и серверный код.

**Серверные реализации.** Thrift включает реализации сервера RPC для ряда языков. Поскольку они оптимизированы только для поддержки запросов Thrift, они легче и более производительны, чем типичные реализации HTTP-сервера.

Таким образом, если вы предоставляете сложную и часто меняющуюся услугу, Thrift сократит количество времени, которое вы тратите на повторение как клиентского, так и серверного интерфейсов.

Наконец, если ваш сервис является полностью внутренним по отношению к вашему продукту/компании, использование Thrift станет огромной победой, поскольку оно устранит барьеры для общения на разных языках и в разных конфигурациях.

# Система типов Thrift

**Thrift** система типов включает в себя базовые типы, такие как bool, byte, double, string и integer, а также специальные типы, такие как двоичные, а также поддерживает структуры (эквивалентные классам, но без наследования), а также контейнеры (список, набор, карта), которые соответствуют общедоступным интерфейсам в большинстве языков программирования. Система типов фокусируется на ключевых типах, доступных во всех языках программирования, и опускает типы, характерные только для некоторых языков программирования.
- Далее следует описание системы типов Thrift, а более подробную информацию можно найти здесь: http://thrift.apache.org/docs/types 
- Если вы хотите проверить язык описания интерфейса Thrift, который позволяет определять типы Thrift, вы можете прочитать здесь: http://thrift.apache.org/docs/idl

## Базовые типы

> -   **bool**: Логическое значение (true или false)
> -   **byte**:  8-битное целое число со знаком
> -   **i16**: 16-битное целое число со знаком
> -   **i32**: 32-битное целое число со знаком
> -   **i64**: 64-битное число с плавающей запятой
> -   **double**: A 64-bit floating point number
> -   **string**: Текстовая строка, закодированная с использованием кодировки UTF-8.

Примечание: Целочисленные типы без знака не поддерживаются из-за того, что во многих языках программирования нет собственных целочисленных типов без знака. При необходимости целые числа со знаком можно безопасно преобразовать в их беззнаковые аналоги.

## Специальные типы

**Двоичный**: последовательность незакодированных байтов

## Структуры

Структура имеет набор строго типизированных полей, каждое из которых имеет уникальный идентификатор имени. Внешний вид очень похож на C-подобные структуры.

~~~
struct Example {
  1:i32 number=10,
  2:i64 bigNumber,
  3:double decimals,
  4:string name="thrifty"
}
~~~

## Контейнеры

> -   **list** (Сопоставляется с  C++ STL vector , Java ArrayList и так далее)
>     
> -   **set** (Сопоставляется с С++ STL set, Java HashSet и так далее)
>     
>  -   PHP не поддерживает наборы, поэтому обрабатывается аналогично List
>     
> -   **map** (Сопоставляется с С++ STL map, Java HashMap и так далее)
>     

Все вышеперечисленное является настройками по умолчанию, но может быть настроено для соответствия различным типам любого языка. По этой причине были добавлены директивы генерации пользовательского кода.

## Исключения

Они наследуются от собственного базового класса исключений соответствующим образом в каждом целевом языке программирования.

~~~
exception InvalidOperation {
1: i32 what,
2: string why
}
~~~
## Службы

Служба состоит из набора именованных функций, каждая из которых имеет список параметров и тип возвращаемого значения. Это семантически эквивалентно определению интерфейса или чистого виртуального абстрактного класса.

~~~service <name> {
<returntype> <name>(<arguments>)
[throws (<exceptions>)]
...
}

An example:
service StringCache {
void set(1:i32 key, 2:string value),
string get(1:i32 key) throws (1:KeyNotFound knf),
void delete(1:i32 key)
}
~~~

## Пример использования Apache Thrift

На этом примере я продемонстрирую создание простого сервиса умножения.

-   Давайте сначала создадим .thrift определение нашего сервиса. 
    ~~~
    namespace java tutorial
    namespace py tutorial
    
    typedef i32 int // We can use typedef to get pretty names for the types we are using
    service MultiplicationService
    {
            int multiply(1:int n1, 2:int n2),
    }
	~~~
-   Назовите этот файл multi.thrift, а затем запустите приведенные ниже команды, чтобы сгенерировать код для java и python.
    ~~~
    thrift --gen java multiple.thrift
    thrift --gen py multiple.thrift
    ~~~

После запуска команд Thrift должен сгенерировать код внутри каталогов gen-java/tutorial и gen-py/tutorial для Java и Python соответственно. Не забудьте использовать sudo, если каталоги не созданы! Было бы полезно взглянуть на этот код, чтобы лучше понять, какой код генерирует для вас Thrift. Вы можете найти краткое объяснение кода здесь: [Thrift’s auto-generated code for the multiplication service example](https://thrift-tutorial.readthedocs.io/en/latest/multiplication-service.html).

-   Now we are ready to write our own code. Lets first write some Java code for our client and server and then we will also write a Python client to send requests to our server. We will not need to change anything on the server part to do this!

### Обработчик умножения

Ниже представлен класс MultiplicationHandler, в котором реализова интерфейс, указанный ранее в нашем определении multi.thrift, и для которого Thrift уже сгенерировал код.
~~~
> import org.apache.thrift.TException;
> 
> public class MultiplicationHandler implements MultiplicationService.Iface {
> 
> 	@Override
> 	 public int multiply(int n1, int n2) throws TException {
> 	    System.out.println("Multiply(" + n1 + "," + n2 + ")");
> 	    return n1 * n2;
> 	 }
> 
> 	
> }
~~~

### Java Сервер умножения

Ниже представлен класс MultiplicationServer, в котором реализован простой сервер. Единственное, что стоит упомянуть о реализации сервера, — это использование класса Processor, автоматически сгенерированного Thrift. Процессор делает две простые вещи. Считывает данные из входного потока и записывает данные в выходной поток. Процессор считывает данные со входа, обрабатывает данные (фактически использует обработчик, указанный пользователем для обработки данных) и записывает обработанные данные на выход. Наконец, я должен упомянуть, что для этого примера я использовал простую серверную реализацию, но было бы так же просто использовать любую из реализаций, предлагаемых thrift (threadPoolServer или nonBlockingServer).

~~~
> import org.apache.thrift.TException;
> import org.apache.thrift.protocol.TBinaryProtocol;
> import org.apache.thrift.protocol.TProtocol;
> import org.apache.thrift.transport.TSocket;
> import org.apache.thrift.transport.TTransport;
> 
> public class MultiplicationClient {
>   public static void main(String [] args) {
> 
>    
>     try {
>       TTransport transport;
>      
>       transport = new TSocket("localhost", 9090);
>       transport.open();
> 
>       TProtocol protocol = new  TBinaryProtocol(transport);
>       MultiplicationService.Client client = new MultiplicationService.Client(protocol);
> 
>       perform(client);
> 
>       transport.close();
>     } catch (TException x) {
>       x.printStackTrace();
>     } 
>   }
> 
>   private static void perform(MultiplicationService.Client client) throws TException
>   {
>    
>     int product = client.multiply(3,5);
>     System.out.println("3*5=" + product);
>   }
> }

### Python Multiplication Client[](https://thrift-tutorial.readthedocs.io/en/latest/usage-example.html#python-multiplication-client "Permalink to this headline")

The python client implements anything as discussed for the java client. The language syntax is the only thing I had to change on my approach.

> #!/usr/bin/env python
> 
> import sys
> sys.path.append('../gen-py')
> 
> from tutorial import MultiplicationService
> from tutorial.ttypes import *
> 
> from thrift import Thrift
> from thrift.transport import TSocket
> from thrift.transport import TTransport
> from thrift.protocol import TBinaryProtocol
> 
> try:
> 
>   # Make socket
>   transport = TSocket.TSocket('localhost', 9090)
> 
>   # Buffering is critical. Raw sockets are very slow
>   transport = TTransport.TBufferedTransport(transport)
> 
>   # Wrap in a protocol
>   protocol = TBinaryProtocol.TBinaryProtocol(transport)
> 
>   # Create a client to use the protocol encoder
>   client = MultiplicationService.Client(protocol)
> 
>   # Connect!
>   transport.open()
> 
>   product = client.multiply(4,5)
>   print '4*5=%d' % (product)
> 
>   # Close!
>   transport.close()
> 
> except Thrift.TException, tx:
>   print '%s' % (tx.message)
~~~~

### Клиент умножения Java

Важно отметить в клиентском коде использование TBinaryProtocol для сериализации и десериализации. Стоит отметит, что можно использовать компактный, протокол JSON или любой другой протокол, поддерживаемый thrift. Дополнительные сведения о протоколах, которые вы можете использовать, можно найти в [Thrift protocol stack](https://thrift-tutorial.readthedocs.io/en/latest/thrift-stack.html). Еще одна важная вещь, на которую следует обратить внимание, — это использование клиента и соответствующего метода client.multiply(), предоставленного нам автоматически сгенерированным кодом экономии. Этот метод вызывает другой метод TServiceClient.sendBase(), который записывает данные в сеть.

~~~
> import org.apache.thrift.TException;
> import org.apache.thrift.protocol.TBinaryProtocol;
> import org.apache.thrift.protocol.TProtocol;
> import org.apache.thrift.transport.TSocket;
> import org.apache.thrift.transport.TTransport;
> 
> public class MultiplicationClient {
>   public static void main(String [] args) {
> 
>    
>     try {
>       TTransport transport;
>      
>       transport = new TSocket("localhost", 9090);
>       transport.open();
> 
>       TProtocol protocol = new  TBinaryProtocol(transport);
>       MultiplicationService.Client client = new MultiplicationService.Client(protocol);
> 
>       perform(client);
> 
>       transport.close();
>     } catch (TException x) {
>       x.printStackTrace();
>     } 
>   }
> 
>   private static void perform(MultiplicationService.Client client) throws TException
>   {
>    
>     int product = client.multiply(3,5);
>     System.out.println("3*5=" + product);
>   }
> }
~~~

### Клиент умножения Python

Клиент Python реализует все, что обсуждалось для клиента Java. Синтаксис языка — единственное, отличие.

~~~
> #!/usr/bin/env python
> 
> import sys
> sys.path.append('../gen-py')
> 
> from tutorial import MultiplicationService
> from tutorial.ttypes import *
> 
> from thrift import Thrift
> from thrift.transport import TSocket
> from thrift.transport import TTransport
> from thrift.protocol import TBinaryProtocol
> 
> try:
> 
>   # Make socket
>   transport = TSocket.TSocket('localhost', 9090)
> 
>   # Buffering is critical. Raw sockets are very slow
>   transport = TTransport.TBufferedTransport(transport)
> 
>   # Wrap in a protocol
>   protocol = TBinaryProtocol.TBinaryProtocol(transport)
> 
>   # Create a client to use the protocol encoder
>   client = MultiplicationService.Client(protocol)
> 
>   # Connect!
>   transport.open()
> 
>   product = client.multiply(4,5)
>   print '4*5=%d' % (product)
> 
>   # Close!
>   transport.close()
> 
> except Thrift.TException, tx:
>   print '%s' % (tx.message)
~~~