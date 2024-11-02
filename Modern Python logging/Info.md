https://www.youtube.com/watch?v=9L77QExPmI0&t=657s

https://github.com/mCodingLLC/VideosSampleCode

https://github.com/mCodingLLC/VideosSampleCode/tree/master/videos/135_modern_logging

---

Объекты класса Logger (регистраторы) — это то, что мы фактически используем в своем коде.
У них есть например метод .info(), и мы можем вызвать logger.info() для регистрации информационных сообщения. Также есть logger.debug() для регистрации отладочных сообщений, logger.exception() для регистрации исключения в процессе и т. д.

Logger создает LogRecord (например при вызове метода .info()), который является объектом, содержащим всевозможную полезную контекстную информацию для регистации, а именно, такие вещи, как:

    - сообщение (message)
    - серьезность (severity)
    - текущее время (current time)
    - текущий поток (current thread) или async task
    - местоположение в исходном коде (location in the source code)
    - и т.д.

Каждый регистратор может установить уровень, чтобы отбрасывать все сообщения ниже определенной серьезности, и, при необходимости, некоторые фильтры, чтобы отбрасывать или изменять сообщения по пути.
Так что вы можете сделать что-то вроде удаления всех сообщений, начинающихся с "some annoying string (какой-то раздражающей строки). Или вы можете сделать что-то более сложное, например, удалить личные данные пользователя, которые не должны отображаться в журналах.
Затем регистратор поочередно передает эти записи журнала каждому из своих обработчиков. Обработчики сообщают вам, как и где регистрировать запись, например, в стандартном выводе, в файле, по электронной почте или в коммерческой службе регистрации.
Каждый обработчик получает запись журнала и, как и у регистраторов, у обработчика есть уровень и некоторые фильтры, которые позволяют ему удалять или изменять сообщение по пути.
Если запись удалена обработчиком, она все равно передается остальным
обработчикам. Но если его сбросил сам регистратор, то он сбросился навсегда.
Если предположить, что сообщение проходит через уровни и фильтры, то когда
обработчику приходит время фактически записать сообщение журнала, ему
необходимо записать текст. Но в настоящее время это объект Python. Поэтому
у каждого обработчика есть форматер, который он использует для преобразования
объекта записи журнала в строку для отправки.
Форматировщик позволяет вам настраивать внешний вид отдельного сообщения.
Например, это уровень журнала, а затем сообщение, или уровень, затем
временная метка, затем сообщение, или, может быть, вы пишете JSON, или,
может быть, вы пишете какой-то другой формат.
Форматировщики, как правило, являются тем местом, где вы видите больше
всего настроек, поскольку именно форматировщик выбирает, какие данные из
записи журнала фактически включить в сообщение, и это во многом зависит
от вашего конкретного варианта использования и того, что вы хотите видеть
в своих журналах.
И это почти полная картина.
За исключением того, что это картина для корневого регистратора,
корня, как в корне дерева регистраторов.
Регистраторы доступны и создаются по имени, и если вы разделите имя точками,
то в итоге получите дерево регистраторов.

