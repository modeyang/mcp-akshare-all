#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
AKShare MCP Server

这是一个基于AKShare的股票数据MCP服务器，使用FastMCP框架构建。
它提供了对中国股票市场数据的访问，通过MCP协议暴露AKShare的API。
"""

import akshare as ak
import pandas
from fastmcp import FastMCP
import datetime

MAX_DATA_ROW = 50

# 创建MCP服务器实例
mcp = FastMCP("AKShare股票期货数据服务", dependencies=["akshare>=1.16.76"])
# 工具函数：获取当前时间
@mcp.tool()
def get_current_time() -> dict:
    """获取当前时间
    
    获取当前时间数据
    
    Returns:
        dict: 包含当前时间的字典
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}

# 工具函数：股票交易日历查询
@mcp.tool()
def stock_trade_date_hist() -> dict:
    """获取股票交易日历数据
    
    数据来源: 新浪财经-交易日历
    网址: https://finance.sina.com.cn/
    
    Returns:
        dict: 包含股票交易日历数据的字典，包括从1990-12-19到当前的所有交易日期
    """
    result = ak.tool_trade_date_hist_sina()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：上海证券交易所股票数据总貌
@mcp.tool()
def stock_sse_summary() -> dict:
    """获取上海证券交易所-股票数据总貌
    
    数据来源: 上海证券交易所-市场数据-股票数据总貌
    网址: http://www.sse.com.cn/market/stockdata/statistic/
    
    Returns:
        dict: 包含上海证券交易所股票数据总貌的字典
    """
    result = ak.stock_sse_summary()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]

    return result.to_dict(orient="records")
