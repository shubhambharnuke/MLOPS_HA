# PRD — Final Assignment Completion & Submission Workspace

## 1. Project Overview

**Project name:** Final Assignments A1–A9  
**Primary workspace:** `final_submissions/`  
**Execution environment:** Antigravity IDE / agent  
**Primary objective:** Complete nine independent assignments by following the instructions in each assignment's `instructions.pdf`, create a report for each assignment using the supplied report template, keep every deliverable inside its corresponding assignment folder, and maintain a Git repository for the overall submission workspace.

Antigravity must treat A1 through A9 as **nine separate projects**. Do not combine their source code, datasets, reports, dependencies, or deliverables unless an assignment explicitly requires a shared resource.

---

## 2. Existing Folder Structure

The user has already created the following structure:

```text
final_submissions/
├── report_template                  # Supplied report template (file or document)
├── A1/
│   └── instructions.pdf
├── A2/
│   └── instructions.pdf
├── A3/
│   └── instructions.pdf
├── A4/
│   └── instructions.pdf
├── A5/
│   └── instructions.pdf
├── A6/
│   └── instructions.pdf
├── A7/
│   └── instructions/
│       └── <existing project files>
├── A8/
│   └── instructions.pdf
└── A9/
    └── instructions.pdf
```

The actual template filename and extension may differ. Inspect the directory rather than assuming a particular extension.

**Special case — A7:** A7 does **not** contain an `instructions.pdf`. Instead, it contains a directory named `instructions/` with the files of an existing project. Treat that directory as the starter project and the source material for A7. Do not expect or search for an A7 PDF. Inspect the complete contents of `A7/instructions/`, including source code, configuration, workflow files, documentation, and Git-related files, before deciding what to implement.

### Required final structure

Preserve the existing folders and source instruction PDFs. Add the files needed to complete each assignment inside its own folder.

```text
final_submissions/
├── report_template
├── README.md
├── A1/
│   ├── instructions.pdf
│   ├── <assignment source files>
│   ├── <required datasets and assets, if applicable>
│   ├── <execution/configuration files, if applicable>
│   └── report.<appropriate-extension>
├── A2/
│   ├── instructions.pdf
│   ├── <assignment source files>
│   └── report.<appropriate-extension>
...
└── A9/
    ├── instructions.pdf
    ├── <assignment source files>
    └── report.<appropriate-extension>
```

The examples above are illustrative. For A1–A6 and A8–A9, determine deliverables from each assignment's PDF and the report template. For A7, determine deliverables from the existing project in `A7/instructions/` and the user's stated objective: study and implement GitHub CI/CD using that project.

**Important:** Do not create a second nested `final_submissions/final_submissions/` directory. The Git repository root must be the existing `final_submissions/` directory.

---

## 3. Goals

1. Read and understand all nine assignment instruction PDFs.
2. Identify the exact requirements, expected outputs, constraints, technologies, and submission format for each assignment.
3. Complete every assignment independently and correctly.
4. Produce all required source files, outputs, evidence, and supporting assets.
5. Create one report per assignment using the supplied report template.
6. Keep each assignment's complete submission within its own `A1`–`A9` directory.
7. Validate that each assignment works and satisfies its PDF requirements.
8. Initialize or use a Git repository rooted at `final_submissions/`.
9. Commit each completed assignment separately, immediately after its validation.
10. Provide a final summary showing the completion status of all nine assignments.

---

## 4. Non-Goals and Restrictions

- Do not merge the nine assignments into one application or one report.
- Do not change the assignment requirements to make implementation easier.
- Do not delete, rename, or modify the original instruction PDFs or supplied report template.
- Do not place final deliverables outside `final_submissions/`, except temporary files that are removed before completion.
- Do not claim that an assignment works unless it has been tested to the extent possible.
- Do not fabricate screenshots, test results, metrics, outputs, citations, references, or implementation details.
- Do not include AI-generated branding, tool watermarks, promotional badges, or unnecessary AI labels in deliverables. Do not attempt to conceal required disclosures, falsify authorship, or misrepresent work where the institution requires disclosure.
- Do not copy another student's submission or reproduce copyrighted work as if it were original. Use references appropriately and cite external material where required.
- Do not expose credentials, API keys, access tokens, private keys, or personal information in source files, reports, screenshots, Git history, or commits.
- Do not push to a remote repository unless a remote is configured and the user has authorized the push. Creating local commits is required; publishing is a separate action.

