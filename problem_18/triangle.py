class Triangle:
    def __init__(self, number_of_rows):
        self.number_of_rows = number_of_rows


    def create_list_of_zeroes(self,list_length):
        return [0]*list_length

    def create_triangle_zeroes_lists(self):
        new_list_of_lists_of_zeroes = []
        for i in len(self.number_of_rows):
            new_list_of_lists_of_zeroes.append([0]*(i+1))



