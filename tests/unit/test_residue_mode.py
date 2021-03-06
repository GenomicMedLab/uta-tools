"""Module for testing residue mode"""
from uta_tools.data_sources.residue_mode import get_inter_residue_pos


def test_get_inter_residue_pos():
    """Test that get_inter_residue_pos method works correctly"""
    expected = ((599, 599), None)
    resp = get_inter_residue_pos(600, "residue")
    assert resp == expected

    resp = get_inter_residue_pos(600, "residue", end_pos=600)
    assert resp == expected

    resp = get_inter_residue_pos(599, "inter-residue")
    assert resp == expected

    resp = get_inter_residue_pos(599, "inter-residue", end_pos=599)
    assert resp == expected

    resp = get_inter_residue_pos(600, "test")
    assert resp == (None, "residue_mode must be either `residue` "
                          "or `inter-residue`, not `test`")
