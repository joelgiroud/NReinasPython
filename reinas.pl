reinas(N, Solucion) :-
    reinas(N, [], Solucion).

reinas(N, L, L) :-
    length(L,N),
    nochoque(L).

reinas(N, L, R) :-
    lista(1, N, A),
    member(X, A),
    nochoque([X|L]),
    reinas(N, [X|L], R).

nochoque([]).
nochoque([X|Xs]) :-
    not(member(X, Xs)),
    no_diag(X, Xs, 1).

no_diag(_, [], _).
no_diag(X, [Y|Ys], D) :-
    A is abs(X - Y),
    A \= D,
    D1 is D + 1,
    no_diag(X, Ys, D1).

lista(M, N, []) :- M > N.
lista(M, N, [M|T]) :-
    M =< N,
    M1 is M + 1,
    lista(M1, N, T).

