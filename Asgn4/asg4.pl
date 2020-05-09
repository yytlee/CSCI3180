% /*
%  * CSCI3180 Principles of Programming Languages
%  *
%  * --- Declaration ---
%  *
%  * I declare that the assignment here submitted is original except for source
%  * material explicitly acknowledged. I also acknowledge that I am aware of
%  * University policy and regulations on honesty in academic work, and of the
%  * disciplinary guidelines and procedures applicable to breaches of such policy
%  * and regulations, as contained in the website
%  * http://www.cuhk.edu.hk/policy/academichonesty/
%  *
%  * Assignment 4
%  * Name : Lee Tsz Yan
%  * Student ID : 1155110177
%  * Email Addr : tylee8@cse.cuhk.edu.hk
%  */


% append/3
append([],L,L).
append([X|L1],L2,[X|L3]):-append(L1,L2,L3).

% Q1
% a
element_last(X, L) :- append(_, [X], L).

%element_n(X, L, N) :- append([A|X], [B], L).
% b
element_n(X, [X|_], s(0)).
element_n(X, [_|L], s(N)) :- element_n(X, L, N).

% c
remove_n(X, [X|K], s(0), K).
remove_n(X, [A|L], s(N), [A|K]) :- remove_n(X, L, N, K).

% d
% remove_n(a, L, s(s(0)), [c, d, b, e]).

% e
insert_n(H, L, N, A) :- remove_n(H, A, N, L).

% f
repeat_three([], []).
repeat_three([A|B], [A,A,A|C]) :- repeat_three(B,C).

% g
% repeat_three(X, [i,i,i,m,m,m,n,n,n]).

% sum(0,0,0) :- sum(s(0), s(0), s(s(0))).

% Q2
% sum/3
sum(0,X,X).
sum(s(X),Y,s(Z)) :- sum(X,Y,Z).

% a
% mt(a, [mt(b, [mt(e, []), mt(f, [])]), mt(c, []), mt(d, [mt(g, [])])]).

% b
% mt(_, []).
is_tree(mt(_, T)) :- tree(T).

tree([]).
tree([T|U]) :- is_tree(T), tree(U).

% c
num_node(mt(_,[]), s(0)).
num_node(mt(_, [R|T]), s(N)) :- num_node(R, N1), sub_node(T, N2), sum(N1, N2, N).
sub_node([], 0).
sub_node([R|T], N) :- num_node(R, N1), sub_node(T, N2), sum(N1, N2, N).

% d
% sum_length(mt(_, []), 0).

sum_length(T, L) :- node_count(T, L, 0).
node_count(mt(_, []), 0, _).
node_count(mt(_, [H|T]), S, L) :- node_count(H, N1, s(L)), tree_node(T, N2, s(L)), sum(N1, N2, N), sum(N, s(L), S).
tree_node([], 0, _).
tree_node([H|T], S, L) :- tree_node(T, N1, L), node_count(H, N2, L), sum(N1, N2, N), sum(L, N, S).

