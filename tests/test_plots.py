# BSD 3-Clause License
#
# Copyright (c) 2019, Rene Jean Corneille
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest

from seaborn_qqplot.plots import (
    _Plot,
    PPPlot,
    QQPlot,
    ProbabilityPlot,
    QuantilePlot
)


class TestEmptyPlot(unittest.TestCase):


    def setUp(self):        
       self.empty_plot = _Plot()

    def test_empty_plot(self):
        self.assertEqual(self.empty_plot.plot_kws, {})


    def test_empy_variables(self):
        self.assertEqual(self.empty_plot.identity, False)
        self.assertEqual(self.empty_plot.fit, False)
        self.assertEqual(self.empty_plot.reg, False)
        self.assertEqual(self.empty_plot.ci, 0.05)


class TestPPPlot(unittest.TestCase):


    def setUp(self):        
        
       self. empty_plot = PPPlot()

    def test_empty_plot(self):
        self.assertEqual(self.empty_plot.plot_kws, {})


    def test_empy_variables(self):
        self.assertEqual(self.empty_plot.identity, False)
        self.assertEqual(self.empty_plot.fit, False)
        self.assertEqual(self.empty_plot.reg, False)
        self.assertEqual(self.empty_plot.ci, 0.05)
