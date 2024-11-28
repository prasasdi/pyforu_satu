input_data = {
    'True Label' : [1,0,1,1,0,1,0,1,0,0],
    'Model 1' : [1,0,0,0,0,1,0,1,0,1],
    'Model 2' : [1,1,1,1,0,1,0,0,0,0]
}

import operator

# todo; buat hasil recall
recall_scores = {
    'Model 1': 0,
    'Model 2': 0
}

# input_data : dictionary
# recall_scores : dictionary
def recall(model_name, input_data, _recall_scores):
    tp_model = 0
    fn_model = 0

    for x in range(10):
        if input_data['True Label'][x] == 1:
            if (input_data['True Label'][x] == input_data[model_name][x]):
                tp_model += 1
            else:
                fn_model += 1

    _recall_scores[model_name] = tp_model / (tp_model + fn_model)
    print(f'skor recall dari {model_name} adalah = {_recall_scores[model_name]}')

recall('Model 1', input_data, recall_scores)
recall('Model 2', input_data, recall_scores)

best_model = max(recall_scores.items(), key=operator.itemgetter(1))[0]

print(f'Best model {best_model} with recall score: {recall_scores[best_model]}')