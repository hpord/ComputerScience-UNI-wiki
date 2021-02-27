:- use_module(minimax).
:- use_module(tictactoe).

% mejorMovimiento(+Pos, -ProxPos)
% Calculamos el mejor ProxPos desde la posicion Pos
% con minimax o el algoritmo alpha-beta.
mejorMovimiento(Pos, ProxPos) :-
    minimax(Pos, ProxPos, _).

% jugar
% Inicializa el juego.
jugar :-
    nl,
    write('===================='), nl,
	  write('= Prolog TicTacToe ='), nl,
	  write('===================='), nl, nl,
	  write('x empieza e juego'), nl,
	  pedirSimbolo.
	

% Preguntar por simbolo a jugar
pedirSimbolo :-
	  nl, write('Simbolo para el jugador humano ? (x - o)'), nl,
	  read(Jugador), nl,
	  (
	    Jugador \= o, Jugador \= x, !,     
	    write('Error : simbolo no valido !'), nl,
	    pedirSimbolo                    
	    ;
	    TableroVacio = [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    show(TableroVacio), nl,
		   
	    jugar([x, jugar, TableroVacio], Jugador)
	  ).


% Indica como debe jugar el jugador
jugar([Jugador, jugar, Tablero], Jugador) :- !,
    nl, write('Proximo movimiento ?'), nl,
    read(Pos), nl,                                 
    (
      movimientoHumano([Jugador, jugar, Tablero], [ProxJugador, Estado, ProxTablero], Pos), !,
      show(ProxTablero),
      (
        Estado = ganar, !,                             
        nl, write('Fin del juego : '),
        write(Jugador), write(' gana !'), nl, nl
        ;
        Estado = dib, !,                            
        nl, write('Fin del juego : '),
        write(' completo !'), nl, nl
        ;
        jugar([ProxJugador, jugar, ProxTablero], Jugador) 
      )
      ;
      write('-> Mal movimiento !'), nl,                
      jugar([Jugador, jugar, Tablero], Jugador)        
    ).

% Calcula el mejor movimiento del computador con minimax o alpha-beta.
% Si es que el jugador humano no le toca jugar 
jugar([Jugador, jugar, Tablero], JugadorHumano) :-
    nl, write('Computador juega : '), nl, nl,
    mejorMovimiento([Jugador, jugar, Tablero], [ProxJugador, Estado, MejorSucTablero]),
    show(MejorSucTablero),
    (
      Estado = ganar, !,                                 
      nl, write('Fin del juego : '),
      write(Jugador), write(' gana !'), nl, nl
      ;
      Estado = dib, !,                                
      nl, write('Fin del juego : '), write('completo !'), nl, nl
      ;
      jugar([ProxJugador, jugar, MejorSucTablero], JugadorHumano)
    ).


% proxJugador(X1, X2)
% True si X2 es el proximo a jugar despues de X1.
proxJugador(o, x).
proxJugador(x, o).

% Cuando un jugador humano realiza un movimiento
movimientoHumano([X1, jugar, Tablero], [X2, Estado, ProxTablero], Pos) :-
    proxJugador(X1, X2),
    set1(Pos, X1, Tablero, ProxTablero),
    (
      ganarPos(X1, ProxTablero), !, Estado = ganar ;
      dibPos(X1,ProxTablero), !, Estado = dib ;
      Estado = jugar
    ).

% set1(+Elem, +Pos, +Lista, -ResLista).
% Ponemos Elem en la posicion Pos en la Lista con result en ResLista.
% Conteo empieza en  1.
set1(1, E, [X|Ls], [E|Ls]) :- !, X = 0.

set1(P, E, [X|Ls], [X|L2s]) :-
    number(P),
    P1 is P - 1,
    set1(P1, E, Ls, L2s).
    
% show(+Tablero)
% Muestra el tablero a la salida actual.
show([X1, X2, X3, X4, X5, X6, X7, X8, X9]) :-
    write('   '), show2(X1),
    write(' | '), show2(X2),
    write(' | '), show2(X3), nl,
    write('  -----------'), nl,
    write('   '), show2(X4),
    write(' | '), show2(X5),
    write(' | '), show2(X6), nl,
    write('  -----------'), nl,
    write('   '), show2(X7),
    write(' | '), show2(X8),
    write(' | '), show2(X9), nl.



% show2(+Termino)
% Escribe Termino a la salida actual
% Se reemplaza 0 por ' '.
show2(X) :-
    X = 0, !,
    write(' ').

show2(X) :-
    write(X).
