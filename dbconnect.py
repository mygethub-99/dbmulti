# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:35:12 2019
SQL code for pulling data from DBs
@author: ow4253
"""
import cx_Oracle
import pyodbc
import pandas as pd


        
def axiomdb():
    #Connects to the Axiom DB
    conn = cx_Oracle.connect(user ='id', password="xxx", dsn="xcfdfd")
    #conn.setencoding(encoding='utf-8')
    q = ("select distinct start_date, eutran_cell_fdd_id, freqband, earfcndl,\
         dl_channel_bandwidth, administrative_state\
         from AXIOM.PMCM_ERIC_LTE_EUTRANCELL\
         where eutran_cell_fdd_id like 'ALL%'")
    axiom = pd.read_sql(q, conn)
    return axiom
    conn.close()
    
def iqiDB():
    #Connects to the IQI DB
    conn3 = pyodbc.connect(DSN="kjkjljkj", UID="id", PWD= "cxfgdf")
    q =("select yyyymm, most_used_ecgi_cellname mostCell,\
        most_used_ecgi_freq freqMostUd, avg_rsrp, avg_rsrq, rsrq_recs,\
        handsets_lte, rrc_attempted numrcc, rrc_failed rccFail,\
        rrc_reestab_attempted, rrc_reestab_failed, noservice_events NSNum,\
        noservice_duration NSDura, sw_long lat, sw_lat long, market\
        FROM IQI_SUMMARY.iqi_mgrs10m_monthly_summary WHERE yyyymm in\
        ('201906','201907') and sw_long >= (-86.524) and sw_long <= (-86.402)\
        and sw_lat >= (31.362) and sw_lat <= (31.422) GROUP BY yyyymm,\
        most_used_ecgi_cellname,avg_rsrp, avg_rsrq, rsrq_recs, handsets_lte,\
        rrc_attempted,rrc_failed, rrc_reestab_attempted, rrc_reestab_failed,\
        noservice_events, most_used_ecgi_freq, noservice_duration, market,\
        sw_lat, sw_long ORDER BY mostCell")
    iqi = pd.read_sql(q, conn3)
    return iqi
    conn3.close()
