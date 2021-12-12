class Triangle:
    def __init__(self, number_of_rows):
        self.number_of_rows = number_of_rows
        self.triangle_of_scores = self.create_triangle_zeroes_lists()


    # def create_list_of_zeroes(self,list_length):
    #     temp_triangle_scores = [0]*list_length
    #     self.triangle_of_scores = temp_triangle_scores
    #     return temp_triangle_scores


    def create_triangle_zeroes_lists(self):
        new_list_of_lists_of_zeroes = []
        for i in range(self.number_of_rows):
            new_list_of_lists_of_zeroes.append([0]*(i+1))
        self.triangle_of_scores = new_list_of_lists_of_zeroes
        return new_list_of_lists_of_zeroes


    def update_triangle_score(self, new_score, row, location_in_list):
        # print(self.triangle_of_scores[row][location_in_list])
        self.triangle_of_scores[row][location_in_list] = new_score
        temp_triangle_of_scores = self.triangle_of_scores
        return temp_triangle_of_scores




