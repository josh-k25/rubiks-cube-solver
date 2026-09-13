import random

from cube import cubeState, Move
from solver import solveWhiteCross, solveWhiteCorners, checkWhiteCrossSolved


def main():

    for test in range(1, 6):

        cube = cubeState()

        # Generate random 10-move scramble
        scramble = tuple(
            random.choice(list(Move))
            for _ in range(10)
        )

        print(f"\nTEST {test}")

        print(
            "Scramble:",
            " ".join(move.name for move in scramble)
        )

        cube = cube.applyMoves(scramble)

        print("After scramble:")
        print("White cross solved:", checkWhiteCrossSolved(cube))
        print("First layer solved:", cube.isFirstLayerSolved())

        # Solve white cross
        cube = solveWhiteCross(cube, [])

        print("\nAfter white cross:")
        print("White cross solved:", checkWhiteCrossSolved(cube))

        assert checkWhiteCrossSolved(cube)

        # Solve white corners
        cube = solveWhiteCorners(cube)

        print("\nAfter white corners:")
        print("First layer solved:", cube.isFirstLayerSolved())

        assert cube.isFirstLayerSolved()

        print(f"TEST {test} PASSED")

    print("\nALL 5 LAYER 1 TESTS PASSED!")


if __name__ == "__main__":
    main()