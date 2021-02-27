# Sistema de inferencia logica simple: resolución y verificacion de modelos 
# para lógica de primer orden.

# Codigo basado en el trabajo de Percy Liang

import collections

# Recursivamente aplicamos str en map
def rstr(x):
    if isinstance(x, tuple): return str(tuple(map(rstr, x)))
    if isinstance(x, list): return str(list(map(rstr, x)))
    if isinstance(x, set): return str(set(map(rstr, x)))
    if isinstance(x, dict):
        newx = {}
        for k, v in list(x.items()):
            newx[rstr(k)] = rstr(v)
        return str(newx)
    return str(x)

class Expression:
    # funciones de ayuda.
    def ensureType(self, arg, wantedType):
        if not isinstance(arg, wantedType):
            raise Exception('%s: quiero %s, pero tengo %s' % (self.__class__.__name__, wantedType, arg))
        return arg
    def ensureFormula(self, arg): return self.ensureType(arg, Formula)
    def ensureFormulas(self, args):
        for arg in args: self.ensureFormula(arg)
        return args
    def isa(self, wantedType): return isinstance(self, wantedType)
    def join(self, args): return ','.join(str(arg) for arg in args)

    def __eq__(self, other): return str(self) == str(other)
    def __hash__(self): return hash(str(self))
    # ! Guarda en cache la cadena para ser mas eficiente
    def __repr__(self):
        if not self.strRepn: self.strRepn = self.computeStrRepn()
        return self.strRepn

# Una formula representa un valor de verdad.
class Formula(Expression): pass

# Un Term (termino coresponde a un objecto.
class Term(Expression): pass

# Variable (debe empezar en  '$')
# Ejemplo: $x
class Variable(Term):
    def __init__(self, name):
        if not name.startswith('$'): raise Exception('Una variable debe empezar en "$", no en %s' % name)
        self.name = name
        self.strRepn = None
    def computeStrRepn(self): return self.name

# Constante 
# Ejemplo: john
class Constant(Term):
    def __init__(self, name):
        if not name[0].islower(): raise Exception(' Las constantes debe empezar con letra minuscula, no en %s' % name)
        self.name = name
        self.strRepn = None
    def computeStrRepn(self): return self.name

# Predicado aplicado a los argumentos.
# Ejemplo: LivesIn(john, palo_alto)
class Atom(Formula):
    def __init__(self, name, *args):
        if not name[0].isupper(): raise Exception(' Los predicados deben empezar con letra mayuscula, no en %s' % name)
        self.name = name
        self.args = list(map(toExpr, args))
        self.strRepn = None
    def computeStrRepn(self):
        if len(self.args) == 0: return self.name
        return self.name + '(' + self.join(self.args) + ')'

def toExpr(x):
    if isinstance(x, str):
        if x.startswith('$'): return Variable(x)
        return Constant(x)
    return x

AtomFalse = False
AtomTrue = True

# Ejemplo: Not(Rain)
class Not(Formula):
    def __init__(self, arg):
        self.arg = self.ensureFormula(arg)
        self.strRepn = None
    def computeStrRepn(self): return 'Not(' + str(self.arg) + ')'

# Ejemplo: And(Rain,Snow)
class And(Formula):
    def __init__(self, arg1, arg2):
        self.arg1 = self.ensureFormula(arg1)
        self.arg2 = self.ensureFormula(arg2)
        self.strRepn = None
    def computeStrRepn(self): return 'And(' + str(self.arg1) + ',' + str(self.arg2) + ')'

# Ejemplo: Or(Rain,Snow)
class Or(Formula):
    def __init__(self, arg1, arg2):
        self.arg1 = self.ensureFormula(arg1)
        self.arg2 = self.ensureFormula(arg2)
        self.strRepn = None
    def computeStrRepn(self): return 'Or(' + str(self.arg1) + ',' + str(self.arg2) + ')'

# Ejemplo: Implies(Rain,Wet)
class Implies(Formula):
    def __init__(self, arg1, arg2):
        self.arg1 = self.ensureFormula(arg1)
        self.arg2 = self.ensureFormula(arg2)
        self.strRepn = None
    def computeStrRepn(self): return 'Implies(' + str(self.arg1) + ',' + str(self.arg2) + ')'

# Ejemplo: Exists($x,Lives(john, $x))
class Exists(Formula):
    def __init__(self, var, body):
        self.var = self.ensureType(toExpr(var), Variable)
        self.body = self.ensureFormula(body)
        self.strRepn = None
    def computeStrRepn(self): return 'Exists(' + str(self.var) + ',' + str(self.body) + ')'

# Ejemplo: Forall($x,Implies(Human($x),Alive($x)))
class Forall(Formula):
    def __init__(self, var, body):
        self.var = self.ensureType(toExpr(var), Variable)
        self.body = self.ensureFormula(body)
        self.strRepn = None
    def computeStrRepn(self): return 'Forall(' + str(self.var) + ',' + str(self.body) + ')'

# Toma una lista de conjunciones/disjunciones y retorna una formula
def AndList(forms):
    result = AtomTrue
    for form in forms:
        result = And(result, form) if result != AtomTrue else form
    return result