---

## 5. Phase 1 — Workspace Inspection and Planning

Before implementation:

1. Locate the existing `final_submissions/` directory.
2. List its contents and verify that `A1` through `A9` are present.
3. Locate and identify the report template file.
4. Confirm that A1–A6 and A8–A9 each contain their `instructions.pdf`.
5. Extract/read each of those eight PDFs fully. If a PDF is scanned, use OCR or another appropriate method and verify that the extracted instructions are readable.
6. For A7, inspect the entire `A7/instructions/` existing project recursively. Read its README and all relevant source, dependency, build, test, and configuration files. Identify its language, framework, build/test commands, current repository structure, and how the application is expected to run.
7. Inspect the report template's structure, sections, formatting, and required fields.
8. Create an internal requirement checklist for every assignment. For A7, derive the checklist from the existing project and the GitHub CI/CD objective rather than looking for a PDF.

For each assignment, record:

- Assignment identifier and title.
- Problem statement and objective.
- Functional and non-functional requirements.
- Required language, frameworks, tools, libraries, and versions, if specified.
- Required inputs, datasets, and expected outputs.
- Required algorithms, workflow, or architecture.
- Required screenshots, diagrams, tables, test evidence, or results.
- Required report sections and submission file formats.
- Evaluation criteria or rubric.
- Any ambiguity, missing resource, or blocker.

For A1–A6 and A8–A9, the corresponding PDF is the source of truth. For A7, the existing project files in `A7/instructions/` are the starting point, and the required outcome is to study and implement GitHub CI/CD for that project. Do not invent a separate A7 project or replace the supplied project with an unrelated example.

### Planning deliverable

Maintain a concise checklist in the root `README.md` or an internal planning file. It must track A1–A9 independently, including status, requirements reviewed, validation status, report status, and commit identifier.

---

## 6. Phase 2 — Assignment Implementation

Complete assignments one at a time, in order from A1 to A9, unless a genuine dependency or user instruction requires a different order.

For each assignment:

1. For A1–A6 and A8–A9, re-read its `instructions.pdf`; for A7, re-inspect the relevant existing project files and the A7 requirement checklist.
2. Inspect any starter files or resources already present in that assignment folder.
3. Choose an implementation approach that satisfies the stated requirements, not merely a minimal demonstration.
4. Create all required source code, configuration, documentation, datasets, diagrams, and other deliverables inside that assignment's folder.
5. Use clear, consistent filenames and a sensible folder structure.
6. Add a `README.md` inside the assignment folder when useful or required. It should explain prerequisites, setup, execution, outputs, and verification.
7. Keep dependencies isolated where appropriate. Do not let one assignment's dependency changes break another assignment.
8. Use relative paths where practical so the project can be run from the submission folder after it is cloned.
9. Do not hard-code machine-specific absolute paths, local usernames, or secrets.
10. Handle errors and edge cases relevant to the assignment.
11. Add comments where they improve understanding; avoid unnecessary boilerplate.
12. Preserve reproducibility: document relevant versions, commands, seeds, and configuration.

If the instructions are incomplete or contradictory, inspect all available files and make the safest reasonable interpretation. If a decision materially changes the required outcome and cannot be resolved from the provided materials, stop that assignment and ask the user a focused question rather than inventing a requirement.

### Completion standard

An assignment is not complete merely because files have been created. It is complete only when:

- Every requirement has been mapped to an implementation or an explicitly documented limitation.
- Required outputs have been generated.
- The implementation has been executed or otherwise validated.
- The report has been created and checked.
- The folder contains the complete submission.
- The assignment has been committed to Git.

