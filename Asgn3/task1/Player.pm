# /*
#  * CSCI3180 Principles of Programming Languages
#  *
#  * --- Declaration ---
#  *
#  * I declare that the assignment here submitted is original except for source
#  * material explicitly acknowledged. I also acknowledge that I am aware of
#  * University policy and regulations on honesty in academic work, and of the
#  * disciplinary guidelines and procedures applicable to breaches of such policy
#  * and regulations, as contained in the website
#  * http://www.cuhk.edu.hk/policy/academichonesty/
#  *
#  * Assignment 3
#  * Name : Lee Tsz Yan
#  * Student ID : 1155110177
#  * Email Addr : tylee8@cse.cuhk.edu.hk
#  */
use strict;
use warnings;
 
package Player;
sub new {
    my $class = shift @_;
    my @cards = ();
    my $self = {
        _name => shift @_,
        _cards => \@cards,
    };
    my $object = bless $self, $class;
    return $object;
}

sub getCards {
    my ($self, $card) = @_;
    push(@{$self->{_cards}}, $card);
}

sub dealCards {
    my ($self) = @_;
    my $cards = $self->{_cards};
    my $card = shift(@$cards);
    return $card;
}

sub numCards {
    my ($self) = @_;
    my $size = scalar @{$self->{_cards}};
    return $size;
}

return 1;