def OrList(forms):
    result = AtomFalse
    for form in forms:
        result = Or(result, form) if result != AtomFalse else form
    return result

# Returna una lista de conjunciones |form|.
# Ejemplo: And(And(A, Or(B, C)), Not(D)) => [A, Or(B, C), Not(D)]
def flattenAnd(form):
    if form.isa(And): return flattenAnd(form.arg1) + flattenAnd(form.arg2)
    else: return [form]

# Returna una lista de disjunciones |form|.
# Ejemplo: Or(Or(A, And(B, C)), D) => [A, And(B, C), Not(D)]
def flattenOr(form):
    if form.isa(Or): return flattenOr(form.arg1) + flattenOr(form.arg2)
    else: return [form]

# Mas sintaxis
def Equiv(a, b): return And(Implies(a, b), Implies(b, a))
def Xor(a, b): return And(Or(a, b), Not(And(a, b)))

# Predicado especial que se usa internamente 
def Equals(x, y): return Atom('Equals', x, y)

# Dado un nombre de predicado (por ejemplo, Parent), devuelve una formula que 
# afirma que ese predicado es anti-reflexivo
# (Ejemplo, Not(Parent(x,x))).
def AntiReflexive(predicate):
    return Forall('$x', Forall('$y', Implies(Atom(predicate, '$x', '$y'),
                                             Not(Equals('$x', '$y')))))

############################################################
# Reglas de inferencia simple

# Una regla toma una secuencia de formulas y produce un conjunto de formulas
# como resultado (posiblemente [] si la regla no se aplica).

class Rule:
    pass

class UnaryRule(Rule):
    def applyRule(self, form): raise Exception('Anula esto')

class BinaryRule(Rule):
    def applyRule(self, form1, form2): raise Exception('Anula esto')
    def symmetric(self): return False

############################################################
# Unificacion

# Devuelve si la unificacion es exitosa
# Asume que las formas son CNF.
def unify(form1, form2, subst):
    if form1.isa(Variable): return unifyTerms(form1, form2, subst)
    if form1.isa(Constant): return unifyTerms(form1, form2, subst)
    if form1.isa(Atom):
        return form2.isa(Atom) and form1.name == form2.name and len(form1.args) == len(form2.args) and \
            all(unify(form1.args[i], form2.args[i], subst) for i in range(len(form1.args)))
    if form1.isa(Not):
        return form2.isa(Not) and unify(form1.arg, form2.arg, subst)
    if form1.isa(And):
        return form2.isa(And) and unify(form1.arg1, form2.arg1, subst) and unify(form1.arg2, form2.arg2, subst)
    if form1.isa(Or):
        return form2.isa(Or) and unify(form1.arg1, form2.arg1, subst) and unify(form1.arg2, form2.arg2, subst)
    raise Exception('Sin manejar: %s' % form1)

# Sigue varios enlaces para llegar a x
def getSubst(subst, x):
    while True:
        y = subst.get(x)
        if y == None: return x
        x = y

def unifyTerms(a, b, subst):
    #imprime 'unifyTerms', a, b, rstr(subst)
    a = getSubst(subst, a)
    b = getSubst(subst, b)
    if a == b: return True
    if a.isa(Variable): subst[a] = b
    elif b.isa(Variable): subst[b] = a
    else: return False
    return True

# Se asume formas en CNF.
def applySubst(form, subst):
    if len(subst) == 0: return form
    if form.isa(Variable):
        #imprime 'applySubst', rstr(form), rstr(subst), rstr(subst.get(form, form))
        #retorna subst.get(form, form)
        return getSubst(subst, form)
    if form.isa(Constant): return form
    if form.isa(Atom): return Atom(*[form.name] + [applySubst(arg, subst) for arg in form.args])
    if form.isa(Not): return Not(applySubst(form.arg, subst))
    if form.isa(And): return And(applySubst(form.arg1, subst), applySubst(form.arg2, subst))
    if form.isa(Or): return Or(applySubst(form.arg1, subst), applySubst(form.arg2, subst))
    raise Exception('Sin manejar: %s' % form)

############################################################
# Convertir a CNF, Reglas de Resolucion 

def withoutElementAt(items, i): return items[0:i] + items[i+1:]

def negateFormula(item):
    return item.arg if item.isa(Not) else Not(item)

# Dada una lista de Formulas, retorna una nueva lista con:
# - Si A y Not(A) existen, retornan [AtomFalse] para una conjuncion, [AtomTrue] para una disjuncion
# - Remueve duplicados
# - Ordena la lista
def reduceFormulas(items, mode):
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if negateFormula(items[i]) == items[j]:
                if mode == And: return [AtomFalse]
                elif mode == Or: return [AtomTrue]
                else: raise Exception("Modo invalido: %s" % mode)
    items = sorted(set(items), key=str)
    return items