# 工具函数：深圳证券交易所证券类别统计
@mcp.tool()
def stock_szse_summary(date: str) -> dict:
    """获取深圳证券交易所-市场总貌-证券类别统计
    
    数据来源: 深圳证券交易所-市场总貌
    网址: http://www.szse.cn/market/overview/index.html
    
    Args:
        date: 统计日期，格式为YYYYMMDD，如"20200619"
        
    Returns:
        dict: 包含证券类别统计数据的字典，包括数量、成交金额、总市值和流通市值
    """
    result = ak.stock_szse_summary(date=date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：深圳证券交易所地区交易排序
@mcp.tool()
def stock_szse_area_summary(date: str) -> dict:
    """获取深圳证券交易所-市场总貌-地区交易排序
    
    数据来源: 深圳证券交易所-市场总貌
    网址: http://www.szse.cn/market/overview/index.html
    
    Args:
        date: 统计年月，格式为YYYYMM，如"202203"
        
    Returns:
        dict: 包含地区交易排序数据的字典，包括序号、地区、各类交易额及占比
    """
    result = ak.stock_szse_area_summary(date=date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：深圳证券交易所股票行业成交数据
@mcp.tool()
def stock_szse_sector_summary(symbol: str, date: str) -> dict:
    """获取深圳证券交易所-统计资料-股票行业成交数据
    
    数据来源: 深圳证券交易所-统计资料
    网址: http://docs.static.szse.cn/www/market/periodical/month/W020220511355248518608.html
    
    Args:
        symbol: 统计周期，可选值: "当月" 或 "当年"
        date: 统计年月，格式为YYYYMM，如"202501"
        
    Returns:
        dict: 包含股票行业成交数据的字典，包括交易天数、成交金额、成交股数、成交笔数等
    """
    result = ak.stock_szse_sector_summary(symbol=symbol, date=date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：风险警示板股票行情
@mcp.tool()
def stock_zh_a_st_em() -> dict:
    """获取风险警示板股票行情数据
    
    数据来源: 东方财富网-行情中心-沪深个股-风险警示板
    网址: https://quote.eastmoney.com/center/gridlist.html#st_board
    
    Returns:
        dict: 包含风险警示板股票行情数据的字典，包括代码、名称、最新价、涨跌幅等完整行情指标
    """
    result = ak.stock_zh_a_st_em()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：新股行情数据
@mcp.tool()
def stock_zh_a_new_em() -> dict:
    """获取新股板块股票行情数据
    
    数据来源: 东方财富网-行情中心-沪深个股-新股
    网址: https://quote.eastmoney.com/center/gridlist.html#newshares
    
    Returns:
        dict: 包含新股板块股票行情数据的字典，包括代码、名称、最新价、涨跌幅等完整行情指标
    """
    result = ak.stock_zh_a_new_em()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：新股上市首日数据
@mcp.tool()
def stock_xgsr_ths() -> dict:
    """获取新股上市首日数据
    
    数据来源: 同花顺-数据中心-新股数据-新股上市首日
    网址: https://data.10jqka.com.cn/ipo/xgsr/
    
    Returns:
        dict: 包含新股上市首日数据的字典，包括发行价、首日价格表现、涨跌幅及破发情况
    """
    result = ak.stock_xgsr_ths()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：科创板股票历史行情数据
@mcp.tool()
def stock_zh_kcb_daily(symbol: str, adjust: str = "") -> dict:
    """获取科创板股票历史行情数据
    
    数据来源: 新浪财经-科创板股票
    示例网址: https://finance.sina.com.cn/realstock/company/sh688001/nc.shtml
    
    Args:
        symbol: 带市场标识的股票代码，如"sh688008"
        adjust: 复权类型，可选值: 
               ""(默认): 不复权
               "qfq": 前复权
               "hfq": 后复权
               "hfq-factor": 后复权因子
               "qfq-factor": 前复权因子
        
    Returns:
        dict: 包含科创板股票历史行情数据的字典，包括日期、价格、成交量等
    """
    result = ak.stock_zh_kcb_daily(symbol=symbol, adjust=adjust)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：A+H股历史行情数据
@mcp.tool()
def stock_zh_ah_daily(symbol: str, start_year: str, end_year: str, adjust: str = "") -> dict:
    """获取A+H股历史行情数据
    
    数据来源: 腾讯财经-A+H股数据
    示例网址: https://gu.qq.com/hk02359/gp
    
    Args:
        symbol: 港股股票代码，如"02318"(可通过ak.stock_zh_ah_name()获取)
        start_year: 开始年份，如"2000"
        end_year: 结束年份，如"2019"
        adjust: 复权类型，可选值: 
               ""(默认): 不复权
               "qfq": 前复权
               "hfq": 后复权
        
    Returns:
        dict: 包含A+H股历史行情数据的字典，包括日期、价格、成交量等
    """
    result = ak.stock_zh_ah_daily(symbol=symbol, start_year=start_year, end_year=end_year, adjust=adjust)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：美股历史行情数据
@mcp.tool()
def stock_us_hist(symbol: str, period: str = "daily", start_date: str = "", end_date: str = "", adjust: str = "") -> dict:
    """获取美股历史行情数据
    
    数据来源: 东方财富网-美股
    示例网址: https://quote.eastmoney.com/us/ENTX.html#fullScreenChart
    
    Args:
        symbol: 美股代码(可通过ak.stock_us_spot_em()获取)
        period: 时间周期，可选值: 'daily'(日线), 'weekly'(周线), 'monthly'(月线)
        start_date: 开始日期，格式为YYYYMMDD，如"20210101"
        end_date: 结束日期，格式为YYYYMMDD，如"20210601"
        adjust: 复权类型，可选值: 
               ""(默认): 不复权
               "qfq": 前复权
               "hfq": 后复权
        
    Returns:
        dict: 包含美股历史行情数据的字典，包括日期、价格、成交量等
    """
    result = ak.stock_us_hist(symbol=symbol, period=period, start_date=start_date, end_date=end_date, adjust=adjust)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：美股分时行情数据
@mcp.tool()
def stock_us_hist_min_em(symbol: str, start_date: str = "1979-09-01 09:32:00", end_date: str = "2222-01-01 09:32:00") -> dict:
    """获取美股分时行情数据
    
    数据来源: 东方财富网-美股分时行情
    示例网址: https://quote.eastmoney.com/us/ATER.html
    
    Args:
        symbol: 美股代码(可通过ak.stock_us_spot_em()获取)，如"105.ATER"
        start_date: 开始日期时间，格式为"YYYY-MM-DD HH:MM:SS"，默认"1979-09-01 09:32:00"
        end_date: 结束日期时间，格式为"YYYY-MM-DD HH:MM:SS"，默认"2222-01-01 09:32:00"
        
    Returns:
        dict: 包含美股分时行情数据的字典，包括时间、价格、成交量等
    """
    result = ak.stock_us_hist_min_em(symbol=symbol, start_date=start_date, end_date=end_date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：A股分时行情数据
@mcp.tool()
def stock_bid_ask_em(symbol: str) -> dict:
    """获取A股分时行情数据
    
    数据来源: 东方财富-股票行情报价
    示例网址: https://quote.eastmoney.com/sz000001.html
    
    Args:
        symbol: 股票代码，如"000001"
        
    Returns:
        dict: 包含股票行情报价数据的字典，包括买卖盘口等详细信息
    """
    result = ak.stock_bid_ask_em(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")
# 工具函数：港股分时行情数据
@mcp.tool()
def stock_hk_hist_min_em(symbol: str, period: str = "5", adjust: str = "", 
                        start_date: str = "1979-09-01 09:32:00", 
                        end_date: str = "2222-01-01 09:32:00") -> dict:
    """获取港股分时行情数据
    
    数据来源: 东方财富网-港股分时行情
    示例网址: http://quote.eastmoney.com/hk/00948.html
    
    Args:
        symbol: 港股代码(可通过ak.stock_hk_spot_em()获取)，如"01611"
        period: 时间周期，可选值: '1'(1分钟), '5'(5分钟), '15'(15分钟), '30'(30分钟), '60'(60分钟)
        adjust: 复权类型，可选值: 
               ""(默认): 不复权
               "qfq": 前复权
               "hfq": 后复权
        start_date: 开始日期时间，格式为"YYYY-MM-DD HH:MM:SS"，默认"1979-09-01 09:32:00"
        end_date: 结束日期时间，格式为"YYYY-MM-DD HH:MM:SS"，默认"2222-01-01 09:32:00"
        
    Returns:
        dict: 包含港股分时行情数据的字典，包括时间、价格、成交量等
    """
    result = ak.stock_hk_hist_min_em(symbol=symbol, period=period, adjust=adjust,
                                   start_date=start_date, end_date=end_date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：上市公司主营构成
@mcp.tool()
def stock_zygc_em(symbol: str) -> dict:
    """获取上市公司主营构成数据
    
    数据来源: 东方财富网-个股-主营构成
    示例网址: https://emweb.securities.eastmoney.com/PC_HSF10/BusinessAnalysis/Index?type=web&code=SH688041
    
    Args:
        symbol: 带市场标识的股票代码，如"SH688041"(上海)或"SZ000001"(深圳)
        
    Returns:
        dict: 包含公司主营构成数据的字典，包括收入、成本、利润及比例等财务指标
    """
    result = ak.stock_zygc_em(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：主力控盘与机构参与度
@mcp.tool()
def stock_comment_detail_zlkp_jgcyd_em(symbol: str) -> dict:
    """获取股票主力控盘与机构参与度数据
    
    数据来源: 东方财富网-数据中心-特色数据-千股千评
    示例网址: https://data.eastmoney.com/stockcomment/stock/600000.html
    
    Args:
        symbol: 股票代码，如"600000"
        
    Returns:
        dict: 包含主力控盘和机构参与度数据的字典，机构参与度单位为%
    """
    result = ak.stock_comment_detail_zlkp_jgcyd_em(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：个股新闻资讯
@mcp.tool()
def stock_news_em(symbol: str) -> dict:
    """获取个股新闻资讯数据
    
    数据来源: 东方财富-个股新闻
    网址: https://so.eastmoney.com/news/s
    
    Args:
        symbol: 股票代码或关键词，如"300059"
        
    Returns:
        dict: 包含个股新闻资讯的字典，包括标题、内容、发布时间等
    """
    result = ak.stock_news_em(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：财经内容精选
@mcp.tool()
def stock_news_main_cx() -> dict:
    """获取财新网财经内容精选数据
    
    数据来源: 财新网-财新数据通
    网址: https://cxdata.caixin.com/pc/
    
    Returns:
        dict: 包含财经内容精选的字典，包括标签、摘要、发布时间等
    """
    result = ak.stock_news_main_cx()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：个股资金流数据
@mcp.tool()
def stock_fund_flow_individual(symbol: str) -> dict:
    """获取个股资金流数据
    
    数据来源: 同花顺-数据中心-资金流向
    网址: https://data.10jqka.com.cn/funds/ggzjl/#refCountId=data_55f13c2c_254
    
    Args:
        symbol: 时间周期，可选值: 
               "即时"(默认), 
               "3日排行", 
               "5日排行", 
               "10日排行", 
               "20日排行"
        
    Returns:
        dict: 包含个股资金流数据的字典，包括流入流出资金、净额等
    """
    result = ak.stock_fund_flow_individual(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：雪球股票热度关注排行榜
@mcp.tool()
def stock_hot_follow_xq(symbol: str) -> dict:
    """获取雪球股票热度关注排行榜数据
    
    数据来源: 雪球-沪深股市-热度排行榜
    网址: https://xueqiu.com/hq
    
    Args:
        symbol: 排行类型，可选值: 
               "最热门"(默认), 
               "本周新增"
        
    Returns:
        dict: 包含股票热度关注数据的字典，包括关注人数、最新价等
    """
    result = ak.stock_hot_follow_xq(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：百度热搜股票数据
@mcp.tool()
def stock_hot_search_baidu(symbol: str, date: str, time: str) -> dict:
    """获取百度热搜股票数据
    
    数据来源: 百度股市通-热搜股票
    网址: https://gushitong.baidu.com/expressnews
    
    Args:
        symbol: 市场类型，可选值: 
               "A股"(默认), 
               "全部", 
               "港股", 
               "美股"
        date: 查询日期，格式为YYYYMMDD，如"20230421"
        time: 时间周期，可选值: 
              "今日"(默认), 
              "1小时"
        
    Returns:
        dict: 包含热搜股票数据的字典，包括股票名称、涨跌幅、所属板块等
    """
    result = ak.stock_hot_search_baidu(symbol=symbol, date=date, time=time)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：富途牛牛快讯数据
@mcp.tool()
def stock_info_global_futu() -> dict:
    """获取富途牛牛快讯数据
    
    数据来源: 富途牛牛-快讯
    网址: https://news.futunn.com/main/live
    
    Returns:
        dict: 包含最近50条快讯数据的字典，包括标题、内容、发布时间等
    """
    result = ak.stock_info_global_futu()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")
# 工具函数：A+H股实时行情数据
@mcp.tool()
def stock_zh_ah_spot() -> dict:
    """获取A+H股实时行情数据
    
    数据来源: 腾讯财经-A+H股数据
    网址: https://stockapp.finance.qq.com/mstats/#mod=list&id=hk_ah&module=HK&type=AH
    
    Returns:
        dict: 包含所有A+H上市公司实时行情数据的字典，包括代码、名称、价格、成交量等
    """
    result = ak.stock_zh_ah_spot()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：科创板实时行情数据
@mcp.tool()
def stock_zh_kcb_spot() -> dict:
    """获取科创板实时行情数据
    
    数据来源: 新浪财经-科创板
    网址: http://vip.stock.finance.sina.com.cn/mkt/#kcb
    
    Returns:
        dict: 包含所有科创板上市公司实时行情数据的字典，包括代码、价格、成交量、市值等
    """
    result = ak.stock_zh_kcb_spot()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：美股实时行情数据
@mcp.tool()
def stock_us_spot_em() -> dict:
    """获取美股实时行情数据
    
    数据来源: 东方财富网-美股
    网址: https://quote.eastmoney.com/center/gridlist.html#us_stocks
    
    Returns:
        dict: 包含所有美股上市公司实时行情数据的字典，包括代码、价格、成交量、市值等
    """
    result = ak.stock_us_spot_em()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# ==================== 期货市场相关工具函数 ====================

# 工具函数：期货实时行情数据
@mcp.tool()
def futures_zh_spot(symbol: str, market: str = "CF", adjust: str = "0") -> dict:
    """获取期货实时行情数据
    
    数据来源: 新浪财经-期货页面的实时行情数据
    网址: https://finance.sina.com.cn/futuremarket/
    
    Args:
        symbol: 期货合约代码，如"V2205"(单品种)或"V2205,P2205,B2201,M2205"(多品种，逗号分隔)
        market: 市场类型，可选值: "CF"(商品期货), "FF"(金融期货)
        adjust: 调整参数，默认"0"
        
    Returns:
        dict: 包含期货实时行情数据的字典，包括开盘价、最高价、最低价、现价、成交量等
    """
    result = ak.futures_zh_spot(symbol=symbol, market=market, adjust=adjust)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：期货主力合约匹配
@mcp.tool()
def match_main_contract(symbol: str) -> str:
    """获取期货主力合约代码
    
    数据来源: AKShare内置函数
    
    Args:
        symbol: 交易所代码，可选值: 
               "dce"(大连商品交易所), 
               "czce"(郑州商品交易所), 
               "shfe"(上海期货交易所),
               "gfex"(广州期货交易所),
               "cffex"(中国金融期货交易所)
        
    Returns:
        str: 主力合约代码字符串，多个合约用逗号分隔
    """
    result = ak.match_main_contract(symbol=symbol)
    return {"main_contracts": result}

# 工具函数：期货交易费用参照表
@mcp.tool()
def futures_fees_info() -> dict:
    """获取期货交易费用参照表
    
    数据来源: openctp 期货交易费用参照表
    网址: http://openctp.cn/fees.html
    
    Returns:
        dict: 包含期货交易费用数据的字典，包括交易所、合约代码、手续费等信息
    """
    result = ak.futures_fees_info()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：期货手续费与保证金
@mcp.tool()
def futures_comm_info(symbol: str = "所有") -> dict:
    """获取期货手续费与保证金数据
    
    数据来源: 九期网-期货手续费数据
    网址: https://www.9qihuo.com/qihuoshouxufei
    
    Args:
        symbol: 查询类型，可选值: "所有"(默认)或具体合约代码
        
    Returns:
        dict: 包含期货手续费与保证金数据的字典，包括交易所名称、合约名称、手续费等
    """
    result = ak.futures_comm_info(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：期货规则-交易日历表
@mcp.tool()
def futures_rule(date: str) -> dict:
    """获取期货规则-交易日历表数据
    
    数据来源: 国泰君安期货-交易日历数据表
    网址: https://www.gtjaqh.com/pc/calendar.html
    
    Args:
        date: 交易日期，格式为YYYYMMDD，如"20231205"
        
    Returns:
        dict: 包含指定交易日所有合约的交易日历数据的字典
    """
    result = ak.futures_rule(date=date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：期货现期图数据
@mcp.tool()
def futures_spot_sys(symbol: str, indicator: str) -> dict:
    """获取期货现期图数据
    
    数据来源: 生意社-商品与期货-现期图
    网址: https://www.100ppi.com/sf/792.html
    
    Args:
        symbol: 品种名称，如"铜"
        indicator: 指标类型，可选值: "市场价格", "基差率", "主力基差"
        
    Returns:
        dict: 包含现期图数据的字典，根据指标类型返回相应数据
    """
    result = ak.futures_spot_sys(symbol=symbol, indicator=indicator)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：上海期货交易所合约信息
@mcp.tool()
def futures_contract_info_shfe(date: str) -> dict:
    """获取上海期货交易所合约信息
    
    数据来源: 上海期货交易所-交易所服务-业务数据-交易参数汇总查询
    网址: https://tsite.shfe.com.cn/bourseService/businessdata/summaryinquiry/
    
    Args:
        date: 查询日期，格式为YYYYMMDD，如"20240513"
        
    Returns:
        dict: 包含上海期货交易所合约信息数据的字典
    """
    result = ak.futures_contract_info_shfe(date=date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：大连商品交易所合约信息
@mcp.tool()
def futures_contract_info_dce() -> dict:
    """获取大连商品交易所合约信息
    
    数据来源: 大连商品交易所-业务/服务-业务参数-交易参数-合约信息查询
    网址: http://www.dce.com.cn/dalianshangpin/ywfw/ywcs/jycs/hyxxcx/index.html
    
    Returns:
        dict: 包含大连商品交易所最近交易日的期货合约信息数据的字典
    """
    result = ak.futures_contract_info_dce()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：郑州商品交易所合约信息
@mcp.tool()
def futures_contract_info_czce(date: str) -> dict:
    """获取郑州商品交易所合约信息
    
    数据来源: 郑州商品交易所-交易数据-参考数据
    网址: http://www.czce.com.cn/cn/jysj/cksj/H770322index_1.htm
    
    Args:
        date: 查询日期，格式为YYYYMMDD，如"20240228"
        
    Returns:
        dict: 包含郑州商品交易所合约信息数据的字典
    """
    result = ak.futures_contract_info_czce(date=date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：中国金融期货交易所合约信息
@mcp.tool()
def futures_contract_info_cffex(date: str) -> dict:
    """获取中国金融期货交易所合约信息
    
    数据来源: 中国金融期货交易所-数据-交易参数
    网址: http://www.gfex.com.cn/gfex/hyxx/ywcs.shtml
    
    Args:
        date: 查询日期，格式为YYYYMMDD，如"20240228"
        
    Returns:
        dict: 包含中国金融期货交易所合约信息数据的字典
    """
    result = ak.futures_contract_info_cffex(date=date)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：外盘期货品种代码表
@mcp.tool()
def futures_hq_subscribe_exchange_symbol() -> dict:
    """获取外盘期货品种代码表
    
    数据来源: 新浪财经-外盘商品期货品种代码表数据
    网址: https://finance.sina.com.cn/money/future/hf.html
    
    Returns:
        dict: 包含外盘期货品种代码表数据的字典
    """
    result = ak.futures_hq_subscribe_exchange_symbol()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：外盘期货实时行情数据
@mcp.tool()
def futures_foreign_commodity_realtime(symbol: str) -> dict:
    """获取外盘期货实时行情数据
    
    数据来源: 新浪财经-外盘商品期货数据
    网址: https://finance.sina.com.cn/money/future/hf.html
    
    Args:
        symbol: 期货品种代码，如"CT,NID"(多个用逗号分隔)或列表格式
        
    Returns:
        dict: 包含外盘期货实时行情数据的字典
    """
    result = ak.futures_foreign_commodity_realtime(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：国际期货实时行情数据-东财
@mcp.tool()
def futures_global_spot_em() -> dict:
    """获取国际期货实时行情数据
    
    数据来源: 东方财富网-行情中心-期货市场-国际期货-实时行情数据
    网址: https://quote.eastmoney.com/center/gridlist.html#futures_global
    
    Returns:
        dict: 包含所有国际期货品种的实时行情数据的字典
    """
    result = ak.futures_global_spot_em()
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

# 工具函数：期货资讯-上海金属网快讯
@mcp.tool()
def futures_news_shmet(symbol: str) -> dict:
    """获取期货资讯-上海金属网快讯
    
    数据来源: 上海金属网-快讯
    网址: https://www.shmet.com/newsFlash/newsFlash.html?searchKeyword=
    
    Args:
        symbol: 查询关键词，如"铜"
        
    Returns:
        dict: 包含期货资讯快讯数据的字典，包括发布时间、内容等
    """
    result = ak.futures_news_shmet(symbol=symbol)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")

def main():
    """启动MCP服务器"""
    # 使用默认的stdio传输协议启动服务器
    mcp.run(transport="http",port=9000)

# 主函数
if __name__ == "__main__":
    main()
