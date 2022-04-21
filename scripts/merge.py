import os
import json


def merge_json(path_results, path_merges):
    d = {"videos": []}
    with open(path_merges, "w+", encoding="utf-8") as f0:
        # for file in os.listdir(path_results):
        # print("processing %s"%(file))
        # if file == 'av_train.json':
        # work on av_train first
        with open(os.path.join(path_results, 'av_train.json'), "r", encoding="utf-8") as f1:
            json_dict = json.load(f1)
            d = json_dict.copy()
        # elif file == 'av_val.json' or file == 'av_test_unannotated.json':
        with open(os.path.join(path_results, 'av_val.json'), "r", encoding="utf-8") as f2:
            json_dict = json.load(f2)
            vs = json_dict['videos']
            for v in vs:
                d['videos'].append(v)
        json.dump(d, f0)