# Genera una lista de todas las subexpresiones de una formula (incluyendo terminos).
# Ejemplo:
# - Entrada: And(Atom('A', Constant('a')), Atom('B'))
# - Salida: [And(Atom('A', Constant('a')), Atom('B')), Atom('A', Constant('a')), Constant('a'), Atom('B')]
def allSubexpressions(form):
    subforms = []
    def recurse(form):
        subforms.append(form)
        if form.isa(Variable): pass
        elif form.isa(Constant): pass
        elif form.isa(Atom):
            for arg in form.args: recurse(arg)
        elif form.isa(Not): recurse(form.arg)
        elif form.isa(And): recurse(form.arg1); recurse(form.arg2)
        elif form.isa(Or): recurse(form.arg1); recurse(form.arg2)
        elif form.isa(Implies): recurse(form.arg1); recurse(form.arg2)
        elif form.isa(Exists): recurse(form.body)
        elif form.isa(Forall): recurse(form.body)
        else: raise Exception("Sin manejar: %s" % form)
    recurse(form)
    return subforms

# Returna una lista de todas las variables libres como |form|.
def allFreeVars(form):
    variables = []
    def recurse(form, boundVars):
        if form.isa(Variable):
            if form not in boundVars: variables.append(form)
        elif form.isa(Constant): pass
        elif form.isa(Atom):
            for arg in form.args: recurse(arg, boundVars)
        elif form.isa(Not): recurse(form.arg, boundVars)
        elif form.isa(And): recurse(form.arg1, boundVars); recurse(form.arg2, boundVars)
        elif form.isa(Or): recurse(form.arg1, boundVars); recurse(form.arg2, boundVars)
        elif form.isa(Implies): recurse(form.arg1, boundVars); recurse(form.arg2, boundVars)
        elif form.isa(Exists): recurse(form.body, boundVars + [form.var])
        elif form.isa(Forall): recurse(form.body, boundVars + [form.var])
        else: raise Exception("Sin manejar: %s" % form)
    recurse(form, [])
    return variables

# Returna |form| con todas los casos libres de |var| remplazadas con |obj|.
def substituteFreeVars(form, var, obj):
    def recurse(form, boundVars):
        if form.isa(Variable):
            if form == var: return obj
            return form
        elif form.isa(Constant): return form
        elif form.isa(Atom):
            return Atom(*[form.name] + [recurse(arg, boundVars) for arg in form.args])
        elif form.isa(Not): return Not(recurse(form.arg, boundVars))
        elif form.isa(And): return And(recurse(form.arg1, boundVars), recurse(form.arg2, boundVars))
        elif form.isa(Or): return Or(recurse(form.arg1, boundVars), recurse(form.arg2, boundVars))
        elif form.isa(Implies): return Implies(recurse(form.arg1, boundVars), recurse(form.arg2, boundVars))
        elif form.isa(Exists):
            if form.var == var: return form 
            return Exists(form.var, recurse(form.body, boundVars + [form.var]))
        elif form.isa(Forall):
            if form.var == var: return form 
            return Forall(form.var, recurse(form.body, boundVars + [form.var]))
        else: raise Exception("Sin manejar: %s" % form)
    return recurse(form, [])

def allConstants(form):
    return [x for x in allSubexpressions(form) if x.isa(Constant)]

