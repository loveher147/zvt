# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import EtfKdataCommon

KdataBase = declarative_base()


class Etf1dKdata(KdataBase, EtfKdataCommon):
    __tablename__ = 'etf_1d_kdata'


register_schema(providers=['sina'], db_name='etf_1d_kdata', schema_base=KdataBase)

__all__ = ['Etf1dKdata']
# the __all__ is generated
__all__ = ['Etf1dKdata']