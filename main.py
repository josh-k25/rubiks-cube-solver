import random

from cube import cubeState, Move, Edge
from solver import checkWhiteCrossSolved, solveFirstLayer, solveSecondLayer


def main():

    for test in range(1, 6):

        cube = cubeState()

        # Generate random 10-move scramble
        scramble = tuple(
            random.choice(list(Move))
            for _ in range(1000)
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

        # solve first layer
        cube = solveFirstLayer(cube)

        print("\nAfter first layer:")
        print("First layer solved:", cube.isFirstLayerSolved())

        assert cube.isFirstLayerSolved()

        # solve second layer
        cube = solveSecondLayer(cube)

        secondLayerSolved = (
            cube.isEdgeSolved(Edge.FL)
            and cube.isEdgeSolved(Edge.FR)
            and cube.isEdgeSolved(Edge.BL)
            and cube.isEdgeSolved(Edge.BR)
        )

        print("\nAfter second layer:")
        print("First layer still solved:", cube.isFirstLayerSolved())
        print("Second layer solved:", secondLayerSolved)

        # second-layer algorithms should not destroy layer 1
        assert cube.isFirstLayerSolved()

        # All four middle-layer edges should now be solved
        assert secondLayerSolved

        print(f"TEST {test} PASSED")

    print("\nALL 5 FIRST + SECOND LAYER TESTS PASSED!")


if __name__ == "__main__":
    main()