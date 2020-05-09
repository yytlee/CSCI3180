(* % /*
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
%  */ *)


datatype suit = Clubs | Diamonds | Hearts | Spades;
datatype hand = Nothing | Pair | Two_Pairs | Three_Of_A_Kind | Full_House | Four_Of_A_Kind | Flush | Straight;
type card = suit * int;
type rank_pair = hand * (int * int)list;

(* fun gt_suit(_:suit, Spades:suit) = false
    | gt_suit(Spades:suit, _:suit) = true
    | gt_suit(_:suit, Clubs:suit) = true
    | gt_suit(Clubs:suit, _:suit) = false
    | gt_suit(s1:suit, s2:suit) = s1 = Hearts andalso s2 = Diamonds; *)

fun last(L:card list):card = 
    if(length(L) = 1)then(hd(L))
    else(last(L));

(* 1. *)
fun check_flush(L:card list):bool = 
    if(length(L) = 1)then(true)
    else((#1(hd(L)) = #1(hd(tl(L)))) andalso check_flush(tl(L)));

(* 2. *)
fun compare_flush(L1:card list, L2:card list):string = 
    if(L1 = nil)then("This is a tie")
    else if(#2(hd(L1)) > #2(hd(L2)))then("Hand 1 wins")
    else if(#2(hd(L1)) < #2(hd(L2)))then("Hand 2 wins")
    (* else if(#1(hd(L1)) <> #1(hd(L2)) andalso gt_suit(#1(hd(L1)), #1(hd(L2))))then("Hand 1 wins")
    else if(#1(hd(L1)) <> #1(hd(L2)))then("Hand 2 wins") *)
    else(compare_flush(tl(L1), tl(L2)));

(* 3. *)
fun check_straight(L:card list):bool = 
    if(length(L) = 1 orelse (length(L) = 2 andalso #2(hd(L)) = 10 andalso #2(hd(tl(L))) = 1))then(true)
    else(#2(hd(L)) - 1 = #2(hd(tl(L))) andalso check_straight(tl(L)));

(* 4. *)
fun compare_straight(L1:card list, L2:card list):string = 
    if(#2(hd(L1)) > #2(hd(L2)))then("Hand 1 wins")
    else if(#2(hd(L1)) < #2(hd(L2)))then("Hand 2 wins")
    else if(#2(hd(L1)) = 13 andalso #2(hd(L2)) = 13 andalso #2(last(L1)) = 1 andalso #2(last(L2)) = 9)then("Hand 1 wins")
    else if(#2(hd(L1)) = 13 andalso #2(hd(L2)) = 13 andalso #2(last(L1)) = 9 andalso #2(last(L2)) = 1)then("Hand 2 wins")
    else("This is a tie");

fun count(L:card list):(int * int)list = 
    let
        fun sub_count(nil, L, i) = (L, i)::nil
        | sub_count((h:card)::t, aCard, i) = 
            if aCard = #2(h) then sub_count(t, #2(h), i+1)
            else(aCard, i)::sub_count(t, #2(h), 1)
    in
        sub_count(tl(L), #2(hd(L)), 1)
    end;

fun sort [] = [] | sort (x::xs) = 
    let
        fun insert(x:(int * int), []) = [x]
            | insert(x:(int * int), y::ys) = 
                if(#2(x) >= #2(y)) then x::y::ys
                else y::insert(x, ys)
    in
        insert(x, sort xs)
    end;

(* 5. *)
fun count_patterns(L:card list):rank_pair = 
    let
        val L2 = sort(count(L))
         
        fun sub_patten(L: (int * int) list as (_, 4)::t, _):rank_pair = (Four_Of_A_Kind, L2)
            | sub_patten((_, 1)::t, 0) = sub_patten(t, 1)
            | sub_patten((_, 2)::t, 0) = sub_patten(t, 2)
            | sub_patten((_, 3)::t, 0) = sub_patten(t, 3)
            | sub_patten((_, 1)::t, 2) = (Pair, L2)
            | sub_patten((_, 2)::t, 2) = (Two_Pairs, L2)
            | sub_patten((_, 1)::t, 3) = (Three_Of_A_Kind, L2)
            | sub_patten((_, 2)::t, 3) = (Full_House, L2)
            | sub_patten(_, _) = (Nothing, L2)
    in
        sub_patten(L2, 0)
    end;

(* 6. *)
fun compare_count(L1:card list, L2:card list):string = 
    (* tie for hand => False, 2nd wins => False, 1st wins => True *)
    let
        fun gt_hand(Nothing, _) = false 
            | gt_hand(_, Four_Of_A_Kind) = false
            | gt_hand(Pair, Pair) = false
            | gt_hand(Pair, Two_Pairs) = false
            | gt_hand(Pair, Three_Of_A_Kind) = false
            | gt_hand(Pair, Full_House) = false
            | gt_hand(Two_Pairs, Two_Pairs) = false
            | gt_hand(Two_Pairs, Three_Of_A_Kind) = false
            | gt_hand(Two_Pairs, Full_House) = false
            | gt_hand(Three_Of_A_Kind, Three_Of_A_Kind) = false
            | gt_hand(Three_Of_A_Kind, Full_House) = false
            | gt_hand(Full_House, Full_House) = false
            | gt_hand(_,_) = true

        val P1 = count_patterns(L1)
        val P2 = count_patterns(L2)
        fun compare(nil, nil) = "This is a tie"
            | compare((h1:(int * int)list), (h2:(int * int)list)) = 
                if (#1(hd(h1)) > #1(hd(h2))) then "Hand 1 wins"
                else if(#1(hd(h1)) < #1(hd(h2))) then "Hand 2 wins"
                else compare(tl(h1), tl(h2))
    in
        if(gt_hand(#1(P1), #1(P2))) then "Hand 1 wins"
        else if(gt_hand(#1(P2), #1(P1))) then "Hand 2 wins"
        else compare(#2(P1), #2(P2))
    end;


