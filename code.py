PlugBoard_F = open("plug_board.txt", "r")
PlugBoard = PlugBoard_F.readlines()
PlugBoard = str(PlugBoard).replace("'","").replace("[","").replace("]","").split()
PlugBoard_F.close()
print("PLUG BOARD: "+str(PlugBoard))

reflector_F = open("reflector_B.txt", "r")
reflector = reflector_F.readlines()
reflector = str(reflector).replace("'","").replace("[","").replace("]","").split()
reflector_F.close()

rotor1_F = open("rotor_I.txt", "r")
rotor1 = rotor1_F.readlines()
rotor1 = str(rotor1).replace("'","").replace("[","").replace("]","").split()
rotor1_F.close()

rotor2_F = open("rotor_II.txt", "r")
rotor2 = rotor2_F.readlines()
rotor2 = str(rotor2).replace("'","").replace("[","").replace("]","").split()
rotor2_F.close()

rotor3_F = open("rotor_III.txt", "r")
rotor3 = rotor3_F.readlines()
rotor3 = str(rotor3).replace("'","").replace("[","").replace("]","").split()
rotor3_F.close()

narzi_input = input("Strings to Encrypt/Decode: ")
setting_rotor_input = input("Rotor Setting(NOT WORK JUST PRESS ENTER): ")
setting_rotor_lst = []

setting_key_input = input("KEY SETTING: ")
setting_key_lst = []

setting_rotor_lst = setting_rotor_input.split(" ")
setting_key_lst = setting_key_input.split(" ")

output = ""
for i in range(0, len(narzi_input)):
    if str(PlugBoard).find(narzi_input[i]) >= 0:
        found_index = str(PlugBoard).find(narzi_input[i])
        if str(PlugBoard)[found_index-1] == "-":
            output += (str(PlugBoard)[found_index-2])
        if str(PlugBoard)[found_index+1] == "-":
            output += (str(PlugBoard)[found_index+2])
    else:
        output += narzi_input[i]

rotor_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rotor_b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rotor_c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
normal_abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
result = ""
Default_a = rotor1
Default_b = rotor2
Default_c = rotor3

def setRotorNum():
    for i in range(1,int(setting_key_lst[2])):
        temp = rotor1[0]
        temp2 = rotor_a[0]
        rotor1.remove(rotor1[0])
        rotor1.append(temp)
        rotor_a.remove(rotor_a[0])
        rotor_a.append(temp2)
    for i in range(1, int(setting_key_lst[1])):
        temp = rotor2[0]
        temp2 = rotor_b[0]
        rotor2.remove(rotor2[0])
        rotor2.append(temp)
        rotor_b.remove(rotor_b[0])
        rotor_b.append(temp2)
    for i in range(1, int(setting_key_lst[0])):
        temp = rotor3[0]
        temp2 = rotor_c[0]
        rotor3.remove(rotor3[0])
        rotor3.append(temp)
        rotor_c.remove(rotor_c[0])
        rotor_c.append(temp2)

def rotor_a_up():
    temp = rotor1[0]
    temp2 = rotor_a[0]
    rotor_a.remove(rotor_a[0])
    rotor_a.append(temp2)
    rotor1.remove(rotor1[0])
    rotor1.append(temp)

def rotor_b_up():
    temp = rotor2[0]
    temp2 = rotor_b[0]
    rotor_b.remove(rotor_b[0])
    rotor_b.append(temp2)
    rotor2.remove(rotor2[0])
    rotor2.append(temp)

def rotor_c_up():
    temp = rotor3[0]
    temp2 = rotor_c[0]
    rotor_c.remove(rotor_c[0])
    rotor_c.append(temp2)
    rotor3.remove(rotor3[0])
    rotor3.append(temp)

setRotorNum()
for i in range(0,len(output)):
    if int(setting_key_lst[1]) == 5:
            rotor_c_up()
            setting_key_lst[0] = str(int(setting_key_lst[0])+1)
            rotor_b_up()
            setting_key_lst[1] = str(int(setting_key_lst[1])+1)
    if int(setting_key_lst[2]) <= 26:
        rotor_a_up()
        setting_key_lst[2] = str(int(setting_key_lst[2]) + 1)
    if int(setting_key_lst[2]) == 18:
        rotor_b_up()
        setting_key_lst[1] = str(int(setting_key_lst[1]) + 1)
            
    if int(setting_key_lst[2]) == 27:
        setting_key_lst[2] = str(1)
    if int(setting_key_lst[1] == 27):
        setting_key_lst[1] == "1"
    if int(setting_key_lst[0] == 27):
        setting_key_lst[0] == "1"

    select_char_a = rotor1[ord(output[i])-65]
    # print(select_char_a)
    
    select_char_b = rotor2[rotor_a.index(select_char_a)]
    # print(select_char_b)
    
    select_char_c = rotor3[rotor_b.index(select_char_b)]
    # print(select_char_c)

    select_char_index_a = rotor_c.index(select_char_c)
    getReflector = str(reflector[select_char_index_a])
    # print(getReflector)

    if "2" in getReflector:
        getReflectorPair_index = reflector.index(getReflector.replace("2",""))
    else:
        getReflectorPair_index = reflector.index(getReflector+"2")
    # print(getReflectorPair_index)

    select_char_d_1 = rotor_c[getReflectorPair_index]
    # print(select_char_d_1)

    select_char_d_2 = rotor_b[rotor3.index(select_char_d_1)]
    # print(select_char_d_2)

    select_char_e = rotor_a[rotor2.index(select_char_d_2)]
    # print(select_char_e)

    result += normal_abc[rotor1.index(select_char_e)]
    # print(result)

    print(normal_abc[int(str(setting_key_lst[0]))-1],normal_abc[int(str(setting_key_lst[1]))-1],normal_abc[int(str(setting_key_lst[2]))-1],"\b:",normal_abc[rotor1.index(select_char_e)])
    
final_result = ""

for i in range(0, len(result)):
    if str(PlugBoard).find(result[i]) >= 0:
        found_index = str(PlugBoard).find(result[i])
        if str(PlugBoard)[found_index-1] == "-":
            final_result += (str(PlugBoard)[found_index-2])
        if str(PlugBoard)[found_index+1] == "-":
            final_result += (str(PlugBoard)[found_index+2])
    else:
        final_result += result[i]

print("RESULT: "+final_result)
