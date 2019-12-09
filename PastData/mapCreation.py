import sys
site_packages = "D:\\\\home\\site\\wwwroot\\env\\Lib\\site-packages"
sys.path.append(site_packages)

import pandas as pd 
import sys
import pickle 
import  json

def createMap(dataset, model):

    dataset_filepath = "D:\\\\home\\site\\wwwroot\\Data\\Crime_data\\PastDatasets\\readyDatasets\\" + dataset
    dataset = pd.read_csv(dataset_filepath)

    dataset.pop('Grid')
    Y_test = dataset.pop('Hotspot')

    model_filepath = "D:\\\\home\\site\\wwwroot\\trained_models\\" + model
    decision_tree = pickle.load(open(model_filepath,'rb'))

    dt_prediction = decision_tree.predict(dataset)

    pred_series = pd.Series(dt_prediction, index=Y_test.index, name="predictions")

    final_output = pd.concat([Y_test,pred_series],axis=1)
    final_output.insert(0,'Grid',range(1,1+len(final_output)))



    with open('D:\\\\home\\site\\wwwroot\\CrimeWebsite\\geojsonTest.json') as json_file:
        json_decoded = json.load(json_file)


    for i in range(len(json_decoded['data']['features'])):
        if i%1000 ==0:
            print("on row: ", i)
        json_decoded['data']['features'][i]['properties']['ActualHot'] = int(final_output['Hotspot'][i])
        json_decoded['data']['features'][i]['properties']['PredictHot'] = int(final_output['predictions'][i])

    with open("CRIME_GEO.json", 'w') as json_file:
        json.dump(json_decoded, json_file)


    dic = ['1','2','3']
    dic.append(test)
    return json.dumps(dic)

if __name__ == "__main__":
    print(createMap(sys.argv[1],sys.argv[2]))





