import kociemba as kc

def CubeState():
    cube = []
    sides = ["U : (UP)", "R : (RIGHT)", "F : (FRONT)", "D : (DOWN)", "L : (LEFT)", "B : (BOTTOM)"]
    print("Keep green-center face in front and white-center face on top")
    for i in sides:
        while True:
            converted_input = ""
            print(f"Enter the colors of the {i} side of the cube")
            faceColors = input().upper()
            for color in faceColors:
                if color == "W":
                    converted_input += "U"
                elif color == "Y":
                    converted_input += "D"
                elif color == "G":
                    converted_input += "F"
                elif color == "B":
                    converted_input += "B"
                elif color == "O":
                    converted_input += "L"
                elif color == "R":
                    converted_input += "R"
            if len(faceColors) != 9:
                print("Please enter exactly 9 colors for each side of the cube")
            else:
                cube.append(converted_input)
                break
    print("Cube state:", cube)
    return ''.join(cube)  # kociemba works on a single string

def ValidateCubeState(cube):
    if len(cube) != 54:
        return False
    color_counts = {color: cube.count(color) for color in set(cube)}
    print("Color counts:", color_counts)
    return all(count == 9 for count in color_counts.values())

cube = CubeState()

if cube :
    try:
        print("Cube string:", cube)
        ValidateCubeState(cube)
        solution = kc.solve(cube)
        print(f"solution : {solution}")
    except Exception as e:
        print(f"Invalid cube state: {e}")
else:
    print("Invalid cube state: The cube must have exactly 9 of each color.")