import yaml
import os

def create_data_yaml(path_to_classes, path_to_data_yaml):
    with open(path_to_classes, 'r') as file:
        classes = []
        
        for line in file.readlines():
            if len(line.strip()) == 0:
                continue
            classes.append(line.strip())

    number_of_classes = len(classes) 

    data = {
        'path': 'TrainingImages/CleanEnvBarGraphs/Labelled',
        'train': 'images/train',
        'val': 'images/val',
        'nc': number_of_classes,
        'names': classes
    }

    with open(path_to_data_yaml, 'w') as file:
        yaml.dump(data, file, sort_keys=False)
    print(f'Created config file at: {path_to_data_yaml}')

    return

path_to_classes = 'TrainingImages/CleanEnvBarGraphs/Labelled/classes.txt'
path_to_data_yaml = 'clean_env_data.yaml'

create_data_yaml(path_to_classes, path_to_data_yaml)