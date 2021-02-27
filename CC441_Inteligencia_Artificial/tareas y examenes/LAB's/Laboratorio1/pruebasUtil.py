"""
Libreria para calificar programas de python
Uso (ver prueba.py):

    # crea un calificador
    prueba = Grader("Nombre asignacion")
    # agrega un test basico 
    prueba.addBasicPart(name, gradeFunc, maxPoints, maxSeconds, description="un test basico")

    # agrega un test oculto
    prueba.addHiddenPart(name, gradeFunc, maxPoints, maxSeconds, description="un test oculto")

    # agrega una calificacion manual
    prueba.addManualPart(name, gradeFunc, maxPoints, description="problema escrito")

    # corre el calificador
    prueba.grade()
"""

import argparse
import datetime, math, pprint, traceback, sys, signal, os, json
import gc

defaultMaxSeconds = 5  
TOLERANCE = 1e-4  

BASIC_MODE = 'basic' 
AUTO_MODE = 'auto'    
ALL_MODE = 'all'     


def isTracebackItemGrader(item):
    return item[0].endswith('pruebasUtil.py')

def isCollection(x):
    return isinstance(x, list) or isinstance(x, tuple)


def isEqual(trueAnswer, predAnswer, tolerance = TOLERANCE):
    if isinstance(trueAnswer, float) or isinstance(predAnswer, float):
        return abs(trueAnswer - predAnswer) < tolerance
    if isCollection(trueAnswer) and isCollection(predAnswer) and len(trueAnswer) == len(predAnswer):
        for a, b in zip(trueAnswer, predAnswer):
            if not isEqual(a, b): return False
        return True
    if isinstance(trueAnswer, dict) and isinstance(predAnswer, dict):
        if len(trueAnswer) != len(predAnswer): return False
        for k, v in list(trueAnswer.items()):
            if not isEqual(predAnswer.get(k), v): return False
        return True
    if type(trueAnswer).__name__ == 'ndarray':
        import numpy as np
        if isinstance(trueAnswer, np.ndarray) and isinstance(predAnswer, np.ndarray):
            if trueAnswer.shape != predAnswer.shape:
                return False
            for a, b in zip(trueAnswer, predAnswer):
                if not isEqual(a, b): return False
            return True

    return trueAnswer == predAnswer

class TimeoutFunctionException(Exception):
    pass
class TimeoutFunction:
    def __init__(self, function, maxSeconds):
        self.maxSeconds = maxSeconds
        self.function = function

    def handle_maxSeconds(self, signum, frame):
        print('Tiempo terminado!')
        raise TimeoutFunctionException()

    def __call__(self, *args):
        if os.name == 'nt':
            timeStart = datetime.datetime.now()
            result = self.function(*args)
            timeEnd = datetime.datetime.now()
            if timeEnd - timeStart > datetime.timedelta(seconds=self.maxSeconds + 1):
                raise TimeoutFunctionException()
            return result
        old = signal.signal(signal.SIGALRM, self.handle_maxSeconds)
        signal.alarm(self.maxSeconds + 1)
        result = self.function(*args)
        signal.alarm(0)
        return result

class Part:
    def __init__(self, number, gradeFunc, maxPoints, maxSeconds, extraCredit, description, basic):
        if not isinstance(number, str):
            raise Exception("Numero invalido: %s" % nombre)
        if gradeFunc != None and not callable(gradeFunc):
            raise Exception("grado de funcion invalido: %s" % gradeFunc)
        if not isinstance(maxPoints, int):
            raise Exception("Puntos maximos invalidos: %s" % maxPoints)
        if maxSeconds != None and not isinstance(maxSeconds, int):
            raise Exception("Tiempo en segundos maximo invalido: %s" % maxSeconds)
        if not description:
            print('ERROR: Descripcion requerida ...{}'.format(number))
       
        #self.name = name
        self.number =number
        self.gradeFunc = gradeFunc  
        self.maxPoints = maxPoints  
        self.maxSeconds = maxSeconds  
        self.extraCredit = extraCredit  
        self.description = description  
        self.basic = basic
        self.points = 0
        self.side = None 
        self.seconds = 0
        self.messages = []
        self.failed = False

    def fail(self):
        self.failed = True

    def is_basic(self):
        return self.gradeFunc is not None and self.basic
    def is_hidden(self):
        return self.gradeFunc is not None and not self.basic
    def is_auto(self):
        return self.gradeFunc is not None
    def is_manual(self):
        return self.gradeFunc is None

class Grader:
    def __init__(self, args=sys.argv):
        self.parts = [] 
        self.useSolution = False  

        parser = argparse.ArgumentParser()
        parser.add_argument('--js', action='store_true', help='Escribe un archivo JS con informacion sobre esta tarea')
        parser.add_argument('--json', action='store_true', help='Escribe un archivo Json con informacion sobre esta tarea')
        parser.add_argument('--summary', action='store_true', help='No se ejecuta codigo')
        parser.add_argument('remainder', nargs=argparse.REMAINDER)
        self.params = parser.parse_args(args[1:])

        args = self.params.remainder
        if len(args) < 1:
            self.mode = AUTO_MODE
            self.selectedPartName = None
        else:
            if args[0] in [BASIC_MODE, AUTO_MODE, ALL_MODE]:
                self.mode = args[0]
                self.selectedPartName = None
            else:
                self.mode = AUTO_MODE
                self.selectedPartName = args[0]

        self.messages = []  
        self.currentPart = None  
        self.fatalError = False  
        cwd = os.getcwd()
        assignment_name = cwd.split('/')[-1]
        num_points = 1
        if 'p-' in assignment_name:
            num_points = 0
        self.addManualPart('style', maxPoints=num_points, extraCredit=True, description='si la redaccion esta bien escrita.')

    def addBasicPart(self, number, gradeFunc, maxPoints=1, maxSeconds=defaultMaxSeconds, extraCredit=False, description=""):
        """Agregue un caso de prueba basico. La prueba sera visible para los estudiantes."""
        self.assertNewNumber(number)
        part = Part(number, gradeFunc, maxPoints, maxSeconds, extraCredit, description, basic=True)
        self.parts.append(part)

    def addHiddenPart(self, number, gradeFunc, maxPoints=1, maxSeconds=defaultMaxSeconds, extraCredit=False, description=""):
        """Agregue un caso de prueba oculto. La salida NO debe ser visible para los estudiantes y, por lo tanto, debe estar dentro de un bloque BEGIN_HIDE."""
        self.assertNewNumber(number)
        part = Part(number, gradeFunc, maxPoints, maxSeconds, extraCredit, description, basic=False)
        self.parts.append(part)

    def addManualPart(self, number, maxPoints, extraCredit=False, description=""):
        """Agregamos la parte manual."""
        self.assertNewNumber(number)
        part = Part(number, None, maxPoints, None, extraCredit, description, basic=False)
        self.parts.append(part)

    def assertNewNumber(self, number):
        if number in [part.number for part in self.parts]:
            raise Exception("Parte del numero %s que existe" % number)

    def load(self, moduleName):
        try:
            return __import__(moduleName)
        except Exception as e:
            self.fail("Excepcion al importar'%s': %s" % (moduleName, e))
            self.fatalError = True
            return None
        except:
            self.fail("Excepcion al importar '%s'" % moduleName)
            self.fatalError = True
            return None

    def gradePart(self, part):
        print('----- Parte Inicial %s%s: %s' % (part.number, ' (punto extra)' if part.extraCredit else '', part.description))
        self.currentPart = part

        startTime = datetime.datetime.now()
        try:
            TimeoutFunction(part.gradeFunc, part.maxSeconds)() 
        except KeyboardInterrupt:
            raise
        except MemoryError as e:
            signal.alarm(0)
            gc.collect()
            self.fail('Memoria limite excedida.')
        except TimeoutFunctionException as e:
            signal.alarm(0)
            self.fail('Tiempo limite (%s segundos) excedido.' % part.maxSeconds)
        except Exception as e:
            signal.alarm(0)
            self.fail('Lanzamiento de excepcion: %s -- %s' % (str(type(e)), str(e)))
            self.printException()
        except SystemExit as e:
            self.fail('Salida inesperada.')
            self.printException()
        endTime = datetime.datetime.now()
        part.seconds = (endTime - startTime).seconds
        if part.is_hidden() and not self.useSolution:
            displayPoints = '???/%s points (prueba oculta sin clasificar)' % part.maxPoints
        else:
            displayPoints = '%s/%s points' % (part.points, part.maxPoints)
        print('----- Parte Final %s [toma %s (maximo permitido %s segundos), %s]' % (part.number, endTime - startTime, part.maxSeconds, displayPoints))
        print()

    def getSelectedParts(self):
        parts = []
        for part in self.parts:
            if self.selectedPartName is not None and self.selectedPartName != part.number:
                continue
            if self.mode == BASIC_MODE:
                if part.is_basic():
                    parts.append(part)
            elif self.mode == AUTO_MODE:
                if part.is_auto():
                    parts.append(part)
            elif self.mode == ALL_MODE:
                parts.append(part)
            else:
                raise Exception("Modo invalido: {}".format(self.mode))
        return parts

    def grade(self):
        parts = self.getSelectedParts()

        result = {}
        result['mode'] = self.mode

        # Calificacion!
        if not self.params.summary and not self.fatalError:
            print('========== EMPEZAR A CALIFICAR')
            for part in parts:
                self.gradePart(part)

            activeParts = [part for part in parts if self.useSolution or part.basic]

            totalPoints = sum(part.points for part in activeParts if not part.extraCredit)
            extraCredit = sum(part.points for part in activeParts if part.extraCredit)
            maxTotalPoints = sum(part.maxPoints for part in activeParts if not part.extraCredit)
            maxExtraCredit = sum(part.maxPoints for part in activeParts if part.extraCredit)

            if not self.useSolution:
                print('Ten en cuenta que los casos de prueba ocultos no comprueban la correccion.' \
                '\nVerifican que las funciones no se bloqueen dentro del limite de tiempo.' \
                '\nPuntos para esas partes no asignadas por el calificador (indicadas por "--").')
            print('========== FIN CALIFICACION [%d/%d points + %d/%d credito extra]' % \
                (totalPoints, maxTotalPoints, extraCredit, maxExtraCredit))

        resultParts = []
        leaderboard = []
        for part in parts:
            r = {}
            r['number'] = part.number
            r['name'] = part.description

            if self.params.summary:
                r['description'] = part.description
                r['maxSeconds'] = part.maxSeconds
                r['maxPoints'] = part.maxPoints
                r['extraCredit'] = part.extraCredit
                r['basic'] = part.basic
            else:
                r['scores'] = part.points
                r['max_score'] = part.maxPoints
                r["visibility"] = "after_published" if part.is_hidden() else "visible"
                r['seconds'] = part.seconds
                if part.side is not None:
                    r['side'] = part.side
                r['output'] = "\n".join(part.messages) #r['messages'] = part.messages
                
                if part.side is not None:
                    for k in part.side:
                        leaderboard.append({"name" : k, "value" : part.side[k]})
            resultParts.append(r)
        result['tests'] = resultParts
        result['leaderboard'] = leaderboard    
        
        self.output(self.mode, result)

        def display(name, extraCredit):
            parts = [part for part in self.parts if part.extraCredit == extraCredit]
            maxBasicPoints = sum(part.maxPoints for part in parts if part.is_basic())
            maxHiddenPoints = sum(part.maxPoints for part in parts if part.is_hidden())
            maxManualPoints = sum(part.maxPoints for part in parts if part.is_manual())
            maxTotalPoints = maxBasicPoints + maxHiddenPoints + maxManualPoints
            print("Total %s (codificacion/auto basico  + codificacion/auto oculto + manual/escrito): %d + %d + %d = %d" % \
                (name, maxBasicPoints, maxHiddenPoints, maxManualPoints, maxTotalPoints))
            if not extraCredit and maxTotalPoints != 20:
                print('Cuidado: maxTotalPoints = {} no es 20'.format(maxTotalPoints))
        if self.params.summary:
            display('points', False)
            display('credito extra', True)

    def output(self, mode, result):
        if self.params.json:
            path = 'calificacion-{}.json'.format(mode)
            with open(path, 'w') as out:
                print(json.dumps(result), file=out)
            print('Escrito a %s' % path)
        if self.params.js:
            path = 'calificacion-{}.js'.format(mode)
            with open(path, 'w') as out:
                print('var ' + mode + 'Resultado = '+ json.dumps(result) + ';', file=out)
            print('Escrito a %s' % path)


    def addPoints(self, amt):
        self.currentPart.points += amt

    def assignFullCredit(self):
        if not self.currentPart.failed:
            self.currentPart.points = self.currentPart.maxPoints
        return True

    def assignPartialCredit(self, credit):
        self.currentPart.points = credit
        return True;

    def setSide(self, side):
        self.currentPart.side = side

    def truncateString(self, string, length=200):
        if len(string) <= length:
            return string
        else:
            return string[:length] + '...'

    def requireIsNumeric(self, answer):
        if isinstance(answer, int) or isinstance(answer, float):
            return self.assignFullCredit()
        else:
            return self.fail("Se esperaba int o float, pero obtuve '%s'" % self.truncateString(answer))

    def requireIsOneOf(self, trueAnswers, predAnswer):
        if predAnswer in trueAnswers:
            return self.assignFullCredit()
        else:
            return self.fail("Se esperaba uno de %s, pero obtuve '%s'" % (self.truncateString(trueAnswers), self.truncateString(predAnswer)))

    def requireIsEqual(self, trueAnswer, predAnswer, tolerance = TOLERANCE):
        if isEqual(trueAnswer, predAnswer, tolerance):
            return self.assignFullCredit()
        else:
            return self.fail("Esperado '%s', pero se consiguio '%s'" % (self.truncateString(str(trueAnswer)), self.truncateString(str(predAnswer))))

    def requireIsLessThan(self, lessThanQuantity, predAnswer ):
        if predAnswer < lessThanQuantity:
            return self.assignFullCredit()
        else:
            return self.fail("Se espera que fuera < %f, pero se consigui %f" % (lessThanQuantity, predAnswer) )

    def requireIsGreaterThan(self, greaterThanQuantity, predAnswer ):
        if predAnswer > greaterThanQuantity:
            return self.assignFullCredit()
        else:
            return self.fail("Se espera que fuera > %f, pero se consiguio %f" %
                    (greaterThanQuantity, predAnswer) )

    def requireIsTrue(self, predAnswer):
        if predAnswer:
            return self.assignFullCredit()
        else:
            return self.fail("Se esperaba que fuera cierto, pero salio falso" )

    def fail(self, message):
        print('FALLO:', message)
        self.addMessage(message)
        if self.currentPart:
            self.currentPart.points = 0
            self.currentPart.fail()
        return False

    def printException(self):
        tb = [item for item in traceback.extract_tb(sys.exc_info()[2]) if not isTracebackItemGrader(item)]
        for item in traceback.format_list(tb):
            self.fail('%s' % item)

    def addMessage(self, message):
        if not self.useSolution:
            print(message)
        if self.currentPart:
            self.currentPart.messages.append(message)
        else:
            self.messages.append(message)
