from jinja2 import Template

HTML_TEMPLATE = '''
<html>
<head>
<title>Intraday Scanner Pro</title>
<style>
body {
    background: #111;
    color: white;
    font-family: Arial;
    padding: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th, td {
    border: 1px solid #333;
    padding: 10px;
    text-align: center;
}

.green {
    color: #00ff99;
}
</style>
</head>

<body>

<h1>Intraday Scanner Pro</h1>

<table>

<tr>
<th>Symbol</th>
<th>Price</th>
<th>Move</th>
<th>%</th>
<th>RSI</th>
<th>Volume Breakout</th>
<th>AI Score</th>
</tr>

{% for stock in stocks %}
<tr>
<td>{{ stock.symbol }}</td>
<td>{{ stock.price }}</td>
<td class="green">₹{{ stock.movement }}</td>
<td>{{ stock.percent }}%</td>
<td>{{ stock.rsi }}</td>
<td>{{ stock.volume_breakout }}</td>
<td>{{ stock.ai_score }}</td>
</tr>
{% endfor %}

</table>

</body>
</html>
'''

def generate_html(stocks, output_file):
    template = Template(HTML_TEMPLATE)
    html = template.render(stocks=stocks)

    with open(output_file, "w") as f:
        f.write(html)