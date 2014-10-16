# -*- coding: utf-8 -*-

# import xlutils # Not yet needed.
import xlrd
import xlwt
# import yaml
import json
import hashlib
# import redis
import codecs
import sys


# print yaml.dump(cells, default_flow_style=False)
# print cells[0]


def sheets(file_):
    book = xlrd.open_workbook(file_)
    sheets = [ book.sheet_by_index(i) for i in range(book.nsheets) ]
    return sheets

def cell_values(sheet):
    '''
    Given a sheet object, extract values from every cell of every row
    in a form of a list of lists.
    '''
    rows = [ sheet.row(i) for i in range(sheet.nrows) ]
    cells = [ [ cell.value for cell in row ] for row in rows ]
    return cells
def metadata(sheet):
    '''
    Given a sheet object, compose a metadata dictionary.
    Keys:
        - dimensions:
            - ncols
            - nrows
    '''
    return {
        'dimensions': [sheet.ncols, sheet.nrows]
    }


def identity_hash(object_):
    '''
    Generate sha1 hash of an object.
    '''
    ret = hashlib.sha1()
    ret.update(bytearray(object_))
    return ret

def select_rows(table, columns):
    '''
    A table is a two-dimensional rectangular discrete space of values.
    We would like to select only specified columns.
    '''
    return [ [ row[column] for column in columns ] for row in table ]

def serialize(object_):
    return ( json.dumps ( object_, ensure_ascii=False, indent=4 ) )

def serial_write(object_, filename):
    codecs.open (filename, 'w', 'utf8') . write(serialize(object_))

def lift(sheet):
    return serialize (
        {
            'metadata': metadata(sheet)
            , 'cell_values': cell_values(sheet)
        }
    ).encode('utf-8')


def main():
    return lift( sheets('refmart.xlsx') [0] )

if __name__ == '__main__':
    print main()