Таким образом, регистратор A.X является дочерним элементом регистратора A,
который является дочерним элементом корня.
По умолчанию после того, как дочерний процесс завершает обработку LofRecord,
он передает ее своему родителю.
Таким образом, если эта запись журнала была сгенерирована здесь, в
регистраторе A.X, то все обработчики A.X будут запущены, затем она
распространится на A, и все обработчики A будут запущены, затем она
распространится на корень, и все корневые обработчики будут запущены.
Это сделано для того, чтобы пользователям было проще отключать сообщения
от целых подсистем, просто отключив определенные регистраторы.
Опять же, если запись удалена обработчиком, она продолжит движение, включая
распространение до родительской записи.
Но если его сбросит логгер, то он остановится и не будет распространяться.
Но не торопитесь, это гораздо более гибкий подход, чем вам обычно требуется.
Наличие всех этих обработчиков, фильтров и распространения на разных
уровнях неоправданно сложно для большинства случаев использования.
И это часто приводит к тонко сломанным конфигурациям.
Итак, вот что я рекомендую.
Просмотреть все эти некорневые обработчики Удалить их.
Если у вас нет веской причины, поместите все обработчики на корневой
регистратор. Это проще, но также размещение всех обработчиков в корневом
регистраторе гарантирует, что любые сообщения, сгенерированные сторонними
библиотеками, будут регистрироваться и форматироваться так же, как
сообщения, сгенерированные вашим собственным приложением.
Фильтры. То же самое.
Есть большая вероятность, что вам вообще не понадобятся никакие фильтры,
но если вы все же решите применить их, поместите их все на корневой
регистратор или его обработчики.
Оставьте propagation (распространение) включенным (это значение по
умолчанию), чтобы все сообщения распространялись до корневого регистратора.
Однако не используйте корневой логгер в своем коде.
Если вы используете любую из функций ведения журнала верхнего уровня,
например logging.info, то она использует корневой регистратор.
Поэтому не используйте ни одну из этих функций.
Обязательно используйте собственный регистратор, который вы получаете,
используя logging.getLogger и передавая имя нужного вам регистратора.
Это сначала создаст регистратор, если его еще нет, затем вы можете
использовать свой logger.info вместо logging.info.
И помните, у вашего регистратора нет обработчиков.
Мы зависим от propagation, чтобы отправлять все события в корневой
регистратор и чтобы корневой регистратор фактически обрабатывал события.
Если у вас небольшое или среднее приложение, вам достаточно одного
некорневого регистратора. Если у вас очень большое приложение, вам
следует создать один некорневой регистратор для каждого основного
подкомпонента вашего приложения.
Вам определенно не нужен регистратор для каждого файла.
Это было бы пустой тратой, потому что это глобальные переменные, которые
живут в течение всего срока службы программы.

После всего этого давайте вернемся к настройке ведения журнала для
нескольких распространенных настроек с помощью dictConfig.

Пример: журнал в stdout
В качестве основы давайте просто создадим простую конфигурацию, которая
записывает все в stdout.
Если вы когда-нибудь запутаетесь в конфигурации, нарисуйте ее вот так,
а затем используйте изображение, чтобы заполнить конфигурацию.
"version" обязательна, и единственное допустимое значение — 1.
Это нужно для того, чтобы они могли изменить все в будущем, не нарушая
старый код.
"disable_existing_loggers" делает то, что говорит, он отключает все,
что явно не указано в этой конфигурации. Я собираюсь пойти дальше и
установить это в false, чтобы я мог получать сообщения журнала из
стороннего кода.
В этой конфигурации нет фильтров, поэтому давайте просто удалим это.
Затем определите форматировщик с именем "simple" и задайте ему простую
строку форматирования.
Мы не указали, к какому классу относится этот форматировщик, поэтому по
умолчанию он просто использует встроенный logging.Formatter.
Он принимает строку форматирования вот так, используя эту странную строку
форматирования в стиле printf.
Да, это немного странно, но просто смиритесь с этим или, предвосхищая
ситуацию, подождите минуту, и мы увидим лучший способ.
Если вы хотите настроить свой собственный формат, вы можете найти список
всех доступных переменных в документации по журналированию.
Далее нам нужно определить один обработчик stdout, поэтому мы создаем этот
один обработчик с именем "stdout" и устанавливаем наш "простой" форматировщик
в качестве форматировщика для этого обработчика.
Чтобы заставить его на самом деле выводить данные на stdout, мы устанавливаем
его класс на встроенный обработчик потока журналирования с потоком
sys.stdout. Косая черта "ext://" здесь означает "внешний", так как это
переменная, которая определена вне этой конфигурации.
И вуаля! Всего за 16 строк мы настроили то, что базовая конфигурация делала в
одной строке.
Я знаю, знаю, но имейте в виду, что этот более подробный стиль будет намного
понятнее, когда у нас будет больше событий.
Так что оставайтесь со мной.

logging JSON/YAML config
Несмотря на то, что мы используем dictConfig, это не значит, что нам нужно
хранить конфигурацию ведения журнала в виде буквального словаря в нашем
исходном коде Python. В этом нет ничего плохого, но многие считают удобным
хранить конфигурацию ведения журнала в отдельном файле в формате JSON
или YAML.

