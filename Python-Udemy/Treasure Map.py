row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_list= list(position)
print(position_list)
row=int(position_list[1])-1
column=int(position_list[0])-1
# print(row)
# print(column)
map[row][column] = "x"

#mythoughtprocess
#map[row][colummn]
#position=columnrow 

print(f"{row1}\n{row2}\n{row3}")
