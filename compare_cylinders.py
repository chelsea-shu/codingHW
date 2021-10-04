from Cylinder import Cylinder
import argparse

def main():
    parser = argparse.ArgumentParser(description='Comparing two cylinders')
    parser.add_argument('-r', '--radius', type=float, help='What radii are you using?')
    parser.add_argument('-hi', '--height', type=float, help='What heights are you using?')
    args = parser.parse_args()

    cylinder_radii = args.radius
    cylinder_heights = args.height

    # Setting the original cylinder and calculating its tsa and csa ** Right now it's saying I can't print
    cyl1 = Cylinder(cylinder_radii, cylinder_heights)
    cyl1_csa = cyl1.get_curved_surface_area()
    cyl1_tsa = cyl1.get_total_sa()

    # Comparing the sizes of the two cylinders
    cyl1.set_radius(3)
    cyl1.set_height(4)
    cyl2_csa = cyl1.get_curved_surface_area()
    cyl2_tsa = cyl1.get_total_sa()

    if cyl1_csa > cyl2_csa:
        print('The curved surface area of cylinder 1 is greater than cylinder 2')
    else:
        print('The curved surface area of cylinder 2 is greater than cylinder 1')

    if cyl1_tsa > cyl2_tsa:
        print('The total surface area of cylinder 1 is greater than cylinder 2')
    else:
        print('The total surface area of cylinder 2 is greater than cylinder 1')

    """Write code here to compare cylinders

    After defining the Cylinder class, in the main function, use
    argparse to get two pairs of radius and height values from the user.

    Print the curved surface area and the total surface area for the
    first cylinder. Store these values.

    Use your mutator functions to change the radius and height of the
    cylinder and print the he curved surface area and the total surface
    area of the new cylinder.

    Now compare which of the two has more curved surface area and which
    one has more total surface area.
    
    You need to use the set function

    """


main()
