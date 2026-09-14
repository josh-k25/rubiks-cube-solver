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

## 2026-09-11

### Worked on

- Continued implementing the Layer-by-Layer solver.
- Developed the white-cross solving strategy.
- Split white-cross solving into two stages:
  - `stageEdge()` moves each white edge to the D layer with orientation 0.
  - `solveEdge()` aligns the staged edge beneath its correct U-layer position and inserts it with a half turn.
- Created lookup tables for:
  - White-edge target D positions.
  - Middle-layer edge staging moves.
  - Final white-edge insertion moves.
- Added logic to protect white edges that have already been staged on the D layer.
- Handled white edges starting in:
  - U layer.
  - Middle layer.
  - D layer with incorrect orientation.
- Continued using the cubie representation to query each edge's current position and orientation.

### Learned

- Breaking the solver into a staging phase and an insertion phase significantly reduces the number of cases each function needs to handle.
- A useful solver invariant is that previously staged white edges should not be destroyed while staging another edge.
- D-layer rotations are useful for repositioning staged pieces without changing their orientation.
- Lookup tables are useful for representing deterministic cube-solving decisions instead of writing large chains of conditionals.
- A solver can normalize many different starting states into a smaller set of predictable states before performing the final solve step.

### Problems

- Need to verify that every possible white-edge position and orientation converges correctly through `stageEdge()`.
- Need to make sure already staged edges remain protected while other edges are manipulated.
- Need to test the complete white-cross process from actual scrambles rather than only individual cases.

### Next

- Connect `stageEdge()` and `solveEdge()` into a full `solveWhiteCross()` function.
- Test the white-cross solver end-to-end.
- Begin first-layer corner solving after the cross is reliable.


## 2026-09-12

### Worked on

- Created `solveWhiteCross()` to coordinate the white-cross solver:
  - Stage all four white edges.
  - Insert all four white edges into their solved positions.
- Started implementing the first-layer corner solver.
- Created `stageCorner()` to normalize unsolved white corners onto the D layer.
- Added handling for:
  - Corners already solved.
  - Corners already somewhere on the D layer.
  - Unsolved corners on the U layer that need to be ejected.
- Created a mapping between each white corner and the D-layer position directly underneath its destination:
  - URF → DFR
  - UFL → DLF
  - ULB → DBL
  - UBR → DRB
- Created corner ejection lookup tables based on the current U-layer position.
- Started `solveCorner()` to rotate the D layer until a staged corner is underneath its destination.
- Replaced the original `R U R' U'` insertion idea with D-layer-based insertion sequences so the completed U-layer white cross is preserved.
- Created separate corner insertion sequences for URF, UFL, ULB, and UBR.
- Added repeated corner insertion until `isCornerSolved()` reports both correct position and orientation.
- Fixed function indentation so solver functions are top-level rather than accidentally nested.
- Corrected use of returned cube states from `applyMove()` and `applyMoves()`.
- Used tuple unpacking with `_` when only the cubie's position is needed.

### Learned

- Because the white layer is being solved on U, the opposite D face should be used as the working layer during first-layer corner insertion.
- `R U R' U'` is not appropriate for this cube orientation because it disturbs the already solved U-layer cross.
- Corner solving can also be reduced to a staging problem:
  - Get the target corner onto D.
  - Align it underneath its target.
  - Apply the target-specific insertion sequence until solved.
- The corner's orientation does not matter while aligning it underneath its destination; orientation is handled during insertion.
- `position, _ = getCornerData(corner)` is useful when orientation is intentionally irrelevant.
- Functions such as `applyMove()` and `applyMoves()` return a new cube state, so the returned state must be reassigned.
- Python indentation determines function scope, so accidentally indenting one `def` inside another changes the program structure.

### Problems

- Need to test the corner insertion sequences against the actual cube model.
- Need to verify that solving a corner preserves the white cross.
- Need to verify that solving later corners preserves previously solved corners.
- Need to test `stageCorner()` for all U-layer and D-layer starting positions and orientations.
- Move-history tracking is still not implemented even though a `moves` parameter exists in parts of the solver.

