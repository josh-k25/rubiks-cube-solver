import random

from cube import cubeState, Move, Edge, Corner
from solver import solveFirstLayer, solveSecondLayer, solveThirdLayer


def isCubeSolved(cube):
    return (
        all(cube.isEdgeSolved(edge) for edge in Edge)
        and all(cube.isCornerSolved(corner) for corner in Corner)
    )


def moveToString(move):
    name = move.name

    if name.endswith("_PRIME"):
        return name.replace("_PRIME", "'")

    return name


def movesToString(moves):
    return " ".join(moveToString(move) for move in moves)


def generateScramble(length=25):
    return tuple(
        random.choice(list(Move))
        for _ in range(length)
    )


def main():
    cube = cubeState()

    # generate and apply a random scramble
    scramble = generateScramble(25)

    print("Rubik's Cube Layer-by-Layer Solver")
    print(f"Scramble ({len(scramble)} moves):")
    print(movesToString(scramble))

    cube = cube.applyMoves(scramble)

    # scramble moves should not be included in the solution history
    cube.moveHistory = []

    print("\nSolving...")

    # solve all three layers
    cube = solveFirstLayer(cube)
    cube = solveSecondLayer(cube)
    cube = solveThirdLayer(cube)

    # verify the solver's final state
    assert isCubeSolved(cube)

    solutionMoves = cube.moveHistory.copy()

    print("\nSolution:")
    print(movesToString(solutionMoves))
    print(f"\nSolution length: {len(solutionMoves)} moves")

    #independently verify the recorded solution
    verificationCube = cubeState()
    verificationCube = verificationCube.applyMoves(scramble)
    verificationCube = verificationCube.applyMoves(solutionMoves)

    assert isCubeSolved(verificationCube)

    print("\nVerification: PASSED")

if __name__ == "__main__":
    main()