use strict;
use warnings;
require "./Player.pm";

package Jail;
sub new {
    my $class = shift;
    my $self  = {};
    bless $self, $class;
    return $self;
}

sub print {
    print("Jail ");
}

sub stepOn {

    # ...
    my $self = shift;
    my $jail = 2;
    # $main::cur_player->{num_rounds_in_jail} = 2;
    print "Pay \$1000 to reduce the prison round to 1? [y/n]\n";
    my $response;
    while($response = <STDIN>){
        chomp($response);
        if($response eq "y" && $main::cur_player->{money} < 1100){
            print("You do not have enough money to reduce the prison round!\n");
            last;
        }
        elsif($response eq "y"){
            $jail = 1;
            local $Player::due = 1000;
            local $Player::handling_fee_rate = 0.1;
            local $Player::income = 0;
            $main::cur_player->payDue();
            last;
        }
        elsif($response eq "n"){
            last;
        }
        print "Pay \$1000 to reduce the prison round to 1? [y/n]\n";
    }
    local $Player::prison_rounds = $jail;

    $main::cur_player->putToJail();
}

1;
