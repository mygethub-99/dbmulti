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
    conn = cx_Oracle.connect(user ='OW4253', password="Breakslowmen6060", dsn="p1c2d831")
    #conn.setencoding(encoding='utf-8')
    q = ("select distinct start_date, eutran_cell_fdd_id, freqband, earfcndl,\
         dl_channel_bandwidth, administrative_state\
         from AXIOM.PMCM_ERIC_LTE_EUTRANCELL\
         where eutran_cell_fdd_id like 'ALL%'")
    axiom = pd.read_sql(q, conn)
    return axiom
    conn.close()

def iqiDB(l1,mon):
    #q=[]
    #Connects to the IQI DB
#l1 =["-87.569122","33.162369","-87.509122","33.222369"]
#mon = ['201907','201908']
    conn3 = pyodbc.connect(DSN="SRVVERTICA", UID="OW4253", PWD= "Breakfoodall6060")
    
    q1= "select yyyymm, most_used_ecgi_cellname mostCell,\
        most_used_ecgi_freq freqMostUd, avg_rsrp, avg_rsrq, rsrq_recs,\
        handsets_lte, rrc_attempted numrcc, rrc_failed rccFail,\
        rrc_reestab_attempted, rrc_reestab_failed, noservice_events NSNum,\
        noservice_duration NSDura, sw_long long, sw_lat lat, market "
    q1 += "FROM IQI_SUMMARY.iqi_mgrs10m_monthly_summary WHERE yyyymm in\
        ('201908')"
    q1 += "and sw_long >= (%s) and sw_long <= (%s)\
        and sw_lat >= (%s) and sw_lat <= (%s)" % (l1[0],l1[2],l1[1],l1[3])
    q1 += "GROUP BY yyyymm, most_used_ecgi_cellname,avg_rsrp, avg_rsrq,\
        rsrq_recs, handsets_lte, rrc_attempted,rrc_failed, rrc_reestab_attempted, \
        rrc_reestab_failed, noservice_events, most_used_ecgi_freq,\
        noservice_duration, market, sw_lat, sw_long ORDER BY mostCell"
    
    
    iqi = pd.read_sql(q1, conn3)
    return iqi
    conn3.close()
