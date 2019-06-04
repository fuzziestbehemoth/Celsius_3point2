# Creator: Ande Pierce
# Purpose: The province class, holds data on the population and attributes
# of one region within the celsius 3.2 game
# Start Date 5/30/2019
#

class Province:
    # Contains data on one region
    def __init__(self, name, pop, lit, mmr, imr, mil, acr_ara,
                 acr_pro, anti, ins_gen, mil_gen,
                 pol_gen, res_gen, ava_food, pres_rate,
                 pre_food):
        self.name = name
        self.pop = pop
        # Number of people
    
        # these first three are Global Coalition of Nations development index
        # attributes, which are used for scoring 
    
        self.literacy = lit
        # percent that can read
        self.mmr_100000 = mmr
        #Number of maternal mortalities per 100,000 live births
        self.imr_1000 = imr
        #Number of infant mortalities per 1000 births
        
        self.militancy = mil
        # Militancy represents how prepared for violence the population
        # is, it encompasses gun ownership, self defense training,
        # and aggressive impulses. It effects the production of
        # militant cadre (state-friendly future officers) and insurgents
        # (anti-state actors or randomly violent asocial individuals)
        # antipathy factors into the proportion of the production of
        # militant cadre vs insurgents, as does the propaganda of
        # other nations
        # Number is from 0 (noone here has ever clenched a fist) to
        # 100 (everyone rides the bus with a handgun and a bazooka) ;P
        
        
        
        # These next two are used to determine food generation
        
        self.acres_arable = acr_ara
        # Acres of productive farmland
        self.prod_per_acre = acr_pro
        # How many tons of food each acre produces in 1 month
        
        # Antipathy measures discontent, suffering, and social alienation
        
        self.antipathy = anti
        self.insurgent_gen = ins_gen
        #Number of insurgents (school shooters, armed opposition guerrilas,
        # etc.) generated per month per 100,000 people. Higher antipathy
        #generates a greater number of insurgents
        
        # These next three variables measure the "production" of talented
        # individuals who can be used to implement social policies and
        
        
        # programs. They are generated per 100,000 people
        
        self.militant_cadre_gen = mil_gen
        # Used as the officer corp of a military, to run counterinsurgency
        #programs, etc.
        self.political_cadre_gen = pol_gen
        # Expended for bureucratic work, (IE state media officials, or
        # implementation of universal healthcare program)
        self.research_cadre_gen = res_gen
        # Used for scientific work (IE national soil survey)
        
        # the next three variables are used to track levels
        # of food, from the amount that is produced each
        # turn, and consumed by citizens or wasted, to the
        # amount that is preserved and the total
        # amount hoarded
        
        self.available_food = ava_food
        # tons of food produced but not preserved, for this month (turn)
        self.pres_rate = pres_rate
        # food hoarded per month
        self.preserved_food = pre_food
        # tons of food hoarded against future want or to be exported
        
        self.starved_this_month = False
        #boolean used to determine if province suffered a food shortage this month
        self.num_starved = 0
        #int used to determine how many people went without food. This many do not reproduce this month
        
        self.structures = []
        # list of structures in province
        
        self.policies = []
        # list of policies in province
    def print_name(self):
        # Displays state population
        print(self.name)

    def print_pop(self):
        # Displays state population
        print(self.pop)
    
    def print_literacy(self):
        # Displays state literacy
        print(self.literacy)
    
    def print_mmr(self):
        # Displays state maternal mortality rate
        print(self.mmr_100000)

    def produce_food(self):
        # Produces food equal to average productivity
        # * number of acres
        produced = self.prod_per_acre * self.acres_arable
        return(produced)
    
    def set_cadre_gen(self):
        # Called each month, sets cadre (and insurgent) gen according to algorithyms
        self.set_mil_gen()
        self.set_res_gen()
        self.set_pol_gen()
        self.set_ins_gen()
        
    def set_mil_gen(self):
        # Sets the mil_gen value to militancy * pop / 100,000
        self.mil_gen = self.militancy * self.pop / 100000
    
    def set_res_gen(self):
        # Sets the res_gen value to literacy * pop / 100,000
        self.res_gen = self.literacy * self.pop / 100000
        
    def set_pol_gen(self):
        # Sets the pol_gen value to literacy * pop / 100,000
        self.pol_gen = self.literacy * self.pop / 100000
        
    def set_ins_gen(self):
        # Sets the generation of insurgents to antipathy * militancy * self.pop / 1,000,000
        self.ins_gen = self.antipathy * self.militancy * self.pop / 1000000
        
    def grow(self):
        # The province grows or shrinks, based on its birthrate (determined by stage in demographic transition) and immigration/emigration
        dem_state = self.determine_dem_state()
        birth_rate = self.determine_birth_rate(dem_state)
        immigration = self.determine_immigration()
        
        growth_rate = birth_rate + (immigration / self.pop)
        self.pop = self.pop + self.pop * growth_rate
        
    def determine_dem_state(self):
        # Uses literacy, mmr and imr to determine what stage of the demographic transition the country is in
        # Very simple algorythm for now just so I can have a working thing
        # 0 = 7+ babies per woman
        # 100 = 1.2 babies per woman, and without constant immigration population shrinks each month
        # This function will be reworked as I get a better idea of realistic algorythms to represent the demographic transition 
        dem_state = 50 + self.literacy - self.mmr_100000 - self.imr_1000
        
        if dem_state < 0:
            dem_state = 0
        if dem_state > 100:
            dem_state = 100
        
        print(self.name + "'s demographic rating is" + str(dem_state) + " out of 100.")
        return(dem_state)
        
    def determine_birth_rate(self, dem_state):
        # Birth rate is determined by dem_state. Dem state determines what stage in the demograpghic transition this nation is in
        # dem_state = 0 == 6%
        #
        # dem_state = 100 == -4%
        
        birth_rate = 60 - dem_state / 100
        print (self.name + "'s birth rate is " + str(birth_rate) + "% per year.")
        return(birth_rate)
    
               
    def determine_immigration(self):
        # Eventually will be determined by other nations feelings towards you, propaganda campaigns, etc
        # for now is just determined by literacy mmr and imr (how nice is your place to live) and antipathy (how many people wanna leave)
        
        placeholder_constant = 10000
        antipathy_mod = -1000 * self.antipathy
        immigration = placeholder_constant + antipathy_mod + (placeholder_constant * self.literacy)
        - (placeholder_constant * (self.mmr_100000 + self.imr_1000))
        return(immigration)