# Round007 integration checkpoint

Exact parent: `d3e29723fcf9df107fc55a75716e5255898c1b53`, tree
`53c4983d9f85d418ed4d7ac74bc4526c82b0c234`. Remote:
`https://github.com/femboy2112/FuckingRH.git`. New branch:
`astra/stratified-succ-fucc-square-007`. No main or other branch merged.

The initially clean parent required reinstalling the declared Python dependencies
in the current runtime. The initial test attempt failed on missing imports;
after `python -m pip install -r requirements.txt`, all 128 tests passed.
The successful baseline output is retained. These tests do not validate every
claim in the later Claude prose or every standalone script.

## Side histories checked

| Side branch | Exact requested head | Integration |
|---|---|---|
| prime-jet-carrier-diagonal | 6aa91dbd5221dce79dee3e3eab479d43c412efd5 | Cherry-picked 035391e and 6aa91db |
| factor-square-moving-window | 9cc4f018d852edd849480334077748545c93c29e | Cherry-picked 1cdb432 and 9cc4f01 |
| chiral-affine-branches | b3252b602fce5395812565913dd5bc831fc71f81 | Cherry-picked edf73b0 and b3252b6 only |
| fucc-succ-composition-carry | 3b71fe8b5ca17822c8ff4b6c99dbb13ee49ca196 | Both requested files already byte-identical in parent; no duplicate pick |

The chiral branch has earlier source-port ancestors not in the parent history
under the same commit IDs. Only its two requested new-file commits were picked;
patch/history nonidentity was not mistaken for missing file content.

Imported notes remain provenance. Their operator statements are independently
proved with domains/boundaries below; imported numerical checks that compare an
expression to itself are not counted as independent verification.
