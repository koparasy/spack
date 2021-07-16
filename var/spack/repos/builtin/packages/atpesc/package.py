# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import sys

from spack import *


class Atpesc(BundlePackage):
    """ATPESC packag install - derived from xSDK
    """

    homepage = "http://xsdk.info"

    maintainers = ['balay']

    version('2021')

    with when('@2021'):
        depends_on('amrex@21.07+plotfile_tools dimensions=2') # 2d for sundials vs 3d for amrex
        depends_on('mfem@develop+mpi+superlu-dist+examples+miniapps')
        #depends_on('pumi@master')
        #depends_on('hypre@develop+superlu-dist+shared')
        #depends_on('trilinos@develop+muelu+cuda+wrapper+hypre+superlu-dist+hdf5~mumps~suite-sparse+tpetra+nox+ifpack2+amesos2~exodus~dtk+intrepid2+shards+stratimikos gotype=int cxxstd=14 cuda_arch=37')
        depends_on('superlu-dist@develop+cuda+openmp cuda_arch=37')
        depends_on('strumpack@master~slate~openmp+cuda cuda_arch=37')
        depends_on('petsc@3.15.2+mpi+hypre+superlu-dist+metis+hdf5+mumps+double~int64+cuda cuda_arch=37')
        depends_on('sundials@5.7.0~int64+cuda cuda_arch=37') #+hypre+petsc+superlu-dist
