import numpy as np
import json
import pickle

class MaterialPrediction():

    def __init__(self,data):
        self.data = data
        print(self.data)

    def __loading(self): # private method
        """
        to predict the material types 
        """
        with open('artifacts\project_data.json','r') as file:
            self.project_data = json.load(file)

        with open('artifacts\logi_model.pkl','rb') as file:
            self.model = pickle.load(file)

    def get_data(self):  # Public method 
        """
        docstring
        """
        self.__loading()

        layer_height=self.data['html_layer_height']
        wall_thickness=self.data['html_wall_thickness']
        infill_density=self.data['html_infill_density']
        infill_pattern=self.data['html_infill_pattern']
        nozzle_temperature=self.data['html_nozzle_temperature']
        bed_temperature=self.data['html_bed_temperature']
        print_speed=self.data['html_print_speed']
        fan_speed=self.data['html_fan_speed']
        roughness=self.data['html_roughness']
        tension_strenght=self.data['html_tension_strenght']
        elongation=self.data['html_elongation']

        user_data = np.zeros(len(self.project_data['columns']))
        user_data[0] = layer_height
        user_data[1] = wall_thickness
        user_data[2] = infill_density
        user_data[3] = self.project_data['infill_pattern'][infill_pattern]
        user_data[4] = nozzle_temperature
        user_data[5] = bed_temperature
        user_data[6] = print_speed
        user_data[7] = fan_speed
        user_data[8] = roughness
        user_data[9] = tension_strenght
        user_data[10] = elongation

        re=self.model.predict([user_data])[0]

        ABS="ABS. Acrylonitrile Butadiene Styrene is a thermoplastic polymer, a highly versatile type of plastic that's used for many different kinds of manufacturing. Thermoplastic polymers are useful because they become flexible (or moldable) above a specified temperature and solidify when cooled."
        PLA="PLA. Polylactic acid or polylactide (PLA) is a polyester derived from renewable biomass, typically from fermented plant starch, such as corn, cassava, sugarcane or sugar beet pulp."
        if re==0:
            return ABS 
        else:
            return PLA