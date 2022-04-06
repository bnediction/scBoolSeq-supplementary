_n_threads = 12
_unim_q = 0.49
_alpha = 0.005

_det_kw = dict(n_threads=_n_threads, unimodal_margin_quantile=_unim_q)
_det_bin_kw = dict(n_threads=_n_threads, alpha=_alpha)

print("Zeroth iteration")
probin_det = ProfileBin(x).fit(**_det_kw).simulation_fit(**_det_kw)
binary_det = random_nan_binariser(
    probin_det.py_binarize(n_threads=_n_threads, alpha=_alpha)
)
simulated_det = probin_det.simulate(binary_det, n_threads=_n_threads)


criteriae_det = [probin_det.criteria]
simulation_criteriae_det = [probin_det.simulation_criteria]
probin_instances_det = [probin_det]
synthetic_data_det = [simulated_det]

for i in range(30):
    print(f"Iteration #{i+1}", flush=True)
    # Create a probin instance on the last simulated dataset
    print("\t Creating ProfileBin instance and training...", flush=True)
    _probin_i = (
        ProfileBin(synthetic_data_det[-1]).fit(**_det_kw).simulation_fit(**_det_kw)
    )
    probin_instances_det.append(_probin_i)
    # save the criteria frame
    criteriae_det.append(_probin_i.criteria)
    # binarise the expression frame
    print("\t Binarising data", flush=True)
    _binary_det = random_nan_binariser(_probin_i.py_binarize(**_det_bin_kw))
    # create new synthetic data
    print("\t Create synthetic frame", flush=True)
    synthetic_data_det.append(_probin_i.simulate(_binary_det, n_threads=_n_threads))
