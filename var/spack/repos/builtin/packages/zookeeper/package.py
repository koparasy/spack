# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Zookeeper(Package):
    """
    Apache ZooKeeper is an effort to develop and maintain an open-source
    server which enables highly reliable distributed coordination.
    """

    homepage = "https://archive.apache.org"
    url = "https://archive.apache.org/dist/zookeeper/zookeeper-3.4.11/zookeeper-3.4.11.tar.gz"

    license("Apache-2.0")

    version("3.4.11", sha256="f6bd68a1c8f7c13ea4c2c99f13082d0d71ac464ffaf3bf7a365879ab6ad10e84")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    def install(self, spec, prefix):
        install_tree(".", prefix)
