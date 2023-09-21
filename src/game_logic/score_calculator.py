class scorer:
    penalty = 10
    def __init__(self, initial_score = 100):
        self.score = initial_score
        
    def decrement_score(self):
        self.score = self.score - self.penalty   
        self.score = max(self.score, 0)

    def get_score(self):
        return self.score
    
if __name__ == '__main__':
    scorer()
