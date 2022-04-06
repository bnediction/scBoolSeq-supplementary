_n_threads = 12
_unim_q = 0.49
_alpha = 0.005

_det_masked_kw = dict(
    n_threads=_n_threads, unimodal_margin_quantile=_unim_q, mask_zero_entries=True
)
_det_masked_bin_kw = dict(n_threads=_n_threads, alpha=_alpha)

print("Zeroth iteration")
probin_det_masked = ProfileBin(x).fit(**_det_masked_kw).simulation_fit(**_det_masked_kw)
binary_det_masked = random_nan_binariser(
    probin_det_masked.py_binarize(n_threads=_n_threads, alpha=_alpha)
)
simulated_det_masked = probin_det_masked.simulate(
    binary_det_masked, n_threads=_n_threads
)


criteriae_det_masked = [probin_det_masked.criteria]
simulation_criteriae_det_masked = [probin_det_masked.simulation_criteria]
probin_instances_det_masked = [probin_det_masked]
synthetic_data_det_masked = [simulated_det_masked]

for i in range(30):
    print(f"Iteration #{i+1}", flush=True)
    # Create a probin instance on the last simulated dataset
    print("\t Creating ProfileBin instance and training...", flush=True)
    _probin_i = (
        ProfileBin(synthetic_data_det_masked[-1])
        .fit(**_det_masked_kw)
        .simulation_fit(**_det_masked_kw)
    )
    probin_instances_det_masked.append(_probin_i)
    # save the criteria frame
    criteriae_det_masked.append(_probin_i.criteria)
    # binarise the expression frame
    print("\t Binarising data", flush=True)
    _binary_det_masked = random_nan_binariser(
        _probin_i.py_binarize(**_det_masked_bin_kw)
    )
    # create new synthetic data
    print("\t Create synthetic frame", flush=True)
    synthetic_data_det_masked.append(
        _probin_i.simulate(_binary_det_masked, n_threads=_n_threads)
    )
