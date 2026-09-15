Installation
============

MoveAtlas targets Python 3.9+.

Local (current, pre-release):

.. code-block:: bash

   git clone <repository>
   pip install -e .

The package will be published on PyPI at the public launch:

.. code-block:: bash

   pip install moveatlas   # after launch

Data location: the hosted tier currently reads MoveAtlas's local record
store; set ``MOVEATLAS_REPO`` to the repository root if you install the
package outside it.
