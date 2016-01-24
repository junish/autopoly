# coding: utf-8
# Here your code !

class Player:
    def __init__(self,number,name='player'):
       self.number = number
       if name == 'player': self.name = "%s-%d" % (name,self.number)
       else               :self.name = name
       self.info = None
    def update(self,info):
        self.info = info
    def _buy(self, target): return False
    def buyA1(self): return self._buy( A1)
    def buyA2(self): return self._buy( A2)
    def buyB1(self): return self._buy( B1)
    def buyB2(self): return self._buy( B2)
    def buyB3(self): return self._buy( B3)
    def buyC1(self): return self._buy( C1)          
    def buyC2(self): return self._buy( C2)
    def buyC3(self): return self._buy( C3)
    def buyD1(self): return self._buy( D1)
    def buyD2(self): return self._buy( D2)
    def buyD3(self): return self._buy( D3)
    def buyE1(self): return self._buy( E1)
    def buyE2(self): return self._buy( E2)
    def buyE3(self): return self._buy( E3)
    def buyF1(self): return self._buy( F1)
    def buyF2(self): return self._buy( F2)
    def buyF3(self): return self._buy( F3)
    def buyG1(self): return self._buy( G1)
    def buyG2(self): return self._buy( G2)
    def buyG3(self): return self._buy( G3)
    def buyH1(self): return self._buy( H1)
    def buyH2(self): return self._buy( H2)
    def buyR1(self): return self._buy( R1)
    def buyR2(self): return self._buy( R2)
    def buyR3(self): return self._buy( R3)
    def buyR4(self): return self._buy( R4)
    def buyU1(self): return self._buy( U1)
    def buyU2(self): return self._buy( U2)

    def _build_house(self, target): return 0
    def build_houseA1(self): return self._build_house( A1)
    def build_houseA2(self): return self._build_house( A2)
    def build_houseB1(self): return self._build_house( B1)
    def build_houseB2(self): return self._build_house( B2)
    def build_houseB3(self): return self._build_house( B3)
    def build_houseC1(self): return self._build_house( C1)
    def build_houseC2(self): return self._build_house( C2)
    def build_houseC3(self): return self._build_house( C3)
    def build_houseD1(self): return self._build_house( D1)
    def build_houseD2(self): return self._build_house( D2)
    def build_houseD3(self): return self._build_house( D3)
    def build_houseE1(self): return self._build_house( E1)
    def build_houseE2(self): return self._build_house( E2)
    def build_houseE3(self): return self._build_house( E3)
    def build_houseF1(self): return self._build_house( F1)
    def build_houseF2(self): return self._build_house( F2)
    def build_houseF3(self): return self._build_house( F3)
    def build_houseG1(self): return self._build_house( G1)
    def build_houseG2(self): return self._build_house( G2)
    def build_houseG3(self): return self._build_house( G3)
    def build_houseH1(self): return self._build_house( H1)
    def build_houseH2(self): return self._build_house( H2)

    def _build_hotel(self, target): return False
    def build_hotelA1(self): return self._build_hotel( A1)
    def build_hotelA2(self): return self._build_hotel( A2)
    def build_hotelB1(self): return self._build_hotel( B1)
    def build_hotelB2(self): return self._build_hotel( B2)
    def build_hotelB3(self): return self._build_hotel( B3)
    def build_hotelC1(self): return self._build_hotel( C1)
    def build_hotelC2(self): return self._build_hotel( C2)
    def build_hotelC3(self): return self._build_hotel( C3)
    def build_hotelD1(self): return self._build_hotel( D1)
    def build_hotelD2(self): return self._build_hotel( D2)
    def build_hotelD3(self): return self._build_hotel( D3)
    def build_hotelE1(self): return self._build_hotel( E1)
    def build_hotelE2(self): return self._build_hotel( E2)
    def build_hotelE3(self): return self._build_hotel( E3)
    def build_hotelF1(self): return self._build_hotel( F1)
    def build_hotelF2(self): return self._build_hotel( F2)
    def build_hotelF3(self): return self._build_hotel( F3)
    def build_hotelG1(self): return self._build_hotel( G1)
    def build_hotelG2(self): return self._build_hotel( G2)
    def build_hotelG3(self): return self._build_hotel( G3)
    def build_hotelH1(self): return self._build_hotel( H1)
    def build_hotelH2(self): return self._build_hotel( H2)

    def _auction(self, target): return 0
    def auctionA1(self): return self._auction( A1)
    def auctionA2(self): return self._auction( A2)
    def auctionB1(self): return self._auction( B1)
    def auctionB2(self): return self._auction( B2)
    def auctionB3(self): return self._auction( B3)
    def auctionC1(self): return self._auction( C1)
    def auctionC2(self): return self._auction( C2)
    def auctionC3(self): return self._auction( C3)
    def auctionD1(self): return self._auction( D1)
    def auctionD2(self): return self._auction( D2)
    def auctionD3(self): return self._auction( D3)
    def auctionE1(self): return self._auction( E1)
    def auctionE2(self): return self._auction( E2)
    def auctionE3(self): return self._auction( E3)
    def auctionF1(self): return self._auction( F1)
    def auctionF2(self): return self._auction( F2)
    def auctionF3(self): return self._auction( F3)
    def auctionG1(self): return self._auction( G1)
    def auctionG2(self): return self._auction( G2)
    def auctionG3(self): return self._auction( G3)
    def auctionH1(self): return self._auction( H1)
    def auctionH2(self): return self._auction( H2)
    def auctionR1(self): return self._auction( R1)
    def auctionR2(self): return self._auction( R2)
    def auctionR3(self): return self._auction( R3)
    def auctionR4(self): return self._auction( R4)
    def auctionU1(self): return self._auction( U1)
    def auctionU2(self): return self._auction( U2)

    def _sell_building(self, target): return 0
    def sell_buildingA1(self): return self._sell_building( A1)
    def sell_buildingA2(self): return self._sell_building( A2)
    def sell_buildingB1(self): return self._sell_building( B1)
    def sell_buildingB2(self): return self._sell_building( B2)
    def sell_buildingB3(self): return self._sell_building( B3)
    def sell_buildingC1(self): return self._sell_building( C1)
    def sell_buildingC2(self): return self._sell_building( C2)
    def sell_buildingC3(self): return self._sell_building( C3)
    def sell_buildingD1(self): return self._sell_building( D1)
    def sell_buildingD2(self): return self._sell_building( D2)
    def sell_buildingD3(self): return self._sell_building( D3)
    def sell_buildingE1(self): return self._sell_building( E1)
    def sell_buildingE2(self): return self._sell_building( E2)
    def sell_buildingE3(self): return self._sell_building( E3)
    def sell_buildingF1(self): return self._sell_building( F1)
    def sell_buildingF2(self): return self._sell_building( F2)
    def sell_buildingF3(self): return self._sell_building( F3)
    def sell_buildingG1(self): return self._sell_building( G1)
    def sell_buildingG2(self): return self._sell_building( G2)
    def sell_buildingG3(self): return self._sell_building( G3)
    def sell_buildingH1(self): return self._sell_building( H1)
    def sell_buildingH2(self): return self._sell_building( H2)

    def offer(self): return {'money':0, 'land':[],'jailcard':0, 'player_id':-1}
    def counter_offer(self, land_infor, players_info): return {'money':0, 'land':[],'jailcard':0, 'player_id':-1}
    def _assess(self, land_infor, players_ target): return 0
    def assessA1(self): return self._assess( A1)
    def assessA2(self): return self._assess( A2)
    def assessB1(self): return self._assess( B1)
    def assessB2(self): return self._assess( B2)
    def assessB3(self): return self._assess( B3)
    def assessC1(self): return self._assess( C1)
    def assessC2(self): return self._assess( C2)
    def assessC3(self): return self._assess( C3)
    def assessD1(self): return self._assess( D1)
    def assessD2(self): return self._assess( D2)
    def assessD3(self): return self._assess( D3)
    def assessE1(self): return self._assess( E1)
    def assessE2(self): return self._assess( E2)
    def assessE3(self): return self._assess( E3)
    def assessF1(self): return self._assess( F1)
    def assessF2(self): return self._assess( F2)
    def assessF3(self): return self._assess( F3)
    def assessG1(self): return self._assess( G1)
    def assessG2(self): return self._assess( G2)
    def assessG3(self): return self._assess( G3)
    def assessH1(self): return self._assess( H1)
    def assessH2(self): return self._assess( H2)
    def assessR1(self): return self._assess( R1)
    def assessR2(self): return self._assess( R2)
    def assessR3(self): return self._assess( R3)
    def assessR4(self): return self._assess( R4)
    def assessU1(self): return self._assess( U1)
    def assessU2(self): return self._assess( U2)

    def useJailCard(self, jail_info): return False
    def buyOfferJailCard(self, jail_ target): return 0
    def sellOfferJailCard(self, jail_info): return 0
    def assessJailCardForSell(self): return 0
    def assessJailCardForBuy(self): return 0
    def payJailFee(self, jail_info): return False

    def auction_house(self): return 0
    def auction_hotel(self): return 0
    def mortgage(self): return {'bland':[]}
    def mortgagefee(self, mortgage_info): return {'bland':[]}

    def _get_mymoney(self): return self.info.player_info.money(self.number)
    def _has_land(self, target): return info.land_info.has_land(self.number, target)
    def _whose_land(self, target): return info.land_info.whose_land(target)
    def _how_many_houses(self, target): return info.land_info.how_many_houses(target)
    def _exist_hotel(self,target): return info.land_info.exist_hotel(target)
    def _how_much_rental_fee(self, target): return info.land_info.how_much_rental_fee(target)
    def _how_much_most_expensive_fee(self, s, f): return info.land_manager.how_much_most_expensive_fee(self.number,s,f)
    def _get_land_info(self,land_target): return land_info.get_land_info(target)
    def _how_many_have_same_group(self, land_ target): return False
    def _has_jail_card(self, player_info): return player_info.get_jail_card(self.number)
    def _get_myname(self): return self.name
    def _how_many_lands_rest(self, land_info): return 0

    def send_message(self,target): return {'player':self.number, 'message':'hello'}

Player(1)
Player(2,'yamaoka')
