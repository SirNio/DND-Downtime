from random import randint


def probability(Insight_DC,Deception_DC,Intimidation_DC,Insight,Deception,Intimidation,lucky,money):
    # DC = 2d10+5 = 16
    # 3 AC fail: -2money
    # 2 AC fail: -0.5money
    # 1 AC Fail: 1.5money
    # 0 AC Fail: 2money

    # FOR MORE INFORMATION look up XGtE p.130

    nat1 = 1 / 20
    if lucky:
        nat1 = 1 / (20 * 20)

    real_Insight_DC = Insight_DC-1-Insight
    real_Deception_DC = Deception_DC-1-Deception
    real_Intimidation_DC = Intimidation_DC-1-Intimidation

    failing_Insight_AC  = real_Insight_DC/20
    failing_Deception_AC = real_Deception_DC/20
    failing_Intimidation_AC = real_Intimidation_DC/20

    if real_Insight_DC < 1:
        if real_Deception_DC < 1:
            if real_Intimidation_DC < 1:
                return [2*money, (1 - nat1) * (1 - nat1) * (1 - nat1),
                        1.5*money, 3 * (1 - nat1) * (1 - nat1) * nat1,
                        -0.5*money, 3 * nat1 * nat1 * (1 - nat1),
                        -2*money, nat1 * nat1 * nat1]
            else:
                return [2*money, (1 - nat1) * (1 - nat1) * (1 - failing_Intimidation_AC),
                        1.5*money, 2 * nat1 * (1 - nat1) * (1 - failing_Intimidation_AC) + failing_Intimidation_AC * nat1 * nat1,
                        -0.5*money, nat1 * nat1 * (1 - failing_Intimidation_AC) + 2 * (1 - nat1) * nat1 * failing_Intimidation_AC,
                        -2*money, nat1 * nat1 * failing_Intimidation_AC]
        else:
            if real_Intimidation_DC < 1:
                return [2*money, (1 - nat1) * (1 - nat1) * (1 - failing_Deception_AC),
                        1.5*money, 2 * nat1 * (1 - nat1) * (1 - failing_Deception_AC) + failing_Deception_AC * nat1 * nat1,
                        -0.5*money, nat1 * nat1 * (1 - failing_Deception_AC) + 2 * (1 - nat1) * nat1 * failing_Deception_AC,
                        -2*money, nat1 * nat1 * failing_Deception_AC]
            else:
                return [2*money, (1 - nat1) * (1 - failing_Deception_AC) * (1 - failing_Intimidation_AC),
                        1.5*money, nat1 * (1 - failing_Deception_AC) * (1 - failing_Intimidation_AC) + (1 - nat1) * failing_Deception_AC * (
                                    1 - failing_Intimidation_AC + (1 - nat1) * (1 - failing_Deception_AC) * failing_Intimidation_AC),
                        -0.5*money, (1 - nat1) * failing_Deception_AC * failing_Intimidation_AC + nat1 * (
                                    1 - failing_Deception_AC) * failing_Intimidation_AC + nat1 * failing_Deception_AC * (1 - failing_Intimidation_AC),
                        -2*money, nat1 * failing_Deception_AC * failing_Intimidation_AC]
    else:
        if real_Deception_DC < 1:
            if real_Intimidation_DC < 1:
                return [2*money, (1 - failing_Insight_AC) * (1 - nat1) * (1 - nat1),
                        1.5*money, failing_Insight_AC * (1 - nat1) * (1 - nat1) + (1 - failing_Insight_AC) * nat1 * (1 - nat1),
                        -0.5*money, (1 - failing_Insight_AC) * nat1 * nat1 + 2 * failing_Insight_AC * (1 - nat1) * nat1,
                        -2*money, failing_Insight_AC * nat1 * nat1]
            else:
                return [2*money, (1 - failing_Insight_AC) * (1 - nat1) * (1 - failing_Intimidation_AC),
                        1.5*money, (1 - failing_Insight_AC) * (1 - nat1) * failing_Intimidation_AC + (1 - failing_Insight_AC) * nat1 * (
                                    1 - failing_Intimidation_AC) + failing_Insight_AC * (1 - nat1) * (1 - failing_Intimidation_AC),
                        -0.5*money, (1 - failing_Insight_AC) * nat1 * failing_Intimidation_AC + failing_Insight_AC * (
                                    1 - nat1) * failing_Intimidation_AC + failing_Insight_AC * nat1 * (1 - failing_Intimidation_AC),
                        -2*money, failing_Insight_AC * nat1 * failing_Intimidation_AC]
        else:
            if real_Intimidation_DC < 1:
                return [2*money, (1 - failing_Insight_AC) * (1 - failing_Deception_AC) * (1 - nat1),
                        1.5*money,
                        failing_Insight_AC * (1 - failing_Deception_AC) * (1 - nat1) + (1 - failing_Insight_AC) * failing_Deception_AC * (
                                    1 - nat1) + (1 - failing_Insight_AC) * (1 - failing_Deception_AC) * nat1,
                        -0.5*money,
                        failing_Insight_AC * failing_Deception_AC * (1 - nat1) + failing_Insight_AC * (1 - failing_Deception_AC) * nat1 + (
                                    1 - failing_Insight_AC) * failing_Deception_AC * nat1,
                        -2*money, failing_Insight_AC * failing_Deception_AC * nat1]
            else:
                return [2*money, (1 - failing_Insight_AC) * (1 - failing_Deception_AC) * (1 - failing_Intimidation_AC),
                        1.5*money, failing_Insight_AC * (1 - failing_Deception_AC) * (1 - failing_Intimidation_AC) + (
                                    1 - failing_Insight_AC) * failing_Deception_AC * (1 - failing_Intimidation_AC) + (
                                    1 - failing_Insight_AC) * (1 - failing_Deception_AC) * failing_Intimidation_AC,
                        -0.5*money, failing_Insight_AC * failing_Deception_AC * (1 - failing_Intimidation_AC) + failing_Insight_AC * (
                                    1 - failing_Deception_AC) * failing_Intimidation_AC + (
                                    1 - failing_Insight_AC) * failing_Deception_AC * failing_Intimidation_AC,
                        -2*money, failing_Insight_AC * failing_Deception_AC * failing_Intimidation_AC]



