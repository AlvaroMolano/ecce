import simplejson
import os
import pandas as pd

import ecce.nave as nave
from ecce.constants import *


def export_nave(args):
    print(f'Writing to {NAVE_EXPORT_REF}')
    if os.path.isfile(NAVE_EXPORT_REF) is False:
        with open(NAVE_EXPORT_REF, 'w') as f:
            simplejson.dump(nave.by_reference(), f, ignore_nan=True)

    print(f'Writing to {NAVE_EXPORT_TOPIC}')
    if os.path.isfile(NAVE_EXPORT_TOPIC) is False:
        with open(NAVE_EXPORT_TOPIC, 'w') as f:
            simplejson.dump(nave.by_topic(), f, ignore_nan=True)

    print(f'Writing to {NAVE_SUBTOPIC_NODES}')
    subtopic_nodes = nave.by_subtopic_nodes()
    if os.path.isfile(NAVE_SUBTOPIC_NODES) is False:
        columns = list(remove(lambda k: k == 'passages', subtopic_nodes.columns))
        (subtopic_nodes[columns].to_csv(
            NAVE_SUBTOPIC_NODES, sep='\t', index=False))

    print(f'Writing to {NAVE_EXPORT_PASSAGES}')
    subtopic_to_passages = dict(subtopic_nodes.apply(
        lambda r: (r.at['id'], r.at['passages']), axis=1).tolist())
    if os.path.isfile(NAVE_EXPORT_PASSAGES) is False:
        with open(NAVE_EXPORT_PASSAGES, 'w') as f:
            simplejson.dump(subtopic_to_passages, f, ignore_nan=True)

    print(f'Writing to {NAVE_CATEGORY_NODES}')
    if os.path.isfile(NAVE_CATEGORY_NODES) is False:
        (nave.by_category_nodes().to_csv(
            NAVE_CATEGORY_NODES, sep='\t', index=False))

    print(f'Writing to {NAVE_TOPIC_NODES}')
    if os.path.isfile(NAVE_TOPIC_NODES) is False:
        (nave.by_topic_nodes().to_csv(
            NAVE_TOPIC_NODES, sep='\t', index=False))

