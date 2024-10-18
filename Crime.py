def probability(DC, DEX, CHAINTWIS, xp1, xp2, xp3, PB, lucky, reliable):
    # DC = {10,15,20,25}
    # xp1 = 0 if not proficient; 1 if proficient; 2 if expertise in Stealth
    # xp2 = 0 if not proficient; 1 if proficient; 2 if expertise in Thieves' tool
    # xp3 = 0 if not proficient; 1 if proficient; 2 if expertise in Deception(CHA)/Investigation(INT)/Perception(WIS)
    # depending on which Ability Check is made => CHAINTWIS is determined
    # PB = proficiency bonus

    #reliable 11th Lvl Rogue Feature
    #Lucky Lineage Feat (Halfling)

    if reliable:
        real_Stealth_DC = DC - 11 - DEX - PB * xp1
        real_Thieves_Tool_DC = DC - 11 - DEX - PB * xp2
        real_Swindling_DC = DC - 1 - CHAINTWIS - PB * xp3

        failing_1st_AC = real_Stealth_DC/20
        failing_2nd_AC = real_Thieves_Tool_DC/20
        failing_3rd_AC = real_Swindling_DC/20

        if real_Stealth_DC <1:
            if real_Thieves_Tool_DC <1:
                if real_Swindling_DC <1:
                    return [1, 1 ,0.5, 0, 0, 0, -1, 0]
                else:
                    return [1, 1-failing_3rd_AC,
                            0.5, failing_3rd_AC,
                            0,0,-1,0]
            else:
                if real_Swindling_DC <1:
                    return [1, 1-failing_2nd_AC,
                            0.5, failing_2nd_AC,
                            0, 0, -1, 0]
                else:
                    return [1, (1-failing_2nd_AC)*(1-failing_3rd_AC),
                            0.5, failing_2nd_AC+failing_3rd_AC,
                            0, failing_2nd_AC*failing_3rd_AC,
                            -1,0]
        else:
            if real_Thieves_Tool_DC <1:
                if real_Swindling_DC <1:
                    return [1, 1-failing_1st_AC,
                            0.5, failing_1st_AC,
                            0, 0, -1, 0]

                else:
                    return [1, (1-failing_1st_AC)*(1-failing_3rd_AC),
                            0.5, failing_1st_AC+failing_3rd_AC,
                            0,0,-1,0]
            else:
                if real_Swindling_DC <1:
                    return [1, (1-failing_1st_AC)*(1-failing_2nd_AC),
                            0.5, failing_1st_AC+failing_2nd_AC,
                            0, failing_1st_AC*failing_2nd_AC,
                            -1,0]
                else:
                    return [1, (1-failing_1st_AC)*(1-failing_2nd_AC)*(1-failing_3rd_AC),
                            0.5, failing_1st_AC*(1-failing_2nd_AC)*(1-failing_3rd_AC)+(1-failing_1st_AC)*failing_2nd_AC*(1-failing_3rd_AC)+(1-failing_1st_AC)*(1-failing_2nd_AC)*failing_3rd_AC,
                            0, (1-failing_1st_AC)*failing_2nd_AC*failing_3rd_AC+failing_1st_AC*(1-failing_2nd_AC)*failing_3rd_AC+failing_1st_AC*failing_2nd_AC*(1-failing_3rd_AC),
                            -1, failing_1st_AC*failing_2nd_AC*failing_3rd_AC]

    else:
        real_Stealth_DC = DC - 1 - DEX - PB * xp1
        real_Thieves_Tool_DC = DC - 1 - DEX - PB * xp2
        real_Swindling_DC = DC - 1 - CHAINTWIS - PB * xp3

        failing_1st_AC = real_Stealth_DC/20
        failing_2nd_AC = real_Thieves_Tool_DC/20
        failing_3rd_AC = real_Swindling_DC/20

        nat1 = 1/20
        if lucky:
            nat1 = 1/(20*20)

        if real_Stealth_DC < 1:
            if real_Thieves_Tool_DC < 1:
                if real_Swindling_DC < 1:
                    return [1, (1-nat1)*(1-nat1)*(1-nat1),
                            0.5, 3*(1-nat1)*(1-nat1)*nat1,
                            0, 3*nat1*nat1*(1-nat1),
                            -1, nat1 * nat1 * nat1]
                else:
                    return [1, (1-nat1)*(1-nat1)*(1-failing_3rd_AC),
                            0,5, 2*nat1*(1-nat1)*(1-failing_3rd_AC)+failing_3rd_AC*nat1*nat1,
                            0,nat1*nat1*(1-failing_3rd_AC)+2*(1-nat1)*nat1*failing_3rd_AC,
                            -1, nat1 * nat1 * failing_3rd_AC]
            else:
                if real_Swindling_DC < 1:
                    return [1, (1-nat1)*(1-nat1)*(1-failing_2nd_AC),
                            0,5, 2*nat1*(1-nat1)*(1-failing_2nd_AC)+failing_2nd_AC*nat1*nat1,
                            0,nat1*nat1*(1-failing_2nd_AC)+2*(1-nat1)*nat1*failing_2nd_AC,
                            -1, nat1 * nat1 * failing_2nd_AC]
                else:
                    return [1,(1-nat1)*(1-failing_2nd_AC)*(1-failing_3rd_AC),
                            0.5,nat1*(1-failing_2nd_AC)*(1-failing_3rd_AC)+(1-nat1)*failing_2nd_AC*(1-failing_3rd_AC+(1-nat1)*(1-failing_2nd_AC)*failing_3rd_AC),
                            0,(1-nat1)*failing_2nd_AC*failing_3rd_AC+nat1*(1-failing_2nd_AC)*failing_3rd_AC+nat1*failing_2nd_AC*(1-failing_3rd_AC),
                            -1, nat1 * failing_2nd_AC * failing_3rd_AC]
        else:
            if real_Thieves_Tool_DC < 1:
                if real_Swindling_DC < 1:
                    return [1, (1-failing_1st_AC)*(1-nat1)*(1-nat1),
                            0.5,failing_1st_AC*(1-nat1)*(1-nat1)+(1-failing_1st_AC)*nat1*(1-nat1),
                            0, (1-failing_1st_AC)*nat1*nat1+2*failing_1st_AC*(1-nat1)*nat1,
                            -1, failing_1st_AC * nat1 * nat1]
                else:
                    return [1,(1-failing_1st_AC)*(1-nat1)*(1-failing_3rd_AC),
                            0.5, (1-failing_1st_AC)*(1-nat1)*failing_3rd_AC+(1-failing_1st_AC)*nat1*(1-failing_3rd_AC)+failing_1st_AC*(1-nat1)*(1-failing_3rd_AC),
                            0, (1-failing_1st_AC)*nat1*failing_3rd_AC+failing_1st_AC*(1-nat1)*failing_3rd_AC+failing_1st_AC*nat1*(1-failing_3rd_AC),
                            -1, failing_1st_AC * nat1 * failing_3rd_AC]
            else:
                if real_Swindling_DC < 1:
                    return [1, (1-failing_1st_AC) * (1-failing_2nd_AC) * (1-nat1),
                            0.5, failing_1st_AC * (1-failing_2nd_AC) * (1-nat1)+ (1-failing_1st_AC) * failing_2nd_AC * (1-nat1)+(1-failing_1st_AC) * (1-failing_2nd_AC) * nat1,
                            0, failing_1st_AC*failing_2nd_AC*(1-nat1)+failing_1st_AC*(1-failing_2nd_AC)*nat1+(1-failing_1st_AC)*failing_2nd_AC*nat1,
                            -1, failing_1st_AC * failing_2nd_AC * nat1]
                else:
                    return [1, (1-failing_1st_AC)*(1-failing_2nd_AC)*(1-failing_3rd_AC),
                            0.5, failing_1st_AC*(1-failing_2nd_AC)*(1-failing_3rd_AC)+(1-failing_1st_AC)*failing_2nd_AC*(1-failing_3rd_AC)+(1-failing_1st_AC)*(1-failing_2nd_AC)*failing_3rd_AC,
                            0, failing_1st_AC*failing_2nd_AC*(1-failing_3rd_AC)+failing_1st_AC*(1-failing_2nd_AC)*failing_3rd_AC+(1-failing_1st_AC)*failing_2nd_AC*failing_3rd_AC,
                            -1, failing_1st_AC * failing_2nd_AC * failing_3rd_AC]