Лично я предпочитаю хранить конфигурацию в формате JSON, поэтому создайте
версию конфигурации в формате JSON, а затем загрузите ее при запуске приложения.
Если бы вы хотели использовать YAML, то все выглядело бы в основном так же,
за исключением того, что, конечно, у вас была бы конфигурация YAML, и вы бы
«импортировали yaml» и загрузили YAML вместо загрузки JSON.
Давайте поместим их рядом, чтобы вы могли видеть две конфигурации.
Очевидно, что YAML намного более сжат, но я также считаю, что он гораздо более
подвержен ошибкам.
И, кроме того, в Python нет встроенного парсера YAML, тогда как есть встроенный
парсер JSON. Поэтому, если бы вы хотели, вам пришлось бы подключить его как зависимость.
«pyyaml» — популярный выбор.
Хранение конфигурации журнала в отдельном файле также позволяет вашим пользователям
настраивать конфигурацию журнала в соответствии со своими предпочтениями.
Знаете, если вы доверяете своим пользователям делать такие вещи.
Пример: ошибки в stdedd и все в файл Second настройка. Давайте изменим конфигурацию
так, чтобы ошибки отправлялись в stderr, а затем все журналы отправлялись в файл.
Измените обработчик "stdout" на "stderr" и установите его уровень на "WARNING".
Затем создайте новый обработчик и установите его класс на RotatingFileHandler.
Обработчик ротационных файлов продолжает добавлять журналы в файл, пока он не
достигнет определенного размера, в данном случае 10 килобайт.
После достижения 10 килобайт он создает резервную копию и начинает новый файл.
После трех резервных копий он начинает удалять самую старую.
10 килобайт — это довольно небольшой предел, это просто для того, чтобы вы
могли видеть, как происходит смена.
Вероятно, вы захотите выбрать несколько мегабайт.
После запуска скрипта несколько раз вы можете увидеть, что он в конечном
итоге создал этот "my_app.log.1", а затем снова начал использовать
"my_app.log".
Мы все еще используем здесь "простой" форматировщик.
Но поскольку мы сохраняем в файл журнала, почему бы нам не включить некоторые
дополнительные подробности?
Мы достигаем этого, добавляя этот новый "подробный" форматировщик и
устанавливая его в качестве форматировщика для обработчика "файла".
Мы включаем гораздо больше информации в строку форматирования, и мы также
демонстрируем здесь формат "datefmt", который позволяет нам настраивать
способ печати дат.
Совет профессионала: используйте формат, совместимый с ISO-8601, и включайте
часовой пояс. Поверьте мне.

Таким образом, наш журнал содержит гораздо больше полезной контекстной
информации.
Для многих приложений это отличное место, чтобы остановиться.
Но если вы действительно заботитесь о качестве данных журнала, то я
настоятельно рекомендую внести одно важное изменение.
Взгляните на этот файл журнала.
Просматривая его, я могу визуально отличить разные сообщения друг от друга,
но обратите внимание, что здесь есть трассировки.
А что, если бы в сообщениях журнала были новые строки?

