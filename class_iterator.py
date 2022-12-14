import os


class Iterator:
    def __init__(self, name_of_file : str) -> None: 
        self.name_of_file = name_of_file
        self.counter = 0
        self.list = []
        file = open(self.name_of_file, "r")
        for row in file:
            self.list.append(row)
        file.close()

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.counter < len(self.list):
            tmp = self.list[self.counter]
            self.counter += 1
            return tmp
        else:
            raise StopIteration
        

if __name__ == "__main__":
    mark = 4
    path_to_dataset = os.path.join("C:/Users/User/Desktop/Lab2/","application_programming_first_lab_and_dataset/dataset")
    print(path_to_dataset)
    
    
    
