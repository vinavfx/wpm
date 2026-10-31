"""
Difficulty scores for the built-in database.

Distributed under the GNU Affero General Public License (AGPL) v3 or later. See
the file LICENSE.txt for the full license text. This software makes use of open
source software.

The quotes database is *not* covered by the AGPL!
"""

import gzip
import os
import pickle

from wpm.quotes import DATA_DIR


class Difficulty(object):
    """Loads difficulty scores."""

    @staticmethod
    def filename():
        """Returns the filename of the packaged difficulty database."""
        return os.path.join(DATA_DIR, "difficulty.pickle.gz")

    @staticmethod
    def normalize(diffs):
        """Normalizes difficulty scores to 0.0-1.0 where 1.0 is hardest."""
        low = min(diffs.values())
        delta = max(diffs.values()) - low
        out = {}

        for text_id, score in diffs.items():
            out[text_id] = 1.0 - (float(score - low) / delta)

        return out

    @staticmethod
    def load():
        """Loads the dictionary that maps text_id to difficulty scores.

        The difficulty scores are normalized and goes from 0.0 (easy) to 1.0
        (hard).
        """
        filename = Difficulty.filename()
        with gzip.open(filename, "rb") as file_obj:
            return Difficulty.normalize(pickle.load(file_obj))
