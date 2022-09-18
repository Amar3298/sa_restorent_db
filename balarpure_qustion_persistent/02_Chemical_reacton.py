list1 = [9,-3,8,-6,-7,8,10]

def maxEnergy(energy,length_energy):
    list1 = energy
    set_a = set(list1)
    set_a_list = list(set_a)
    set_a_list.sort(reverse=True)
    return set_a_list[0]+set_a_list[1]

print(maxEnergy([9,-3,8,-6,-7,8,10],7))