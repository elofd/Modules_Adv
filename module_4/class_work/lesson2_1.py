from typing import Optional, List
import datetime as dt
from datetime import datetime


from flask import Flask, request


app = Flask(__name__)


@app.route('/search/', methods=['GET'])
def search():
    cell_tower_ids: List[int] = request.args.getlist('cell_tower_id', type=int)
    if not cell_tower_ids:
        return f'Вы должны указать хотя бы 1 call_tower_id', 400
    for elem in cell_tower_ids:
        if elem <= 0:
            return 'cell_tower_id must be more than 0', 400
    phone_prefixes: List[str] = request.args.getlist('phone_prefix')
    for elem in phone_prefixes:
        if len(elem) > 11 or not elem.endswith('*'):
            return 'phone_prefix len must be more than 10 and end with *', 400
    protocols: List[str] = request.args.getlist('protocol')
    for elem in protocols:
        if elem not in ('2G', '3G', '4G', '5G'):
            return 'protocols can be 2G, 3G, 4G or 5G', 400
    signal_level: Optional[float] = request.args.get('signal_level', type=float, default=None)
    date_from: str = request.args.get('date_from', type=str)
    date_to: str = request.args.get('date_to', type=str)
    if date_from:
        try:
            date_from = datetime.strptime(date_from, '%Y%m%d').date()
        except ValueError:
            return 'Invalid date format. Use YYYYMMDD format', 400
        if date_from > dt.date.today():
            return 'Date cannot be in future', 400
    if date_to:
        try:
            date_to = datetime.strptime(date_to, '%Y%m%d').date()
        except ValueError:
            return 'Invalid date format. Use YYYYMMDD format', 400
        if date_to > dt.date.today():
            return 'Date cannot be in future', 400
        if date_from and date_to < date_from:
            return 'The end date cannot be earlier than the start date'
    return (
        f'Search for {cell_tower_ids} cell towers. Search criteria:<br>'
        f'phone_prefixes={phone_prefixes}<br>'
        f'protocols={protocols}<br>'
        f'signal_level={signal_level}<br>'
        f'date_from={date_from}<br>'
        f'date_to={date_to}<br>'
    )


if __name__ == '__main__':
    app.run(debug=True)