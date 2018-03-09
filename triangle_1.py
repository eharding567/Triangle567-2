'''Triangle Classifier'''
def classify_triangle(a_a, b_b, c_c):
    '''Classify Triangles based on sides'''

    valid_a = isinstance(a_a, (float, int))
    valid_b = isinstance(b_b, (float, int))
    valid_c = isinstance(c_c, (float, int))
    if not (valid_a and valid_b and valid_c):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a_a > 200 or b_b > 200 or c_c > 200:
        return 'InvalidInput'

    if a_a <= 0 or b_b <= 0 or c_c <= 0:
        return 'InvalidInput'



    if (a_a > (b_b + c_c)) or (b_b > (a_a + c_c)) or (c_c > (a_a + b_b)):
        return 'NotATriangle'


    one_percent_a = 0.01 * a_a
    one_percent_b = 0.01 * b_b
    one_percent_c = 0.01 * c_c

    triangle_type = ""
    hyp_c = abs(pow(a_a, 2) + pow(b_b, 2) -pow(c_c, 2)) <= one_percent_c
    hyp_b = abs(pow(a_a, 2) + pow(c_c, 2) -pow(b_b, 2)) <= one_percent_b
    hyp_a = abs(pow(b_b, 2) + pow(c_c, 2) -pow(a_a, 2)) <= one_percent_a
    if hyp_a or hyp_b or hyp_c:
        if (a_a != b_b) and  (b_b != c_c) and (a_a != c_c):
            triangle_type = 'Right Scalene'
        else:
            triangle_type = "Right Isosceles"
    elif a_a == b_b and b_b == a_a and c_c == a_a:
        triangle_type = 'Equilateral'
    elif (a_a != b_b) and  (b_b != c_c) and (a_a != c_c):
        triangle_type = 'Scalene'
    else:
        triangle_type = 'Isoceles'
    return triangle_type
