import numpy as np

class dArbol:
	""" Un simple arbol de decision"""
	
	def __init__(self):
		""" Constructor """

	def leer_data(self,nombreArchivo):
		fid = open(nombreArchivo,"r")
		data = []
		d = []
		for line in fid.readlines():
			d.append(line.strip())
		for d1 in d:
			data.append(d1.split(","))
		fid.close()

		self.nombreCaracteristicas = data[0]
		self.nombreCaracteristicas = self.nombreCaracteristicas[:-1]
		data = data[1:]
		self.clases = []
		for d in range(len(data)):
			self.clases.append(data[d][-1])
			data[d] = data[d][:-1]

		return data,self.clases,self.nombreCaracteristicas

	def clasificar(self,arbol,puntodato):

		if type(arbol) == type("string"):
			return arbol
		else:
			a = list(arbol.keys())[0]
			for i in range(len(self.nombreCaracteristicas)):
				if self.nombreCaracteristicas[i]==a:
					break
			
			try:
				t = arbol[a][puntodato[i]]
				return self.clasificar(t,puntodato)
			except:
				return None

	def clasificarTodo(self,arbol,data):
		resultados = []
		for i in range(len(data)):
			resultados.append(self.clasificar(arbol,data[i]))
		return resultados

	def construye_arbol(self,data,clases,nombreCaracteristicas,maxnivel=-1,nivel=0,bosque=0):
		""" La funcion que construye recursivamente el arbol de decision"""

		nData = len(data)
		nCaracteristicas = len(data[0])
		
		try: 
			self.nombreCaracteristicas
		except:
			self.nombreCaracteristicas = nombreCaracteristicas
			
		# Lista de todas las posibles clases
		nuevasClases = []
		for aclass in clases:
			if nuevasClases.count(aclass)==0:
				nuevasClases.append(aclass)

		# Calcula la clase predeterminada (y la entropia total)
		frecuencia = np.zeros(len(nuevasClases))

		totalEntropia = 0
		totalGini = 0
		index = 0
		for aclass in nuevasClases:
			frecuencia[index] = clases.count(aclass)
			totalEntropia += self.calc_entropia(float(frecuencia[index])/nData)
			totalGini += (float(frecuencia[index])/nData)**2

			index += 1

		totalGini = 1 - totalGini
		estandar = clases[np.argmax(frecuencia)]

		if nData==0 or nCaracteristicas == 0 or (maxnivel>=0 and nivel>maxnivel):
			return estandar
		elif clases.count(clases[0]) == nData:
			return clases[0]
		else:

			# Escoge que caracteristica es mejor
			gain = np.zeros(nCaracteristicas)
			ggain = np.zeros(nCaracteristicas)
			conjuntoCaracteristicas = list(range(nCaracteristicas))
			if bosque != 0:
				np.random.shuffle(conjuntoCaracteristicas)
				conjuntoCaracteristicas = conjuntoCaracteristicas[0:bosque]
			for caracteristica in conjuntoCaracteristicas:
				g,gg = self.calc_info_gain(data,clases,caracteristica)
				gain[caracteristica] = totalEntropia - g
				ggain[caracteristica] = totalGini - gg

			mejorCaracteristica = np.argmax(gain)
			arbol = {nombreCaracteristicas[mejorCaracteristica]:{}}

			# Lista los valoes que mejorCaracteristica puede tomar
			valores = []
			for puntodato in data:
				if puntodato[caracteristica] not in valores:
					valores.append(puntodato[mejorCaracteristica])

			for valor in valores:
				# Encuentra los puntos de datos con cada valor de caracteristica
				nuevaData = []
				nuevasClases = []
				index = 0
				for puntodato in data:
					if puntodato[mejorCaracteristica]==valor:
						if mejorCaracteristica==0:
							nuevopuntodato = puntodato[1:]
							nuevosNombres = nombreCaracteristicas[1:]
						elif mejorCaracteristica==nCaracteristicas:
							nuevopuntodato = puntodato[:-1]
							nuevosNombres = nombreCaracteristicas[:-1]
						else:
							nuevopuntodato = puntodato[:mejorCaracteristica]
							nuevopuntodato.extend(puntodato[mejorCaracteristica+1:])
							nuevosNombres = nombreCaracteristicas[:mejorCaracteristica]
							nuevosNombres.extend(nombreCaracteristicas[mejorCaracteristica+1:])
						nuevaData.append(nuevopuntodato)
						nuevasClases.append(clases[index])
					index += 1

				# Ahora de manera recursiva al siguiente nivel
				subarbol = self.construye_arbol(nuevaData,nuevasClases,nuevosNombres,maxnivel,nivel+1,bosque)

				# Y al retornar, agrega el subarbol al arbol
				arbol[nombreCaracteristicas[mejorCaracteristica]][valor] = subarbol

			return arbol

	def imprimeArbol(self,arbol,nombre):
		if type(arbol) == dict:
			print(nombre, list(arbol.keys())[0])
			for item in list(arbol.values())[0].keys():
				print(nombre, item)
				self.imprimeArbol(list(arbol.values())[0][item], nombre + "\t")
		else:
			print(nombre, "\t->\t", arbol)

	def calc_entropia(self,p):
		if p!=0:
			return -p * np.log2(p)
		else:
			return 0

	def calc_info_gain(self,data,clases,caracteristica):

        # Calcula la ganancia de informacion basada tanto en la entropia como en la impureza de Gini
		gain = 0
		ggain = 0
		nData = len(data)

        # Lista los valores que puede tomar esa caracteristica

		valores = []
		for puntodato in data:
			if puntodato[caracteristica] not in valores:
				valores.append(puntodato[caracteristica])

		conteoCaracteristicas = np.zeros(len(valores))
		entropia = np.zeros(len(valores))
		gini = np.zeros(len(valores))
		valorIndex = 0
        # Encuentra donde aparecen esos valores en los datos [caracteristica] y la clase correspondiente
		for valor in valores:
			dataIndex = 0
			nuevasClases = []
			for puntodato in data:
				if puntodato[caracteristica]==valor:
					conteoCaracteristicas[valorIndex]+=1
					nuevasClases.append(clases[dataIndex])
				dataIndex += 1

            # Obtenga los valores en nuevasClases
			valorClases = []
			for aclass in nuevasClases:
				if valorClases.count(aclass)==0:
					valorClases.append(aclass)

			conteoClases = np.zeros(len(valorClases))
			claseIndex = 0
			for valorClase in valorClases:
				for aclass in nuevasClases:
					if aclass == valorClase:
						conteoClases[claseIndex]+=1 
				claseIndex += 1
			
			for claseIndex in range(len(valorClases)):
				entropia[valorIndex] += self.calc_entropia(float(conteoClases[claseIndex])/np.sum(conteoClases))
				gini[valorIndex] += (float(conteoClases[claseIndex])/np.sum(conteoClases))**2

            # Calcula tanto la ganancia de Gini como la entropia
			gain = gain + float(conteoCaracteristicas[valorIndex])/nData * entropia[valorIndex]
			ggain = ggain + float(conteoCaracteristicas[valorIndex])/nData * gini[valorIndex]
			valorIndex += 1
		return gain, 1-ggain	
			
