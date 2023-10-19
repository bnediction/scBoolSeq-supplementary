"""

"""
import typing
import itertools

import pandas as pd


def positive_markers(marker_names: typing.Iterable[str]) -> typing.Dict[str, int]:
    """Generate the dict of positive markers"""
    return {name: 1 for name in marker_names}


## name, t-SNE clusters in the original article, other comments
states_and_markers = {
    ### Progenitors
    "RPC": {"Sox2", "Fos", "Hes1"},  # Retinal Progenitor Cells, 0-3 'central'
    ### Neuroblast bottleneck
    "NB1": {  # Neuroblast 1, 4 'narrower',
        "Top2a",
        "Prc1",  # cell cycle exit genes
        "Sstr2",
        "Penk",
        "Btg2",  # Neuronal-specific genes, latter known inducer of neuronal diff.
    },
    "NB2": {  # Neuroblast 2, 5
        "Neurod4",
        "Pax6",  # early neuroblast TF
        "Pcdh17",  # Axonal growth
    },
    ### Branch 1 (clusters 9-12)
    "RGC": {"Isl1", "Pou4f2", "Pou6f2", "Elavl4"},  # Retinal Ganglion Cells
    ### Branch 2 'second neuronal group' (clusters 7-8)
    "AC": {"Onecut2", "Prox1"},  # Amacrine cells, in the root (7)
    "HC": {"Onecut1", "Prox1"},  # Horizontal Cells, at the extremity (8)
    ### Branch 3 (cluster 6)
    "Cones": {
        "Otx2",
        "Crx",
        "Thrb",  # Early marker
        "Rbp4",  # Confirmed using mice expressing Cre (under the control of Rbp4 promoter)
    },
    ### Smallest cluster 2.9% of cells (undetermined):
    ## This is expressing some mitochondrial genes and lacking Rps/Rpl genes
    #
}

marker_genes: pd.Series = pd.Series(
    list(set(itertools.chain.from_iterable(states_and_markers.values())))
)
