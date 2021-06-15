:- module(minimax, [minimax/3]).
% minimax(Pos, MejorProxPos, Val)
% Pos es una  posicion, Val es el valor minimax.
% Mejor movimiento desde Pos conduce a la posicion MejorProxPos.

minimax(Pos, MejorProxPos, Val) :-     % Pos tiene sucesores                
    bagof(ProxPos, mover(Pos, ProxPos), ProxPosLista),
    mejor(ProxPosLista, MejorProxPos, Val), !.

minimax(Pos, _, Val) :-           % Pos no tiene sucesores        
    utilidad(Pos, Val).


mejor([Pos], Pos, Val) :-
    minimax(Pos, _, Val), !.

mejor([Pos1 | PosList], MejorPos, MejorVal) :-
    minimax(Pos1, _, Val1),
    mejor(PosList, Pos2, Val2),
    mejor1(Pos1, Val1, Pos2, Val2, MejorPos, MejorVal).



mejor1(Pos0, Val0, _, Val1, Pos0, Val0) :-    % Pos0 mejor que Pos1
    minMover(Pos0),                         
    Val0 > Val1, !                             
    ;
    maxMover(Pos0),                         
    Val0 < Val1, !.                          

mejor1(_, _, Pos1, Val1, Pos1, Val1).        % En otro caso Pos1 mejor que Pos0
