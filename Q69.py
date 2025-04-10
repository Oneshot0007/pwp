class Shape:
  def square_area(self,side):
    cal_square_area=side*side
    print("Area of square is :",cal_square_area)

  def recangle_area(area,length,breadth):
    cal_rectangle_area = length*breadth
    print("Area of Rectangle is :",cal_rectangle_area)

s=Shape()
s.square_area(4)
s.recangle_area(4,5)