from packagetree import PackageTree


def test_get_full_directory():
    """Ensure _get_full_directory combines the module, root, and directory
    correctly."""
    x = PackageTree._get_full_directory(
        None,
        module="zab",
        root=None,
        directory="foo/bar/biz/bin/bat",
    )

    assert "foo/bar/biz/bin/bat/zab" == x


def test_get_full_directory_nested_module():
    """Ensure _get_full_directory combines the module, root, and directory
    correctly."""
    x = PackageTree._get_full_directory(
        None,
        module="zab.zim",
        root=None,
        directory="foo/bar/biz/bin/bat",
    )

    assert "foo/bar/biz/bin/bat/zab/zim" == x
