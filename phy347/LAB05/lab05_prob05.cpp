include <iostream>
using namespace std;

// Class to represent a box
class Box
{
  public:
    double length;
    double breadth;
    double height;

    // Inline initialization
    Box(double lv = 1.0, double bv = 1.0, double hv = 1.0):length(lv),
                                                           breadth(bv),
                                                           height(hv)
    {
      cout << "Box constructor called" << endl;
    }

    // Function to calculate the volume of a box
    double volume()
    {
      return length * breadth * height;
    }
};

int main()
{
  Box firstBox(80.0, 50.0, 40.0);

  // Calculate the volume of the box
  double firstBoxVolume = firstBox.volume();
  cout << endl;
  cout << "Size of first Box object is "
       << firstBox.length  << " by "
       << firstBox.breadth << " by "
	<< firstBox.height
       << endl;
  cout << "Volume of first Box object is " << firstBoxVolume
       << endl;

  return 0;
}
