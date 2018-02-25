package-tree
============

.. image:: https://travis-ci.org/jsfehler/package-tree.svg?branch=master
    :target: https://travis-ci.org/jsfehler/package-tree
    :alt: See Build Status on Travis CI
    
.. image:: https://coveralls.io/repos/github/jsfehler/package-tree/badge.svg?branch=master
    :target: https://coveralls.io/github/jsfehler/package-tree?branch=master

.. image:: https://api.codacy.com/project/badge/Grade/8798922189014521b67b1865ddc63a87
    :target: https://www.codacy.com/app/joshua-fehler_2/package-tree?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jsfehler/package-tree&amp;utm_campaign=Badge_Grade

Imports a package and sub-packages into a tree based Class structure.

Sub-packages become child PackageTree instances of the root PackageTree.

Classes in a package become attributes of the PackageTree.

    
Example:

.. code-block:: python

    RootPackage:
        packageA:
            - ClassA
            - ClassAB
            packageAA:
                - ClassAA
        packageB:
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

