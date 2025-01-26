

#Task 01: Merge Lineup

def mergeLineup(pokemon_1, pokemon_2):

  for i in range (len(pokemon_1)):
    if pokemon_1[i]==None:
      pokemon_1[i]=0

  for i in range (len(pokemon_2)):
    if pokemon_2[i]==None:
      pokemon_2[i]=0

  new_hp= np.zeros(len(pokemon_1),dtype=int)

  for i in range(0, len(pokemon_1),1):
    new_hp[i]= pokemon_1[i]+ pokemon_2[len(pokemon_2)-1-i]

  return new_hp


print("///  Task 01: Merge Lineup  ///")
pokemon_1 = np.array([12, 3, 25, 1, None])
pokemon_2 = np.array([5, -9, 3, None, None] )
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [12, 3, 28, -8, 5]
unittest.output_test(returned_value, np.array([12, 3, 28, -8, 5]))
pokemon_1 = np.array([4, 5, -1, None, None])
pokemon_2 = np.array([2, 27, 7, 12, None])
returned_value =mergeLineup(pokemon_1, pokemon_2)
print(f'Task 1: {returned_value}') # This should print [4,17,6,27,2]
unittest.output_test(returned_value, np.array([4,17,6,27,2]))