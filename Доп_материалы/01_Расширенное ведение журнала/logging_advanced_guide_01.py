# Example 7
# logging_advanced_guide_01.py 
# https://coderzcolumn.com/tutorials/python/logging-simple-guide-to-log-events-in-python

# До сих пор мы видели средство ведения журнала по умолчанию с именем root, которое используется модулем ведения журнала всякий раз,
# когда его метод вызываются непосредственно, например следующим образом: logging.debug().
# Вы можете (и должны) определить свой собственный регистратор, создав объект класса Logger, особенно если ваше приложение имеет несколько модулей.

# Наиболее часто используемые классы, определенные в модуле logging, следующие:
#   Logger:    это класс, объекты которого будут использоваться в коде приложения непосредственно для вызова функций.
#   LogRecord: регистраторы автоматически создают объекты LogRecord, содержащие всю информацию, относящуюся к регистрируемому событию,
#              например имя регистратора, функцию, номер строки, сообщение и т. д.
#   Handler:   обработчики отправляют объекты LogRecord в требуемое место назначения вывода, например, на консоль или в файл.
#              Класс Handler является основой для подклассов, таких как StreamHandler, FileHandler, SMTPHandler, HTTPHandlerи т. д.
#              Эти подклассы отправляют выходные данные журнала в соответствующие места назначения, например sys.stdoutили в файл на диске.
#   Formatter: Здесь вы указываете формат вывода, указав строковый формат, в котором перечислены атрибуты, которые должен содержать вывод.
#
# Объекты класса Logger, экземпляры которого создаются с помощью функции уровня модуля logging.getLogger(name).
# Множественные вызовы getLogger() с тем же самым name вернут ссылку на один и тот же объект Logger, что избавит нас от передачи объектов регистратора в каждую часть,
# где это необходимо. Вот пример
#        import logging
#        logger = logging.getLogger('example_logger')
#        logger.warning('This is a warning')
# При этом создается пользовательское средство ведения журнала с именем example_logger, но, в отличие от корневого средства ведения журнала,
# имя пользовательского средства ведения журнала не является частью формата вывода по умолчанию и должно быть добавлено в конфигурацию.
# В отличие от корневого регистратора, собственный регистратор нельзя настроить с помощью basicConfig(). Надо настроить его с помощью Handlers и Formatters
# Рекомендуется использовать логгеры на уровне модуля, передав __name__в качестве параметра имени getLogger()для создания объекта логгера,

#-------------------------------------------------------------
# Обработчики появляются, когда вы хотите настроить свои собственные регистраторы и отправлять журналы в несколько мест при их создании.
# Обработчики отправляют сообщения журнала в настроенные места назначения, такие как стандартный поток вывода или файл, или по HTTP, или на вашу электронную почту через SMTP.
# Созданный вами регистратор может иметь более одного обработчика, что означает, что вы можете настроить его на сохранение в файл журнала, а также на отправку по электронной почте.
# Как и в случае с регистраторами, вы также можете установить уровень критичности в обработчиках.
# Это полезно, если вы хотите установить несколько обработчиков для одного и того же регистратора, но хотите иметь разные уровни критичности для каждого из них.
# Например, вы можете захотеть, чтобы журналы с уровнем WARNING и выше выводились на консоль, но все с уровнем ERROR и выше также должны сохраняться в файл.
# Пример:
#
#         # logging_example.py
#
#         import logging
#
#         # Create a custom logger
#         logger = logging.getLogger(__name__)
#
#         # Create handlers
#         c_handler = logging.StreamHandler()
#         f_handler = logging.FileHandler('file.log')
#
#         c_handler.setLevel(logging.WARNING)
#         f_handler.setLevel(logging.ERROR)
#
#         # Create formatters and add it to handlers
#         c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#         f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         c_handler.setFormatter(c_format)
#         f_handler.setFormatter(f_format)
#
#         # Add handlers to the logger
#         logger.addHandler(c_handler)
#         logger.addHandler(f_handler)
#
#         logger.warning('This is a warning')
#         logger.error('This is an error')
 




# Как можно создать экземпляр Logger для регистрации событий и экземпляр StreamHandler для обработки/направления сообщений, сгенерированных экземпляром Logger.

