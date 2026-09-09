from cube import cubeState, Move, Edge, Corner

def main():
    cube = cubeState()

    for move in Move:
        cube.identityTest(move)

    print(cube.checkWhiteCrossSolved())

    cube = cube.applyMove(Move.U)

    print(cube.checkWhiteCrossSolved())


if __name__ == "__main__":
    main()
