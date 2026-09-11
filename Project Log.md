# Project Log

## 2026-09-07

### Worked on
- Cubie (one individual piece of a Rubix Cube) representation
- rotateLeft helper

### Learned
- Functions and enums (for Python)
- Moves are permutations of cubies plus orientation changes.

### Problems
- Still need to figure out how to make the move functions

### Next
- Work through U and F manually.
- Create and test move functions on cube model

## 2026-09-08

### Worked on
- Mapping for move function
- Mapping takes current cube and provides the next orientation and position of edges and corners based on move type

### Learned
- Kociembas way of describing cubies with a deeper understanding (Probably going to stick with this notation for now it should port to hardware well)

### Problems
- Still need to figure out how to write the move function

### Next
- Create and test move functions on cube model

## 2026-09-09

### Worked on
- Created `applyMove` method.
- Created identity test to prove that applying the same quarter-turn 4 times returns the cube to its original state.
- Added support for all 18 standard moves by representing double and prime moves as repeated applications of the 6 base moves.
- Created a `MOVE_DEFINITIONS` dictionary that maps a requested move to its base move and number of repetitions.
- Added a white-cross solved checker.
- Started planning the structure for the white-cross solving control logic.
- Decided to separate cube representation/move mechanics from solver logic into different files.


### Learned
- A dictionary uses a key to reference associated data.
- Tuple unpacking can assign multiple values from a tuple at once.
- Move.R, for example, is an enum member while Move is the enum class.
- The six base move tables only need to describe the fundamental quarter-turns. Prime and double moves can be built from repeated base moves.
- Cubie identity already contains color information. For example, Edge.UF represents the physical U-F edge, so an extra color field is unnecessary.
- Phase-checking logic and solving logic should be kept separate:
  - A checker asks whether a condition is currently satisfied.
  - The solver decides which moves should be performed next.
- Solving control logic will hasve the rough structure off the following (FSM will also look similar)
  - inspect cube state
  - classify current case
  - choose move
  - apply move
  - inspect state again

### Problems
- Need to design the control logic for actually solving the white cross.
- Need to decide how to classify the possible position/orientation cases for an individual white edge.
- Need a clean way for the solver to locate a specific cubie in the current state.

### Next
- Create a findEdge() helper that determines which position currently contains a requested edge cubie.
- Create an isEdgeSolved() helper for checking one target edge.
- Write down the manual solving process for that edge based on:
  - its current position
  - its current orientation
- Translate those decisions into white-cross control logic.
- Test solving one edge from several different locations before generalizing to all four white edges.
- Only after individual white-edge solving works, build `solveWhiteCross()`.

## 2026-09-10

### Worked on

- Created `isEdgeSolved()` which checks if an edge is in its solved state (first used for white cross).
- Created `getEdgeData()` which returns an edge's current position and orientation.
- Started designing the control logic for solving individual white-cross edges.
- Decided to base the solver on my own human solving process rather than immediately using a predefined algorithm.
- Created a full state-transition flow for solving the `UF` edge based on its current position and orientation.
- Designed the edge-solving process so that after each move the cubie state is re-checked instead of hardcoding one long algorithm for every possible starting state.
- Started thinking about how the same `solveWhiteEdge()` structure can eventually be reused for `UF`, `UR`, `UB`, and `UL`.

### Learned

- A solver can be structured similarly to an FSM:
  - inspect the current state
  - classify the state
  - choose an action
  - apply the action
  - re-check the state
- `isEdgeSolved()` and `getEdgeData()` serve different purposes:
  - `isEdgeSolved()` answers whether a target edge is finished.
  - `getEdgeData()` tells the solver where the target edge currently is and how it is oriented.
- Python's `.index()` can be used to locate a particular cubie in the position list.
- When manually looping through a list, `for value in list` iterates through the stored values rather than the indices. To explicitly access indices, use an index-based loop or `enumerate()`.
- Edge orientation is stored by **position**, so after finding where a cubie is, its orientation has to be read from that same position.
- Solving cases can be simplified by making different states converge into common intermediate states instead of defining a complete independent algorithm for every possible state.
- For example, several `UF` states can transition toward known states such as `DF,0`, `FL,1`, or `FR,1`, which can then be solved using already-defined logic.
- Breaking the solver into individual state transitions should make the eventual RTL implementation easier because the software control flow already resembles controller/FSM behavior.
- The four white-cross edges are rotationally similar:
  - `UF` uses the F side
  - `UR` uses the R side
  - `UB` uses the B side
  - `UL` uses the L side
- Because of this symmetry, I should be able to reuse one general `solveWhiteEdge()` structure rather than writing four completely separate solvers.

### Problems

- Need to convert the completed `UF` state-transition flow into working Python control logic.
- Need to verify every `(position, orientation)` transition against the cube model rather than relying only on visualization.
- Need to figure out how to generalize the `UF` logic cleanly for `UR`, `UB`, and `UL`.
- Solving later white-cross edges may disturb edges that were already solved, so the full cross solver will need to preserve previous progress.
- Need to decide whether the final controller should use:
  - `if/elif` logic for each state, or
  - a lookup table mapping `(position, orientation)` directly to the next move.
- The current transition flow is only designed for one target edge and has not yet been tested end-to-end.

### Next

- Implement `solveWhiteEdge()` for `Edge.UF` using the state-transition flow.
- Start with an `if/elif` implementation so the decision logic is easy to inspect and debug.
- For each loop iteration:
  1. Check whether `UF` is solved.
  2. Retrieve its current position and orientation.
  3. Select one move based on the current state.
  4. Apply the move.
  5. Record the move.
  6. Re-check the resulting state.
- Test the `UF` solver from many different starting positions and both orientations.
- Verify that every possible UF state eventually reaches `UF, orientation 0`.
- Once the UF solver works reliably, generalize the same structure to `UR`, `UB`, and `UL`.
- After individual edge solving works, create `solveWhiteCross()` to sequence the four white edges while preserving previously solved ones.