# Расширенное ведение журнала 
# В этом разделе мы расскажем, как создавать объекты Logger, которые можно использовать для ведения журнала в сложных приложениях с большим количеством модулей.
# Объекты Logger можно использовать для направления сообщений журнала в разные места назначения для разных модулей,
# а также сообщения могут форматироваться по-разному для разных модулей.
# Это также позволяет нам фильтровать сообщения журнала, которые необходимо игнорировать или изменять.
#
# Компоненты ведения журнала 
# Ниже приведен список компонентов, которые взаимодействуют друг с другом для ведения журнала в сложных приложениях.
# Logger     - это основной интерфейс для работы с модулем
#              экземпляры этого класс (регистраторы) создаются в разных частях приложения для регистрации событий.
# Handler    - обработчики — это объекты, которые отвечают за направление сообщений в разные места назначения (отправляет log-сообщения конкретному получателю).
#              Обработчики присоединяются к регистратору в зависимости от того, какие сообщения этого регистратора направляются в пункт назначения, указанный обработчиком.
#              В модуле logging.handlers есть список классов обработчиков, которые могут помочь нам направлять сообщения журнала в места назначения,
#              такие как стандартный вывод, электронная почта, сокет, файл и т.д.
# Formatter  - форматтеры — это объекты, которые помогают нам определить формат log-сообщений. Нам нужно прикрепить экземпляр средства форматирования к обработчику
#              для форматирования сообщений, обрабатываемых этим обработчиком. Мы можем создать экземпляр logging.Formatter с деталями форматирования и прикрепить его
#              к обработчику.
# Filter     - фильтры — это объекты, которые можно использовать для фильтрации log-сообщений, их игнорирования или изменения. Мы можем создать фильтр,
#              расширив класс logging.Filter и реализовав метод filter().
#              например так:
#                class LevelFilter(logging.Filter):
#                    def __init__(self, level):
#                        self.level = level
#
#                    def filter(self, record):
#                        return record.levelno == self.level

# Обработка сообщений журнала 
# Как правило, регистратор создается со всеми спецификациями (обработчики, средства форматирования и фильтры) на верхнем уровне модуля,
# называется корневым регистратором.
# Все подмодули просто определяют свои экземпляры регистратора с их именем. Регистраторы, созданные на уровне подмодуля, являются вспомогательными регистраторами
# нашего корневого регистратора.
# Объекты регистратора следуют иерархии так же, как модуль python, который также следует иерархии, разделенной точкой. Все сообщения, созданные отдельным регистратором,
# распространяются на все его родительские регистраторы вплоть до корневого регистратора. Поскольку мы определили обработчики, средства форматирования и фильтры
# в корневом регистраторе, он затем будет обрабатывать сообщения журнала, переданные ему подчиненными регистраторами.
# Мы также можем определить обработчики, средства форматирования и фильтры на любом уровне вспомогательного регистратора, если нам нужна специальная обработка сообщений,
# сгенерированных этим регистратором.
# Чтобы объяснить это на простом примере, предположим, что в нашем приложении есть модули, расположенные в соответствии с приведенной ниже схемой.
#
#                 A
#                 |
#         -----------------
#         |               |
#         B               C
#         |               |
#   ------------     -----------
#   |          |     |         |
#   D          E     F         G
#              |               |
#        ----------        ----------
#        |        |        |        |
#        H        I        J        K
# 
# Мы определим один корневой регистратор в модуле A, который будет иметь обработчики, средства форматирования и фильтры.
# Затем мы определим вспомогательные регистраторы во всех подмодулях ( A.B, A.C, A.B.D, A.B.E, A.C.F, A.C.G, A.B.E.H, A.B.E.I, A.C.G.J, A.C.G.K ).
# Мы не будем определять обработчики, средства форматирования и фильтры для логгеров, созданных в этих подмодулях.
# Мы создадим все регистраторы подмодулей с иерархией имен, за которой следуют имена модулей. Мы можем дать регистраторам то же имя,
# что и имя их модуля, используя атрибут __name__ скрипта, который извлечет полное имя модуля (модуль I будет иметь значение A.B.E.I для атрибута __name__ ).
# Точка говорит модулю logging о том, что, что конкретный logger является дочерним регистратором другого регистратора. Если нам нужна специальная обработка
# log-сообщений на уровне любого подмодуля, мы можем определить обработчики, средства форматирования и фильтры для регистратора, прикрепленного к этому модулю.
# Все log-сообщения, сгенерированные всеми регистраторами подмодулей, будут направляться вплоть до корневого регистратора, определенного в модуле A , который
# будет их обрабатывать.
# Надо подчеркнуть, что если мы определяем обработчики, средства форматирования и фильтры в регистраторе подмодуля, тогда сообщения журнала будут
# обрабатываться ими, а затем будут направляться всем родительским регистраторам до корневого регистратора.
# Это может привести к тому, что одно и то же сообщение журнала будет напечатано дважды или более раз в зависимости от количества обработчиков, которые его обработали.
# Если мы не хотим распространять сообщения журнала, созданные каким-либо регистратором, мы можем установить для параметра propagate (распространения) значение False
# при создании регистратора.
# Теперь мы объясним на простых примерах, как мы можем создать компоненты, описанные выше, и заставить их координировать друг с другом для регистрации событий.

