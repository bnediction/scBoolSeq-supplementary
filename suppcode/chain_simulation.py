""" Temp helper module
"""

from ..wrappers.probinr import ProfileBin
from ..simulation import random_nan_binariser


def chain_binarization_and_generation(
    expr_df,
    n_threads,
    alpha,
    training_kw,
):
    """ """
    _n_threads = n_threads
    x = expr_df
    _ = training_kw.pop("n_threads", None)

    print("Zeroth iteration")
    probin_ = (
        ProfileBin(x)
        .fit(n_threads=_n_threads, **training_kw)
        .simulation_fit(n_threads=_n_threads, **training_kw)
    )
    binary_ = random_nan_binariser(
        probin_.py_binarize(n_threads=_n_threads, alpha=alpha)
    )
    simulated_ = probin_.simulate(binary_, n_threads=_n_threads)

    criteriae_ = [probin_.criteria]
    simulation_criteriae_ = [probin_.simulation_criteria]
    probin_instances_ = [probin_]
    synthetic_data_ = [simulated_]

    for i in range(30):
        print(f"Iteration #{i+1}", flush=True)
        # Create a probin instance on the last simulated dataset
        print("\t Creating ProfileBin instance and training...", flush=True)
        _probin_i = (
            ProfileBin(synthetic_data_[-1])
            .fit(**training_kw)
            .simulation_fit(**training_kw)
        )
        probin_instances_.append(_probin_i)
        # save the criteria frame
        criteriae_.append(_probin_i.criteria)
        simulation_criteriae_.append(_probin_i.simulation_criteria)
        # binarise the expression frame
        print("\t Binarising data", flush=True)
        _binary_ = random_nan_binariser(
            _probin_i.py_binarize(n_threads=n_threads, alpha=alpha)
        )
        # create new synthetic data
        print("\t Create synthetic frame", flush=True)
        synthetic_data_.append(_probin_i.simulate(_binary_, n_threads=_n_threads))
        # avoid saturating the memory
        _probin_i.clear_r_envir()

        return criteriae_, simulation_criteriae_
