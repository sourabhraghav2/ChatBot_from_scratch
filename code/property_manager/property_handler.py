import os

class Properties:
    @staticmethod
    def get_properties():
        myvars = {}

        current_directory = os.path.dirname(os.path.abspath(__file__))
        file_path=current_directory+'\\'+'ConfigFile.properties'
        print('Reading Configuration from : {}'.format(file_path))
        with open(file_path) as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                myvars[name.strip()] = var.strip()
        return myvars



property_list=Properties.get_properties()

print(property_list['sentence_min_length'])