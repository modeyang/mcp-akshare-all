# mcp-akshare-all

基于 [AKShare](https://akshare.akfamily.xyz/) 数据接口的 MCP (Model Context Protocol) 服务器，提供全面的中国股票和期货市场数据访问能力。

## 功能特性

- 🚀 **全面的数据覆盖**：支持股票、期货、新闻、资金流等多维度金融数据
- 🔧 **标准化接口**：将 AKShare 数据接口转换为标准的 MCP 工具格式
- 📊 **实时数据**：提供实时行情、历史数据、财务指标等
- 🌐 **多市场支持**：覆盖A股、港股、美股、期货等多个市场
- ⚡ **高性能**：基于 FastMCP 框架，支持异步数据处理
- 🛡️ **数据限制**：内置数据行数限制，避免过大数据传输

## 支持的数据类型

### 📈 股票市场数据
- **基础行情**：实时行情、历史K线、分时数据
- **市场概览**：上交所、深交所数据总貌和统计
- **特色板块**：科创板、创业板、ST股票、新股数据
- **跨市场**：A+H股、中概股、美股数据
- **资金流向**：个股资金流、主力控盘数据
- **财务数据**：主营构成、财务指标
- **市场情绪**：热搜排行、关注度数据

### 🔮 期货市场数据
- **实时行情**：商品期货、金融期货实时数据
- **合约信息**：各大交易所合约详情
- **交易规则**：手续费、保证金、交易日历
- **国际期货**：外盘期货实时行情
- **现期分析**：现货与期货价格对比

### 📰 资讯与新闻
- **个股新闻**：东方财富个股资讯
- **财经快讯**：富途牛牛、财新网内容
- **期货资讯**：上海金属网快讯

## 工具函数列表

### 基础工具
- `get_current_time()` - 获取当前时间
- `stock_trade_date_hist()` - 股票交易日历查询

### 股票市场概览
- `stock_zh_a_gdhs_detail_em()` - 上海证券交易所股票数据总貌
- `stock_szse_sector_summary()` - 深圳证券交易所证券类别统计
- `stock_zh_a_gdhs_detail_em_area()` - 地区交易排序
- `stock_board_industry_summary_ths()` - 股票行业成交数据

### 股票行情数据
- `stock_zh_a_st_em()` - 风险警示板股票行情
- `stock_zh_a_new_em()` - 新股行情数据
- `stock_xgsr_ths()` - 新股上市首日数据
- `stock_zh_kcb_daily()` - 科创板股票历史行情
- `stock_zh_ah_daily()` - A+H股历史行情
- `stock_us_hist()` - 美股历史行情
- `stock_us_hist_min_em()` - 美股分时行情
- `stock_bid_ask_em()` - A股分时行情
- `stock_hk_hist_min_em()` - 港股分时行情
- `stock_zh_ah_spot()` - A+H股实时行情
- `stock_zh_kcb_spot()` - 科创板实时行情
- `stock_us_spot_em()` - 美股实时行情

### 股票分析工具
- `stock_zygc_em()` - 上市公司主营构成
- `stock_comment_detail_zlkp_jgcyd_em()` - 主力控盘与机构参与度
- `stock_fund_flow_individual()` - 个股资金流数据
- `stock_hot_follow_xq()` - 雪球股票热度关注排行
- `stock_hot_search_baidu()` - 百度热搜股票数据

### 股票资讯
- `stock_news_em()` - 个股新闻资讯
- `stock_news_main_cx()` - 财经内容精选
- `stock_info_global_futu()` - 富途牛牛快讯

### 期货市场
- `futures_zh_spot()` - 期货实时行情
- `match_main_contract()` - 期货主力合约匹配
- `futures_fees_info()` - 期货交易费用参照表
- `futures_comm_info()` - 期货手续费与保证金
- `futures_rule()` - 期货交易日历
- `futures_spot_sys()` - 期货现期图数据

### 期货合约信息
- `futures_contract_info_shfe()` - 上海期货交易所合约信息
- `futures_contract_info_dce()` - 大连商品交易所合约信息
- `futures_contract_info_czce()` - 郑州商品交易所合约信息
- `futures_contract_info_cffex()` - 中国金融期货交易所合约信息

### 国际期货
- `futures_hq_subscribe_exchange_symbol()` - 外盘期货品种代码表
- `futures_foreign_commodity_realtime()` - 外盘期货实时行情
- `futures_global_spot_em()` - 国际期货实时行情
- `futures_news_shmet()` - 期货资讯快讯

## 安装与配置

### 环境要求

- Python 3.8+
- 依赖包：`fastmcp>=2.0.0`, `akshare`, `pandas`

### 安装方式

#### 方式一：直接使用 uvx（推荐）

```json
{
  "mcpServers": {
    "mcp-akshare-all": {
      "command": "uvx",
      "args": [
        "mcp-akshare-all"
      ]
    }
  }
}
```

#### 方式二：从源码安装

```bash
# 克隆项目
git clone https://github.com/August1996/mcp-akshare.git
cd mcp-akshare-all

# 安装依赖
uv sync

# 运行服务器
uv run python main.py
```

在 MCP 客户端配置中添加：

```json
{
  "mcpServers": {
    "mcp-akshare-all": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "/path/to/mcp-akshare-all/main.py"
      ],
      "cwd": "/path/to/mcp-akshare-all"
    }
  }
}
```

#### 方式三：使用 HTTP 接口连接

首先启动服务器：

```bash
# 克隆项目
git clone https://github.com/August1996/mcp-akshare.git
cd mcp-akshare-all

# 安装依赖
uv sync

# 启动 HTTP 服务器（默认端口 9000）
uv run python main.py
```

然后在 MCP 客户端配置中使用 HTTP 传输协议：

```json
{
  "mcpServers": {
    "mcp-akshare-all": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-everything",
        "http://localhost:9000/mcp"
      ]
    }
  }
}
```

或者直接使用 HTTP URL：

```json
{
  "mcpServers": {
    "mcp-akshare-all": {
      "url": "http://localhost:9000/mcp"
    }
  }
}
```

### HTTP 服务模式

服务器支持 HTTP 传输协议，默认运行在端口 9000：

```bash
uv run python main.py
```

服务器启动后，可通过 HTTP 接口访问 MCP 服务。

## 使用示例

### 获取股票实时行情

```python
# 获取科创板实时行情
result = stock_zh_kcb_spot()
print(result)
```

### 获取期货数据

```python
# 获取期货实时行情
result = futures_zh_spot(symbol="V2205", market="CF")
print(result)

# 获取主力合约
result = match_main_contract(symbol="dce")
print(result)
```

### 获取财经新闻

```python
# 获取个股新闻
result = stock_news_em(symbol="300059")
print(result)

# 获取财经快讯
result = stock_info_global_futu()
print(result)
```

## 数据限制说明

为了避免数据传输过大，所有返回的数据都限制在 `MAX_DATA_ROW = 100` 行以内。如需获取更多数据，可以：

1. 修改 `main.py` 中的 `MAX_DATA_ROW` 常量
2. 使用分页或时间范围参数获取特定数据

## 技术架构

- **框架**：基于 [FastMCP](https://github.com/jlowin/fastmcp) 2.0+
- **数据源**：[AKShare](https://akshare.akfamily.xyz/) 金融数据接口
- **传输协议**：支持 HTTP 和 STDIO 传输
- **数据格式**：统一返回 JSON 格式数据
- **异步支持**：所有工具函数支持异步调用

## 常见问题

### Q: 数据更新频率如何？
A: 数据来源于 AKShare，更新频率取决于各数据源的更新策略，一般实时数据延迟在几分钟内。

### Q: 支持哪些股票代码格式？
A: 支持多种格式：
- A股：`000001`（深圳）、`600000`（上海）
- 港股：`00700`
- 美股：`AAPL`
- 带市场标识：`SZ000001`、`SH600000`

### Q: 如何处理数据获取失败？
A: 服务器内置错误处理机制，当数据获取失败时会返回空结果或错误信息。建议检查：
1. 网络连接是否正常
2. 股票代码是否正确
3. 交易时间是否在开市期间

### Q: 可以自定义数据行数限制吗？
A: 可以修改 `main.py` 中的 `MAX_DATA_ROW` 常量来调整返回数据的最大行数。

## 贡献指南

我们欢迎社区贡献！如果您想要添加新的数据接口或改进现有功能：

1. **Fork 项目**并创建您的功能分支
2. **添加新接口**：参考现有工具函数的格式
3. **测试功能**：确保新接口正常工作
4. **提交 Pull Request**：详细描述您的更改

### 添加新接口的步骤

```python
@mcp.tool()
def your_new_function(param1: str, param2: str = "default") -> dict:
    """函数描述
    
    数据来源: 数据源网站
    网址: https://example.com
    
    Args:
        param1: 参数1描述
        param2: 参数2描述
        
    Returns:
        dict: 返回数据的字典格式描述
    """
    result = ak.your_akshare_function(param1=param1, param2=param2)
    if type(result) is pandas.core.frame.DataFrame:
        result = result[:min(MAX_DATA_ROW, len(result))]
    return result.to_dict(orient="records")
```

### 参考资源

- [AKShare 官方文档](https://akshare.akfamily.xyz/)
- [FastMCP 框架文档](https://github.com/jlowin/fastmcp)
- [MCP 协议规范](https://modelcontextprotocol.io/)

## 更新日志

### v1.0.0
- 初始版本发布
- 支持 40+ 股票和期货数据接口
- 基于 FastMCP 2.0 框架
- 支持 HTTP 和 STDIO 传输协议

## 许可证

MIT License

Copyright (c) 2024 mcp-akshare-all

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## 免责声明

本项目仅供学习和研究使用，不构成任何投资建议。使用本项目获取的金融数据进行投资决策的风险由用户自行承担。项目维护者不对数据的准确性、完整性或及时性做任何保证。
