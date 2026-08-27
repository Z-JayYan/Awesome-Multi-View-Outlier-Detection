# Reference repository analysis: `awesome-industrial-anomaly-detection`

## Scope and snapshot

This report is based only on the cloned reference `README.md`, `paper_tree.png`, and
`timeline.png` in `C:\Users\JayZ\AppData\Local\Temp\awesome-industrial-ad-reference`.
No links in the README were followed, and no MVOD project files were inspected. The
snapshot has 1,434 README lines, two raster assets, and a strongly hand-maintained
structure.

The reference is a useful living index: it combines a short “start here” layer,
curated code-bearing methods, benchmarks, a broad paper catalog, datasets, and two
visual summaries. Its main weakness is that these views are maintained independently.
The text has grown to 2026 while the diagrams, TOC, and some sections have not kept
up. Awesome-MVOD should inherit the entry points and metadata cues, but generate all
views from one normalized paper/dataset registry.

## Information architecture

The README is organized as follows (line numbers refer to the snapshot):

| Layer | Location | Contents and purpose |
|---|---:|---|
| Landing page | 1–29 | Awesome badge, scope keywords, survey/benchmark/result links, project announcements, and a PR invitation. |
| Table of contents | 31–90 | Manually nested links to highlights and the detailed taxonomy. |
| Curated methods | 92–125 | “SOTA methods with code”: a 29-row table with title, venue, date, code, and topic. |
| Curated benchmarks | 127–135 | Five rows covering Anomalib, IM-IAD, ADer, MMAD, and RobustMAD. |
| Recent research | 137–541 | Venue/year blocks plus special-topic blocks such as “MLLM related” and “SAM segment anything.” |
| Visual overview | 543–547 | Static paper tree and timeline images. |
| Context | 550–577 | A mixed survey, benchmark, framework, thesis, and tutorial list. |
| Method catalog | 579–1282 | Unsupervised/supervised methods, then other settings such as zero/few-shot, 3D, continual, logical, MLLM, and video AD. |
| Datasets | 1284–1400 | A 31-row dataset matrix followed by 79 additional unheaded dataset-paper entries. |
| Reuse/community | 1401–1434 | Three BibTeX records and a Star History chart. |

The top-level headings are partly numbered and partly not: SOTA, benchmarks, recent
research, tree, timeline, and surveys precede numbered sections 2–4. This makes the
README feel like several useful pages concatenated into one long page rather than a
single deliberate reading path.

### Table of contents

The TOC is a helpful map of the deep taxonomy and exposes the repository’s intended
categories before the reader reaches them. It also advertises the code and benchmark
entry points near the top. However, it is visibly manual and stale:

* The source contains 28 `##` blocks under “Recent research,” but the TOC lists only
  the early 2026 and 2025 blocks (and omits later 2024/2023 and special-topic blocks).
* The source has an empty `# Paper list for industrial image anomaly detection`
  heading at line 548; the TOC still points to it.
* Typos become permanent navigation labels, for example `Vison Language AD` and
  `Rubustness`, including their corresponding anchors.
* Large research blocks are hidden inside HTML comments (for example the ICLR/AAAI
  2025 block beginning at line 325 and the block beginning at line 346). A source
  reader and a rendered-page reader therefore see different catalogs.

For MVOD, the TOC should be generated from the same registry that drives the catalog,
and it should distinguish “curated highlights,” “complete catalog,” “datasets,” and
“how to contribute.”

## What each catalog layer does well, and where it breaks

### SOTA methods with code

The five-column table is an excellent practical first stop. Each row places a paper,
venue/year, GitHub link, and coarse topic next to one another; GitHub star badges make
the code signal immediately visible. The 29-row list includes representative families
such as teacher–student, one-class classification, distribution maps, memory banks,
reconstruction, few-shot, multi-class, RGB-D, point cloud, zero-shot, logical, and
MLLM methods.

The label “SOTA” is not defined and is subjective. There is no dataset, task level,
metric, input modality, number of views, training regime, inference cost, license,
commit/version, or code status. Rows are not normalized chronologically or by topic,
and the same work reappears in later catalogs. A dynamic star badge is a useful signal
but is not a reproducibility or quality check. For MVOD, keep this table as a small
“recommended implementations” view and rename it to avoid claiming a timeless SOTA.

### Recommended benchmarks