class ToCNFRule(UnaryRule):
    def __init__(self):
        # Para estandarizar variables
        # Para cada nombre de variable existente, el numero de veces que ha ocurrido
        self.varCounts = collections.Counter()

    def applyRule(self, form):
        newForm = form

        # Paso 1: remueve implicaciones
        def removeImplications(form):
            if form.isa(Atom): return form
            if form.isa(Not): return Not(removeImplications(form.arg))
            if form.isa(And): return And(removeImplications(form.arg1), removeImplications(form.arg2))
            if form.isa(Or): return Or(removeImplications(form.arg1), removeImplications(form.arg2))
            if form.isa(Implies): return Or(Not(removeImplications(form.arg1)), removeImplications(form.arg2))
            if form.isa(Exists): return Exists(form.var, removeImplications(form.body))
            if form.isa(Forall): return Forall(form.var, removeImplications(form.body))
            raise Exception("Sin manejar: %s" % form)
        newForm = removeImplications(newForm)

        # Paso 2:  (de Morgan)
        def pushNegationInwards(form):
            if form.isa(Atom): return form
            if form.isa(Not):
                if form.arg.isa(Not):  # Doble negacion
                    return pushNegationInwards(form.arg.arg)
                if form.arg.isa(And):  # De Morgan
                    return Or(pushNegationInwards(Not(form.arg.arg1)), pushNegationInwards(Not(form.arg.arg2)))
                if form.arg.isa(Or):  # De Morgan
                    return And(pushNegationInwards(Not(form.arg.arg1)), pushNegationInwards(Not(form.arg.arg2)))
                if form.arg.isa(Exists):
                    return Forall(form.arg.var, pushNegationInwards(Not(form.arg.body)))
                if form.arg.isa(Forall):
                    return Exists(form.arg.var, pushNegationInwards(Not(form.arg.body)))
                return form
            if form.isa(And): return And(pushNegationInwards(form.arg1), pushNegationInwards(form.arg2))
            if form.isa(Or): return Or(pushNegationInwards(form.arg1), pushNegationInwards(form.arg2))
            if form.isa(Implies): return Or(Not(pushNegationInwards(form.arg1)), pushNegationInwards(form.arg2))
            if form.isa(Exists): return Exists(form.var, pushNegationInwards(form.body))
            if form.isa(Forall): return Forall(form.var, pushNegationInwards(form.body))
            raise Exception("Sin manejar: %s" % form)
        newForm = pushNegationInwards(newForm)

        # Paso 3: estandarizar variables: debes asegurarte que todas las variables sean diferentes
        def updateSubst(subst, var):
            self.varCounts[var.name] += 1
            newVar = Variable(var.name + str(self.varCounts[var.name]))
            return dict(list(subst.items()) + [(var, newVar)])
        def standardizeVariables(form, subst):
            if form.isa(Variable):
                if form not in subst: raise Exception("Variables libres encontradas: %s" % form)
                return subst[form]
            if form.isa(Constant): return form
            if form.isa(Atom): return Atom(*([form.name] + [standardizeVariables(arg, subst) for arg in form.args]))
            if form.isa(Not): return Not(standardizeVariables(form.arg, subst))
            if form.isa(And): return And(standardizeVariables(form.arg1, subst), standardizeVariables(form.arg2, subst))
            if form.isa(Or): return Or(standardizeVariables(form.arg1, subst), standardizeVariables(form.arg2, subst))
            if form.isa(Exists):
                newSubst = updateSubst(subst, form.var)
                return Exists(newSubst[form.var], standardizeVariables(form.body, newSubst))
            if form.isa(Forall):
                newSubst = updateSubst(subst, form.var)
                return Forall(newSubst[form.var], standardizeVariables(form.body, newSubst))
            raise Exception("Sin manejar: %s" % form)
        newForm = standardizeVariables(newForm, {}) 

        # Paso 4: reemplazar variables cuantificadas existencialmente con funciones de Skolem.
        def skolemize(form, subst, scope): 
            if form.isa(Variable): return subst.get(form, form)
            if form.isa(Constant): return form
            if form.isa(Atom): return Atom(*[form.name] + [skolemize(arg, subst, scope) for arg in form.args])
            if form.isa(Not): return Not(skolemize(form.arg, subst, scope))
            if form.isa(And): return And(skolemize(form.arg1, subst, scope), skolemize(form.arg2, subst, scope))
            if form.isa(Or): return Or(skolemize(form.arg1, subst, scope), skolemize(form.arg2, subst, scope))
            if form.isa(Exists):
                # Crea una funcion que dependa de las variables en el alcnce (lista de variables)
                # Ejemplo:
                # - Supongamos alcance = [$x, $y] y la forma = Exists($z,F($z)).
                # - Normalmente, deberia retornar F(Z($x,$y)), donde Z es una nueva funcion Skolem.
                # - Pero como no tenemos simbolos de funcion, los reemplazamos con un predicado de Skolem:
                #   Forall($z,Implies(Z($z,$x,$y),F($z)))
                #   Importante: al hacer la resolucion, necesitamos indicar a Not(Z($z,*,*)) como una contradiccion.
                if len(scope) == 0:
                    subst[form.var] = Constant('skolem' + form.var.name)
                    return skolemize(form.body, subst, scope)
                else:
                    skolem = Atom(*['Skolem' + form.var.name, form.var] + scope)
                    return Forall(form.var, Or(Not(skolem), skolemize(form.body, subst, scope)))
            if form.isa(Forall):
                return Forall(form.var, skolemize(form.body, subst, scope + [form.var]))
            raise Exception("Sin manejar: %s" % form)
        newForm = skolemize(newForm, {}, [])

        # Paso 5: quitar cuantificadores universales
        def removeUniversalQuantifiers(form):
            if form.isa(Atom): return form
            if form.isa(Not): return Not(removeUniversalQuantifiers(form.arg))
            if form.isa(And): return And(removeUniversalQuantifiers(form.arg1), removeUniversalQuantifiers(form.arg2))
            if form.isa(Or): return Or(removeUniversalQuantifiers(form.arg1), removeUniversalQuantifiers(form.arg2))
            if form.isa(Forall): return removeUniversalQuantifiers(form.body)
            raise Exception("Sin manejar: %s" % form)
        newForm = removeUniversalQuantifiers(newForm)

        # Paso 6: distribuir Or sobre And : Or(And(A,B),C) es  And(Or(A,C),Or(B,C))
        def distribute(form):
            if form.isa(Atom): return form
            if form.isa(Not): return Not(distribute(form.arg))
            if form.isa(And): return And(distribute(form.arg1), distribute(form.arg2))
            if form.isa(Or):
                # Necesitamos distribuir tanto como sea posible
                f1 = distribute(form.arg1)
                f2 = distribute(form.arg2)
                if f1.isa(And):
                    return And(distribute(Or(f1.arg1, f2)), distribute(Or(f1.arg2, f2)))
                if f2.isa(And):
                    return And(distribute(Or(f1, f2.arg1)), distribute(Or(f1, f2.arg2)))
                return Or(f1, f2)
            if form.isa(Exists): return Exists(form.var, distribute(form.body))
            if form.isa(Forall): return Forall(form.var, distribute(form.body))
            raise Exception("Sin manejar: %s" % form)
        newForm = distribute(newForm)

        # Post-procesamiento: dividir las conjunciones en conjunciones y ordenar los disjunciones en cada conjuncion
        # Eliminar instancias de A y Not(A)
        conjuncts = [OrList(reduceFormulas(flattenOr(f), Or)) for f in flattenAnd(newForm)]
        #imprimir rstr(form), rstr(conjuncts)
        assert len(conjuncts) > 0
        if any(x == AtomFalse for x in conjuncts): return [AtomFalse]
        if all(x == AtomTrue for x in conjuncts): return [AtomTrue]
        conjuncts = [x for x in conjuncts if x != AtomTrue]
        results = reduceFormulas(conjuncts, And)
        if len(results) == 0: results = [AtomFalse]
        #imprimir 'CNF', form, rstr(results)
        return results

