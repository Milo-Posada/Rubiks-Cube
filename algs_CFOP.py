# Force yellow daisy
cross = { #needs alg_prespective and set up
    "top": { 
        #white up
        "1": "F2",  
        #white not up
        "2": "U' R' F  R"
    },
    "middle": {
        #white right
        "1": "R U R'",
        #white left
        "2": "L' U L", 
        #white aligned
        "2": "F",
        "3": "F'"
    },
    "bottom": { #needs alg_prespective 
        #white not down
        "1": "F' D R' D'",
        #white down
        "2": "F (Dx) F' (D'x)" #need to figure how to solve x moves
    },
}

f2l = {
    "easy": {
        #basics
        "1": "U R U' R'",
        "2": "U' F' U F",
        "3": "F' U' F",
        "4": "R U R'",
        #corner and edge top
        "5": "U' R U R' U' R U2 R'",
        "6": "U F' U' F U F' U2 F",
        "7": "U' R U2 R' U' R U2 R'",
        "8": "U F' U2 F U F' U2 F",
        "9": "U F' U' F U' F' U' F",
        "10": "U' R U R' U R U R'",
        "11": "U' R U2 R' d R' U' R",
        "12": "d R' U2 R d' R U R'",
        "13": "U F' U F U' F' U' F",
        "14": "U' R U' R' U R U R'",
        "15": "F' U F U' d' F U F'",
        "16": "R U' R' U d R' U' R",
        #corner point up
        "17": "R U2 R' U' R U R'",
        "18": "F' U2 F U F' U' F",
        "19": "U R U2 R' U R U' R'",
        "20": "U' F' U2 F U' F' U F",
        "21": "U2 R U R' U R U' R'",
        "22": "U2 F' U' F U' F' U F",
        "23": "R U R' U' U' R U R' U' R U R'",
        #"24": "y' R' U' R U U R' U' R U R' U' R", #Original alg with y'
        "24": "F' U' F U2 F' U' F U F' U' F", #Transcription of the above without y'
        #corner bottom and ege top
        "25": "U' F' U F U R U' R'",
        "26": "U R U' R' U' F' U F",
        "27": "R U' R' U R U' R'",
        "28": "F' U F U' F' U F",
        "29": "F' U' F U F' U' F",
        "30": "R U R' U' R U R'",
        #corner top and edge middle
        "31": "R U' R' d R' U R",
        "32": "R U R' U' R U R' U' R U R'",
        "33": "U' R U' R' U' R U2 R'",
        "34": "U F' U F U F' U2 F",
        "35": "U' R U R' d R' U' R",
        "36": "U F' U' F d' F U F'",
        #corner bottom and edge middle
        "37": "R U' R' d R' U2 R U R' U2 R",
        "38": "R U' R' U' R U R' U' R U2 R'",
        "39": "R U' R' U R U2 R' U R U' R'",
        "40": "R U' R' d R' U' R U' R' U' R",
        "41": "R U R' U' R U' R' U d R' U' R"
    },
}

oll = {
    "2OLL": {
        "Dot": "F R U R' U' F' f R U R' U' f'",
        "l-Shape": "F R U R' U' F'",
        "L-Shape": "f R U R' U' f'",
        "Antisune": "R U2 R' U' R U' R'",
        "H": "R U R' U R U' R' U R U2 R'",
        "L": "F R' F' r U R U' r'",
        "Pi": "R U2 R2 U' R2 U' R2 U2 R",
        "Sune": "R U R' U R U2 R'",
        "T": "r U R' U' r' F R F'",
        "U": "R2 D R' U2 R D' R' U2 R'"
    },
}

pll = {
    "2PLL": {
        "Diagonal": "F R U' R' U' R U R' F' R U R' U' R' F R F'",
        "Headlights": "R U R' U' R' F R2 U' R' U' R U R' F'",
        "H": "M2 U M2 U2 M2 U M2",
        "Ua": "R U' R U R U R U' R' U' R2",
        "Ub": "R2 U R U R' U' R' U' R' U R'",
        "Z": "M' U M2 U M2 U M' U2 M2"
    },
}

from_left = str.maketrans("FRBL", "RBLF")
from_right = str.maketrans("FRBL", "LFRB")
from_back = str.maketrans("FRBL", "BLFR")
#how to mirror an alg?

# Returns prespective-based moves of an algorithm
def alg_prespective(piece_face, alg):
    if piece_face == 'L': alg = alg.translate(from_left)
    elif piece_face == 'R': alg = alg.translate(from_right)
    elif piece_face == 'B': alg = alg.translate(from_back)
    return alg
#alg_prespective("L", oll["2OLL"]["Sune"])


# Defines the CFOP stages
stages = {
    "cross": 1,
    "f2l": 2,
    "oll": 3,
    "pll": 4
}

# Reverse lookup to convert numbers back to stage names
stages_reverse = {v: k for k, v in stages.items()}

# Solves the cube recursively according to the CFOP method
def solve_cube(stage, layer):
    print(f"Solving {stage}, Layer: {layer}")

    if stage == "cross" or stage == 1:
        print("doing layer one")
        # solve_cube(1, 2) 
        if layer == 2 or layer == 3:
            solve_cube(1, 1)
        next_stage = stages_reverse[stages[stage] + 1] if stage in stages else stage + 1
        solve_cube(next_stage, 1)

    # elif stage == "f2l" or stage == 2:
    #     if layer == 2 or layer == 3:
    #         solve_cube(2, 1)
    #     next_stage = stages_reverse[stages[stage] + 1] if stage in stages else stage + 1
    #     solve_cube(next_stage, 1)

    # elif stage == "oll" or stage == 3:
    #     next_stage = stages_reverse[stages[stage] + 1] if stage in stages else stage + 1
    #     solve_cube(next_stage, 1)

    # elif stage == "pll" or stage == 4:
    #     next_stage = stages_reverse[stages[stage] + 1] if stage in stages else stage + 1
    #     solve_cube(next_stage, 1)

    else: print("Solved the cube!")
solve_cube("cross", 1)