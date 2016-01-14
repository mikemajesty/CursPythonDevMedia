import random;

class Table:
    def __init__(self, players):
        self.players = [Player(name,Hand()) for name in players];
        self.deck = Deck();
        self.rounds = 0;

    def deal_cards(self):
        self.deck.shuffle();
        self.deck.setup_hands(self.players);
        for player in self.players:
            player.show_hand();

    def play_once(self,tied = None):
        if tied is None:
            self.count_round();
        collection = Pot();
        for player in (self.players if tied is None else tied):
            player.drop_card(collection);
            if tied:
                player.drop_bonus(collection,3)
        winner = collection.winner;
        if winner is not None:
            collection.reward(winner);
        else: 
            winner = self.play_once(collection.tied);
            collection.reward(winner);
        return winner;

    def count_round(self):
        self.rounds += 1;
        print_underline("Starting.....".format(self.rounds),"=");

    def play_all(self):
        while not self.finished:
            self.play_once();
        self.show_winner();
    def show_winner(self):
        for player in self.players:
            if player.hand.has_cards:
                print();
                print(player.name, " Winner....");
                break;
    @property
    def finished(self):
        return sum(bool(player.hand.cards) for player in self.players) == 1;

class Player:
    def __init__(self,name,hand):
        self.name,self.hand = name,hand;
    def drop_card(self,collection):
        if self.hand.has_cards:
            collection.add_card(self.hand.take_top(),self);
    def drop_bonus(self,collection,count):
        collection.add_bonus(self.hand.cards[:count]);
        self.hand.cards = self.hand.cards[count:];
    def give_cards(self,cards):
        self.hand.add_all(cards);
    def show_hand(self):
        print(self.name," has ",self.hand);