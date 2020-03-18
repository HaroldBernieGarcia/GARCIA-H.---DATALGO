class Triangle(Polygon):
T = Triangle([-2, -0.5], [0, -0.5], [-1, 2])
print("Area and perimeter of the triangle:" ,
      T.area(), T.perimeter())

class Quad(Polygon):
# Create a quad:
Q = Quad([-3, -1], [0, -1], [-1, 1], [-2, 1])
print("Area and perimeter of the quad: ",
      Q.area(), Q.perimeter())

# Plot the geometries:
plt.clf()
T.draw(Triangle)
Q.draw(Quad)
plt.ylim(-3, 4)
plt.legend()
plt.show()