class ResolutionRule(BinaryRule):
    # Se asume formulas em CNF
    # Se asume que A y Not(A) no existen ambos en una forma (conversion CNF)
    def applyRule(self, form1, form2):
        items1 = flattenOr(form1)
        items2 = flattenOr(form2)
        results = []
        #Imprime 'RESOLVE', form1, form2
        for i, item1 in enumerate(items1):
            for j, item2 in enumerate(items2):
                subst = {}
                if unify(negateFormula(item1), item2, subst):
                    newItems1 = withoutElementAt(items1, i)
                    newItems2 = withoutElementAt(items2, j)
                    newItems = [applySubst(item, subst) for item in newItems1 + newItems2]

                    if len(newItems) == 0:  # Contradiccion: False
                        results = [AtomFalse]
                        break

                    #Imprime 'STEP: %s %s => %s %s' % (form1, form2, rstr(newItems), rstr(subst))
                    result = OrList(reduceFormulas(newItems, Or))

                    # Not(Skolem$x($x,...)) es una contradiccion
                    if isinstance(result, Not) and result.arg.name.startswith('Skolem'):
                        results = [AtomFalse]
                        break

                    if result == AtomTrue: continue
                    if result in results: continue

                    results.append(result)
            if results == [AtomFalse]: break

        #imprime 'RESOLUTION: %s %s => %s' % (form1, form2, rstr(results))
        return results
    def symmetric(self): return True

############################################################
# Comprobacion del modelo

# Retorna el conjunto de modelos
def performModelChecking(allForms, findAll, objects=None, verbose=0):
    if verbose >= 3:
        print(('comprobacionModelos', rstr(allForms)))
    # Proposicionalizar, convertir a CNF, deducir
    allForms = propositionalize(allForms, objects)
    # Convierte a CNF: lento
    #allForms = [f for form in allForms for f in ToCNFRule().applyRule(form)]
    #if any(x == AtomFalse for x in allForms): return []
    #if all(x == AtomTrue for x in allForms): return [set()]
    #allForms = [x for x in allForms if x != AtomTrue]
    #allForms = reduceFormulas(allForms, And)
    allForms = [universalInterpret(form) for form in allForms]
    allForms = list(set(allForms) - set([AtomTrue, AtomFalse]))
    if verbose >= 3:
        print(('Todas las formas:', rstr(allForms)))

    if allForms == []: return [set()]  # un modelo
    if allForms == [AtomFalse]: return []  # Sin modelos

    # Los atomos son las variables
    atoms = set()
    for form in allForms:
        for f in allSubexpressions(form):
            if f.isa(Atom): atoms.add(f)
    atoms = list(atoms)

    if verbose >= 3:
        print(('Atomos:', rstr(atoms)))
        print(('Restricciones:', rstr(allForms)))

    # Para cada atomo, lista el conjunto de formulas 
    # indice en atoms => lista de formulas
    atomForms = [
        (atom, [form for form in allForms if atom in allSubexpressions(form)]) \
        for atom in atoms \
    ]
    # Grado heuristico
    atomForms.sort(key = lambda x : -len(x[1]))
    atoms = [atom for atom, form in atomForms]

    # Conserva solo las formas de un atomo si solo usa atomos hasta ese punto.
    atomPrefixForms = []
    for i, (atom, forms) in enumerate(atomForms):
        prefixForms = []
        for form in forms:
            useAtoms = set(x for x in allSubexpressions(form) if x.isa(Atom))
            if useAtoms <= set(atoms[0:i+1]):
                prefixForms.append(form)
        atomPrefixForms.append((atom, prefixForms))

    if verbose >= 3:
        print('Plan:')
        for atom, forms in atomForms:
            print(("  %s: %s" % (rstr(atom), rstr(forms))))
    assert sum(len(forms) for atom, forms in atomPrefixForms) == len(allForms)

    # Construccion de una interpretacion
    N = len(atoms)
    models = []  # Lista de modelos que son verdaderos
    model = set()  # Conjunto de atomos verdaderos 
    def recurse(i): # i: indice de atomos
        if not findAll and len(models) > 0: return
        if i == N:  # Encuentra un modelo en el que las formulas son verdaderas
            models.append(set(model))
            return
        atom, forms = atomPrefixForms[i]
        result = universalInterpretAtom(atom)
        if result == None or result == False:
            if interpretForms(forms, model): recurse(i+1)
        if result == None or result == True:
            model.add(atom)
            if interpretForms(forms, model): recurse(i+1)
            model.remove(atom)
    recurse(0)

    if verbose >= 5:
        print('Modelos:')
        for model in models:
            print(("  %s" % rstr(model)))

    return models

