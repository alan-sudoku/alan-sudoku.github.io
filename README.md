# alan-sudoku.github.io

Publication site for SIRC, Entropic Compact, and Argument Structure Audit.

Live at: https://alan-sudoku.github.io

Built with [Quartz v5](https://quartz.jzhao.xyz).

## Content

| Folder | Source repo | Description |
|---|---|---|
| `content/sirc/` | [SIRC](https://github.com/alan-sudoku/SIRC) | Principles, glossary, retraction log |
| `content/entropic_compact/` | [entropic_compact](https://github.com/alan-sudoku/entropic_compact) | Constraint theory |
| `content/argument_structure_audit/` | [argument_structure_audit](https://github.com/alan-sudoku/argument_structure_audit) | Audit methodology |

Content folders are read-only here — edit in source repos. Each source repo has a sync Action that pushes to this repo on commit, triggering a Pages rebuild.

## Local preview

```bash
npm ci
npx quartz build --serve
# open http://localhost:8080
```

## Cross-repo sync

Each source repo needs a secret `PAGES_WRITE_TOKEN` — a GitHub PAT (classic) with `repo` scope pointing at this repo.