The five-row table gives newcomers a compact list of reusable infrastructure. It is
particularly good that it surfaces both a general library (Anomalib) and benchmark
projects (IM-IAD, ADer, MMAD, RobustMAD), rather than only individual methods.

The category mixes a software library with datasets/benchmark suites, and the common
columns do not say what is evaluated. There are no task definitions, splits, protocols,
metrics, modality/view coverage, annotation granularity, or expected baseline list.
MVOD should separate “toolkits,” “datasets,” and “leaderboards,” then show the exact
protocol and metric in each row.

### Recent research and conference/year organization

The recent section is broad and easy to scan by venue: it starts with ECCV 2026 and
proceeds through ICML/CVPR/ICLR/AAAI 2026, 2025, 2024, and 2023, with special MLLM
and SAM blocks. This is a good fast-moving-news layer and makes conference browsing
natural. Titles usually carry direct paper links and often a `code` link.

Its weaknesses are maintenance and discoverability:

* Venue/year is a publication index, not a method taxonomy. A reader cannot filter by
  task, dataset, modality, supervision, or deployment constraint without searching.
* Entries are duplicated across recent research, SOTA, the method taxonomy, and
  settings sections. The source visibly repeats, among others, MRAD in ICLR 2026,
  Commonality in Few in AAAI 2026, and Correcting Deviations from Normality in CVPR
  2025. Cross-listing is useful, but it needs one canonical record and generated
  references rather than copied rows.
* Status and link conventions vary: `Arxiv`/`arxiv`, `code`, `code coming soon`,
  `unofficial code`, project pages, and data links are all used without a legend.
* Some accepted-paper, preprint, workshop, and future-looking entries are mixed in a
  single stream; there is no distinction between first preprint year and venue year.
* Several major source blocks are commented out, so adding a paper can silently have
  no effect on the rendered page.

For MVOD, keep a venue/year view as one generated filter, not the canonical hierarchy.
Store both first-publication and venue information, with explicit status such as
`preprint`, `accepted`, `published`, `code available`, and `data available`.

### Taxonomy and paper tree

The text catalog (lines 579–1282) has a clear high-level decomposition:

* **Unsupervised AD** → feature embedding (teacher–student, OCC, distribution map,
  memory bank, vision-language) or reconstruction (AE, GAN, transformer, diffusion).
* **Supervised AD** → more normal/weak-label data versus more abnormal samples.
* **Other research directions** → zero/few-shot, noisy, synthesis, RGB-D, 3D,
  continual, uniform/multi-class, logical, MLLM, video, and smaller settings such as
  test-time training, adversarial robustness, defect classification, and universal
  tasks.

This gives strong coverage of the industrial anomaly-detection vocabulary and is
useful when a visitor already knows the field. It also exposes evolution from classic
feature/reconstruction methods to foundation models and operational settings.

The taxonomy mixes different axes at the same level: supervision, model family,
modality, data regime, task semantics, and deployment setting. A method can therefore
belong in several places, which explains the repeated entries and makes the hierarchy
hard to interpret as a lineage. “Vision Language AD” under feature embedding and
“MLLM-based AD” under other directions are overlapping examples. The unnumbered
“Other settings” subtree further weakens navigation. The empty “Paper list” heading
is a visible abandoned branch.

The paper tree image makes the intended mental model clearer than the text. Its root
is “Anomaly Detection,” with three large branches: “Unsupervised/Supervised AD,” “AD
with other settings,” and “Datasets.” The method branch then splits into feature
embedding/reconstruction/supervised families; colored branches and thin horizontal
labels connect representative papers to venues/years. Conceptually this is a good
overview, but it is a classification of representative works, not a complete or
exclusive taxonomy.

### Datasets

The dataset matrix is one of the strongest reusable ideas. It has 31 records and the
fields `Dataset`, `Class`, `Normal`, `Abnormal`, `Total`, `Annotation level`, `Source`,
and `Time`. That lets a newcomer quickly compare dataset scale, label type, real versus
synthetic origin, and publication era. The follow-on list also links dataset papers
and data sources, including major image, RGB-D, and point-cloud benchmarks.

