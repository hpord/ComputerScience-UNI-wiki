import torch
import numpy as np
import pdb

class HMM(object):
    """
    Clase de un modelo oculto de Markov

    Parametros:
    -----------
    
    - S: Numero de estados.
    - T: numpy.array Matriz de transicion SxS
         almacena la probabilidad del estado i al estado j.   
    - E: numpy.array Matriz de observacion SxN (numero de observaciones)
         almacena de la probabilidad de observar O_j desde el estado S_i. 
    - T0: numpy.array Probabilidades de estado inicial de tam S.
    """

    def __init__(self, T, E, T0, epsilon = 0.001, maxPaso = 10):
        # Maximo numero de interaciones
        self.maxPaso = maxPaso
        # Criterio de convergencia
        self.epsilon = epsilon 
        # Numero posible de estados
        self.S = T.shape[0]
        # Numero de posibles observaciones
        self.O = E.shape[0]
        self.prob_estado_1 = []
        self.E = torch.tensor(E)
        # Matriz de transicion
        self.T = torch.tensor(T)
        # Vector de estado inicial
        self.T0 = torch.tensor(T0)
        
    def inicializa_variables_viterbi(self, shape): 
        rutaEstados = torch.zeros(shape, dtype=torch.float64)
        rutaPuntuaciones = torch.zeros_like(rutaEstados)
        seq_estados = torch.zeros([shape[0]], dtype=torch.int64)
        return rutaEstados, rutaPuntuaciones, seq_estados
    
    def belief_propagacion(self, puntuaciones):
        return puntuaciones.view(-1,1) + torch.log(self.T)
    
    def inferencia_viterbi(self, x):
        # x secuencia de observacion     
        self.N = len(x)
        shape = [self.N, self.S]
        rutaEstados, rutaPuntuaciones, seq_estados = self.inicializa_variables_viterbi(shape) 
        # Log-probabilidad de una secuencia de observaciones
        prob_obs_completa = torch.log(self.E[x])
        # Inicializa con estado empezando log-priors
        rutaPuntuaciones[0] = torch.log(self.T0) + prob_obs_completa[0]
        for paso, prob_obs in enumerate(prob_obs_completa[1:]):
            # Propaga la creencia del estado
            belief = self.belief_propagacion(rutaPuntuaciones[paso, :])
            # El estado inferido maximizando la funcion global
            rutaEstados[paso + 1] = torch.argmax(belief, 0)
            # y actualizar las matrices de estado y puntuacion 
            rutaPuntuaciones[paso + 1] = torch.max(belief, 0)[0] + prob_obs
        # infiere el ultimo estado mas probable
        seq_estados[self.N - 1] = torch.argmax(rutaPuntuaciones[self.N-1, :], 0)
        for paso in range(self.N - 1, 0, -1):
            # por cada paso de tiempo recupera el estado inferido
            state = seq_estados[paso]
            state_prob = rutaEstados[paso][state]   
            seq_estados[paso -1] = state_prob
        return seq_estados, torch.exp(rutaPuntuaciones) 
    
    def inicializa_variables_forw_back(self, shape):
        self.forward = torch.zeros(shape, dtype=torch.float64)
        self.backward = torch.zeros_like(self.forward)
        self.posterior = torch.zeros_like(self.forward)
        
    def _forward(model, prob_obs_seq):
        model.scale = torch.zeros([model.N], dtype=torch.float64) 
        # Inicializa con estado inicial a priori
        init_prob = model.T0 * prob_obs_seq[0]
        # Factor de escala en t=0
        model.scale[0] = 1.0 / init_prob.sum()
        model.forward[0] = model.scale[0] * init_prob
        for paso, prob_obs in enumerate(prob_obs_seq[1:]):
            # Probabilidad de estado anterior
            prev_prob = model.forward[paso].unsqueeze(0)
            # Transicion previa
            prior_prob = torch.matmul(prev_prob, model.T)
            #  propagacion de creencia forward
            puntuacion_forward = prior_prob * prob_obs
            prob_forward = torch.squeeze(puntuacion_forward)
            # Factor de escala
            model.scale[paso + 1] = 1 / prob_forward.sum()
            # Actualiza la matrix forward
            model.forward[paso + 1] = model.scale[paso + 1] * prob_forward
    
    def _backward(self, prob_obs_seq_rev):
        # Inicializa con el estado previo final
        self.backward[0] = self.scale[self.N - 1] * torch.ones([self.S], dtype=torch.float64)
        for paso, prob_obs in enumerate(prob_obs_seq_rev[:-1]):
            # Probabilidad de estado siguiente
            next_prob = self.backward[paso, :].unsqueeze(1)
            # Probabilidad de observacion
            prob_obs_d = torch.diag(prob_obs)
            # Transicion previa
            prior_prob = torch.matmul(self.T, prob_obs_d)
            # Propagacion de creencia backward
            prob_backward = torch.matmul(prior_prob, next_prob).squeeze()
            # Actualiza la matriz backward 
            self.backward[paso + 1] = self.scale[self.N - 2 - paso] * prob_backward
        self.backward = torch.flip(self.backward, [0, 1])
        
    def forward_backward(self, prob_obs_seq):
        """ 
        Ejecuta el algoritmo forward-backward en la secuencia de observacion

        Argumentos
        ---------
        - prob_obs_seq : matriz  NxS, donde N es el numero de pasos de tiempo N  
            S es el numero de estados

        Respuestas
        -------
        - forward : matriz N x S representando la
            probabilidad de forward de cada estado en cada paso de tiempo
        - backward : matriz N x S representando la
            probabilidad de backward de cada estado en cada paso de tiempo
        - posterior : matriz N x S representando la  
            probabilidad posterior de cada estado en cada paso de tiempo
        """        
        self._forward(prob_obs_seq)
        prob_obs_seq_rev = torch.flip(prob_obs_seq, [0, 1])
        self._backward(prob_obs_seq_rev)
    
    def reestimar_transicion(self, x):
        self.M = torch.zeros([self.N - 1, self.S, self.S], dtype = torch.float64)

        for t in range(self.N - 1):
            tmp_0 = torch.matmul(self.forward[t].unsqueeze(0), self.T)
            tmp_1 = tmp_0 * self.E[x[t + 1]].unsqueeze(0)
            denom = torch.matmul(tmp_1, self.backward[t + 1].unsqueeze(1)).squeeze()

            r_trans = torch.zeros([self.S, self.S], dtype = torch.float64)

            for i in range(self.S):
                numer = self.forward[t, i] * self.T[i, :] * self.E[x[t+1]] * self.backward[t+1]
                r_trans[i] = numer / denom

            self.M[t] = r_trans

        self.gamma = self.M.sum(2).squeeze()
        T_nuevo = self.M.sum(0) / self.gamma.sum(0).unsqueeze(1)

        T0_nuevo = self.gamma[0,:]

        prod = (self.forward[self.N-1] * self.backward[self.N-1]).unsqueeze(0)
        s = prod / prod.sum()
        self.gamma = torch.cat([self.gamma, s], 0)
        self.prob_estado_1.append(self.gamma[:, 0]) 
        return T0_nuevo, T_nuevo
    
    def reestimar_emision(self, x):
        marginal_estados = self.gamma.sum(0)
        seq_one_hot = torch.zeros([len(x), self.O], dtype=torch.float64)
        seq_one_hot.scatter_(1, torch.tensor(x).unsqueeze(1), 1)
        puntuacion_emision = torch.matmul(seq_one_hot.transpose_(1, 0), self.gamma)
        return puntuacion_emision / marginal_estados
    
    def verificar_convergencia(self, nuevo_T0, nueva_transicion, nueva_emision):
  
        delta_T0 = torch.max(torch.abs(self.T0 - nuevo_T0)).item() < self.epsilon
        delta_T = torch.max(torch.abs(self.T - nueva_transicion)).item() < self.epsilon
        delta_E = torch.max(torch.abs(self.E - nueva_emision)).item() < self.epsilon

        return delta_T0 and delta_T and delta_E
    
    def pasoEM(self, obs_seq): ### Expectation-Maximization algorithm
    
        # Probabilidad de secuencias de emision
        prob_obs_seq = self.E[obs_seq]

        self.forward_backward(prob_obs_seq)

        nuevo_T0, nueva_transicion = self.reestimar_transicion(obs_seq)

        nueva_emision = self.reestimar_emision(obs_seq)

        converge = self.verificar_convergencia(nuevo_T0, nueva_transicion, nueva_emision)
        
        self.T0 = nuevo_T0
        self.E = nueva_emision
        self.T = nueva_transicion
        
        return converge
    
    def Baum_Welch(self, obs_seq):
        # Longitud de secuencia observada
        self.N = len(obs_seq)

        shape = [self.N, self.S]

        # Inicializa las variables
        self.inicializa_variables_forw_back(shape)

        converge = False

        for i in range(self.maxPaso):
            converge = self.pasoEM(obs_seq)
            if converge:
                print('converge en el paso {}'.format(i))
                break      
        return self.T0, self.T, self.E, converge
