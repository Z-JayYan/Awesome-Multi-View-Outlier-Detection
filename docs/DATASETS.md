# Dataset Registry

The same base dataset is often converted into different multi-view feature sets by different papers. Counts and dimensions below describe the cited public variant only; `variant-dependent` is deliberate, not missing data. Always inspect the paper/code that defines the benchmark split before comparing results.

| Dataset | Track | Samples | Views | Feature / modality | Variants |
|---|---|---:|---:|---|---|
| [100Leaves](https://archive.ics.uci.edu/dataset/241/one-hundred-plant-species-leaves-data-set) | CORE | 1600 | 3 | 64/64/64 in the UCI feature files | unknown |
| [3Sources](http://erdos.ucd.ie/datasets/3sources.html) | CORE | 416 | 3 | variant-dependent | unknown |
| [BBCSport](http://mlg.ucd.ie/datasets/segment.html) | CORE | 544 | 2 | variant-dependent | unknown |
| [Caltech101](https://data.caltech.edu/records/mzrjq-6wc02) | CORE | unknown | unknown | variant-dependent | unknown |
| [CiteSeer](https://linqs-data.soe.ucsc.edu/public/lbc/citeseer.tgz) | CORE | unknown | unknown | variant-dependent | unknown |
| [COIL-20](https://www.cs.columbia.edu/CAVE/software/softlib/coil-20.php) | CORE | 1440 | unknown | variant-dependent | unknown |
| [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) | CORE | 70000 | unknown | variant-dependent | unknown |
| [M2AD](https://hustcyq.github.io/M2AD/) | industrial / natural | 119880 | 12 | RGB images; 1024x1024 and 256x256 public variants | M2AD-1024, M2AD-256, M2AD-Synergy, M2AD-Invariant |
| [MNIST](http://yann.lecun.com/exdb/mnist/) | CORE | 70000 | unknown | variant-dependent | unknown |
| [MVTec 3D-AD](https://www.mvtec.com/company/research/datasets/mvtec-3d-ad) | industrial / natural | 4147 | 2 | RGB image and organized 3D point cloud | unknown |
| [NUSWIDEOBJ](https://lms.comp.nus.edu.sg/wp-content/uploads/2019/research/nuswide/NUS-WIDE.html) | CORE | unknown | unknown | variant-dependent | unknown |
| [Real-IAD](https://realiad4ad.github.io/Real-IAD/) | industrial / natural | 150000 | 5 | image pixels | unknown |
| [Reuters](https://archive.ics.uci.edu/dataset/137/reuters+21578+text+categorization+collection) | CORE | unknown | unknown | variant-dependent | unknown |

## Registry usage map

- **100Leaves:** No paper entry currently names this exact public variant.
- **3Sources:** No paper entry currently names this exact public variant.
- **BBCSport:** No paper entry currently names this exact public variant.
- **Caltech101:** No paper entry currently names this exact public variant.
- **CiteSeer:** No paper entry currently names this exact public variant.
- **COIL-20:** [dPoE](https://doi.org/10.1145/3581783.3612487) (2023)
- **Fashion-MNIST:** [dPoE](https://doi.org/10.1145/3581783.3612487) (2023), [RCPMOD](https://doi.org/10.1145/3664647.3681125) (2024)
- **M2AD:** [M2AD](https://arxiv.org/abs/2505.10996) (2026)
- **MNIST:** [NCMOD](https://doi.org/10.1609/AAAI.V35I8.16873) (2021), [dPoE](https://doi.org/10.1145/3581783.3612487) (2023)
- **MVTec 3D-AD:** [Learning Diffusion Models for Multi-view Anomaly Detection](https://doi.org/10.1007/978-3-031-73414-4_19) (2024)
- **NUSWIDEOBJ:** No paper entry currently names this exact public variant.
- **Real-IAD:** [Multi-Flow](https://doi.org/10.1109/CVPRW67362.2025.00378) (2025), [IDIF](https://doi.org/10.1609/AAAI.V39I12.33349) (2025), [IMMoE](https://arxiv.org/abs/2607.19032) (2026), [MVAS](https://doi.org/10.1109/TMM.2026.3660076) (2026), [MATCH](https://arxiv.org/abs/2606.24375) (2026)
- **Reuters:** [NCMOD](https://doi.org/10.1609/AAAI.V35I8.16873) (2021)