def calculate_profit(Insight_DC, Deception_DC, Intimidation_DC, Insight, Deception, Intimidation, lucky, money):
    data = probability(Insight_DC,Deception_DC,Intimidation_DC,Insight,Deception,Intimidation,lucky,money)

    Full_fail_money = data[0] * data[1]
    Half_fail_money = data[2] * data[3]
    Half_success_money = data[4] * data[5]
    Full_success_money = data[6] * data[7]



    profit = round(Full_fail_money+Half_fail_money+Half_success_money+ Full_success_money,10)
    #print("-------------------------------------------------------------")
    #print("DC",DC,"Gambling")
    #print("-------------------------------------------------------------")
    #print("You gain", round(profit,1), "gp in this week")
    #print("\nDetailed Report:")
    #print("     0/3AC:   ", round(Full_fail_money,1), "gp =",data[0],"gp *",round(100*data[1],2),"%")
    #print("     1/3AC:   ", round(Half_fail_money,1), "gp = ",data[2],"gp *",round(100*data[3],2),"%")
    #print("     2/3AC:   ", round(Half_success_money,1), "gp = ",data[4],"gp *",round(100*data[5],2),"%")
    #print("     3/3AC:   ", round(Full_success_money,1), "gp = ",data[6],"gp *",round(100*data[7],2),"%")
    return profit



def random_roll(Insight,Deception,Intimidation, money):
    Insight_DC = randint(7, 25)
    Deception_DC = randint(7, 25)
    Intimidation_DC = randint(7, 25)

    first_roll = randint(1, 20) + Insight
    second_roll = randint(1, 20) + Deception
    third_roll = randint(1, 20) + Intimidation

    #print("DC for Insight",Insight_DC,": ",first_roll,"rolled")
    #print("DC for Deception", Deception_DC, ": ", second_roll, "rolled")
    #print("DC for Intimidation", Intimidation_DC, ": ", third_roll, "rolled")

    if Insight_DC <= first_roll and Deception_DC <=second_roll and Intimidation_DC <=third_roll:
        #print("Thus you got 3/3AC")
        return 2*money
    elif Insight_DC > first_roll and Deception_DC <=second_roll and Intimidation_DC <=third_roll or Insight_DC <= first_roll and Deception_DC > second_roll and Intimidation_DC <= third_roll or Insight_DC <= first_roll and Deception_DC <= second_roll and Intimidation_DC > third_roll:
        #print("Thus you got 2/3AC")
        return 1.5*money
    elif Insight_DC > first_roll and Deception_DC > second_roll and Intimidation_DC <= third_roll or Insight_DC > first_roll and Deception_DC > second_roll and Intimidation_DC <= third_roll or Insight_DC > first_roll and Deception_DC <= second_roll and Intimidation_DC > third_roll:
        #print("Thus you got 1/3AC")
        return -0.5*money
    else:
        #print("Thus you got 0/3AC")
        return -2*money


def mean_profit(Insight,Deception,Intimidation):
    #DC can be 2d10+5
    sum = 0
    for DC1 in range(7,26):
        for DC2 in range(7,26):
            for DC3 in range(7,26):
                value = calculate_profit(DC1, DC2, DC3, Insight, Deception, Intimidation, False, 1000)
                sum += value
                #print("DC",DC1,DC2,DC3,": ",round(value,2))
    return round(sum/(18**3),0)


print("Over time you will gain", mean_profit(6,6,6),"gp per 1000gp bet with your ability scores")
print("This time you gambled:",random_roll(6,6,6,1000),"gp")
#If the modifiers summed up are 12 or larger, the character will earn money overtime!!!
#the amount of money will increase linear with your modifiers.