def rollProfit():
    pass

def medianProfit(DC):
    data = probability(DC, 5, 2, 2, 2, 2, 5, False, True)

    investment = -25
    if DC < 11:         earnings = 50
    elif DC <16:        earnings = 100
    elif DC <21:        earnings = 200
    else:        earnings = 1000

    full_success_money = earnings * data[0] * data[1]
    half_success_money = earnings * data[2] * data[3]
    escaped_probability = (data[5])
    jail_time = round((earnings / 25) * data[7],1)

    jail_fine = earnings*-data[7]

    profit = round(full_success_money+half_success_money+jail_fine,10)
    print("-------------------------------------------------------------")
    print("DC",DC ,"Heist")
    print("-------------------------------------------------------------")
    print("You gain", round(profit,1), "gp in this week")
    print("You spent", jail_time, "days in jail")
    print("\nDetailed Report:")
    print("     Full Success:   ", round(full_success_money,1), "gp = ",earnings,"gp *",round(100*data[1],2),"%")
    print("     Half Success:   ", round(half_success_money,1), "gp = ",round(0.5*earnings),"gp *",round(100*data[3],2),"%")
    print("     Jail Fine:     ", round(jail_fine,1), "gp = ",earnings,"gp *",round(-100*data[7],4),"%\n")



medianProfit(25)
medianProfit(20)
medianProfit(15)
medianProfit(10)
