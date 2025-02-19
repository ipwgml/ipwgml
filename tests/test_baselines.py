"""
Tests for the ipwgml.baselines module.
"""

from ipwgml.baselines import load_baseline_results


def test_load_baseline_results():
    """
    Test that loading of baseline results works as expected.
    """
    results = load_baseline_results("gmi")
    assert "IMERG Final V7 (GMI)" in results.algorithm
    assert "GPROF V7 (GMI)" in results.algorithm

    results_austria = load_baseline_results("gmi", domain="austria")
    assert results["bias"].data[0] != results_austria["bias"].data[0]
    assert "IMERG Final V7 (GMI)" in results_austria.algorithm
    assert "GPROF V7 (GMI)" in results_austria.algorithm

    results = load_baseline_results("gmi", baselines=["imerg_final_v07b_gmi"])
    assert "IMERG Final V7 (GMI)" in results.algorithm
    assert "GPROF V7 (GMI)" not in results.algorithm

    results = load_baseline_results("gmi", baselines=["gprof_v07a_gmi"])
    assert "IMERG Final V7 (GMI)" not in results.algorithm
    assert "GPROF V7 (GMI)" in results.algorithm
