input_data = {
    'True Label' : [1,0,1,1,0,1,0,1,0,0],
    'Model 1' : [1,0,0,0,0,1,0,1,0,1],
    'Model 2' : [1,1,1,1,0,1,0,0,0,0],
}

# contoh array
arr = [1,2,3]
print("akses array tanpa loop")
print(arr[0])
print(arr[1])
print(arr[2])

print("akses array dengan loop")
for x in range(3):
    print(f'index ke x = {x}')
    print(arr[x])

print("akses diktioner dari key True Label dengan loop for x in range(10)")
# # for (int i = 0; i < 10; i++)
for x in range(10):
    print(f'akses index ke-x (x = {x}) dari larik input_data[\'True Label\']')
    print(input_data['True Label'][x])
    # if input_data['True Label'][x] == 1:

# # todo; buat hasil recall
# recall_score_model1 = 0
# recall_score_model2 = 0

# # for (int i = 0; i < 10; i++)
# for x in range(10):
#     if input_data['True Label'][x] == 1:
