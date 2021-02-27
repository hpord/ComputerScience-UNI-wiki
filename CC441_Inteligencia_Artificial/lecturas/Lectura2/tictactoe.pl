:- module(tictactoe, [mover/2,minMover/1,maxMover/1,utilidad/2,ganarPos/2,dibPos/2]).
% mover(+Pos, -ProxPos)
% True si hay un cambio legal de Pos a ProxPos.

mover([X1, jugar, Tablero], [X2, ganar, ProxTablero]) :-
    proxJugador(X1, X2),
    moverAux(X1, Tablero, ProxTablero),
    ganarPos(X1, ProxTablero), !.

mover([X1, jugar, Tablero], [X2, dib, ProxTablero]) :-
    proxJugador(X1, X2),
    moverAux(X1, Tablero, ProxTablero),
    dibPos(X1,ProxTablero), !.

mover([X1, jugar, Tablero], [X2, jugar, ProxTablero]) :-
    proxJugador(X1, X2),
    moverAux(X1, Tablero, ProxTablero).


% moverAux(+Jugador, +Tablero, -ProxTablero)
% True si ProxTablero es un tablero con un elemento vacio reemplazado por la marca que hace un jugador.
moverAux(P, [0|Bs], [P|Bs]).

moverAux(P, [B|Bs], [B|B2s]) :-
    moverAux(P, Bs, B2s).

% minMover(+Pos)
% True si el  proximo jugador  a jugar es  MIN .
minMover([o, _, _]).

% maxMover(+Pos)
% True si el  proximo jugadora jugar es  MAX .
maxMover([x, _, _]).

% utilidad(+Pos, -Val) :-
% True si Val es el resultado de la función de utilidad en Pos.
% Solo se evalua  la posicion final.
% Tenemos MAX gana, MIN gana o el tablero esta completo  .
% Usamos   1 cuando MAX gana
%         -1 cuando MIN gana
%          0 en otros casos.
utilidad([o, ganar, _], 1).
utilidad([x, ganar, _], -1).
utilidad([_, dib, _], 0).

% ganarPos(+Jugador, +Tablero)
% True si  Jugador ganar en Tablero.
ganarPos(P, [X1, X2, X3, X4, X5, X6, X7, X8, X9]) :-
    equal(X1, X2, X3, P) ;
    equal(X4, X5, X6, P) ;
    equal(X7, X8, X9, P) ;
    equal(X1, X4, X7, P) ;
    equal(X2, X5, X8, P) ;
    equal(X3, X6, X9, P) ;
    equal(X1, X5, X9, P) ;
    equal(X3, X5, X7, P).

% dibPos(+Jugador, +Tablero)
% True si el juego esta completo
dibPos(_,Tablero) :-
    \+ member(0, Tablero).


% equal(+W, +X, +Y, +Z).
% True si  W = X = Y = Z.
equal(X, X, X, X).