Журналы JSON
Если бы я хотел проанализировать это программно, мне нужно было бы иметь
возможность проанализировать все данные, которые я в него вставил.
Но это просто текст в свободной форме с новыми строками, которые могут быть
где угодно в этой точке.
Это довольно неразрешимо.
Решение? Хранить постоянные журналы в формате JSON, чтобы их можно было
легко проанализировать позже.
Это изменение в том, как преобразовать запись журнала в строку, так что
это работа форматировщика, нам нужен форматировщик JSON.
Но, подождите, нет встроенного форматировщика JSON для ведения журнала.
Есть несколько, которые можно установить с помощью pip, но давайте просто
напишем свой собственный.
Предположим, что мы это сделали, вы могли бы подумать, что вы сможете просто
установить здесь ключ "class", а затем передать любые аргументы здесь,
и это будут аргументы ключевых слов в конструктор.
Вот что происходит здесь с обработчиком, верно?
Эээ, нет.
Вы можете использовать здесь свой собственный класс, используя ключевое
слово "class", но если вы это сделаете, то все ключи будут жестко
закодированы, чтобы быть теми, которые использует встроенный/
Так что я мог бы использовать "format" и "datefmt", но я не мог бы создать
свой собственный "fmt_keys".
Почему так? Отличный вопрос! Двигаемся дальше.
Измените "class" на "()", и тогда он сделает то, что вам на самом деле нужно:
вызовите это и передайте это как аргумент ключевого слова.
Вам придется делать то же самое в любом другом месте конфигурации, как если
бы я создал свой собственный обработчик, интерфейс которого отличается от
встроенного.
Ладно, разобравшись с этой странной проблемой, продолжим.
Итак, мы передадим эти ключи формата, которые будут словарем, где ключ — это
ключ, который я хочу отобразить в сообщении журнала, а значение здесь,
например «levelname», — это переменная, которую мы будем искать в записи
журнала.
Ладно, давайте продолжим и напишем этот класс.
Мы находимся в новом файле и просто наследуем от встроенного Formatter для
ведения журнала.
Ничего особенного в init, мы просто сохраняем ключи формата, которые
получаем из конфигурации.
Затем нам нужно определить эту функцию «format».
Это то, что берет запись и преобразует ее в строку.
Я использую здесь «@override», чтобы указать, что мы переопределяем что-то
из родительского класса.
Это не обязательно, но это хорошая привычка — отмечать такие вещи.
Все, что мы делаем, это извлекаем данные записи в словарь, а затем
используем модуль «json», чтобы вывести их в строку.
Что касается фактического извлечения этих полей, это довольно просто.
Независимо от конфигурации, я решил включить сообщение и временную метку
в формате ISO в часовом поясе UTC.

Мы извлекаем любые данные об исключениях, если они присутствуют, используя
некоторые родительские методы, чтобы извлечь все красиво.
А для остальных ключей мы просто извлекаем их из атрибутов записи.
Это довольно просто, и вы, вероятно, можете делать здесь все, что захотите.
И donzo! Обновите конфигурацию, чтобы использовать новый форматировщик JSON, и все готово.
Проверьте наш файл журнала, и мы увидим хорошо отформатированный JSON.
Небольшое предупреждение, однако, этот файл не является допустимым JSON.
Каждая строка является допустимым JSON.
Этот формат называется JSON Lines, а общее расширение файла — «.jsonl».
Поэтому для его анализа вы просто читаете файл построчно и анализируете каждую
строку как JSON.
Дополнительный контекст с дополнительным параметром
И двойной совет: теперь, когда мы выводим JSON, на самом деле очень легко
добавить много дополнительной контекстной информации.
Для этого мы можем просто использовать аргумент «extra» в одном из наших
вызовов журнала.
Дайте ему словарь дополнительной информации, и Python внесет ее в запись журнала.
Затем просто обновите ваш форматировщик, чтобы извлечь эти дополнительные
атрибуты, и теперь любые дополнительные данные будут отображаться в нашем JSON.
Вот {"x": "hello"}.