The section needs stricter data hygiene. Counts are often `-`, names and venues vary in
style, and there are visible typos such as `Fabirc dataset` and `RBG synthetic`. The
`RAD` row shows Normal 213 and Abnormal 1224 but Total 1224, an internal arithmetic
inconsistency. The 79-entry follow-on list has no heading explaining whether it is a
paper bibliography, an extended dataset list, or historical references. There are no
split definitions, license/access constraints, annotation format, resolution, sensor
calibration, view count, or recommended metrics. MVOD needs those fields, especially
for multi-view geometry and fair cross-dataset comparison.

### Surveys, benchmarks, and contribution model

The landing section links the project’s survey, benchmark, and result pages; the
related list adds surveys, frameworks, software, a thesis, tutorials, and adjacent
OOD/vision-language resources. This gives a newcomer context before the long paper
lists. BibTeX and Star History provide citation and community signals, and the README
explicitly welcomes categorization and pull requests.

The contribution invitation does not specify a submission schema, inclusion criteria,
required paper/code/data links, link-checking policy, or review process. There is no
visible last-updated date, changelog, release/version, maintainer handoff, or
canonical metadata source. A stronger MVOD contribution section should make one new
paper entry predictable and machine-validatable.

### Visual design

The two assets have distinct jobs:

* `paper_tree.png` is 4,224 × 5,690 px. It uses a light background, a green root
  label, thick colored branches, and a very tall left-to-right method/dataset tree.
  It communicates hierarchy and representative lineage well, but labels become tiny
  at normal README width and the image is not searchable or screen-reader friendly.
* `timeline.png` is 6,453 × 2,009 px. It uses a horizontal baseline, year blocks from
  2018 through 2023, and colored branches with paper title plus venue/category in
  parentheses. It communicates chronology at a glance and complements the tree.

Both are static raster views with only short alt text (`PaperTree`, `Timeline`). The
timeline visibly stops at 2023, while the README’s text has active research through
2026. The tree likewise shows an older representative set. This is strong evidence
that manually regenerated visuals drift from the catalog. MVOD should provide an
accessible text/HTML/SVG equivalent and treat images as generated exports, not the
source of truth.

## What Awesome-MVOD should inherit

1. A concise landing statement with scope, keywords, and prominent links to the main
   catalog, survey/overview, benchmark, and results.
2. A layered reading path: a small curated “start here” list, then the complete
   catalog, datasets, surveys, and implementation resources.
3. Consistent paper/code/data affordances. The reference’s title–venue–year–code–topic
   row is an effective minimum, provided MVOD adds task and protocol fields.
4. A benchmark landing area and a compact comparison matrix. Keep toolkit rows
   separate from dataset and leaderboard rows.
5. Two complementary discovery views: a conceptual tree and a chronological timeline.
   Generate both from canonical records and include links, legends, and text fallback.
6. A related-resources section, citation block, and explicit contribution invitation.
   Add a contribution template, validation rules, and maintenance policy to make that
   invitation actionable.

## What is industrial-AD-specific and should not be copied blindly

The reference’s domain assumptions include anomaly/defect detection and localization
in industrial images; normal-only or one-class learning; few/zero-shot and open-set
defects; anomaly synthesis; noisy and continual inspection; RGB-D and point clouds;
logical/structural anomalies; MLLM reasoning; high-resolution/real-time inspection;
and industrial datasets such as MVTec, VisA, Real-IAD, Real3D-AD, and related defect
sets. Its method vocabulary (teacher–student, OCC, memory bank, distribution map,
reconstruction, diffusion) and dataset columns (normal/abnormal counts, annotation
level, real/synthetic source) are tailored to that problem.

Those categories should not become MVOD’s top-level taxonomy merely because they are
well presented. MVOD should replace defect/anomaly-specific branches with its own task,
view, geometry, fusion, output, and evaluation axes. Industrial-AD datasets and
anomaly-specific metrics belong in MVOD only when they are genuinely in scope.

## MVOD-specific information missing from the reference

The reference contains no MVOD task contract. Assuming MVOD means multi-view object
detection, the missing minimum is:

* **Problem definition:** what counts as a view, whether views are calibrated and
  synchronized, what is detected, and whether output is per-view 2D boxes, a common
  3D/BEV scene, tracks, or another representation.
* **View and sensor metadata:** camera/sensor type, number and arrangement of views,
  overlap, intrinsics/extrinsics, coordinate frame, synchronization, resolution, and
  missing/partial-view conditions.
* **Cross-view reasoning:** association/correspondence, triangulation or geometric
  constraints, occlusion handling, duplicate suppression, and how a single object is
  counted across views.
