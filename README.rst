package-tree
============

.. image:: https://github.com/jsfehler/stere/workflows/CI/badge.svg
    :target: https://github.com/jsfehler/package-tree/actions/workflows/main.yml
    :alt: Build status

.. image:: https://coveralls.io/repos/github/jsfehler/package-tree/badge.svg?branch=master
    :target: https://coveralls.io/github/jsfehler/package-tree?branch=master

Imports a package and sub-packages into a tree based Class structure.

Sub-packages become child PackageTree instances of the root PackageTree.

Classes in a package become attributes of the PackageTree.

The package must be available on the python path and able to be imported.

Example:

.. code-block:: python

    RootPackage:
        packageA:
            moduleA.py
                - ClassA
                - ClassAB
            packageAA:
                moduleAA.py
                    - ClassAA
        packageB:
            moduleB.py
                - ClassB
                - ClassBC

Will become:

.. code-block:: python

    root = PackageTree(module="RootPackage")

    root.packageA
    root.packageB

    root.packageA.ClassA
    root.packageA.ClassAB
    root.packageA.packageAA.ClassAA

    root.packageB.ClassB
    root.packageB.ClassBC
