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
package Land;

sub new {
    my $class = shift;
    my $self  = {
        owner => undef,
        level => 0,
    };
    bless $self, $class;
    return $self;
}

sub print {
    my $self = shift;
    if (!defined($self->{owner})) {
        print("Land ");
    } else {
        print("$self->{owner}->{name}:Lv$self->{level}");
    }
}

sub buyLand {

    # ...

    my $self = shift;
    if($main::cur_player->{money} < 1100){
        print("You do not have enough money to buy the land\n");
        return;
    }
    $self->{owner} = $main::cur_player;
    local $Player::due = 1000;
    local $Player::handling_fee_rate = 0.1;

    $main::cur_player->payDue();
}

sub upgradeLand {

    # ... 
    my $self = shift;
    my $fee = 1000;
    if($self->{level} == 1){
        $fee = 2000;
    }
    elsif($self->{level} == 2){
        $fee = 5000;
    }
    local $Player::due = $fee;
    local $Player::handling_fee_rate = 0.1;
    if($main::cur_player->{money} < ($fee * (1 + $Player::handling_fee_rate))){
        print "You do not have enough money to upgrade the land!\n";
        return;
    }
    $self->{level} = $self->{level} + 1;

    $main::cur_player->payDue();
}

sub chargeToll {

    # ...
    my $self = shift;
    my $fee = 500;
    if($self->{level} == 1){
        $fee = 1000;
    }
    elsif($self->{level} == 2){
        $fee = 1500;
    }
    elsif($self->{level} == 3){
        $fee = 3000;
    }
    local $Player::due = $fee;
    local $Player::handling_fee_rate = 0;
    local $Player::income = 0;
    if($main::cur_player->{money} < $fee){
        $Player::due = $main::cur_player->{money};
    }
    $main::cur_player->payDue();

    # ...
    $Player::due = 0;
    $Player::income = $fee;
    local $Player::tax_rate = 0.1;
    if($self->{level} == 1){
        $Player::tax_rate = 0.15;
    }
    elsif($self->{level} == 2){
        $Player::tax_rate = 0.2;
    }
    elsif($self->{level} == 3){
        $Player::tax_rate = 0.25;
    }

    $self->{owner}->payDue();
}

sub stepOn {

    # ...
    my $self = shift;
    if(!defined($self->{owner})){ #nobody own the land
        print "Pay \$1000 to buy the land? [y/n]\n";
        my $response = " ";
        while($response = <STDIN>){
            chomp($response);
            if($response eq "y"){
                $self->buyLand();
                last;
            }
            elsif($response eq "n"){
                last;
            }
            print "Pay \$1000 to buy the land? [y/n]\n";
        }
    }
    elsif($self->{owner} ne $main::cur_player){ # step on the other player's land
        my $fee = 500;
        if($self->{level} == 1){
            $fee = 1000;
        }
        elsif($self->{level} == 2){
            $fee = 1500;
        }
        elsif($self->{level} == 3){
            $fee = 3000;
        }
        my $ownerName = $self->{owner}->{name};
        print("You need to pay player $ownerName \$$fee\n");
        $self->chargeToll();
    }
    elsif($self->{level} == 3){}
    elsif($self->{owner} eq $main::cur_player){
        my $fee = 1000;
        if($self->{level} == 1){
            $fee = 2000;
        }
        elsif($self->{level} == 2){
            $fee = 5000;
        }
        print "Pay \$$fee to upgrade the land? [y/n]\n";
        my $response = " ";
        while($response = <STDIN>){
            chomp($response);
            if($response eq "y"){
                $self->upgradeLand();
                last;
            }
            elsif($response eq "n"){
                last;
            }
            print "Pay \$$fee to upgrade the land? [y/n]\n";
        }
    }
    

}
1;