# Un modelo es un conjunto de atomos.
def printModel(model):
    for x in sorted(map(str, model)):
        print(('*', x, '=', 'True'))
    print(('*', '(otros atomos si los hay)', '=', 'False'))

# Convierte una formula logica de primer orden en una formula proposicional,
# asumiendo la semantica de la base de datos.
# Ejemplo: 
# - Entrada: form = Forall('$x', Atom('Alive', '$x')), objects = ['alice', 'bob']
# - Salida: And(Atom('Alive', 'alice'), Atom('Alive', 'bob'))
# Ejemplo: 
# - Entrada: form = Exists('$x', Atom('Alive', '$x')), objects = ['alice', 'bob']
# - Salida: Or(Atom('Alive', 'alice'), Atom('Alive', 'bob'))
def propositionalize(forms, objects=None):
    # Si no se especifica, establece los objetos en todas las constantes mencionadas en |form|.
    if objects == None:
        objects = set()
        for form in forms:
            objects |= set(allConstants(form))
        objects = list(objects)
    else:
        # Los objetos deben ser expresiones: Convert ['a', 'b'] to [Constant('a'), Constant('b')]
        objects = [toExpr(obj) for obj in objects]

    # Recursivamente convierte |form|, que contiene Exists y Forall, a formas que no tienen esos cuantificadores.
    # |subst| es un mapeo desde variables a constantes.
    def convert(form, subst):
        if form.isa(Variable):
            if form not in subst: raise Exception("Variable libre encontrada: %s" % form)
            return subst[form]
        if form.isa(Constant): return form
        if form.isa(Atom):
            return Atom(*[form.name] + [convert(arg, subst) for arg in form.args])
        if form.isa(Not): return Not(convert(form.arg, subst))
        if form.isa(And): return And(convert(form.arg1, subst), convert(form.arg2, subst))
        if form.isa(Or): return Or(convert(form.arg1, subst), convert(form.arg2, subst))
        if form.isa(Implies): return Implies(convert(form.arg1, subst), convert(form.arg2, subst))
        if form.isa(Exists):
            return OrList([convert(form.body, dict(list(subst.items()) + [(form.var, obj)])) for obj in objects])
        if form.isa(Forall):
            return AndList([convert(form.body, dict(list(subst.items()) + [(form.var, obj)])) for obj in objects])
        raise Exception("Sin manejar: %s" % form)

    # Nuevas formas como unidad
    newForms = []
    # Convierte todas esas formas
    for form in forms:
        newForm = convert(form, {})
        if newForm == AtomFalse: return [AtomFalse]
        if newForm == AtomTrue: continue
        newForms.extend(flattenAnd(newForm))
    return newForms

# Algunos atomos tienen un valor fijo, por lo que deberiamos evaluarlos.
# Suposicion: atomo es logica proposicional.
def universalInterpretAtom(atom):
    if atom.name == 'Equals':
        return AtomTrue if atom.args[0] == atom.args[1] else AtomFalse
    return None

# Reduce la expresion (ejemplo Equals(a,a) => True)
# Suposicion: atomo es logica proposicional.
def universalInterpret(form):
    if form.isa(Variable): return form
    if form.isa(Constant): return form
    if form.isa(Atom):
        result = universalInterpretAtom(form)
        if result != None: return result
        return Atom(*[form.name] + [universalInterpret(arg) for arg in form.args])
    if form.isa(Not):
        arg = universalInterpret(form.arg)
        if arg == AtomTrue: return AtomFalse
        if arg == AtomFalse: return AtomTrue
        return Not(arg)
    if form.isa(And):
        arg1 = universalInterpret(form.arg1)
        arg2 = universalInterpret(form.arg2)
        if arg1 == AtomFalse: return AtomFalse
        if arg2 == AtomFalse: return AtomFalse
        if arg1 == AtomTrue: return arg2
        if arg2 == AtomTrue: return arg1
        return And(arg1, arg2)
    if form.isa(Or):
        arg1 = universalInterpret(form.arg1)
        arg2 = universalInterpret(form.arg2)
        if arg1 == AtomTrue: return AtomTrue
        if arg2 == AtomTrue: return AtomTrue
        if arg1 == AtomFalse: return arg2
        if arg2 == AtomFalse: return arg1
        return Or(arg1, arg2)
    if form.isa(Implies):
        arg1 = universalInterpret(form.arg1)
        arg2 = universalInterpret(form.arg2)
        if arg1 == AtomFalse: return AtomTrue
        if arg2 == AtomTrue: return AtomTrue
        if arg1 == AtomTrue: return arg2
        if arg2 == AtomFalse: return Not(arg1)
        return Implies(arg1, arg2)
    raise Exception("Sin manejar: %s" % form)