* **Learning regime and transfer:** fully supervised, weak/few-shot, self-supervised,
  domain adaptation, unseen-camera/generalization, and whether training sees all views.
* **Benchmark contract:** official splits, scene/object leakage rules, per-view versus
  cross-view evaluation, 2D/3D/BEV metrics, calibration assumptions, latency/resource
  reporting, and baseline implementations.
* **Reproducibility:** code/data/license status, configuration, checkpoint, hardware,
  input preprocessing, and exact evaluation command.

If MVOD expands differently, retain the same gap analysis but replace these fields
with the project’s actual task contract. The key lesson is that the visitor must learn
the task and evaluation semantics before seeing a method taxonomy.

## How a first-time visitor should understand MVOD

For a multi-view object-detection resource, the first screen should answer in plain
language: “Multiple cameras or sensors observe the same scene; MVOD combines their
evidence to detect objects in a declared output space, while addressing geometry,
occlusion, and cross-view consistency.” It should then offer this short path:

1. **Scope card:** in-scope task(s), output space, views/sensors, and explicit
   out-of-scope neighbors (ordinary single-view detection, tracking, or 3D detection
   unless included).
2. **Setting matrix:** rows for input/view geometry and columns for supervision,
   fusion stage, output space, and deployment condition.
3. **Canonical map:** a small tree showing the main families and a one-sentence
   explanation of each branch.
4. **Benchmark chooser:** dataset cards with view count, calibration, labels, split,
   metric, and license; link to a reproducible baseline.
5. **Method cards:** each card states the problem setting, key idea, code/data status,
   and reported protocol before linking to the paper.
6. **Timeline:** a few milestones that explain how multi-view geometry, fusion, and
   foundation/generalist methods evolved.

This sequence lets a newcomer form a task model first and use the catalog second.

## How to rebuild the tree and timeline

### One canonical registry

Create a structured record for every paper, dataset, toolkit, and benchmark, with a
stable ID and fields such as:

`title`, `authors`, `paper_url`, `year_first`, `venue`, `status`, `code_url`,
`data_url`, `task`, `output_space`, `view_count`, `sensor`, `calibration`, `fusion`,
`supervision`, `datasets`, `metrics`, `license`, and `notes`.

Require one primary classification and allow cross-cutting tags. Validate duplicate
IDs, required fields, year/venue format, URL presence, and dataset arithmetic where
counts are supplied. Render the README tables, TOC, tree, timeline, and filtered
landing pages from this registry.

### Replacement tree

Use a primary, non-overlapping path such as:

`MVOD → task/output → view & geometry → fusion/representation → supervision or deployment`

For example, task/output can distinguish per-view 2D, joint 3D/BEV, and any declared
tracking or open-vocabulary extension; view/geometry can distinguish calibrated,
uncalibrated, sparse, panoramic, or heterogeneous sensors; fusion can distinguish
early/input, feature/cross-view attention, query/object-level, late/score, and
explicit geometric methods. Supervision and deployment (fully supervised, few-shot,
domain shift, real-time, missing views) should be tags or a final branch, not mixed
arbitrarily with model family. Datasets should be a sibling branch with links to cards,
not mixed into method lineage.

The diagram should show representative milestones only, link each node to its
canonical card, include a legend, and have an accessible text outline. An SVG/HTML
tree with a PNG export is preferable to a giant raster-only image.

### Replacement timeline

Use a chronological axis with three lanes: (1) method/architecture milestones,
(2) datasets and benchmarks, and (3) toolkits/protocol milestones. Color should encode
the semantic lane or method family, not silently encode the year. Each marker should
link to a canonical record and display a short title plus task tag. Store first
preprint and venue year separately, and deduplicate preprint/accepted/published
versions.

Keep the default view readable by showing milestones, with filters for all entries,
venue, task, sensor, fusion, and supervision. Generate the timeline on every catalog
update so it cannot remain frozen at an earlier year. Retain a text table below it for
search, accessibility, and link checking.

## Bottom line

The reference succeeds as a broad, community-maintained industrial-AD index because
it gives visitors several entry points and consistently exposes paper/code/data links.
Its independent hand-edited views create stale navigation, duplicated records,
mixed-axis categories, and visual drift. Awesome-MVOD should preserve the layered
discovery experience while making task semantics, multi-view metadata, protocols, and
reproducibility the canonical data model.
