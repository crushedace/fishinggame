import csv


def GetFish(DiceRoll):
 #count = 0
 data_arr = []
 # open file
 with open("C:\\fishing game\Fishing.csv", 'r') as file:
    # set variable and reader
    csv_file = csv.DictReader(file)
    for row in csv_file:
      data_arr.append(dict(row))
    # print Name and points for keeping fish
 if DiceRoll == 1:
    flist = list(data_arr[0].values())
    #print(flist[0], flist[1], flist[3])
    return str(flist[0]), int(flist[1]), int(flist[2])
 elif DiceRoll == 2:
    flist = list(data_arr[1].values())
    #print(flist[0], flist[1], flist[3])
    return str(flist[0]), int(flist[1]), int(flist[2])
 elif DiceRoll == 3:
    flist = list(data_arr[2].values())
    #print(flist[0], flist[1], flist[3])
    return str(flist[0]), int(flist[1]), int(flist[2])
 elif DiceRoll == 4:
    flist = list(data_arr[3].values())
    #print(flist[0], flist[1], flist[3])
    return str(flist[0]), int(flist[1]), int(flist[2])
 elif DiceRoll == 5:
    flist = list(data_arr[4].values())
    #print(flist[0], flist[1], flist[3])
    return str(flist[0]), int(flist[1]), int(flist[2])
 elif DiceRoll == 6:
    flist = list(data_arr[5].values())
    #print(flist[0], flist[1], flist[3])
    return str(flist[0]), int(flist[1]), int(flist[2])