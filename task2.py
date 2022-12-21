#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 Alberto Pérez García-Plaza
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Alberto Pérez García-Plaza <alberto.perez@lsi.uned.es>
#

import json

from armin.evaluation import NLI4CTEvaluator
from armin.extractors import Baseline, OntobioSim

DATASET_PATH = "./training_data/dev.json"
RESULTS_PATH = "./results/results.json"


if __name__ == '__main__':

    baseline = Baseline(DATASET_PATH, "./training_data/CT json")

    evidences = baseline.retrieve_evidences()
    print(evidences)
    print("Writing results to " + RESULTS_PATH)
    with open(RESULTS_PATH, 'w') as jsonFile:
        jsonFile.write(json.dumps(evidences, indent=4))

    # Evaluate results
    evaluator = NLI4CTEvaluator(DATASET_PATH)
    metrics = evaluator.evaluate(RESULTS_PATH)

    print('BM25 F1:{:f}'.format(metrics["f1"]))
    print('BM25 precision_score:{:f}'.format(metrics["precision"]))
    print('BM25 recall_score:{:f}'.format(metrics["recall"]))

    ob_sim = OntobioSim(DATASET_PATH, "./training_data/CT json")
    evidences = ob_sim.retrieve_evidences()
    metrics = evaluator.evaluate(RESULTS_PATH)
    print(evidences)
    print("Writing results to " + RESULTS_PATH)
    with open(RESULTS_PATH, 'w') as jsonFile:
        jsonFile.write(json.dumps(evidences, indent=4))

    print('Ontobio F1:{:f}'.format(metrics["f1"]))
    print('Ontobio precision_score:{:f}'.format(metrics["precision"]))
    print('Ontobio recall_score:{:f}'.format(metrics["recall"]))

