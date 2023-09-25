sum([], 0).
sum([H|T], N):-
    sum(T, X),
    N is X + H.
?- sum([1,2,3,3,4,4],N), write(N).