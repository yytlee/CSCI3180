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