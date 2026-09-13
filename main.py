from cube import cubeState, Move
from solver import solveWhiteCross, solveWhiteCorners, checkWhiteCrossSolved

def main():

    cube = cubeState()

    # mini scramble
    scramble = (
        Move.R,
        Move.F,
        Move.D
    )

    cube = cube.applyMoves(scramble)

    print("After scramble:")
    print("White cross solved:", checkWhiteCrossSolved(cube))
    print("First layer solved:", cube.isFirstLayerSolved())


    # solve white cross
    cube = solveWhiteCross(cube, [])

    print("\nAfter white cross:")
    print("White cross solved:", checkWhiteCrossSolved(cube))


    # solve white corners
    cube = solveWhiteCorners(cube)

    print("\nAfter white corners:")
    print("First layer solved:", cube.isFirstLayerSolved())

    assert cube.isFirstLayerSolved()

    print("\nLayer 1 test passed!")


if __name__ == "__main__":
    main()