---

## 6A. Special Requirements for A7 — GitHub CI/CD on the Existing Project

A7 is different from the other assignments. It has no `instructions.pdf`. Its `instructions/` directory contains an existing project that must be studied and used as the basis for implementing GitHub CI/CD.

### A7 discovery and study

1. Recursively inspect `A7/instructions/` before changing anything.
2. Identify the project's purpose, programming language, framework, dependencies, entry point, build process, test framework, and current run instructions.
3. Read existing documentation and configuration. Understand how the project currently builds and runs.
4. Identify suitable automated checks for this particular project. Do not assume it is a Python, Node.js, Java, or other project until the files confirm it.
5. Preserve the original project and its meaningful functionality. Avoid replacing it with a generic CI/CD demo.

### A7 GitHub CI/CD implementation

Implement a GitHub Actions workflow appropriate to the discovered project. At minimum, aim to provide:

- **Continuous Integration (CI):** Trigger automated checks on pushes and pull requests to the relevant branch(es).
- **Environment setup:** Select a suitable runner and install/configure the required language runtime and dependencies.
- **Build and validation:** Run the project's appropriate build, lint, static checks, and/or test commands, where supported.
- **Continuous Delivery/Deployment (CD):** Determine a safe, project-appropriate delivery or deployment step. If the project has no deployable target or deployment credentials are unavailable, implement the delivery portion that can be completed safely and clearly document what is required for actual deployment.
- **Workflow visibility:** Ensure workflow status and execution results are understandable from the GitHub Actions interface.
- **Documentation:** Explain the workflow, triggers, jobs, steps, required repository settings/secrets (without recording secret values), and how to verify a successful run.

Use `.github/workflows/` for GitHub Actions YAML workflow files unless the existing project structure or requirements justify another arrangement. Prefer secure practices: least-privilege `permissions`, pinned or appropriately constrained actions, no secrets in source code, and no unnecessary privileged workflows. Do not add deployment secrets or invent credentials.

### A7 repository and GitHub handling

1. Determine whether `A7/instructions/` already contains Git metadata or is linked to an existing remote. Do not overwrite or discard its history.
2. The overall coursework repository still has its root at `final_submissions/`.
3. Do not create an accidental nested Git repository. If the supplied project already has its own `.git` directory, inspect it and decide how to preserve it while satisfying the overall repository requirement. Ask the user before removing or flattening existing Git history.
4. Add and validate the workflow in the appropriate project location. If the overall repository is the intended GitHub repository, ensure the workflow path is visible to GitHub Actions at the repository root. GitHub Actions only discovers workflows in the repository's `.github/workflows/` directory; a workflow buried in a subfolder of a larger repository will not automatically run as a repository-root workflow. If necessary, adapt the workflow with correct working-directory paths or propose a safe repository layout.
5. Do not claim that a GitHub Actions run succeeded unless it has actually run and its result has been checked.
6. If GitHub authentication, repository creation, remote configuration, or user permissions are required and unavailable, complete all local workflow preparation and validation possible, then ask the user for the minimum necessary action. Never claim a workflow was published or executed on GitHub when it was not.

### A7 evidence and report

The A7 report must explain the existing project that was studied, the CI/CD design, workflow triggers, jobs and steps, validation performed, and the observed result of an actual workflow run if one was available. Include genuine screenshots or logs when required by the report template. Clearly distinguish local validation from a workflow run executed by GitHub Actions.

## 7. Phase 3 — Testing and Verification

Validate each assignment against its own PDF before preparing its report.

Use the relevant checks for the assignment, such as:

- Run the program, application, notebook, workflow, or build process.
- Verify that required inputs are read correctly.
- Verify that expected outputs are produced in the specified format.
- Check important edge cases and error handling.
- Confirm that all required files are present.
- Check that paths work from the assignment directory.
- Confirm that instructions in the assignment README are accurate.
- Check that there are no missing dependencies or references to files outside the submission.
- Review generated screenshots and evidence for readability and authenticity.

