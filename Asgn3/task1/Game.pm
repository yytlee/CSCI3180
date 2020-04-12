use strict;
use warnings;

package Game;
use MannerDeckStudent; 
use Player;

sub new {
	my $class = shift @_;
    my @players = (); # list of players
    my @cardList = (); # the list of cards in gameplay area
    my $self = {
        # _numPlayer => shift @_,
        _players => \@players,
        _cardList => \@cardList,
    };
    my $object = bless $self, $class;
    return $object;
}

sub setPlayers {
    my $self = @_;
    foreach my $i (@_){
        my $player = new Player($i, ());
        push(@{$self->{_players}}, $player);
    }
    my $numPlayer = $self->{_players};
    if(52 % $numPlayer == 0 && $numPlayer != 1){
        return 1;
    }
    print "Error: cards' number 52 can not be divided by players number $numPlayer!\n";
    return 0;
}

sub getReturn {
    # only count the cards in array, new card is not counted
    my($self, $card) = @_;
    my $count = 0;
    my $size = $self->{_cardList};
    if($card eq "J"){
        return $size;
    }
    foreach(@{$self->{_cardList}}){
        if($_ eq $card){
            return $size - $count;
        }
        $count = $count + 1;
    }
    return 0;
}

sub showCards {
    my $self = @_;
	print join(" ", @{$self->{_cardList}});
    print "\n";
}

sub startGame {
    
}

return 1;