def interpretForm(form, model):
    if form.isa(Atom): return form in model
    if form.isa(Not): return not interpretForm(form.arg, model)
    if form.isa(And): return interpretForm(form.arg1, model) and interpretForm(form.arg2, model)
    if form.isa(Or): return interpretForm(form.arg1, model) or interpretForm(form.arg2, model)
    if form.isa(Implies): return not interpretForm(form.arg1, model) or interpretForm(form.arg2, model)
    raise Exception("Sin manejar: %s" % form)

# Conjuncion
def interpretForms(forms, model):
    return all(interpretForm(form, model) for form in forms)

############################################################

# Una Derivacion es un arbol donde cada nodo corresponde a la aplicacion de una regla.
# Para cualquier formula, podemos extraer un conjunto de categorias.
#Los argumentos de las reglas estan etiquetados con categoria.
class Derivation:
    def __init__(self, form, children, cost, derived):
        self.form = form
        self.children = children
        self.cost = cost
        self.permanent = False  
        self.derived = derived
    def __repr__(self): return 'Derivation(%s, cost=%s, permanent=%s, derived=%s)' % (self.form, self.cost, self.permanent, self.derived)

# Posibles respuestas a consultas a la base de conocimientos
ENTAILMENT = "ENTAILMENT"
CONTINGENT = "CONTINGENT"
CONTRADICTION = "CONTRADICTION"

# Una respuesta a una consulta
class KBResponse:
    # query: cual es la consulta (solo una descripcion de la cadena para imprimir)
    # modify: si modificamos la base de conocimientos
    # status: uno de estos ENTAILMENT, CONTINGENT, CONTRADICTION
    # trueModel: si esta disponible, un modelo consistente con la KB para el que la consulta es verdadera
    # falseModel: si esta disponible, un modelo consistente con la KB para el que la consulta es falsa
    def __init__(self, query, modify, status, trueModel, falseModel):
        self.query = query
        self.modify = modify
        self.status = status
        self.trueModel = trueModel
        self.falseModel = falseModel

    def show(self, verbose=1):
        padding = '>>>>>'
        print(padding + ' ' + self.responseStr())
        if verbose >= 1:
            print(('Consulta: %s[%s]' % ('Dice' if self.modify else 'Pregunta', self.query)))
            if self.trueModel:
                print('Un ejemplo de un modelo donde la consulta es TRUE:')
                printModel(self.trueModel)
            if self.falseModel:
                print('Un ejemplo de un modelo donde la consulta es FALSE:')
                printModel(self.falseModel)

    def responseStr(self):
        if self.status == ENTAILMENT:
            if self.modify: return 'Yo se eso.'
            else: return 'Si.'
        elif self.status == CONTINGENT:
            if self.modify: return 'Aprendi algo.'
            else: return 'No se.'
        elif self.status == CONTRADICTION:
            if self.modify: return 'Desconozco.'
            else: return 'No.'
        else:
            raise Exception("Estado invalido: %s" % self.status)

    def __repr__(self): return self.responseStr()

def showKBResponse(response, verbose=1):
    if isinstance(response, KBResponse):
        response.show(verbose)
    else:
        items = [(obj, r.status) for ((var, obj), r) in list(response.items())]
        print(('Si: %s' % rstr([obj for obj, status in items if status == ENTAILMENT])))
        print(('Tal vez: %s' % rstr([obj for obj, status in items if status == CONTINGENT])))
        print(('No: %s' % rstr([obj for obj, status in items if status == CONTRADICTION])))