For code-based assignments, run appropriate syntax checks, tests, and execution commands. For document/design/research assignments, verify content completeness, formatting, references, and compliance with the rubric.

Never fabricate successful execution. If a tool, service, hardware device, paid API, or external account is unavailable, document the limitation and what remains unverified. Ask the user for access or input only when it is genuinely necessary.

---

## 8. Phase 4 — Assignment Report Generation

After an assignment has been implemented and validated, create its report using the supplied `report_template`.

### Report requirements

1. Inspect the template carefully before generating any report.
2. Preserve its section order, headings, formatting conventions, tables, and required fields as closely as possible.
3. Create one separate report for each assignment.
4. Save the report inside the relevant assignment folder.
5. Use an appropriate format based on the template and assignment instructions. If the template is a DOCX, normally create a DOCX report; if it is a PDF or another format, follow its intended format.
6. Replace all placeholders with assignment-specific information.
7. Include the actual objective, methodology, implementation details, results, discussion, conclusion, and references wherever the template requires them.
8. Include genuine screenshots, diagrams, tables, outputs, or test evidence when required.
9. Ensure figures and tables have clear captions and are referenced in the report text.
10. Ensure the report describes what was actually implemented and tested. Do not claim unperformed work or invent results.
11. Use clear academic/professional language and proofread the report.
12. Do not leave template placeholders, sample text, or instructions for the report author in the final report.

Suggested report filename: `report` with the template's appropriate extension. If the PDF specifies a filename, follow the PDF instead.

**The original report template must remain unchanged.** Create a separate copy or generated report for each assignment.

---

## 9. Phase 5 — Git Repository and Commit Policy

The Git repository must track the complete `final_submissions/` workspace, including all nine assignment folders, reports, and the root README.

### Repository setup

1. Check whether `final_submissions/` is already a Git repository.
2. If it is, inspect its current branch, working tree, commit history, and remotes before making changes.
3. If it is not, initialize Git with `final_submissions/` as the repository root.
4. Check for an existing GitHub remote. If one exists, preserve it unless the user explicitly asks to change it.
5. If no remote exists, prepare the repository for GitHub and use available authenticated GitHub tooling to create a repository only if the user has authorized that action and the repository name/visibility can be determined safely. If not, ask the user for the missing decision.
6. Never place credentials or tokens in the repository or remote URL stored in scripts/configuration.

### Commit after every assignment

After each assignment has passed validation and its report is complete:

1. Review `git status`.
2. Inspect the diff and ensure no secrets, unrelated files, temporary files, caches, virtual environments, or generated clutter are included.
3. Stage only the completed assignment's files plus any genuinely relevant root-level progress update.
4. Commit the changes before starting the next assignment.
5. Use a clear commit message, for example:
   - `Complete A1 assignment and report`
   - `Complete A2 assignment and report`
   - Continue consistently through A9.
6. Record the commit hash in the root progress tracker.

This must produce a clear sequence of assignment-level commits. Do not wait until all nine assignments are finished to make the first commit.

### Git hygiene

Create or update `.gitignore` as appropriate for the technologies used. Exclude items such as:

- Virtual environments (`.venv/`, `venv/`, `env/`).
- Python caches (`__pycache__/`, `*.pyc`).
- IDE and operating-system clutter.
- Temporary files and logs.
- Large generated artifacts that are not required for submission.
- Credentials, `.env` files, and local secret/configuration files.

Do not ignore any dataset, model, report, screenshot, or output that the assignment explicitly requires for submission. If a required artifact is too large for ordinary GitHub storage, explain the issue and propose an appropriate solution (for example, Git LFS) rather than silently omitting it.

### GitHub publication

Local commits are mandatory. Push commits to GitHub only when the remote is correctly configured and the user has authorized publishing. Verify the push result; do not claim that work is on GitHub if only local commits exist.

---

## 10. Phase 6 — Final Audit

After A1–A9 are complete, perform a final audit.

