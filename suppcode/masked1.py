_n_threads = 12
_unim_q = 0.49
_alpha = 0.005

_masked_kw = dict(n_threads=_n_threads, mask_zero_entries=True)
_masked_bin_kw = dict(n_threads=_n_threads, alpha=_alpha)

print("Zeroth iteration")
probin_masked = ProfileBin(x).fit(**_masked_kw).simulation_fit(**_masked_kw)
binary_masked = random_nan_binariser(
    probin_masked.py_binarize(n_threads=_n_threads, alpha=_alpha)
)
simulated_masked = probin_masked.simulate(binary_masked, n_threads=_n_threads)


criteriae_masked = [probin_masked.criteria]
simulation_criteriae_masked = [probin_masked.simulation_criteria]
probin_instances_masked = [probin_masked]
synthetic_data_masked = [simulated_masked]

for i in range(30):
    print(f"Iteration #{i+1}", flush=True)
    # Create a probin instance on the last simulated dataset
    print("\t Creating ProfileBin instance and training...", flush=True)
    _probin_i = (
        ProfileBin(synthetic_data_masked[-1])
        .fit(**_masked_kw)
        .simulation_fit(**_masked_kw)
    )
    probin_instances_masked.append(_probin_i)
    # save the criteria frame
    criteriae_masked.append(_probin_i.criteria)
    # binarise the expression frame
    print("\t Binarising data", flush=True)
    _binary_masked = random_nan_binariser(_probin_i.py_binarize(**_masked_bin_kw))
    # create new synthetic data
    print("\t Create synthetic frame", flush=True)
    synthetic_data_masked.append(
        _probin_i.simulate(_binary_masked, n_threads=_n_threads)
    )
