class Polynomial:
    def __init__(self, lst_of_polynomials=None):
        self.items = lst_of_polynomials
        if self.items is None:
            self.items = [0]
        self.length = len(lst_of_polynomials)
    
    def __len__(self):
        return len(self.items)

    def __repr__(self):
        poly_str = ""
        list_of_coefficients = self.items[::-1]
        exponent = len(list_of_coefficients) - 1
        for coefficient in list_of_coefficients:
            if str(coefficient)[0] == "-":
                symbol = "-"
                index = 1
            else:
                symbol = "+"
                index = 0
            num = int(str(coefficient)[index:])
            if num != 0:
                if exponent == len(list_of_coefficients) - 1:
                    symbol = ""
                if exponent == 0:
                    exponent_str = ""
                    carrot = ""
                    variable = ""
                else:
                    exponent_str = exponent
                    carrot = "^"
                    variable = "x"
                poly_str += symbol + str(num) + variable + carrot + str(exponent_str)
            exponent -= 1
        return poly_str

    def eval(self, val):
        result = 0
        list_of_coefficients = self.items
        for i in range(len(list_of_coefficients)):
            result += list_of_coefficients[i] * (val ** i)
        return result

    def addition(self, polynomial):
        len_self = len(self)
        len_polynomial = len(polynomial)
        len_new_poly = len_self + len_polynomial
        new_poly = [0] * (len_polynomial + len_self)
        for i in range(len_)
        return new_poly

    def multiplication(self, polynomial):
        result = [0] * ((len(self) + len(polynomial)) + 1)
        for i in range(len(self.items)):
            for j in range(len(polynomial)):
                product = self.items[i] * polynomial.items[j]
                exponent_sum = i + j
                result[exponent_sum] += product


def main():
    poly = Polynomial([2, 2])
    poly2 = Polynomial([0, 9, 0, 0, 0, 0, 0])
    # print(poly)
    # print(poly.eval(3))
    print(poly.addition(poly2))


main()
