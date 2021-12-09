class Triangle:
    def __init__(self, number_of_rows):
        self.number_of_rows = number_of_rows
        self.triangle_of_scores = None


    def create_list_of_zeroes(self,list_length):
        temp_triangle_scores = [0]*list_length
        self.triangle_of_scores = temp_triangle_scores
        return temp_triangle_scores


    def create_triangle_zeroes_lists(self):
        new_list_of_lists_of_zeroes = []
        for i in len(self.number_of_rows):
            new_list_of_lists_of_zeroes.append([0]*(i+1))


    def update_triangle_score(self, new_score, row, location_in_list):
        
        pass




