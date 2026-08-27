# Dataset Registry

The same base dataset is often converted into different multi-view feature sets by different papers. Counts and dimensions below describe the cited public variant only; `variant-dependent` is deliberate, not missing data. Always inspect the paper/code that defines the benchmark split before comparing results.

| Dataset | Instances | Views | Feature dimensions | Domain | Notes |
|---|---:|---:|---|---|---|
| [100Leaves](https://archive.ics.uci.edu/dataset/241/one-hundred-plant-species-leaves-data-set) | 1600 | 3 | 64/64/64 in the UCI feature files | plant leaf shape, margin, and texture | Many MVOD studies subsample or corrupt the complete UCI feature set. |
| [3Sources](http://erdos.ucd.ie/datasets/3sources.html) | 416 | 3 | variant-dependent | multilingual/news text | Article alignment and feature construction vary across redistributed benchmark files. |
| [BBCSport](http://mlg.ucd.ie/datasets/segment.html) | 544 | 2 | variant-dependent | news text | Multi-view versions use different vocabulary partitions or feature preprocessing. |
| [Caltech101](https://data.caltech.edu/records/mzrjq-6wc02) | variant-dependent | variant-dependent | variant-dependent | object images represented by multiple handcrafted or learned features | MVOD papers usually use a derived multi-feature subset; class count, sample count, and views are paper-specific. |
| [CiteSeer](https://linqs-data.soe.ucsc.edu/public/lbc/citeseer.tgz) | variant-dependent | variant-dependent | variant-dependent | scientific documents/citation network | Text, citation, and label variants differ; record the exact preprocessing when reporting a result. |
| [COIL-20](https://www.cs.columbia.edu/CAVE/software/softlib/coil-20.php) | 1440 | variant-dependent | variant-dependent | multi-angle object images | The base dataset has 72 poses per object; feature-view construction is paper-specific. |
| [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) | 70000 | variant-dependent | variant-dependent | clothing images represented by constructed feature views | Not inherently multi-view; views and anomaly corruption are constructed by each study. |
| [MNIST](http://yann.lecun.com/exdb/mnist/) | 70000 | variant-dependent | variant-dependent | handwritten digits represented by constructed feature views | Not inherently multi-view; view construction and sampling vary across papers. |
| [MVTec 3D-AD](https://www.mvtec.com/company/research/datasets/mvtec-3d-ad) | 4147 | 2 | RGB image and organized 3D point cloud | multimodal industrial inspection | Related RGB+3D track; modalities are spatially registered but use natural-defect protocols. |
| [NUSWIDEOBJ](https://lms.comp.nus.edu.sg/wp-content/uploads/2019/research/nuswide/NUS-WIDE.html) | variant-dependent | variant-dependent | variant-dependent | web images with visual features and tags | MVOD subsets differ in concepts, retained samples, visual descriptors, and tag features. |
| [Real-IAD](https://realiad4ad.github.io/Real-IAD/) | 150000 | 5 | image pixels | industrial multi-view images | Related natural multi-view track; protocol and metrics are not comparable to tabular classical MVOD. |
| [Reuters](https://archive.ics.uci.edu/dataset/137/reuters+21578+text+categorization+collection) | variant-dependent | variant-dependent | variant-dependent | multilingual/news text | “Reuters” denotes several incompatible multi-view constructions; never assume one canonical shape. |

## Registry usage map

- **100Leaves:** No paper entry currently names this exact public variant.
- **3Sources:** No paper entry currently names this exact public variant.
- **BBCSport:** No paper entry currently names this exact public variant.
- **Caltech101:** No paper entry currently names this exact public variant.
- **CiteSeer:** No paper entry currently names this exact public variant.
- **COIL-20:** [dPoE](https://doi.org/10.1145/3581783.3612487) (2023)
- **Fashion-MNIST:** [dPoE](https://doi.org/10.1145/3581783.3612487) (2023), [RCPMOD](https://doi.org/10.1145/3664647.3681125) (2024)
- **MNIST:** [NCMOD](https://doi.org/10.1609/AAAI.V35I8.16873) (2021), [dPoE](https://doi.org/10.1145/3581783.3612487) (2023)
- **MVTec 3D-AD:** [Learning Diffusion Models for Multi-view Anomaly Detection](https://doi.org/10.1007/978-3-031-73414-4_19) (2024)
- **NUSWIDEOBJ:** No paper entry currently names this exact public variant.
- **Real-IAD:** [IDIF](https://doi.org/10.1609/AAAI.V39I12.33349) (2025), [IMMoE](https://arxiv.org/abs/2607.19032) (2026), [MVAS](https://doi.org/10.1109/TMM.2026.3660076) (2026), [MATCH](https://arxiv.org/abs/2606.24375) (2026)
- **Reuters:** [NCMOD](https://doi.org/10.1609/AAAI.V35I8.16873) (2021)
