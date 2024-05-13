class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

        self.foodict = {}
        for i in range(0, len(self.foods)):
            self.foodict[self.foods[i]] = [self.cuisines[i], self.ratings[i]]
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        self.foodict[food][1] = newRating
        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        max = 0
        results = []
        result = []
        dicty = sorted(self.foodict.items())
        for i in dicty:
            if i[1][0] == cuisine and i[1][1] > max:
                max = i[1][1]
                result.append(i)
        for i in result:
            if i[1][1] == max:
                results.append(i[0])
        results.sort()
        return results[0]