# Una base de conocimientos en una coleccion de formulas.
# - addRule: agregamos reglas de inferencia
# - tell: modifica la KB con una nueva formula.
# - ask: consulta la KB 
class KnowledgeBase:
    def __init__(self, standardizationRule, rules, modelChecking, verbose=0):
        # Regla para aplicar a cada formula que se agrega a la KB (None es posible).
        self.standardizationRule = standardizationRule

        # Conjunto de reglas de inferencia
        self.rules = rules

        #Se utiliza la verificacion de modelos en lugar de aplicar reglas
        self.modelChecking = modelChecking

        # Para depurar
        self.verbose = verbose 

        # Formulas que creemos que son verdaderas (usadas cuando no se hace la verificacion del modelo).
        self.derivations = {} 

    # Agrega una formula |form| a la KB si esta no contradice.  Retorna una  respuesta KB.
    def tell(self, form):
        return self.query(form, modify=True)

    # Pregunta si la formula logica |form| is True, False, o unknown basado
    # en la KB.  Retorna una respuesta KB.
    def ask(self, form):
        return self.query(form, modify=False)

    def dump(self):
        print(('==== Base de conocimiento [%d derivaciones] ===' % len(self.derivations)))
        for deriv in list(self.derivations.values()):
            print((('-' if deriv.derived else '*'), deriv if self.verbose >= 2 else deriv.form))

    ####### Funciones internas

    # Retorna una respuesta KB o si hay variables libres, un mapeo desde (var, obj) => query sin esas variables.
    def query(self, form, modify):
        freeVars = allFreeVars(form)
        if len(freeVars) > 0:
            if modify:
                raise Exception("No se puede modificar la base de datos database con una consulta con variables libres: %s" % form)
            var = freeVars[0]
            allForms = AndList([deriv.form for deriv in list(self.derivations.values())])
            if allForms == AtomTrue: return {} 
            objects = allConstants(allForms) 
            # Intenta juntar |var| a |obj|
            response = {}
            for obj in objects:
                response[(var, obj)] = self.query(substituteFreeVars(form, var, obj), modify)
            return response

        # No hay variables libres
        formStr = '%s, estandarizado: %s' % (form, rstr(self.standardize(form)))

        # Modelos como evidencia de soporte 
        falseModel = None  # Hace la consulta falsa
        trueModel = None  # Hace la consulta verdadera

        # Agrega Not(form)
        if not self.addAxiom(Not(form)):
            self.removeTemporary()
            status = ENTAILMENT
        else:
            # Poco concluyente
            falseModel = self.consistentModel
            self.removeTemporary()

            # Agrega (form)
            if self.addAxiom(form):
                if modify:
                    self.makeTemporaryPermanent()
                else:
                    self.removeTemporary()
                trueModel = self.consistentModel
                status = CONTINGENT
            else:
                self.removeTemporary()
                status = CONTRADICTION

        return KBResponse(query = formStr, modify = modify, status = status, trueModel = trueModel, falseModel = falseModel)

    # Aplicamos la regla de estandarizacion a |form|.
    def standardize(self, form):
        if self.standardizationRule:
            return self.standardizationRule.applyRule(form)
        return [form]

    # Retorna si agregar |form| es consistente con la actual base de conocimiento.
    # Agrega |form| a la base de conocimiento si es posible.  Nota: esto es temporal!
    # Solo llama a addDerivation.
    def addAxiom(self, form):
        self.consistentModel = None
        for f in self.standardize(form):
            if f == AtomFalse: return False
            if f == AtomTrue: continue
            deriv = Derivation(f, children = [], cost = 0, derived = False)
            if not self.addDerivation(deriv): return False
        return True

    # Retorna si la derivacion es consistente con el KB.
    def addDerivation(self, deriv):
        # Deriva una contradiccion
        if deriv.form == AtomFalse: return False

        key = deriv.form
        oldDeriv = self.derivations.get(key)
        maxCost = 100
        if oldDeriv == None and deriv.cost <= maxCost:
        #Si oldDeriv == None o (deriv.cost < oldDeriv.cost y (deriv.permanent >= oldDeriv.permanent)):
            #imprime 'UPDATE %s %s' % (deriv, oldDeriv)
            #self.dump()
            # Hay que actualizar
            self.derivations[key] = deriv
            if self.verbose >= 3: print(('agrega %s [%s derivaciones]' % (deriv, len(self.derivations))))

            if self.modelChecking:
                allForms = [deriv.form for deriv in list(self.derivations.values())]
                models = performModelChecking(allForms, findAll=False, verbose=self.verbose)
                if len(models) == 0: return False
                else: self.consistentModel = models[0]

            # Se aplica reglas hacia adelante
            if not self.applyUnaryRules(deriv): return False
            for key2, deriv2 in list(self.derivations.items()):
                if not self.applyBinaryRules(deriv, deriv2): return False
                if not self.applyBinaryRules(deriv2, deriv): return False

        return True

    # Surge una excepcion si |form| no esta en lista de Formulas.
    def ensureFormulas(self, rule, formulas):
        if isinstance(formulas, list) and all(formula == False or isinstance(formula, Formula) for formula in formulas):
            return formulas
        raise Exception('Lista esperada de formulas, pero %s devuelve %s' % (rule, formulas))

    # Retorna si todo esta bien (sin contradicciones).
    def applyUnaryRules(self, deriv):
        for rule in self.rules:
            if not isinstance(rule, UnaryRule): continue
            for newForm in self.ensureFormulas(rule, rule.applyRule(deriv.form)):
                if not self.addDerivation(Derivation(newForm, children = [deriv], cost = deriv.cost + 1, derived = True)):
                    return False
        return True

    # Retorna si todo esta bien (sin contradicciones).
    def applyBinaryRules(self, deriv1, deriv2):
        for rule in self.rules:
            if not isinstance(rule, BinaryRule): continue
            if rule.symmetric() and str(deriv1.form) >= str(deriv2.form): continue  # Optimizacion
            for newForm in self.ensureFormulas(rule, rule.applyRule(deriv1.form, deriv2.form)):
                if not self.addDerivation(Derivation(newForm, children = [deriv1, deriv2], cost = deriv1.cost + deriv2.cost + 1, derived = True)):
                    return False
        return True

    # Elimina todas las derivaciones temporales de la KB.
    def removeTemporary(self):
        for key, value in list(self.derivations.items()):
            if not value.permanent:
                del self.derivations[key]

    # Marca todas las derivaciones marcadas como temporales a permanentes.
    def makeTemporaryPermanent(self):
        for deriv in list(self.derivations.values()):
            deriv.permanent = True

# Cree una KB vacia equipada con las reglas de inferencia habituales.
def createResolutionKB():
    return KnowledgeBase(standardizationRule = ToCNFRule(), rules = [ResolutionRule()], modelChecking = False)

def createModelCheckingKB():
    return KnowledgeBase(standardizationRule = None, rules = [], modelChecking = True)