### Next

- Test `solveWhiteCross()` on several controlled scrambles.
- Test `stageCorner()` and `solveCorner()` first with URF.
- Test URF from different positions and orientations.
- Verify the white cross remains solved after every corner insertion.
- Repeat testing for UFL, ULB, and UBR.
- Build `solveWhiteCorners()` to coordinate all four corners.     
- Verify the complete first layer before beginning second-layer edges.

## 2026-09-13

### Worked on

- Finished debugging the underlying cube-state move engine.
- Fixed `applyMove()` so:
  - The requested move is actually used.
  - Prime and double moves are implemented as repeated quarter turns.
  - Each repeated turn operates on the result of the previous turn.
  - A fresh cube state is created for each permutation so source values are not overwritten while calculating the destination state.
- Fixed `getEdgeData()` and `getCornerData()` so orientation is retrieved from the cubie's current position.
- Finished the full first-layer Layer-by-Layer solver.
- Created `solveFirstLayer()` to combine:
  - White-cross solving.
  - White-corner solving.
- Completed white-cross solving using:
  - `stageEdge()`
  - `solveFirstLayerEdge()`
  - `solveWhiteCross()`
- Completed first-layer corner solving using:
  - `stageCorner()`
  - `solveFirstLayerCorner()`
  - `solveWhiteCorners()`
- Added `isFirstLayerSolved()` to verify that all four U-layer edges and all four U-layer corners are solved.
- Tested the first-layer solver using randomized scrambles.

- Started and completed the second-layer edge solver.
- Defined the four second-layer target edges:
  - FL
  - FR
  - BL
  - BR
- Created middle-layer ejection sequences so an incorrectly placed target edge can first be moved onto the D layer.
- Initially tried solving second-layer edges by forcing every D-layer edge into orientation 1 before insertion.
- Created a separate `D_EDGE_FLIP_DATA` approach for flipping D-layer edges.
- Discovered through testing that these flip sequences could solve the current target while destroying previously solved second-layer edges.
- Debugged the problem by printing each target edge's:
  - Position.
  - Orientation.
  - Solved status.
- Traced failures where a later edge insertion displaced an edge that had already been solved.
- Removed the separate edge-flipping approach.
- Redesigned second-layer solving around all eight `(edge, orientation)` cases:
  - FL,0
  - FL,1
  - FR,0
  - FR,1
  - BL,0
  - BL,1
  - BR,0
  - BR,1
- Created `SECOND_EDGE_SOLVE_DATA` where each `(edge, orientation)` maps directly to:
  - The required D-layer setup position.
  - The corresponding insertion sequence.
- Finished `solveSecondLayer()`:
  - Skip edges that are already solved.
  - Eject incorrectly placed middle-layer edges to D.
  - Read the target edge's position and orientation.
  - Select the correct setup case from the lookup table.
  - Rotate D until the edge reaches the required setup position.
  - Apply the insertion sequence.
- Added `isSecondLayerSolved()` to verify:
  - The entire first layer remains solved.
  - FL, FR, BL, and BR are all solved.
- Successfully got both the first-layer and second-layer solvers working.

### Learned

- A cube move is fundamentally a permutation plus orientation changes.
- `list.index()` returns the current position of a cubie, but returns a normal Python integer even when the list contains `IntEnum` members.
- Cubie orientation is stored by position, so after finding a cubie's current position, orientation must be read using that position.
- Position plus orientation is enough to determine which second-layer insertion case should be used.
- Setup states for algorithms can be derived by working backward from the solved state:
  - Start with a solved piece.
  - Reverse the insertion sequence.
  - Observe the resulting `(position, orientation)`.
  - Use that state as the required forward setup condition.

### Problems

- The initial second-layer design assumed every target edge should have orientation 1 before insertion.
- Debugging required distinguishing between:
  - The current edge being solved correctly.
  - The entire previously solved portion of the cube remaining intact.
- Long move sequences are difficult to trust visually and need to be verified against the cubie model.

### Next

- Create final Layer solver