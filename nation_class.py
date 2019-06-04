# Creator: Ander Pierce
# Objective: Nation class for Celsius 3.2, holds info on terrain,
# social, and demographic characteristics of each nation
# May alters national info, and runs monthly cycle when told to by
# the time_controller class.
# Start Date 5/30/2019


from province_class import Province

class Nation:
    def __init__(self, name, abrv):
        self.name = name
        self.abbreviation = abrv
        self.turn = 0
        self.months = ['Jan', 'Feb', 'Mar', 'Apr',
                       'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec'
                       ]
        self.current_month = self.months[0]
        self.month_num = 0
        self.provinces = []
        self.mil_cadre = 0
        self.res_cadre = 0
        self.pol_cadre = 0
        self.insurgents = 0
        
        denver = Province('denver', 10000000, 35.4, 22.5, 30, 15, 200000, 1, 15, 4, 8, 8,
                  8,0, 0, 0)
        
        # For now the only nation is the Republic of the Colorado River
        # and its only province is Denver
        self.provinces.append(denver)
        self.month_food = 0
        
        #certainly unfinished
    def month_change(self):
        #The month changes, commodities are produced, people eat or starve
        # cadre are generated, agricultural lands degrade or improve
        # watersheds recharge or are depleted, regional temps change
        # and time generally moves onwards
        
        
        # Change the month, December becomes January 
        if self.current_month == 'Dec':
            self.month_num = 0
        else:
            self.current_month = self.months[self.month_num + 1]
            
        print("The month is " + self.current_month + ".")
        
        # Provinces produce food
        self.provinces_produce()
        
        # People eat or starve
        self.provinces_eat()
        
        self.provinces_grow()
        self.provinces_gen_cadre()

    def provinces_produce(self):
        #Provinces produce food
        for province in self.provinces:
            self.month_food += province.produce_food()
            print(province.name + " produces " + str(province.produce_food()
                                                     )
                  + "tons of food."
                  )
        # Provinces exploit non-food resources
        
    def provinces_eat(self,):
        #Assumes people eat 3 pounds each day, 90 pounds a month
        # or .045 tons a year  --> should turn into a global constant
        # People eat or starve
        
        # Soon, we should make people tap into stored foods, after
        # they eat monthly production
        for province in self.provinces:
            tons_consumed = province.pop * 0.045
            if self.month_food >= tons_consumed:
                self.month_food -= tons_consumed
                print("People in " + province.name + " eat "
                      + str(tons_consumed) + " tons of food!")
                print("There are " + self.month_food +
                      " tons of food left, nationally")
            else:
                self.people_starve(tons_consumed - self.month_food, province)
                self.month_food = 0              
    
    def provinces_grow(self):
        # All the provinces grow
        for province in self.provinces:
            province.grow()
        
    def people_starve(self, tons_short, province):
        # If food production + importation +
        # stored food is
        # not sufficient to feed pop, call this
        num_starved = int(22.22 * tons_short)
        print("Your people are starving! They are short " +
              str(tons_short) + " tons of food, which means "
              + str(num_starved) + " people go hungry."
              + " Unrest increases, and the Global Coalition of Nations shakes its head.")
        
        #antipathy is generated (right now a flat antipathy amount is added each time anyone starves)
        province.antipathy = province.antipathy + 5
        
    def provinces_gen_cadre(self):
        for province in self.provinces:
            province.set_cadre_gen()
            self.mil_cadre += province.mil_gen
            self.res_cadre += province.res_gen
            self.pol_cadre += province.pol_gen
            self.insurgents += province.ins_gen
            print(province.name + " produces " + str(province.mil_gen) + " new militant cadre. The " + self.name + "s total is " + str(self.mil_cadre) + ".")
            print(province.name + " produces " + str(province.res_gen) + " new scientific cadre. The " + self.name + "s total is " + str(self.res_cadre) + ".")
            print(province.name + " produces " + str(province.pol_gen) + " new political cadre. The " + self.name + "s total is " + str(self.pol_cadre) + ".")
            print(province.name + " produces " + str(province.ins_gen) + " new insurgents! The " + self.name + "s total is " + str(self.insurgents) + ".")

        
"""  
    def store_resources(self, provinces):
        # Add preserved food and lasting
        # exploitables to the provinical or national lists
        for province in provinces:
            if province.ava_food > province.pres_rate:
                # If the food preservation rate is less
                # than food produced this month
                # store some food and subtract the amount
                # stored from food that must be eaten this
                # month or wasted
                province.ava_food = province.ava_food -
                pres_rate
                
                province.preserved_food += pres_rate
                
            else:
                province.ava_food = 0
                province.preserved_food +=
                province.ava_food
                
    
        def award_points():
        # Points are awarded for meeting GCN development
        # goals
        
        #IE high Literacy, low maternal and infant mortality
        # everybody eats
        

"""