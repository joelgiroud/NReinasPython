%
:- use_module(library(socket)).

:- consult(reinas).

servidor:-
    tcp_socket(Socket), 
    tcp_bind(Socket, 50000), 
    tcp_listen(Socket, 5), 
    tcp_open_socket(Socket, AcceptFd, _),
    dispatch(AcceptFd).

dispatch(AcceptFd):-
    tcp_accept(AcceptFd, Socket, Peer),
    process_client(Socket, Peer).
    thread_create(process_client(Socket, Peer), _, [ detached(true)]).
    dispatch(AcceptFd). % Con esta linea se pueden atender muchas llamadas
    % Sin ella solo se atiende una llamada

process_client(Socket, Peer) :-
    write(' Recibi llamada de: '), write(Peer), nl,
    setup_call_cleanup(
        tcp_open_socket(Socket, StreamPair),
        doService(Peer, StreamPair),  % Actualizado: se pasa Peer como primer argumento
        close(StreamPair)).

doService(ClientIP, Stream):-
    write('Recibi llamada de: '), write(ClientIP), nl,
    repeat, % Manda Varias cadenas
    read(Stream, N),
    (N == end_of_file ->
        true % No hagas nada en caso de end_of_file
    ;
        (reinas(N, L), write(Stream, L), put(Stream, 13), put(Stream, 10));
        write(Stream, no), put(Stream, 13), put(Stream, 10)
    ),
    flush_output(Stream),
    (N == end_of_file ->
        true % No hagas nada en caso de end_of_file
    ;
        N == fin ->
        write(' Adios '), nl
    ;
        fail
    ).

member(X, [X|Xs]).
member(X, [Y|Ys]):-member(X,Ys).