For every assignment, verify:

- [ ] Original `instructions.pdf` is still present for A1–A6 and A8–A9; A7's original `instructions/` project is preserved.
- [ ] Every requirement in the PDF has been addressed.
- [ ] All required implementation/source files are present.
- [ ] All required datasets/assets are present or properly referenced.
- [ ] The solution has been executed or validated.
- [ ] Required outputs and evidence are present.
- [ ] The report follows the supplied template.
- [ ] No placeholders or sample content remain in the report.
- [ ] No unnecessary AI branding or tool watermarks appear in deliverables.
- [ ] No secrets or unrelated files are included.
- [ ] The assignment has its own Git commit.

At the root level, verify:

- [ ] All nine assignment folders exist.
- [ ] The original report template is preserved.
- [ ] The root README contains accurate setup and progress information.
- [ ] Git repository root is `final_submissions/`.
- [ ] Git history contains a separate completion commit for each assignment.
- [ ] Working tree is clean, except for any explicitly documented user-owned changes.
- [ ] GitHub push status is accurately reported.

---

## 11. Root README Requirements

Create or update `final_submissions/README.md` with:

- Project title and brief overview.
- Folder structure.
- A1–A9 assignment titles and one-line descriptions, taken from their PDFs.
- Setup and execution instructions for each assignment, or links to the assignment-level READMEs.
- Required software/dependency overview.
- A completion table with columns for assignment, implementation, validation, report, and commit.
- Any known limitations or steps that require external access.
- Git repository and publication status.

Do not include unsupported claims or expose private information.

---

## 12. Execution Strategy and Progress Tracking

Work sequentially. Do not attempt all nine assignments in one unverified batch.

Use the following status values:

- `NOT STARTED`
- `IN REVIEW`
- `IN PROGRESS`
- `BLOCKED`
- `IMPLEMENTED`
- `VALIDATED`
- `REPORTED`
- `COMMITTED`
- `COMPLETE`

An assignment can be marked `COMPLETE` only after implementation, validation, report generation, and its Git commit are all finished.

Suggested tracker:

| Assignment | Requirements reviewed | Implementation | Validation | Report | Commit | Status |
|---|---|---|---|---|---|---|
| A1 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |
| A2 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |
| A3 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |
| A4 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |
| A5 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |
| A6 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |
| A7 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |
| A8 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |
| A9 | Pending | Pending | Pending | Pending | Pending | NOT STARTED |

Update the tracker after each meaningful stage. Do not mark a stage complete prematurely.

---

## 13. Final Handoff

When all work is finished, provide a concise final handoff that includes:

1. Completion status of A1 through A9.
2. The title and key deliverables of each assignment.
3. The path to each assignment's report.
4. The validation performed for each assignment.
5. The commit hash and commit message for each assignment.
6. Whether the commits were pushed to GitHub or remain local.
7. Any limitations, unverified requirements, or user actions still needed.

The final handoff must distinguish clearly between completed, partially completed, blocked, locally committed, and remotely published work.

---

## 14. Primary Instruction to Antigravity

**Start by inspecting the existing `final_submissions/` directory, the eight instruction PDFs in A1–A6 and A8–A9, the existing starter project in `A7/instructions/`, and the supplied report template. Build a requirement checklist for A1–A9 before implementation. For A7, study the supplied project and implement GitHub CI/CD using GitHub Actions; do not look for an A7 PDF or substitute an unrelated project. Then complete A1 through A9 sequentially and independently. For each assignment, implement the full requirements, run appropriate validation, create its report using the supplied template, save every deliverable inside that assignment's folder, and make a separate Git commit before moving to the next assignment. For A7, validate the CI/CD workflow locally where possible and verify an actual GitHub Actions run if repository access is available. Preserve the original instructions and template. Finish only after the final audit and provide an accurate completion and Git status report.**

Do not stop after creating a plan or skeleton files. Continue through implementation and verification, asking the user only when a genuine blocker or consequential ambiguity requires their input.
