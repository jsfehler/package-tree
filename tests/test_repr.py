from packagetree import PackageTree


def test_repr():
    """Test the string formatting of .__repr__()."""
    container = PackageTree(
        module='TopLevelPackage', root=None, directory="tests",
    )

    expected = ("PackageTree(module=TopLevelPackage, "
                "root=None, directory=tests/TopLevelPackage)")
    assert str(container) == expected