#===============================================================================
# В рамках нашего седьмого примера мы объясним, как мы можем создать экземпляр Logger для регистрации событий и экземпляр StreamHandler для обработки/направления
# log-сообщений, сгенерированных экземпляром Logger .
# StreamHandler(stream=None) — этот конструктор создает экземпляр StreamHandler, который можно использовать для направления сообщений журнала в определенный поток.
# Поток может быть потоком ввода-вывода, стандартным выводом, файлоподобным объектом и т.д. По умолчанию он направляет сообщения журнала в поток sys.stderr.
# Мы можем установить поток в sys.stdout, если мы хотим направить на стандартный вывод.
#
# Важные методы StreamHandler 
#   setLevel(level) — этот метод может помочь установить уровень обработки сообщений. Он может принимать целые числа или строки, которые предопределены,
#                     например INFO, DEBUG и т. д.
#
# Важные методы Logging Instance 
#   getLogger(name=None) — метод принимает имя регистратора и возвращает экземпляр регистратора с этим именем.
#   setLevel(level)      — метод может помочь установить уровень обработки сообщений.
#   addHandler(handler)  — метод примет экземпляр обработчика в качестве входных данных и добавит этот обработчик в список обработчиков для этого регистратора.
#                          Один регистратор может иметь более одного обработчика для направления вывода в разные места назначения.
#   getEffectiveLevel()  — возвращает эффективный уровень регистрации событий для регистратора.
#   debug(message)       — метод работает точно так же, как одноименный метод модуля logging.
#   info(message)        — метод работает точно так же, как одноименный метод модуля logging.
#   warning(message)     — метод работает точно так же, как одноименный метод модуля logging.
#   error(message)       — метод работает точно так же, как одноименный метод модуля logging.
#   log(log_level, message) — этот метод работает точно так же, как одноименный метод модуля logging.

# Наш код для этого примера начинается с создания экземпляра регистратора и обработчика.
# Сначала мы создали экземпляр Logger, используя метод getLogger(), передав ему имя модуля в качестве входных данных.
# Затем мы установили уровень ведения журнала - DEBUG для регистратора, используя метод setLevel(), так что бы регистрировались все сообщения на уровне DEBUG и выше.
#
# Затем мы создали экземпляр StreamHandler и прикрепили его к экземпляру Logger. Мы также установили уровень в обработчике.
#
# Ф-ция addition() и основная часть кода имеют тот же код, что и наши предыдущие примеры, с единственным изменением,
# которое заключается в том, что мы вызываем методы, такие как info(), debug(), warn() и error() для экземпляра регистратор а не модуля  logging.
# Во всех наших предыдущих примерах мы вызывали эти методы из модуля logging .
# Когда мы запускаем приведенный ниже скрипт, мы можем заметить, что на выходе просто печатаются log сообщения. Выходные данные для этого скрипта отличаются
# от предыдущих скриптов способом форматирования log-сообщений. В этом примере нет форматирования сообщений журнала. Мы представим его в следующем примере.


import logging
from typing import Any, Optional

################ Logger ###################
#  создания экземпляра регистратора 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

################ Handler ##################
#  создания обработчика 
std_out = logging.StreamHandler()
std_out.setLevel(logging.DEBUG)
logger.addHandler(std_out)

#===============================================================================
def addition(a: Any, b: Any) -> Optional[float]:

    logger.debug("Inside Addition Function")

    if isinstance(a, str) and a.isdigit():
        logger.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

    if isinstance(b, str) and b.isdigit():
        logger.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

    result = None
    try:
        result = float(a) + float(b)
        logger.info("Addition Function Completed Successfully")
    except Exception as e:
        logger.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
    finally:
        return result

################################################################################

if __name__ == "__main__":
    logger.info("Current Log Level : {}\n".format(logger.getEffectiveLevel()))

    result = addition(10,20)
    logger.info("{} + {} = {}\n".format(10,20, result))

    result = addition("20", 20)
    print("{} + {} = {}\n".format("'20'", 20, result))

    result = addition(20, "20")
    print("{} + {} = {}\n".format(20, "'20'", result))

    result = addition("A",20)
    logger.info("{} + {} = {}".format("A",20, result))

# Current Log Level : 10
#
# Inside Addition Function
# Addition Function Completed Successfully
# 10 + 20 = 30.0
#
# Inside Addition Function
# Warning : Parameter A is passed as String. Future versions won't support it.
# Addition Function Completed Successfully
# '20' + 20 = 40.0
#
# Inside Addition Function
# Error Type : ValueError, Error Message : could not convert string to float: 'A'
# A + 20 = None
