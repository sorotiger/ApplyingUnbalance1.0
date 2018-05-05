"""
测试文件

"""

from factors.StockPool import StockPool
from factors.FactorPreprocess import FactorProcess
from factors.FactorsZoo import FactorsZoo
from pandas import DataFrame
from factors.FactorPreprocess import FactorProcess


def run():

    date1 = '2018-05-02'
    date = '2017-12-01'
    stock = StockPool(date1).select_stock()
    df = DataFrame()
    df['cash_net_oper_act'] = FactorsZoo.CashNetOperAct(date, stock, label='cash_net_oper_act').get_data()
    df['deductedprofit'] = FactorsZoo.DeductedProfit(date, stock, 'deductedprofit').get_data()
    df['dividend'] = FactorsZoo.Dividend(date, stock, 'dividend').get_data()
    df['industry'] = FactorsZoo.Industry(date, stock, 'industry').get_data()
    df['net_inc'] = FactorsZoo.NetInc(date, stock, 'net_inc').get_data()
    df['pct'] = FactorsZoo.Pct(date, stock, 'pct', -6).get_data()
    df['pe'] = FactorsZoo.Pe(date, stock, 'pe').get_data()
    df['size'] = FactorsZoo.Size(date, stock, 'size').get_data()
    df['turn_per'] = FactorsZoo.TurnPer(date, stock, 'turn_per', -6).get_data()
    df['volitality']  = FactorsZoo.Volitality(date, stock, 'volitality', -6).get_data()
    df['vol_per'] = FactorsZoo.VolPer(date, stock, 'vol_per', -6).get_data()
    df['yoyprofit'] = FactorsZoo.Yoyprofit(date, stock, 'yoyprofit').get_data()
    df['yoytr'] = FactorsZoo.YoyTr(date, stock, 'yoytr').get_data()
    # 因子中性化
    factors = df.columns.tolist()
    df['Codes'] = stock
    df = df.dropna()
    stock = df['Codes'].values.tolist()
    df = df[factors]
    fp = FactorProcess()
    df = fp.neutralize_factor(df, factors)
    alpha = fp.get_alpha(stock, date, -6)
    df['alpha'] = alpha
    coef_ = fp.calac_beta(df['alpha'], df[factors], factors)
    df1 = DataFrame()

    df1['cash_net_oper_act'] = FactorsZoo.CashNetOperAct(date1, stock, label='cash_net_oper_act').get_data()
    df1['deductedprofit'] = FactorsZoo.DeductedProfit(date1, stock, 'deductedprofit').get_data()
    df1['dividend'] = FactorsZoo.Dividend(date1, stock, 'dividend').get_data()
    df1['industry'] = FactorsZoo.Industry(date1, stock, 'industry').get_data()
    df1['net_inc'] = FactorsZoo.NetInc(date1, stock, 'net_inc').get_data()
    df1['pct'] = FactorsZoo.Pct(date1, stock, 'pct', -6).get_data()
    df1['pe'] = FactorsZoo.Pe(date1, stock, 'pe').get_data()
    df1['size'] = FactorsZoo.Size(date1, stock, 'size').get_data()
    df1['turn_per'] = FactorsZoo.TurnPer(date1, stock, 'turn_per', -6).get_data()
    df1['volitality'] = FactorsZoo.Volitality(date1, stock, 'volitality', -6).get_data()
    df1['vol_per'] = FactorsZoo.VolPer(date1, stock, 'vol_per', -6).get_data()
    df1['yoyprofit'] = FactorsZoo.Yoyprofit(date1, stock, 'yoyprofit').get_data()
    df1['yoytr'] = FactorsZoo.YoyTr(date1, stock, 'yoytr').get_data()
    factors = df1.columns.tolist()
    df1['Codes'] = stock
    df1 = df1.dropna()
    stock = df1['Codes'].values.tolist()
    df1 = df1[factors]
    df1 = fp.neutralize_factor(df1, factors)
    alpha = fp.forcast_alpha(coef_, df1, factors)

    df1['Codes'] = stock
    df1['alpha'] = alpha
    df1 = df1
    df1.to_csv("test.csv", encoding='gbk')







if __name__ == '__main__':
    run()
