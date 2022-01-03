from packagetree import PackageTree

import pytest


def test_container():
    """Ensure a PackageTree has the expected structure."""
    container = PackageTree(
        module='TopLevelPackage', root=None, directory="tests",
    )

    assert 2 == len(container.classes)
    assert 1 == len(container.subpackages)
    assert "ClassA", "ClassAA" in container.classes.keys()
    assert "packageB" in container.subpackages.keys()
    assert "not_a_package" not in container.subpackages.keys()

    assert 1 == container.ClassA.a
    assert 2 == container.packageB.ClassB.b


def test_container_level_2():
    """Ensure nesting works at multiple levels."""
    container = PackageTree(
        module='TopLevelPackage', root=None, directory="tests",
    )

    assert "ClassBB", "ClassBB2" in container.packageB.packageBB.classes.keys()


def test_container_level_3():
    """Ensure nesting works at multiple levels."""
    container = PackageTree(
        module='TopLevelPackage', root=None, directory="tests",
    )

    keys = container.packageB.packageBB.packageBBB.classes.keys()
    assert "ClassBBB", "ClassBBB2" in keys


def test_container_level_4():
    """Ensure nesting works at multiple levels."""
    container = PackageTree(
        module='TopLevelPackage', root=None, directory="tests",
    )

    keys = container.packageB.packageBB.packageBBB.packageBBBB.classes.keys()
    assert "ClassBBBB", "ClassBBBB2" in keys


def test_multiple_containers():
    """Ensure that 2 PackageTree objects do not share any state."""
    container = PackageTree(
        module='TopLevelPackage', root=None, directory="tests",
    )

    assert 2 == len(container.classes)
    assert 1 == len(container.subpackages)
    assert "ClassA", "ClassAA" in container.classes.keys()
    assert "packageB" in container.subpackages.keys()
    assert "not_a_package" not in container.subpackages.keys()

    another_container = PackageTree(
        module='AnotherTopLevelPackage', root=None, directory="tests",
    )

    assert 2 == len(another_container.classes)
    assert 1 == len(another_container.subpackages)
    assert "ClassA", "ClassAA" in another_container.classes.keys()
    assert "packageB" in another_container.subpackages.keys()
    assert "not_a_package" not in another_container.subpackages.keys()

    container.ClassA.a = 15

    assert 1 == another_container.ClassA.a
    assert 15 == container.ClassA.a


def test_container_attribute_not_present():
    """Ensure a PackageTree raises an error when getting a non-existent attribute."""
    container = PackageTree(
        module='TopLevelPackage', root=None,
    )

    with pytest.raises(AttributeError) as e:
        container.foobar

    assert "foobar is not an imported Subpackage or Class." == str(e.value)


def test_from_subpackage():
    """Build the package tree from a package inside another."""
    container = PackageTree(
        module='packageB', root='TopLevelPackage', directory="tests",
    )

    assert 2 == len(container.classes)
    assert 1 == len(container.subpackages)


def test_from_subpackage_level_2():
    """Build the package tree from a package inside another."""
    container = PackageTree(
        module='packageBB', root='TopLevelPackage.packageB', directory="tests",
    )

    assert 2 == len(container.classes)
    assert 1 == len(container.subpackages)


def test_from_subpackage_level_3():
    """Build the package tree from a package inside another."""
    container = PackageTree(
        module='packageBBB',
        root='TopLevelPackage.packageB.packageBB',
        directory="tests",
    )

    assert 2 == len(container.classes)
    assert 1 == len(container.subpackages)
