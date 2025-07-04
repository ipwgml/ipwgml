import pytest

from ipwgml.data import (
    enable_testing,
    download_missing,
    download_dataset
)


enable_testing()


@pytest.fixture(scope="session")
def spr_gmi_gridded_train(tmp_path_factory):
    """
    Fixture to download satellite-precipitation retrieval benchmark data for GMI with
    gridded geometry.
    """
    dest = tmp_path_factory.mktemp("ipwgml")
    for source in ["gmi", "target", "geo_ir", "geo", "ancillary"]:
        download_missing(
            dataset_name="spr",
            reference_sensor="gmi",
            geometry="gridded",
            split="training",
            source=source,
            destination=dest
        )
    return dest


@pytest.fixture(scope="session")
def spr_gmi_on_swath_train(tmp_path_factory):
    """
    Fixture to download satellite-precipitation retrieval benchmark data for GMI with
    on_swath geometry.
    """
    dest = tmp_path_factory.mktemp("ipwgml")
    for source in ["gmi", "target", "geo_ir", "geo", "ancillary"]:
        download_missing(
            dataset_name="spr",
            reference_sensor="gmi",
            geometry="on_swath",
            split="training",
            source=source,
            destination=dest
        )
    return dest


@pytest.fixture(scope="session")
def spr_gmi_on_swath_train_dataset(tmp_path_factory):
    """
    Fixture to download satellite-precipitation retrieval benchmark data for GMI with
    on_swath geometry.
    """
    return download_dataset(
        "spr",
        "gmi",
        ["gmi"],
        split="training",
        geometry="on_swath",
    )


@pytest.fixture(scope="session")
def spr_gmi_evaluation(tmp_path_factory):
    """
    Fixture to download satellite-precipitation retrieval evaluation data for GMI.
    """
    dest = tmp_path_factory.mktemp("ipwgml")
    for source in ["gmi", "target", "geo_ir", "geo", "ancillary"]:
        for geometry in ["gridded", "on_swath"]:
            download_missing(
                dataset_name="spr",
                reference_sensor="gmi",
                geometry=geometry,
                split="evaluation",
                domain="conus",
                source=source,
                destination=dest
            )
    return dest
