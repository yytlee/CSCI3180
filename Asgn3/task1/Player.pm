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
    my $self = @_;
    my $card = @_;
    push(@{$self->{_name}}, $card);
}

sub dealCards {
    my $self = @_;
    my $card = shift(@{$self->{_cards}});
    return $card;
}

sub numCards {
    my $self = @_;
    my $size = $self->{_cards};
    return $size;
}

return 1;