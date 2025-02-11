""" visitor.py """

from arpeggio import PTNodeVisitor
from collections import namedtuple

SIPopulation = namedtuple('SIPopulation_a', 'scenario instances')
"""All data from scenario instance parse"""

class ScenarioVisitor(PTNodeVisitor):

    # Root
    @classmethod
    def visit_si_population(cls, node, children):
        """
        EOL* scenario class_pop* EOF
        """
        # scenario = children.results['scenario'][0]  # Required by si parser
        # instances = children.results.get('instances', [])  # Optional section
        # return SI_population(
        #     subsystem=subsys_name, domain=domain_name,
        #     classes=class_data, rels=rel_data if not rel_data else rel_data[0],
        #     instances=None if not instances else instances
        # )
        pass

    @classmethod
    def visit_scenario(cls, node, children):
        """ scenario_name block_end """
        pass
        # items = {k: v for c in children for k, v in c.items()}
        # return items

    @classmethod
    def visit_class_pop(cls, node, children):
        """ class_name class_attrs block_end """
        # name = ''.join(children)
        # return {'name': name }
        pass

    @classmethod
    def visit_class_attrs(cls, node, children):
        """ col_name (' | ' col_name)* block_end """
        # return { 'alias': children[0] }
        pass

    @classmethod
    def visit_col_name(cls, node, children):
        """ col_name (' | ' col_name)* block_end """
        # items = {k: v for d in children for k, v in d.items()}
        # return items
        pass

    @classmethod
    def visit_rnum_list(cls, node, children):
        """ rnum (', ' rnum)* """
        # items = {k: v for d in children for k, v in d.items()}
        # return items
        pass

    @classmethod
    def visit_instance_block(cls, node, children):
        """ row* block_end """
        # name = ''.join(children)
        # return {'name': name }
        pass

    @classmethod
    def visit_row(cls, node, children):
        """ row_value (', ' row_value)* """
        # name = ''.join(children)
        # return {'name': name }
        pass

    @classmethod
    def visit_icaps_name(cls, node, children):
        """
        word (delim word)*
        """
        name = ''.join(children)
        return name

    @classmethod
    def visit_EOL(cls, node, children):
        """
        SP* COMMENT? '\n'

        end of line: Spaces, Comments, blank lines, whitespace we can omit from the parser result
        """
        return None

    @classmethod
    def visit_SP(cls, node, children):
        """ ' '  Single space character (SP) """
        return None
