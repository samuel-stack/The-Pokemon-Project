def capabilities(type1, type2, advantages = advantages):

    # Offensive Advantages
    advantages_o = []
    for types in [type1, type2]:
        try:
            [advantages_o.append(item) for item in list(advantages[advantages.T[types] == 2.0].index.values) if item not in advantages_o]
        except:
            pass

    # Offensive Disadvantages
    disadvantages_o = []
    for def_type in advantages.columns:
        sub_set = list(advantages.T[[type1, type2]].loc[def_type])
        if (sub_set[0] < 1 and  sub_set[1] < 1):
            max_weak = max(sub_set)
            disadvantages_o.append('%s : %s' %(def_type,max_weak ))

    # Offensive Power
    offensive_power = sum([a if a > b else b for a,b in advantages.loc[[type1, type2]].T.values])

    # Defensive Advantages, Disadvantages & Immunities
    advantages_d = []
    disadvantages_d = []
    immunity = []
    defensive_power = 0

    # If statement for similar types
    if type1 == type2:
        defensive_power = advantages[type1].sum()
        for name, value in zip(advantages[['Fire']].index, advantages[['Fire']].values) :
            if value[0] == 0:
                immunity.append(name)

            if 0 < value[0] < 1 :
                advantages_d.append('%s : %s' %(name, value[0]))

            if value[0] > 1:
                disadvantages_d.append('%s : %s' %(name, value[0]))

    else:
        for types in advantages.columns:
            row = advantages[[type1,type2]].loc[types]
            defensive_power += row[0]*row[1]
            if 0 < row[0]*row[1] < 1:
                advantages_d.append('%s : %s' %(row.name, row[0]*row[1]))

            if  row[0]*row[1] > 1:
                disadvantages_d.append('%s : %s' %(row.name, row[0]*row[1]))

            if row[0]*row[1] == 0:
                immunity.append(row.name)

    # dictionary for storing info
    capabilitys = {'off_adv'       : advantages_o    , 'count_off_adv' : len(advantages_o),
                    'off_disadv'    : disadvantages_o , 'count_off_dis' : len(disadvantages_o),
                    'off_pwr'       : offensive_power ,
                    'def_adv'       : advantages_d    , 'count_def_adv' : len(advantages_d),
                    'def_disadv'    : disadvantages_d , 'count_def_dis' : len(disadvantages_d),
                    'def_pwr'       : defensive_power ,
                    'immunities'    : immunity        , 'count_imm'     : len(immunity)}

    return capabilitys