Пользовательский фильтр
Если вы получаете слишком много журналов и хотите более точно контролировать,
какие из них удалять, вам может понадобиться фильтр.
Процесс создания пользовательского фильтра очень похож на создание пользовательского
форматировщика.
Наследуйте от встроенного фильтра, затем определите собственное переопределение
функции "filter".
После записи вы возвращаете bool, чтобы указать, следует ли обрабатывать эту запись.
Таким образом, этот фильтр без ошибок делает нечто противоположное установке уровня
на "INFO".
Установка уровня на "INFO" будет означать, что вы сохраните только сообщения,
которые были "INFO", "WARNING", "ERROR", "CRITICAL", но установка этого фильтра
без ошибок даст вам вместо этого "DEBUG" и "INFO".
Вы также можете изменить запись здесь, например, если вы хотите подвергнуть
цензуре личные данные или вернуть измененную копию.
Я не буду разбираться с фильтрами в оставшейся части видео, но вот домашнее задание.
Используя этот фильтр без ошибок, создайте конфигурацию ведения журнала,
которая выводит обычные сообщения на stdout, а сообщения об ошибках на stderr.
Фильтр вам понадобится для предотвращения дубликатов.
Явный недостаток
Ладно, ладно, наверняка больше нет явных недостатков в этой настройке ведения журнала, верно?
Рискуя использовать запрещенное слово в Python, давайте поговорим о производительности.
По своей природе вызов функции журнала приводит к вводу-выводу.
Если пользователь делает запрос к моему веб-приложению, и это приводит к 10 сообщениям
журнала, я не хочу добавлять 10 циклов выполнения в мою службу ведения журнала,
прежде чем я отвечу своему пользователю.
Но в настоящее время это то, что произойдет, потому что все вызовы ведения журнала
синхронные и блокирующие.
Решение? Используйте QueueHandler для выхода из основного потока.
Выход из основного потока с помощью QueueHandler Сбор данных журнала — не медленная часть.
Медленная часть — отправка их туда, куда нужно.
Обработчик очереди хранит ваши записи журнала в очереди без блокировки, в то время
как связанный прослушиватель очереди принимает эти сообщения и передает их другим
обработчикам в другом потоке.
Чтобы настроить это, создайте новый обработчик очереди в своей конфигурации.
Класс — «logging.handlers.QueueHandler», а затем он принимает другой список обработчиков.
Это обработчики, которым он отправляет, так что по сути возьмите обработчики,
которые у вас были в корневом обработчике раньше, поместите их сюда, а затем
измените обработчик очереди, чтобы он был вашим единственным обработчиком в корне.
Этот «respect_handler_level» по какой-то причине по умолчанию имеет значение false,
что приводит к поведению отправки каждого сообщения каждому обработчику независимо
от уровня журнала, так что да, это, вероятно, не то, что нам нужно.
Я собираюсь установить это в значение true, чтобы оно делало то, что вы ожидаете.
Есть еще одна вещь, которую нам нужно обработать здесь в основном файле, а именно,
поскольку обработчик очереди запускает поток, это не то, что произойдет автоматически.
Когда мы настраиваем наше ведение журнала, нам нужно вручную запустить этот поток.
Мы достигаем этого, получая обработчик очереди по имени, а затем, если он существует,
мы запускаем поток его слушателя.
Мы также регистрируем обратный вызов atexit, чтобы вызвать метод stop слушателя
и корректно завершить его работу, когда программа завершится.
В качестве альтернативы, если вы хотите сохранить всю работу внутри конфигурации,
вы также можете создать подкласс класса обработчика очереди и заставить его делать
это в его init.
Успех!
И успех!
Наконец-то у нас есть высококачественная, анализируемая, многоцелевая, неблокирующая
настройка ведения журнала для нашего приложения Python.
Здорово, не так ли?
Библиотечное ведение журнала?
Но заметьте, я сказал ведение журнала для вашего «приложения», а не для «библиотеки».
Авторы приложений знают, кто их пользователи, и знают, какие журналы они хотят видеть.
В то время как если вы пишете код библиотеки, вы не знаете, кто ваш конечный
пользователь, и вы не знаете, какие журналы они хотят видеть.
Вывод: для кода библиотеки не настраивайте журналирование.
Вы по-прежнему можете использовать журналирование, создавать регистраторы, сообщения
журнала и другие важные события.
Просто не настраивайте его с помощью dictConfig или любой другой конфигурации.
Пусть приложения выполняют настройку.
Если пользователь не настраивает ведение журнала, то ожидаемым поведением по умолчанию
будет вывод предупреждений и выше в stderr.
Если пользователь вашей библиотеки настраивает ведение журнала, то не мешайте ему
делать то, что он хочет, добавляя обработчики
форматеры или другие вещи, о которых он не знает.

logging4p
Наконец, вы помните log4j?
Это чрезвычайно популярная библиотека ведения журнала для Java, в которой
уязвимость 0-day нанесла ущерб и вызвала настоящий переполох в деловом мире,
поскольку тысячи крупных продуктов и сервисов с миллионами или миллиардами
пользователей мгновенно стали уязвимы для легкодоступной уязвимости
удаленного выполнения произвольного кода.
В основе уязвимости лежала комбинация ведения журнала пользовательского ввода
в сочетании с плагином, который позволял загружать удаленные данные как
данные объекта Java.
В любом случае, вот функция Python "makeLogRecord", которую можно
использовать для создания записей журнала вручную. Например, "из
консервированного события, полученного по сети". Я не говорю, что это
активно уязвимо.
но на случай, если "logging4p" станет чем-то ... назовем это.
Спасибо!

Так что если вы все еще не удовлетворены настройками вашего журнала или
другого проекта, возможно, мы можем помочь.