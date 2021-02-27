#!/usr/bin/env python3

from logic import *

import pickle, gzip, os, random
import pruebasUtil

pruebas = pruebasUtil.Grader()
respuestas = pruebas.load('ejercicios')

# name: nombre de una formula (usada para cargar los modelos)
# predForm: la formula predicha en las respuestas
# preconditionForm: solo considera modelos tal que preconditionForm es verdadero
def checkFormula(name, predForm, preconditionForm=None):
    filename = os.path.join('modelos', name + '.pklz')
    objects, targetModels = pickle.load(gzip.open(filename))
    # Si existe una condicion previa, cambia la formula a lo siguiente
    preconditionPredForm = And(preconditionForm, predForm) if preconditionForm else predForm
    predModels = performModelChecking([preconditionPredForm], findAll=True, objects=objects)
    ok = True
    def hashkey(model): return tuple(sorted(str(atom) for atom in model))
    targetModelSet = set(hashkey(model) for model in targetModels)
    predModelSet = set(hashkey(model) for model in predModels)
    for model in targetModels:
        if hashkey(model) not in predModelSet:
            pruebas.fail("Tu formula (%s) dice que este modelo es FALSE, pero debe ser TRUE:" % predForm)
            ok = False
            printModel(model)
            return
    for model in predModels:
        if hashkey(model) not in targetModelSet:
            pruebas.fail("Tu formula (%s) dice que el siguiente modelo es TRUE, pero debe ser FALSE:" % predForm)
            ok = False
            printModel(model)
            return
    pruebas.addMessage('Coinciden los %d modelos' % len(targetModels))
    pruebas.addMessage('Ejemplo de modelo: %s' % rstr(random.choice(targetModels)))
    pruebas.assignFullCredit()

# name: nombre de una formula (usada para cargar los modelos)
# predForms: formula predicha en las respuestas
# predQuery: formula de consulta predicha en las respuestas
def addParts(name, numForms, predictionFunc):
    # aqui tenemos una formula individual (0:numForms), all (combina todo)
    def check(part):
        predForms, predQuery = predictionFunc()
        if len(predForms) < numForms:
            pruebas.fail("Queria %d formulas, pero obtuve %d formulas:" % (numForms, len(predForms)))
            for form in predForms: print(('-', form))
            return
        if part == 'all':
            checkFormula(name + '-all', AndList(predForms))
        elif part == 'run':
            # Ejecutar sobre una base conocimiento
            kb = createModelCheckingKB()

            # Necesito decir a KB sobre los objetos para realizar la verificacion del modelo.
            filename = os.path.join('modelos', name + '-all.pklz')
            objects, targetModels = pickle.load(gzip.open(filename))
            for obj in objects:
                kb.tell(Atom('Object', obj))

            # Agrega las formulas
            for predForm in predForms:
                response = kb.tell(predForm)
                showKBResponse(response)
                pruebas.requireIsEqual(CONTINGENT, response.status)
            response = kb.ask(predQuery)
            showKBResponse(response)

        else:  # Verifica una parte de la formula
            checkFormula(name + '-' + str(part), predForms[part])

    def createCheck(part): return lambda : check(part)  # Para crear la clausura

    for part in list(range(numForms)) + ['all', 'run']:
        if part == 'all':
            description = 'prueba de implementacion de %s para %s' % (part, name)
        elif part == 'run':
            description = 'prueba de implementacion de %s para %s' % (part, name)
        else:
            description = 'prueba de implementacion de la declaracion %s para %s' % (part, name)
        pruebas.addBasicPart(name + '-' + str(part), createCheck(part), maxPoints=1, maxSeconds=10000, description=description)

############################################################
# Problem 1: Logica proposicional

pruebas.addBasicPart('1a', lambda : checkFormula('1a', respuestas.formula1a()), 2, description='Prueba la implementacion de la formula 1a')
pruebas.addBasicPart('1b', lambda : checkFormula('1b', respuestas.formula1b()), 2, description='Prueba la implementacion de la formula 1b')
pruebas.addBasicPart('1c', lambda : checkFormula('1c', respuestas.formula1c()), 2, description='Prueba la implementacion de la formula 1c')

############################################################
# Problema 2: Logica de primer orden

formula2a_precondition = AntiReflexive('Mother')
formula2b_precondition = AntiReflexive('Child')
formula2c_precondition = AntiReflexive('Child')
formula2d_precondition = AntiReflexive('Parent')
pruebas.addBasicPart('2a', lambda : checkFormula('2a', respuestas.formula2a(), formula2a_precondition), 2, description='Prueba la implementacion de la formula 2a')
pruebas.addBasicPart('2b', lambda : checkFormula('2b', respuestas.formula2b(), formula2b_precondition), 2, description='Prueba la implementacion de la formula 2b')
pruebas.addBasicPart('2c', lambda : checkFormula('2c', respuestas.formula2c(), formula2c_precondition), 2, description='Prueba la implementacion de la formula 2c')
pruebas.addBasicPart('2d', lambda : checkFormula('2d', respuestas.formula2d(), formula2d_precondition), 2, description='Prueba la implementacion de la formula 2d')

############################################################
# Problema 3: Puzzle

# Agrega 3a-[0-5], 3a-all, 3a-run
addParts('3a', 6, respuestas.liar)

############################################################
# Problema 5: Enteros pares y impares

# Agrega 5a-[0-5], 5a-all, 5a-run
addParts('5a', 6, respuestas.ints)

pruebas.addManualPart('5b', 10, description='Prueba el argumento de que no hay un modelo finito donde las 7 formulas sean consistentes')

############################################################


pruebas.grade()
