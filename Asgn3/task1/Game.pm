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
        _players => \@players,
        _cardList => \@cardList,
        _deck => new MannerDeckStudent(),
    };
    my $object = bless $self, $class;
    return $object;
}

sub set_players {
    my ($self, $arr) = @_;
    my @name = @$arr;
    foreach(@name){
        my $player = new Player($_, ());
        push(@{$self->{_players}}, $player);
    }
    my $numPlayer = @{$self->{_players}};
    if(52 % $numPlayer == 0 && $numPlayer != 1){
        my $player = @{$self->{_players}};
        print "There $numPlayer players in the game:\n";
        foreach my $i(@{$self->{_players}}){
            print $i->{_name} . " ";
        }
        print("\n\n");
        return 1;
    }
    print "Error: cards' number 52 can not be divided by players number $numPlayer!\n";
    return 0;
}

sub getReturn {
    # only count the cards in array, new card is not counted
    my ($self, $card) = @_;
    my $count = 0;
    my $size = scalar @{$self->{_cardList}};
    if($card eq "J"){
        return $size;
    }
    foreach(@{$self->{_cardList}}){
        if($_ eq $card){
            # print "size: $size, count: $count\n";
            return ($size - $count);
        }
        $count = $count + 1;
    }
    return 0;
}

sub showCards {
    my ($self) = @_;
	print join(" ", @{$self->{_cardList}});
    print "\n";
}

sub checkLoser {
    my $p = shift @_;
    my $loser = 0;
    foreach my $elem (@$p){
        if($elem->numCards() == 0){
            $loser = $loser + 1;
        }
    }
    return $loser;
}

sub start_game {
    my ($self) = @_;
    $self->{_deck}->shuffle();
    my @aPlayer = @{$self->{_players}};
    my $numPlayer = @{$self->{_players}};
    # my $numCard = 52 / $numPlayer;
    my @shuffleCards = ($self->{_deck}->AveDealCards($numPlayer));

    for my $i (0..$#shuffleCards){
        for my $j (@{$shuffleCards[$i]}){
            $aPlayer[$i]->getCards($j);
        }
    }

    print("Game begin!!!\n\n");
    my $loser = 0;
    my $flag = 1;
    my $round = 0;
    while($flag){
        foreach(@{$self->{_players}}){
            if($_->numCards() == 0){
                next;
            }
            my $name = $_->{_name};
            my $playerCard = $_->numCards();
            print "Player $name has $playerCard cards before deal.\n";
            print "=====Before player's deal=======\n";
            $self->showCards();
            print "================================\n";
            my $currentCard = $_->dealCards();
            print "$name ==> card $currentCard\n";
            my $returnCard = $self->getReturn($currentCard);
            # print "return $returnCard\n";
            if($returnCard == 0){
                push(@{$self->{_cardList}}, $currentCard);
            }
            else{
                # print $returnCard;
                $_->getCards($currentCard);
                for my $i (0..$returnCard - 1){
                    my $shiftCard = pop @{$self->{_cardList}};
                    $_->getCards($shiftCard);
                }
            }
            $playerCard = $_->numCards();
            print "=====After player's deal=======\n";
            $self->showCards();
            print "================================\n";
            print "Player $name has $playerCard cards after deal.\n";
            if($_->numCards() == 0){
                print "Player $name has no cards, out!\n";
                $loser = $loser + 1;
                if(checkLoser(\@{$self->{_players}}) == $numPlayer - 1){
                    $flag = 0;
                    last;
                }
            }
            print "\n";
        }
        $round = $round + 1;
        if($loser == $numPlayer - 1){
            last;
        }
        $loser = 0;
    }
    foreach(@{$self->{_players}}){
        if($_->numCards() != 0){
            my $name = $_->{_name};
            print "\nWinner is $name in game $round\n";
            last;
        }
    }
}

return 1;
